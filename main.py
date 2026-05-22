import discord
import os

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")
    await bot.tree.sync()

@bot.slash_command(name="ping", description="Test if bot works")
async def ping(ctx):
    await ctx.respond("Pong! Maternity Hospital Reminder is alive 🍼")

@bot.slash_command(name="duedate", description="Set your due date: YYYY-MM-DD")
async def duedate(ctx, date: str):
    await ctx.respond(f"📅 Due date set to {date}! Use /remindme to set alerts.")

@bot.slash_command(name="announce", description="Post a maternity announcement")
async def announce(ctx, message: str):
    embed = discord.Embed(title="🍼 Maternity Announcement", description=message, color=0xffc0cb)
    await ctx.respond(embed=embed)

bot.run(os.getenv('DISCORD_TOKEN'))
