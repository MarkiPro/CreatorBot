import discord
from discord.ext import commands, tasks
import os
import asyncio
import datetime
import math

token = os.environ['TOKEN']

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
            'description': "This command will inform you about any command that you'd like to, or all the commands by leaving the command argument empty."
        })
        self.dm_help = False

    # Set the embed colour here
    COLOUR = 0x1E90FF

    def command_not_found(self, string):
        return 'Command not found.'

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
        await self.get_destination().send(embed=embed)

    async def send_cog_help(self, cog):
        embed = discord.Embed(title='{0.qualified_name} Commands'.format(cog), colour=self.COLOUR,
                              image=client.user.avatar_url)
        if cog.description:
            embed.description = cog.description

        filtered = await self.filter_commands(cog.get_commands(), sort=True)
        for command in filtered:
            embed.add_field(name=self.get_command_signature(command), value=command.description or '...', inline=False)

        await self.get_destination().send(embed=embed)

    async def send_group_help(self, group):
        embed = discord.Embed(title=group.qualified_name.upper(), colour=self.COLOUR, image=client.user.avatar_url)

        desc = ''

        if isinstance(group, commands.Group):
            filtered = await self.filter_commands(group.commands, sort=True)
            for command in filtered:
                desc = desc + f'**{self.get_command_signature(command)}**\n\n'

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

        await self.get_destination().send(embed=embed)

client = commands.Bot(command_prefix='>', case_insensitive=True, help_command=EmbedHelpCommand())

@client.event
async def on_ready():
    print(f"Ready. Logged onto {client.user}")
    activity = discord.Activity(type=discord.ActivityType.watching, name="Content Creators")
    await client.change_presence(activity=activity)
    send_meme.start()

for file in os.listdir('cogs/'):
    if file.endswith('.py'):
        print(f"LOADED {file}")
        client.load_extension(f'cogs.{file[:-3]}')

@client.command()
async def meme_config(ctx):
    send_meme.start()

@tasks.loop(seconds=3600)
async def send_meme():
    channel = client.get_channel(id=712625666490761297)
    embed = discord.Embed(title="A nice meme for you!", color=0xe700ff)
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=data[0]['url'])
            await channel.send(embed=embed)

@client.event
async def on_member_join(member):
    if client.get_guild(id=729495109963612270):
        content_creators = client.get_guild(id=611227128020598805)
        content_creators_staff = client.get_guild(id=729495109963612270)

        # CONTENT CREATORS

        content_creators_community_helper = discord.utils.get(content_creators.roles, id=712732582365757470)
        content_creators_senior_community_helper = discord.utils(content_creators.roles, id=722861996504121456)
        content_creators_head_community_helper = discord.utils.get(content_creators.roles, id=722860980782235819)
        content_creators_trial_application_reader = discord.utils(content_creators.roles, id=722860699327397950)
        content_creators_application_reader = discord.utils.get(content_creators.roles, id=722860570998603827)
        content_creators_senior_application_reader = discord.utils(content_creators.roles, id=722860303993405572)
        content_creators_head_application_reacer = discord.utils.get(content_creators.roles, id=722860184845680791)
        content_creators_trial_scam_investigator = discord.utils(content_creators.roles, id=722859531784421376)
        content_creators_scam_investigator = discord.utils.get(content_creators.roles, id=722859441350770719)
        content_creators_senior_scam_investigator = discord.utils(content_creators.roles, id=722859802690060430)
        content_creators_head_scam_investigator = discord.utils.get(content_creators.roles, id=722859343560704050)
        content_creators_trial_moderator = discord.utils(content_creators.roles, id=722792418922987550)
        content_creators_moderator = discord.utils(content_creators.roles, id=695328029303635998)
        content_creators_senior_moderator = discord.utils(content_creators.roles, id=722792492969492540)
        content_creators_head_moderator = discord.utils(content_creators.roles, id=722792338073714759)
        content_creators_administrator = discord.utils(content_creators.roles, id=695328300364464248)
        content_creators_senior_administrator = discord.utils(content_creators.roles, id=722791896480612362)
        content_creators_head_administrator = discord.utils(content_creators.roles, id=722791558088491038)
        content_creators_server_manager = discord.utils(content_creators.roles, id=722792808896921711)
        content_creators_founder = discord.utils(content_creators.roles, id=695328208844881972)

        # CONTENT CREATORS STAFF

        content_creators_staff_community_helper = discord.utils.get(content_creators_staff.roles, id=729495109984321537)
        content_creators_staff_senior_community_helper = discord.utils(content_creators_staff.roles, id=729495109984321538)
        content_creators_staff_head_community_helper = discord.utils.get(content_creators_staff.roles, id=729495109984321539)
        content_creators_staff_trial_application_reader = discord.utils(content_creators_staff.roles, id=729495109984321540)
        content_creators_staff_application_reader = discord.utils.get(content_creators_staff.roles, id=729495109984321541)
        content_creators_staff_senior_application_reader = discord.utils(content_creators_staff.roles, id=729495109984321542)
        content_creators_staff_head_application_reacer = discord.utils.get(content_creators_staff.roles, id=729495109984321543)
        content_creators_staff_trial_scam_investigator = discord.utils(content_creators_staff.roles, id=729495109984321544)
        content_creators_staff_scam_investigator = discord.utils.get(content_creators_staff.roles, id=729495109984321545)
        content_creators_staff_senior_scam_investigator = discord.utils(content_creators_staff.roles, id=729495109984321546)
        content_creators_staff_head_scam_investigator = discord.utils.get(content_creators_staff.roles, id=729495109984321547)
        content_creators_staff_trial_moderator = discord.utils(content_creators_staff.roles, id=729495109984321548)
        content_creators_staff_moderator = discord.utils(content_creators_staff.roles, id=729495109984321549)
        content_creators_staff_senior_moderator = discord.utils(content_creators_staff.roles, id=729495110001361000)
        content_creators_staff_head_moderator = discord.utils(content_creators_staff.roles, id=729495110001361001)
        content_creators_staff_administrator = discord.utils(content_creators_staff.roles, id=729495110001361002)
        content_creators_staff_senior_administrator = discord.utils(content_creators_staff.roles, id=729495110001361003)
        content_creators_staff_head_administrator = discord.utils(content_creators_staff.roles, id=729495110001361004)
        content_creators_staff_server_manager = discord.utils(content_creators_staff.roles, id=729495110001361005)
        content_creators_staff_founder = discord.utils(content_creators_staff.roles, id=729495110001361006)

        if member.has_role(content_creators_community_helper):
            member.add_role(content_creators_staff_community_helper)
        if member.has_role(content_creators_senior_community_helper):
            member.add_role(content_creators_staff_senior_community_helper)
        if member.has_role(content_creators_head_community_helper):
            member.add_role(content_creators_staff_head_community_helper)
        if member.has_role(content_creators_trial_application_reader):
            member.add_role(content_creators_staff_trial_application_reader)
        if member.has_role(content_creators_application_reader):
            member.add_role(content_creators_staff_application_reader)
        if member.has_role(content_creators_senior_application_reader):
            member.add_role(content_creators_staff_senior_application_reader)
        if member.has_role(content_creators_head_application_reader):
            member.add_role(content_creators_staff_head_application_reader)
        if member.has_role(content_creators_trial_scam_investigator):
            member.add_role(content_creators_staff_trial_scam_investigator)
        if member.has_role(content_creators_scam_investigator):
            member.add_role(content_creators_staff_scam_investigator)
        if member.has_role(content_creators_senior_scam_investigator):
            member.add_role(content_creators_staff_senior_scam_investigator)
        if member.has_role(content_creators_head_scam_investigator):
            member.add_role(content_creators_staff_head_scam_investigator)
        if member.has_role(content_creators_trial_moderator):
            member.add_role(content_creators_staff_trial_moderator)
        if member.has_role(content_creators_moderator):
            member.add_role(content_creators_staff_moderator)
        if member.has_role(content_creators_senior_moderator):
            member.add_role(content_creators_staff_senior_moderator)
        if member.has_role(content_creators_head_moderator):
            member.add_role(content_creators_staff_head_moderator)
        if member.has_role(content_creators_administrator):
            member.add_role(content_creators_staff_administrator)
        if member.has_role(content_creators_senior_administrator):
            member.add_role(content_creators_staff_senior_administrator)
        if member.has_role(content_creators_head_administrator):
            member.add_role(content_creators_staff_head_administrator)
        if member.has_role(content_creators_server_manager):
            member.add_role(content_creators_staff_server_manager)
        if member.has_role(content_creators_founder):
            member.add_role(content_creators_staff_founder)
        else:
            member.kick(reason="Not a staff member.")

    SomeRandomEmbed = discord.Embed(
        title="**WELCOME MESSAGE**",
        description=f"*Welcome to the **{member.guild}**!*",
        color=0xffa200,
        timestamp=datetime.datetime.now(tz=None)
    )
    await member.send(embed=SomeRandomEmbed)

@client.event
async def on_command_error(ctx, error):
    embed = discord.Embed(
        title="**ERROR**",
        description=f"***:no_entry_sign: {error}***",
        color=0xff0000
    )
    await ctx.send(embed=embed)

client.run(token)