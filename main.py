import os
import discord
from discord_slash import SlashCommand
from discord.ext import commands
from slash_help import SlashHelp
from webserver import keep_alive

intents = discord.Intents.all()

bot = commands.Bot(commands.when_mentioned_or(">"), help_command=None, case_insensitive=True, intents=intents)


@bot.event
async def on_ready():
    print(f"Ready. Logged onto {bot.user}")
    activity = discord.Activity(type=discord.ActivityType.watching, name="Content Creators")
    await bot.change_presence(activity=activity)


for file in os.listdir('cogs/'):
    if file.endswith('.py'):
        print(f"LOADED {file}")
        bot.load_extension(f'cogs.{file[:-3]}')

keep_alive()

token = os.environ.get("DISCORD_BOT_SECRET")

slash = SlashCommand(bot, sync_commands=True)
help_slash = SlashHelp(bot, slash, token, author_only=True, color=0x0064ff, dpy_command=True, auto_create=True)


@slash.slash(name="help")
async def help(ctx, command=None):
    await help_slash.send_help(ctx, command, guild_id=ctx.guild.id)

bot.run(token)
