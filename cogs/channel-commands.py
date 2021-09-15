import discord
from discord.ext import commands

class ChannelCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms!")

    @commands.command()
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount + 1)   
    
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)

    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
    @commands.command()
    async def sprout(self, ctx, name: str, ch_type=""):
        topics = ["News", "Music", "Gaming", "Misc"]
        
        if ch_type == "":
            return await ctx.send("No channel type given! Valid types are: [News, Music, Gaming, and Misc]")
        elif ch_type not in topics:
            return await ctx.send("Invalid channel type! Valid types are: [News, Music, Gaming, and Misc]")
        elif ch_type == topics[0]:
            await ctx.guild.create_text_channel(name)
        elif ch_type == topics[1]:
            await ctx.guild.create_text_channel(name)
        elif ch_type == topics[2]:
            await ctx.guild.create_text_channel(name)
        elif ch_type == topics[3]:
            await ctx.guild.create_text_channel(name)
        
        await ctx.send(f"{ch_type} channel created!")
def setup(bot):
    bot.add_cog(ChannelCommands(bot))