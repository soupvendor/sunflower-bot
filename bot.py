from time import asctime
import discord
import os
import logging
from discord.ext import commands
from dotenv import load_dotenv



##Intents###
intents = discord.Intents.default()
intents.members = True

load_dotenv()

#Logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#Token
TOKEN = os.getenv('TOKEN')
client = commands.Bot(command_prefix = '.', intents=intents)


@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        print(f"Loading {filename}")
        client.load_extension(f"cogs.{filename[:-3]}")
    else:
        print(f'Unable to load {filename[:-3]}')



############
###Events###
############
@client.event
async def on_ready():
    print("Bot is ready.")
    try:
        logger.setLevel(logging.INFO)
        ready_handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
        handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
        logger.addHandler(ready_handler)
    except Exception:
        print("Added to log!")

@client.event
async def on_member_join(member):
    w = open("member_join_leave.txt", "a")
    print(f"{member} has joined the server!")
    w.write(f"{member} has joined the server!\n")
    w.close()

@client.event
async def on_member_remove(member):
    w = open("member_join_leave.txt", "a")
    print(f"{member} has left the server!")
    w.write(f"{member} has left the server!\n")
    w.close()

############
##Commands##
############

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms!")

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount + 1)


client.run(TOKEN)