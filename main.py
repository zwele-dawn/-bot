import discord
from discord.ext import keep_alive

TOKEN = os.getenv('BOT_TOKEN')

intents = discord.Intents.default()
intents.message_centent = True
bot = commands.Bot(command_prefix="!",intents=intents)

@bot.event
async def on_ready():
  print(f'we have logged in as {bot.user}')

@botcommand()
async def hello(ctx):
  await ctx.send(f'hello {ctx.author.display_name}!')

keep_arrive()
bot.run(TOKEN)
