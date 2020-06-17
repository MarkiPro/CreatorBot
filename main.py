import discord
from discord.ext import commands
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


client = commands.Bot(command_prefix='>', case_insensitive=True, help_command=EmbedHelpCommand())
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

    @commands.command()
    async def boosters(self, ctx):

        boosters = "\n".join([i.mention for i in ctx.guild.premium_subscribers])

        embed = discord.Embed(
            title="**BOOSTERS**",
            description=f"***These are the boosters on the server:\n\n***{boosters}",
            color=0x0089ff,
            timestamp=datetime.datetime.utcnow()
            )

        if boosters is "":
            embed.description = "There are no boosters in this guild  :cry:"

        await ctx.send(embed=embed)

    @commands.command()
    async def dog(self, ctx):
        message = await ctx.send("Generating a dog image for you!")
        request = requests.get('https://dog.ceo/api/breeds/image/random')
        data = request.json()
        request.close()
        embed = discord.Embed(title=f"A nice dog, for you!", colour=discord.Color.blurple())
        embed.set_image(url=data['message'])
        await ctx.send(embed=embed)
        await message.edit("Here is a dog image for you")

    @commands.command()
    async def cat(self, ctx):
        await ctx.send("Generating a cat image for you!")
        request = requests.get("https://api.thecatapi.com/v1/images/search", params={'limit': 1})
        data = request.json()
        request.close()
        embed = discord.Embed(title=f"A nice cat, for you!", colour=discord.Color.blurple())
        embed.set_image(url=data[0]['url'])
        await ctx.send(embed=embed)


    @commands.command()
    async def mushroom(self, ctx, member: discord.Member, *, reason):
        await ctx.send(f"{member.mention} has been mushroomed for `{reason}`")

        def check(m):
            if m.author.id == member.id:
                return True
            else:
                return False

        message = await self.client.wait_for('message', check=check)

        await message.add_reaction(":timthemushroom:716208401675452437")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def bean(self, ctx, member: discord.Member, *, reason=None):

        await ctx.send(f"{member} were beaned for `{reason}`")

        await member.send("https://tenor.com/EQmg.gif")

        def check(m):
            if m.author == member:
                return True
            else:
                return False
        
        message = await self.client.wait_for("message", check=check)

        await message.add_reaction(":bean:721246373957074984")

    @commands.command(name="8ball")
    async def Magic8Ball(self, ctx, *, question):
        random_answers = ['Is Einstein bold? I think not!', 'Can we time travel? Science says yes!', 'Ahh, maybe.', 'That is a yes.', 'Nah, I am good', 'I would love to, but unfortunately... no.', 'The idea is not compatible with myself.', 'I think I will go find a lake of piranhas to jump in instead.', 'My schedule is packed with better things', 'There are worse things I could agree to, I just cannot think of any at the moment.', 'There are many cool things to do. ***Your idea does not fall into such a category.***', 'You\’re not giving me that much of a choice, huh?', 'Then, let’s seal it with a kiss.', 'Just be sure to pay me back later.', 'Just be sure that we won’t get caught.', 'Life\’s too short to be saying no.', 'Who put you up to this? Tell me!', 'Kiss my butt first.', 'Have you forgotten? I’m a yes-man!', 'Thought you\’d never ask!', 'Hell, you bet-cha, matey!', 'I\’ll even kiss you!', 'Even my dog is saying yes.', 'Let\’s say I agreed to this. But, can I still change my mind later?', 'My answer would probably be yes, but I totally forgot—I have another appointment!', 'You should know my answer by the way I\’m nodding my head up and down.', 'Just be sure that we won\’t go to jail for this.', 'If I say yes, will you give me a million bucks?', 'Abso-f*kin-lutely!', 'Preach!', 'What are we waiting for? Let\’s close the deal!', 'Probably yes, but I\’ll have my people call your people to discuss.', 'Well then, what are we waiting for?', 'There\’s a chance that I might regret this, but—YOLO—let\’s do it!', 'Even if I hate you, I would say yes to this one.', 'Say no more!', 'It would take a whole army to keep me from saying yes.', 'Right on the money!', 'Yes, yes, and yes!', 'If there\’s a reward, I\’m in!', 'Hallelujah!', 'You get my vote.', 'I\’m here to the rescue!', 'It\’s fine now. Why? Because I\’m here!', 'I love you, so yeah.', 'I don\’t have a choice, do I?', 'Let me check my schedule first. Oh, I\’m available.', 'Take off your clothes because you\’ve hit the spot!', 'Why, that\'s the nicest offer I\'ve had all day!', 'Give me a \‘ **Y**.\’ Give me an \‘ **E**.\’ Give me an \‘ **S**.\’ Give me a \‘ **Y-E-S!**\’', 'May-be!', 'Do aliens even exist? Maybe!', '**M**y **A**rt **Y**ikes **B**asketball **E**ar!', 'I.... don\'t know! 😢']

        await ctx.send(random.choice(random_answers))

@client.command(description="This command is used for suggesting useful ideas!")
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

client.run(token)