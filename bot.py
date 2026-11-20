import asyncio
import discord
import os

import utils
from discord.ext import commands

TOKEN = os.environ["DISCORD_BOT_TOKEN"]
PREFIX = '!'

class DiscordBot(commands.Bot):
    async def setup_hook(self):
        await self.tree.sync()


async def main():
    intents = discord.Intents().all()
    intents.members = True
    bot = DiscordBot(command_prefix=commands.when_mentioned_or(PREFIX), intents=intents, case_insensitive=True)

    await utils.setup_bot(bot)

    await bot.start(TOKEN)

if __name__=='__main__':
    asyncio.run(main())
