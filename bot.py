import datetime
import os

import discord
from discord.ext import commands

from webserver import keep_alive


class EmbedHelpCommand(commands.MinimalHelpCommand):

    def __init__(self):
        super().__init__(command_attrs={
            'description': "This command will inform you about any command that you'd like to, or all the commands by leaving the command argument empty."
        })
        self.dm_help = False

    COLOUR = 0x1E90FF

    def command_not_found(self, string):
        return 'Command not found.'

    def get_command_signature(self, command):
        if command.signature:
            return f'``{self.clean_prefix}{command.qualified_name} {command.signature}``'
        else:
            return f"``{self.clean_prefix}{command.qualified_name}``"

    async def send_bot_help(self, mapping):
        embed = discord.Embed(title='**BOT COMMANDS**', colour=self.COLOUR, image=bot.user.avatar_url)
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
        await self.context.author.send(embed=embed)

    async def send_cog_help(self, cog):
        embed = discord.Embed(title='{0.qualified_name} Commands'.format(cog), colour=self.COLOUR,
                              image=bot.user.avatar_url)
        if cog.description:
            embed.description = cog.description

        filtered = await self.filter_commands(cog.get_commands(), sort=True)
        for command in filtered:
            embed.add_field(name=self.get_command_signature(command), value=command.description or '...', inline=False)

        await self.get_destination().send(embed=embed)

    async def send_group_help(self, group):
        embed = discord.Embed(title=group.qualified_name.upper(), colour=self.COLOUR, image=bot.user.avatar_url)

        desc = ''

        if isinstance(group, commands.Group):
            filtered = await self.filter_commands(group.commands, sort=True)
            for command in filtered:
                desc = desc + f'**{self.get_command_signature(command)}**\n\n'

        embed.description = desc
        await self.get_destination().send(embed=embed)

    async def send_command_help(self, command):
        cog = 'Uncategorized' if command.cog is None else command.cog.qualified_name
        embed = discord.Embed(title=f"{command.name} - {cog}".upper(), colour=self.COLOUR, image=bot.user.avatar_url,
                              timestamp=datetime.datetime.utcnow())
        # embed.set_author(name=f"{self.context.author}", icon_url=self.context.author.avatar_url)
        no_desc = "No description assigned."
        command_aliases = ", ".join([f"``{i}``" for i in command.aliases])
        no_aliases = 'This command has no aliases.'

        if isinstance(command, commands.Command):
            embed.description = f"\n\n{self.get_command_signature(command)} - This is the correct usage of the ``{command.name}`` command. {command.description or no_desc}\n\nAliases: {command_aliases or no_aliases} "
            # embed.add_field(name=self.get_command_signature(command), value=command.description or 'No description  assigned.', inline=False)

        await self.get_destination().send(embed=embed)


intents = discord.Intents.all()

bot = commands.Bot(commands.when_mentioned_or(">"), case_insensitive=True, help_command=EmbedHelpCommand(), intents=intents)


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

bot.run(token)
