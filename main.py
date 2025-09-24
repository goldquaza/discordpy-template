import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")

@bot.command()
async def ping(ctx):
    before = discord.utils.utcnow()
    message = await ctx.send("Pinging...")
    after = discord.utils.utcnow()
    latency = (after - before).total_seconds() * 1000
    await message.edit(content=f"Pong! {int(latency)}ms")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

bot.run("TOKEN HERE") # I strongly recommend you always store your token/s and your API key/s in a hidden config file
