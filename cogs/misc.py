import discord
from discord.ext import commands
import datetime
import asyncio

class Misc(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.client.help_command.cog = self

    @commands.command(description="This command is used for posting hiring requests.")
    @commands.cooldown(4, 10800, commands.BucketType.member)
    async def post(self, ctx):
        cancel_prompt_embed = discord.Embed(
            title="**CANCELLED**",
            description="***The setup has been cancelled.***",
            color=0xff0000,
            timestamp=datetime.datetime.now(tz=None)
        )
        categories_embed = discord.Embed(
            title="**POST SETUP**",
            description="***Please continue the setup in DMs.***",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
        )
        categories = discord.Embed(
            title="**POST SETUP**",
            description="""
            ***What would you like to do? Reply with the number in front of the category you would like to post in.***


                **1** `hiring`;
            
                **2** `for-hire`;
            
                **3** `suggestions`;
            
                **4** `report`;
            """
        )
        categories.set_footer(text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
        title_embed = discord.Embed(
            title="**POST SETUP**",
            description="***How would you like to name your post?***",
            color=0x0064ff
        )
        title_embed.set_footer(text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
        await ctx.send(embed=categories_embed)
        await ctx.author.send(embed=categories)
        def check(m):
            if isinstance(m.channel, discord.DMChannel):
                if m.author == ctx.author:
                    return True
                else:
                    return False
            else:
                return False
        try:
            category_message = await client.wait_for('message', check=check, timeout=1000)
            category = category_message.content
        except asyncio.TimeoutError or category == ['0']:
            await ctx.author.send(embed=cancel_prompt_embed)
            return
        if category == "1":
            hiring_categories_embed = discord.Embed(
                title="**POST SETUP**",
                description=f"""
                ***Reply with a number in front of the hiring category you would like to post in.***


                    **1** - `programmer-hiring`;

                    **2** - `scripter-hiring`;

                    **3** - `gfx-designer-hiring`;

                    **4** - `artist-hiring`;

                    **5** - `modeler-hiring`;

                    **6** - `builder-hiring`;

                    **7** - `staff-hiring`;

                    **8** - `ui-designer-hiring`;

                    **9** - `animator-hiring`;

                    **10** - `tutor-hiring`;

                    **11** - `music-composer-hiring`;

                    **12** - `clothing-designer-hiring`.
                """,
                color=0x0064ff
            )
            hiring_categories_embed.set_footer(text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
            await ctx.author.send(embed=hiring_categories_embed)
            try:
                hiring_category_message = await client.wait_for('message', check=check, timeout=1000)
                hiring_category = hiring_category_message.content
            except asyncio.TimeoutError or category == ['0']:
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if hiring_category == "1":
                programmer_hiring_embed = discord.Embed(
                    title="**PROGRAMMER HIRING POST**",
                    description="***Tell us more about the job, you may freely go into detail as much as you feel like is needed.***",
                    color=0x0064ff
                )
                programmer_hiring_embed.set_footer(text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
                await ctx.author.send(embed=programmer_hiring_embed)
                try:
                    programmer_hiring_details_message = await client.wait_for('message', check=check, timeout=1000)
                    programmer_hiring_details = programmer_hiring_details_message.content
                except asyncio.TimeoutError or programmer_hiring_details == ['0']:
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_hiring_embed2 = discord.Embed(
                    title="**PROGRAMMER HIRING POST**",
                    description="***Describe the payment to this job.***",
                    color=0x0064ff
                )
                programmer_hiring_embed2.set_footer.set_footer(text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
                await ctx.author.send(embed=programmer_hiring_embed2)
                try:
                    programmer_hiring_payment_message = await client.wait_for('message', check=check, timeout=1000)
                    programmer_hiring_payment = programmer_hiring_payment_message.content
                except asyncio.TimeoutError or programmer_hiring_payment == ['0']:
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_hiring_embed3 = discord.Embed(
                    title="**PROGRAMMER HIRING POST**",
                    description="***You may send links leading to the project ideas/screenshots, anything really.***",
                    color=0x0064ff
                )
                programmer_hiring_embed3.set_footer.set_footer(text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
                await ctx.author.send(embed=programmer_hiring_embed3)
                try:
                    programmer_hiring_image_message = await client.wait_for('message', check=check, timeout=1000)
                    programmer_hiring_image = programmer_hiring_other_message.content
                except asyncio.TimeoutError or programmer_hiring_other == ['0']:
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_hiring_embed4.set_footer.set_footer(text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
                await ctx.author.send(embed=programmer_hiring_embed3)
                try:
                    programmer_hiring_other_message = await client.wait_for('message', check=check, timeout=1000)
                    programmer_hiring_other = programmer_hiring_other_message.content
                except asyncio.TimeoutError or programmer_hiring_other == ['0']:
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                some_long_text = "blah blah ISUIBGUIBOIOGERONGIPOENOGPA"
                text_splitter = TextSplitter(char_per_page=11, text=some_long_text)

                for i, entry in enumerate(text_splitter.words_list):
                    prepared_embed = discord.Embed(title="A simple Paginated thing") # do not set the footer and descriping they get overriden.
                    
                    if i != 0:
                        prepared_embed.title = None
                    
                    prepared_embed.description = discord.utils.escape_mentions(entry)
                    prepared_embed.set_footer(text=f"Page {i + 1} of {len(text_splitter.words_list)}")
                    some_channel = client.get_channel(id=729498148057382994)
                    
                    await some_channel.send(embed=prepared_embed)
                

    @commands.command(aliases=['suggestion'], description="This command is used for suggesting useful ideas!")
    async def suggest(self, ctx):
        suggestionsChannel = client.get_channel(id=712655570737299567)
        cancel_prompt_embed = discord.Embed(
            title="**CANCELLED**",
            description="***The setup has been cancelled.***",
            color=0xff0000,
            timestamp=datetime.datetime.now(tz=None)
        )
        startedEmbed = discord.Embed(
            title="**SUGGESTION SETUP**",
            description="***Please continue the setup in DMs.***",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
        )
        startedEmbed.set_footer(text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
        furstEmbed = discord.Embed(
            title="**SUGGESTION SETUP**",
            description="***What would you like to name your suggestion?***",
            color=0x0064ff
        )
        furstEmbed.set_footer(text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
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
        try:
            title_message = await client.wait_for('message', check=check, timeout=1000)
            title = title_message.content
        except asyncio.TimeoutError or title == ['cancel', 'Cancel', 'CaNcEl', 'cAnCeL', 'cAncel', 'caNcel', 'canCel', 'cancEl', 'canceL', 'CANcel', 'CANCEL']:
            await ctx.author.send(embed=cancel_prompt_embed)
            return
        startEmbed = discord.Embed(
            title="**SUGGESTION SETUP**",
            description="***Please write down your suggestion in detail.***",
            color=0x0064ff,
        )
        startEmbed.set_footer(text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
        await ctx.author.send(embed=startEmbed)
        try:
            body_message = await client.wait_for('message', check=check, timeout=1000)
            body = body_message.content
        except TimeoutError or body == ['cancel', 'Cancel', 'CaNcEl', 'cAnCeL', 'cAncel', 'caNcel', 'canCel', 'cancEl', 'canceL', 'CANcel', 'CANCEL']:
            await ctx.author.send(embed=cancel_prompt_embed)
            return
        suggestedEmbed2 = discord.Embed(
            title=f"**FINISHED PRODUCT**",
            description=f"""***Say `done` to post.***""",
            color=0x0064ff,
        )
        suggestedEmbed2.set_footer(text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
        suggestedEmbed1 = discord.Embed(
            title=f"**{title}**",
            description=f"{body}",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
        )
        suggestedEmbed1.set_footer(text=f"by: {ctx.author}")
        await ctx.author.send(embed=suggestedEmbed2)
        await ctx.author.send(embed=suggestedEmbed1)
        try:
            body_message2 = await client.wait_for('message', check=check, timeout=1000)
            body2 = body_message2.content
        except asyncio.TimeoutError or body2 == ['cancel', 'Cancel', 'CaNcEl', 'cAnCeL', 'cAncel', 'caNcel', 'canCel', 'cancEl', 'canceL', 'CANcel', 'CANCEL']:
            await ctx.author.send(embed=cancel_prompt_embed)
            return
        if body2 == ['Done', 'dOne', 'DonE', 'DOne', 'DONe', 'DONE', 'done', 'donE', 'doNe', 'DoNe', 'DOnE', 'dOnE', 'doNE', 'DoNE', 'dONE']:
            finalEmbed = discord.Embed(
                title="**SUGGESTION SETUP**",
                description="***Your suggestion has been posted.***",
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
        else:
            await ctx.author.send(embed=cancel_prompt_embed)

    @commands.command(aliases=['who'],
                    description="Displays basic information about the supplied user. If the user is not provided, it would default to the command requester.")
    async def whois(self, ctx, user: discord.Member = None):
        if not user:
            user = ctx.message.author

        embed = discord.Embed(title=f"**Who is {user.name}**".upper(),
                              description="Displays basic information about the given user", colour=0xd9ac32)
        format = "%A, %d %B, %Y : %I:%M %p"
        delta_joined = datetime.datetime.utcnow() - user.joined_at
        delta_created = datetime.datetime.utcnow() - user.created_at
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="Joined on", value=f"{user.joined_at.strftime(format)} ({delta_joined.days} days)",
                        inline=True)
        embed.add_field(name="Account created on",
                        value=f"{user.created_at.strftime(format)} ({delta_created.days} days)", inline=True)
        embed.add_field(name="Nickname", value=f"{user.nick}", inline=True)
        roles = ", ".join([i.mention for i in user.roles if i.name != '@everyone']) or "No roles assigned."
        embed.add_field(name="Guild Roles", value=f"{roles}", inline=False)
        perms = ", ".join(list(i[0].title() for i in user.guild_permissions if i[1] == True)) or "No permissions in the guild."
        embed.add_field(name="Guild Permissions",
                        value=f"{perms}",
                        inline=False)
        await ctx.send(embed=embed)

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
            embed.description = "There are no boosters in this guild.  :cry:"

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Misc(client))