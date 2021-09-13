import discord
from discord.ext import commands

class Chanel_Commands(commands.Cog):

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
    async def sprout(self, ctx, name: str, ch_type="Misc"):
        topics = ["News", "Music", "Gaming", "Misc"]
        
        if ch_type not in topics:
            return await ctx.send("Not a valid type! Valid types are: [News, Music, Gaming, and Misc]")
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
    bot.add_cog(Chanel_Commands(bot))