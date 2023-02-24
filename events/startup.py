import nextcord
from nextcord import *
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True
bot = commands.Bot(command_prefix="doas ", intents=intents)

class Startup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener
    async def on_ready():
        print("Bot is online!")

def setup(bot):
    bot.add_cog(Startup(bot))