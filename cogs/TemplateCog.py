import discord
from discord.ext import commands


class TemplateCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Template ready")

    @commands.command(name="test")
    async def template(self, ctx):
        await ctx.send('this is a template command :) og jeg blir oppdatert gjennom github og discord)')


async def setup(bot):
    await bot.add_cog(TemplateCog(bot))
