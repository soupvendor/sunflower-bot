import discord
from discord.ext import commands
import random
import requests




class Trivia(commands.Cog):
    @commands.command(aliases=["8-Ball"])
    async def _8ball(self, ctx, *, question):
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
    
    @commands.command()
    async def cheesecake(self, ctx):
        await ctx.send("https://media.discordapp.net/attachments/852594474412277803/864678152676048916/image0.jpg?width=904&height=678")
    
    @commands.command()
    async def kd(self, ctx):
        await ctx.send("https://i.pinimg.com/474x/57/65/40/5765406c444679a20c078831b232b313.jpg")
    @commands.command()
    async def cat(self, ctx):
      response = requests.get('https://aws.random.cat/meow')
      data = response.json()
      embed = discord.Embed(
          title = 'Kitty Cat 🐈',
          description = 'Cats :star_struck:',
          colour = discord.Colour.purple()
          )
      embed.set_image(url=data['file'])            
      embed.set_footer(text="")
      await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Trivia(bot))
