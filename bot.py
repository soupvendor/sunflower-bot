import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import random

load_dotenv()

TOKEN = os.getenv('TOKEN')

client = commands.Bot(command_prefix = '.')

############
###Events###
############


@client.event
async def on_ready():
    print("Bot is ready.")

@client.event
async def on_member_join(member):
    print(f"{member} has joined the server!")
    

@client.event
async def on_member_remove(member):
    print(f"{member} has left the server!")
    


############
##Commands##
############



@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms!")

@client.command(aliases=(['8ball']))
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "Ah I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount + 1)

@client.command()
async def kd(ctx):
    await ctx.send("https://i.pinimg.com/474x/57/65/40/5765406c444679a20c078831b232b313.jpg")

@client.command()
async def cheesecake(ctx):
    await ctx.send("https://media.discordapp.net/attachments/852594474412277803/864678152676048916/image0.jpg?width=904&height=678")




client.run(TOKEN)


