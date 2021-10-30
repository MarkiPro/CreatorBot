import datetime
import os
import discord
from discord.ext import commands
from paginator import Paginator
from webserver import keep_alive

intents = discord.Intents.all()

bot = commands.Bot(commands.when_mentioned_or(">"), case_insensitive=True, intents=intents)


class EmbedHelpCommand(commands.MinimalHelpCommand):
    def __init__(self):
        super().__init__(command_attrs={
            'description': "This command will inform you about any command that you'd like to, or all the commands by leaving the command argument empty."
        })
        self.dm_help = False

    def command_not_found(self, string):
        return 'Command not found.'

    def get_command_signature(self, command):
        if command.signature:
            return f'``{self.clean_prefix}{command.qualified_name} {command.signature}``'
        else:
            return f"``{self.clean_prefix}{command.qualified_name}``"

    async def send_bot_help(self, mapping):

        commands_dict = {}

        for cog, bot_commands in mapping.items():
            name = 'Uncategorized' if cog is None else cog.qualified_name
            filtered = await self.filter_commands(bot_commands, sort=True)
            if filtered:
                commands_dict[name] = []
                for c in bot_commands:
                    commands_dict.get(f"{name}").append(c)

        description = '**``[]``: OPTIONAL, ``<>``: REQUIRED**\n\n'

        for cog in commands_dict.keys():
            description = description + f"**{cog}**\n\n".upper()
            for command in commands_dict.get(cog):
                description = description + f"**{self.get_command_signature(command)}**\n\n"

        pag = Paginator(description, 1985)
        await pag.send(bot=bot, channel=self.context.author, title='**BOT COMMANDS**')

    async def send_cog_help(self, cog):

        title = f'{cog.qualified_name} Commands'

        description = ""

        if cog.description:
            description = cog.description

        filtered = await self.filter_commands(cog.get_commands(), sort=True)
        for command in filtered:
            description += f"\n{self.get_command_signature(command)}\n{command.description or '...'}\n"

        pag = Paginator(description, 1985)
        await pag.send(bot=bot, channel=self.get_destination(), title=title)

    async def send_group_help(self, group):

        title = group.qualified_name.upper()
        description = ''

        if isinstance(group, commands.Group):
            filtered = await self.filter_commands(group.commands, sort=True)
            for command in filtered:
                description += f'**{self.get_command_signature(command)}**\n\n'

        pag = Paginator(description, 1985)

        await pag.send(bot=bot, channel=self.get_destination(), title=title)

    async def send_command_help(self, command):
        cog = 'Uncategorized' if command.cog is None else command.cog.qualified_name
        no_desc = "No description assigned."
        command_aliases = ", ".join([f"``{i}``" for i in command.aliases])
        no_aliases = 'This command has no aliases.'

        title = f"{command.name} - {cog}".upper()

        description = ""

        if isinstance(command, commands.Command):
            description = f"\n\n{self.get_command_signature(command)} - This is the correct usage of the ``{command.name}`` command. {command.description or no_desc}\n\nAliases: {command_aliases or no_aliases} "

        pag = Paginator(description, 1985)
        await pag.send(bot=self.bot, channel=self.get_destination(), title=title)


bot.help_command = EmbedHelpCommand()


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
