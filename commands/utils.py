import nextcord
from nextcord import *
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True
bot = commands.Bot(command_prefix="doas ", intents=intents)

class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx:Interaction):
        await ctx.send(f"Pong! Latency: {round(self.bot.latency * 1000)}ms")

def setup(bot):
    bot.add_cog(Utils(bot))