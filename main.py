import discord
from discord.ext import commands
import os
import asyncio
import mysql.connector
import datetime
import math

token = os.environ['TOKEN']
client = commands.Bot(command_prefix='r!', case_insensitive=True)

class EmbedHelpCommand(commands.MinimalHelpCommand):
    """This is an example of a HelpCommand that utilizes embeds.
    It's pretty basic but it lacks some nuances that people might expect.
    1. It breaks if you have more than 25 cogs or more than 25 subcommands. (Most people don't reach this)
    2. It doesn't DM users. To do this, you have to override `get_destination`. It's simple.
    Other than those two things this is a basic skeleton to get you started. It should
    be simple to modify if you desire some other behaviour.
    To use this, pass it to the bot constructor e.g.:
    bot = commands.Bot(help_command=EmbedHelpCommand())
    """

    def __init__(self):
        super().__init__(command_attrs={
            'description': "This command will inform you about any command that you'd like to, or all the commands, by leaving the command argument empty."
        })
        self.dm_help = False

    # Set the embed colour here
    COLOUR = 0x1E90FF

    def command_not_found(self, string):
        return 'Command Not Found.'

    async def get_ending_note(self):
        prefix = await client.get_prefix(self.context.message)
        return f'Please run {prefix}help for more information on a command.'

    def get_command_signature(self, command):
        if command.signature:
            return f'``{self.clean_prefix}{command.qualified_name} {command.signature}``'
        else:
            return f"``{self.clean_prefix}{command.qualified_name}``"

    async def send_bot_help(self, mapping):
        embed = discord.Embed(title='**BOT COMMANDS**', colour=self.COLOUR, image=client.user.avatar_url)
        # description = f'**{self.context.bot.description}**'

        commands_dict = {}

        for cog, commands in mapping.items():
            name = 'Uncategorized' if cog is None else cog.qualified_name
            filtered = await self.filter_commands(commands, sort=True)
            if filtered:
                commands_dict[name] = []
                for c in commands:
                    commands_dict.get(f"{name}").append(c)


        description = '**``[]``: OPTIONAL, ``<>``: REQUIRED**\n\n'

        for cog in commands_dict.keys():
            description = description + f"**{cog}**\n\n".upper()
            for command in commands_dict.get(cog):
                description = description + f"**{self.get_command_signature(command)}**\n\n"

        embed.description = description
        embed.set_footer(text=await self.get_ending_note())
        await self.get_destination().send(embed=embed)

    async def send_cog_help(self, cog):
        embed = discord.Embed(title='{0.qualified_name} Commands'.format(cog), colour=self.COLOUR,
                              image=client.user.avatar_url)
        if cog.description:
            embed.description = cog.description

        filtered = await self.filter_commands(cog.get_commands(), sort=True)
        for command in filtered:
            embed.add_field(name=self.get_command_signature(command), value=command.description or '...', inline=False)

        embed.set_footer(text=self.get_ending_note())
        await self.get_destination().send(embed=embed)

    async def send_group_help(self, group):
        embed = discord.Embed(title=group.qualified_name.upper(), colour=self.COLOUR, image=client.user.avatar_url)

        desc = ''

        if isinstance(group, commands.Group):
            filtered = await self.filter_commands(group.commands, sort=True)
            for command in filtered:
                desc = desc + f'**{self.get_command_signature(command)}**\n\n'

        embed.set_footer(text=f"Requester: {self.context.author}")
        embed.description = desc
        await self.get_destination().send(embed=embed)

    async def send_command_help(self, command):
        cog = 'Uncategorized' if command.cog is None else command.cog.qualified_name
        embed = discord.Embed(title=f"{command.name} - {cog}".upper(), colour=self.COLOUR, image=client.user.avatar_url, timestamp=datetime.datetime.utcnow())
        #embed.set_author(name=f"{self.context.author}", icon_url=self.context.author.avatar_url)
        no_desc = "No description assigned."
        command_aliases = ", ".join([f"``{i}``" for i in command.aliases])
        no_aliases = 'This command has no aliases.'

        if isinstance(command, commands.Command):
            embed.description = f"\n\n{self.get_command_signature(command)} - This is the correct usage of the ``{command.name}`` command. {command.description or no_desc}\n\nAliases: {command_aliases or no_aliases}"
            # embed.add_field(name=self.get_command_signature(command), value=command.description or 'No description assigned.', inline=False)

        embed.set_footer(text=f"Requester: {self.context.author}")

        # embed.set_footer(text=self.get_ending_note())
        await self.get_destination().send(embed=embed)


client = commands.Bot(command_prefix='r!', case_insensitive=True)
@client.event
async def on_ready():
    print(f"Ready. Logged onto {client.user}")
    activity = discord.Activity(type=discord.ActivityType.watching, name="Content Creators")
    await client.change_presence(activity=activity)

@client.event
async def on_member_join(member):
    SomeRandomEmbed = discord.Embed(
        title="**WELCOME MESSAGE**",
        description=f"*Welcome to the **{member.guild}**!*",
        color=0xffa200,
        timestamp=datetime.datetime.now(tz=None)
    )
    await member.send(embed=SomeRandomEmbed)

@client.command()
async def suggest(ctx):
    suggestionsChannel = client.get_channel(id=712655570737299567)
    startedEmbed = discord.Embed(
        title="**SUGGESTION SETUP**",
        description="Please continue the setup in dms.",
        color=0x0064ff,
        set_footer=f"{datetime.datetime.now(tz=None)} Reply to this message within `16 minutes`. Say `cancel` to cancel this prompt."
    )
    furstEmbed = discord.Embed(
        title="**SUGGESTION SETUP**",
        description="What would you like to name your suggestion?",
        color=0x0064ff,
        set_footer=f"{datetime.datetime.now(tz=None)} Reply to this message within `16 minutes`. Say `cancel` to cancel this prompt."
    )
    await ctx.send(embed=startedEmbed)
    await ctx.author.send(embed=furstEmbed)
    def check(m):
        if isinstance(m.channel, discord.DMChannel):
            if m.author == ctx.author:
                return True
            else:
                return False
        else:
            return False
    title_message = await client.wait_for('message', check=check, timeout=1000)
    title = title_message.content
    startEmbed = discord.Embed(
        title="**SUGGESTION SETUP**",
        description="Please write down your suggestion in detail.",
        color=0x0064ff,
        set_footer=f"{datetime.datetime.now(tz=None)} Reply to this message within `16 minutes`. Say `cancel` to cancel this prompt."
    )
    await ctx.author.send(embed=startEmbed)
    body_message = await client.wait_for('message', check=check, timeout=1000)
    body = body_message.content
    suggestedEmbed2 = discord.Embed(
        title=f"**FINISHED PRODUCT**",
        description=f"""*Say `done` to post.*""",
        color=0x0064ff,
        set_footer=f"{datetime.datetime.now(tz=None)} Reply to this message within `16 minutes`. Say `cancel` to cancel this prompt."
    )
    suggestedEmbed1 = discord.Embed(
        title=f"**{title}**",
        description=f"{body}",
        color=0x0064ff,
        set_footer=f"{datetime.datetime.now(tz=None)} Reply to this message within `16 minutes`. Say `cancel` to cancel this prompt."
    )
    suggestedEmbed1.set_footer(text=f"by: {ctx.author}")
    await ctx.author.send(embed=suggestedEmbed2)
    await ctx.author.send(embed=suggestedEmbed1)
    body_message2 = await client.wait_for('message', check=check, timeout=1000)
    body2 = body_message2.content
    if(body2 == "done"):
        finalEmbed = discord.Embed(
            title="**SUGGESTION SETUP**",
            description="Your suggestion has been posted.",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        await ctx.author.send(embed=finalEmbed)
        suggestedEmbed = discord.Embed(
            title=f"**{title}**",
            description=f"{body}",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
            )
        suggestedEmbed.set_footer(text=f"by: {ctx.author}")
        sent = await suggestionsChannel.send(embed=suggestedEmbed)
        await sent.add_reaction('👍')
        await sent.add_reaction('👎')

