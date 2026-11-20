import os
import asyncio

from discord.ext import commands


async def get_cogs():
    """Gets all cog extensions in the cogs directory."""
    cogs_dir = os.path.join(os.path.dirname(__file__), "cogs")
    cogs = []
    for file in os.listdir(cogs_dir):
        if file.endswith('.py') and not file.startswith('_'):
            cogs.append(f"cogs.{file[:-3]}")
    return cogs


def register_update_command(bot):
    @bot.hybrid_command(name="reload", description="Reload all loaded cogs")
    @commands.is_owner()
    async def update(ctx):
        extensions = sorted(name for name in bot.extensions if name.startswith("cogs."))
        results = []

        for extension in extensions:
            try:
                await bot.reload_extension(extension)
            except Exception as error:
                print(f"Failed to reload {extension}: {type(error).__name__}: {error}")
                results.append(f"❌ {extension}: reload failed (see bot console)")
            else:
                results.append(f"✅ {extension}: reloaded")

        if not results:
            results.append("No loaded cogs to reload.")

        await ctx.send("\n".join(results), ephemeral=ctx.interaction is not None)

update_lock = asyncio.Lock()


@commands.command(name="update")
@commands.is_owner()
@commands.guild_only()
async def update(ctx):
    if update_lock.locked():
        await ctx.send("En oppdatering pågår allerede.")
        return

    async with update_lock:
        await ctx.send("Sjekker etter oppdateringer på GitHub …")

        env = os.environ.copy()
        env["GIT_TERMINAL_PROMPT"] = "0"
        env["GIT_SSH_COMMAND"] = "ssh -o BatchMode=yes"

        async def run_git(*args):
            process = await asyncio.create_subprocess_exec(
                "/usr/bin/git",
                "-C",
                "/opt/discordbot",
                *args,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                env=env,
            )

            try:
                stdout, stderr = await asyncio.wait_for(
                    process.communicate(),
                    timeout=60,
                )
            except asyncio.TimeoutError:
                if process.returncode is None:
                    process.kill()
                await process.communicate()
                raise

            output = stdout.decode(errors="replace").strip()
            errors = stderr.decode(errors="replace").strip()

            print(
                f"Git {args}: exit={process.returncode}\n"
                f"{output}\n{errors}",
                flush=True,
            )

            if process.returncode != 0:
                raise RuntimeError(f"Git-kommandoen feilet: {args}")

            return output

        try:
            # Finn versjonen som ligger på serveren før oppdateringen.
            old_commit = await run_git("rev-parse", "HEAD")

            await run_git("pull", "--ff-only")

            # Finn versjonen etter oppdateringen.
            new_commit = await run_git("rev-parse", "HEAD")

            if old_commit == new_commit:
                await ctx.send(
                    "✅ Ingen nye oppdateringer. "
                    "Serveren har allerede siste versjon."
                )
                return

            # Sammenlign filene i gammel og ny versjon.
            changes = await run_git(
                "diff",
                "--name-status",
                "--no-renames",
                old_commit,
                new_commit,
                "--",
            )

        except asyncio.TimeoutError:
            await ctx.send(
                "❌ Git-operasjonen tok for lang tid og ble avbrutt. "
                "Kontroller serverloggen og repositoryet før du prøver igjen."
            )
            return
        except (RuntimeError, OSError):
            await ctx.send(
                "❌ Oppdateringen eller kontrollen av endringer feilet. "
                "Se serverloggen for detaljer."
            )
            return

        await ctx.send(
            f"✅ Oppdatert fra `{old_commit[:7]}` til `{new_commit[:7]}`."
        )

        if not changes:
            await ctx.send(
                "Nye commits ble hentet, men filinnholdet er uendret."
            )
            return

        labels = {
            "A": "➕ Lagt til",
            "M": "✏️ Endret",
            "D": "🗑️ Slettet",
            "T": "🔄 Endret filtype",
        }

        # Send én melding per fil for å unngå for lange Discord-meldinger.
        for line in changes.splitlines():
            status, path = line.split("\t", 1)
            label = labels.get(status, status)

            # Hindre at filnavn lager omtaler eller ødelegger formateringen.
            safe_path = path.replace("`", "'").replace("@", "@\u200b")
            await ctx.send(f"{label}: `{safe_path[:1500]}`")

        await ctx.send(
            "Bruk `!reload` for å laste inn endrede cogs. "
            "Endringer i utils.py, startfil eller avhengigheter "
            "kan kreve restart og eventuell installasjon."
        )


@update.error
async def update_error(ctx, error):
    print(f"Feil i update: {error!r}", flush=True)

    if isinstance(error, commands.NotOwner):
        await ctx.send("Denne kommandoen er bare tilgjengelig for botens eier.")
    else:
        await ctx.send("Kommandoen feilet. Se serverloggen.")


async def setup_bot(bot):
    register_update_command(bot)
    bot.add_command(update)
    for extension in await get_cogs():
        try:
            await bot.load_extension(extension)
            print(f"loaded cog {extension}")
        except Exception as error:
            print(f"Error loading cog {extension}: {type(error).__name__}: {error}")
