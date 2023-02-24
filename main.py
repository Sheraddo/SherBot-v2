import nextcord, os
from nextcord.ext import commands
from myconfig import TOKEN

# Bot Initialization
intents = nextcord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True
bot = commands.Bot(command_prefix="doas ", intents=intents)

# Cog Setup
for fn in os.listdir("./commands"):
    if fn.endswith(".py"):
        bot.load_extension(f"commands.{fn[:- 3]}")

for fn in os.listdir("./events"):
    if fn.endswith(".py"):
        bot.load_extension(f"events.{fn[:- 3]}")

# Bot Startup
bot.run(TOKEN)