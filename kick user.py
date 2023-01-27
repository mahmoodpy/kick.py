import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents = discord.Intents.all()

bot = commands.Bot(command_prefix=".", intents=intents)

@bot.command()
async def kick(ctx, member: discord.Member = None, *, reason: str = None):
    if member is None:
        await ctx.send(f"{ctx.author.mention},الرجاء تحديد اسم المستخدم")
        return
    # Check if the user has the kick_members permission
    if not ctx.message.author.guild_permissions.kick_members:
        await ctx.send(f"{ctx.author.mention},ليس لديك الصلاحيات الازمه")
        return
    try:
        await member.kick(reason=reason)
    except discord.Forbidden:
        await ctx.send(f"{ctx.author.mention},ليس لديك الصلاحيات الازمه")
        return
    await ctx.send(f"{member} تم طرده")

bot.run("token-bot-here")