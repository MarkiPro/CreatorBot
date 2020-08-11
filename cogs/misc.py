import discord
from discord.ext import commands
import datetime
import asyncio
from main import client

class Misc(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.client.help_command.cog = self

    @commands.command(aliases=["for-hire", "forhire"], description="Toggle Not For Hire role off, and For Hire on, that way everyone knows you are for hire.")
    @commands.cooldown(1, 300, commands.BucketType.member)
    async def fh(self, ctx):
        cc_guild = client.get_guild(id=611227128020598805)
        
        nfh_role = discord.utils.get(cc_guild.roles, id=729491617630912613)
        fh_role = discord.utils.get(cc_guild.roles, id=738814225614635100)

        member = ctx.author

        embed1 = discord.Embed(
            title="**ERROR**",
            description="***:no_entry_sign: You already have the `For Hire` role.***",
            color=0xff0000
        )

        embed3 = discord.Embed(
            title="**SUCCESS**",
            description="***:white_check_mark: Removed the `Not For Hire` role.***",
            color=0x00fa00
        )

        embed2 = discord.Embed(
            title="**SUCCESS**",
            description="***:white_check_mark: You now have the `For Hire` role.***",
            color=0x00fa00
        )

        if nfh_role in member.roles:
            await member.remove_roles(nfh_role)
            await member.add_roles(fh_role)
            await member.send(embed=embed3)
            await member.send(embed=embed2)
            return
        if nfh_role and fh_role not in member.roles:
            await member.add_roles(fh_role)
            await member.send(embed=embed2)
            return
        if fh_role in member.roles:
            await member.send(embed=embed1)
            return
        
    @commands.command(aliases=["not-for-hire", "notforhire"], description="Toggle Not For Hire role off, and For Hire on, that way everyone knows you are for hire.")
    @commands.cooldown(1, 300, commands.BucketType.member)
    async def nfh(self, ctx):
        cc_guild = client.get_guild(id=611227128020598805)
        
        nfh_role = discord.utils.get(cc_guild.roles, id=729491617630912613)
        fh_role = discord.utils.get(cc_guild.roles, id=738814225614635100)

        member = ctx.author

        embed1 = discord.Embed(
            title="**ERROR**",
            description="***:no_entry_sign: You already have the `Not For Hire` role.***",
            color=0xff0000
        )

        embed3 = discord.Embed(
            title="**SUCCESS**",
            description="***:white_check_mark: Removed the `For Hire` role.***",
            color=0x00fa00
        )

        embed2 = discord.Embed(
            title="**SUCCESS**",
            description="***:white_check_mark: You now have the `Not For Hire` role.***",
            color=0x00fa00
        )

        if fh_role in member.roles:
            await member.remove_roles(fh_role)
            await member.add_roles(nfh_role)
            await member.send(embed=embed3)
            await member.send(embed=embed2)
            return
        if nfh_role and fh_role not in member.roles:
            await member.add_roles(nfh_role)
            await member.send(embed=embed2)
            return
        if nfh_role in member.roles:
            await member.send(embed=embed1)
            return

    @commands.command(description="This command is used for posting hiring requests.")
    @commands.cooldown(3, 10800, commands.BucketType.member)
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


                **1** - `hiring`;
            
                **2** - `for-hire`;
            
                **3** - `suggestions`;
            
                **4** - `report`;

            """,
            color=0x0064ff
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
            hiring_embed1 = discord.Embed(
                title="**HIRING POST**",
                description="***Tell us more about the job, you may freely go into detail as much as you feel like is needed.***",
                color=0x0064ff
            )
            hiring_embed1.set_footer(text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
            await ctx.author.send(embed=hiring_embed1)
            try:
                hiring_details_message = await client.wait_for('message', check=check, timeout=1000)
                hiring_details = hiring_details_message.content
            except asyncio.TimeoutError or hiring_details == ['0']:
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            hiring_embed2 = discord.Embed(
                title="**HIRING POST**",
                description="***Describe the payment to this job.***",
                color=0x0064ff
            )
            hiring_embed2.set_footer.set_footer(text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
            await ctx.author.send(embed=hiring_embed2)
            try:
                hiring_payment_message = await client.wait_for('message', check=check, timeout=1000)
                hiring_payment = hiring_payment_message.content
            except asyncio.TimeoutError or hiring_payment == ['0']:
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            hiring_embed3 = discord.Embed(
                title="**HIRING POST**",
                description="***You may send links leading to the project ideas/screenshots, anything really.***",
                color=0x0064ff
            )
            hiring_embed3.set_footer.set_footer(text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
            await ctx.author.send(embed=hiring_embed3)
            try:
                hiring_image_message = await client.wait_for('message', check=check, timeout=1000)
                hiring_image = hiring_other_message.content
            except asyncio.TimeoutError or hiring_other == ['0']:
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            hiring_embed4 = discord.Embed(
                title="**HIRING POST**",
                description="***In case you have something else that you would like to add onto the previous statements, please provide it now.***",
                color=0x0064ff
            )
            hiring_embed4.set_footer.set_footer(text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
            await ctx.author.send(embed=hiring_embed3)
            try:
                hiring_other_message = await client.wait_for('message', check=check, timeout=1000)
                hiring_other = hiring_other_message.content
            except asyncio.TimeoutError or hiring_other == ['0']:
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            some_long_text = "blah blah blah blah test"
            text_splitter = TextSplitter(char_per_page=11, text=some_long_text)

            for i, entry in enumerate(text_splitter.words_list):
                prepared_embed = discord.Embed(title="A simple Paginated thing") # do not set the footer and descriping they get overriden.
                
                if i != 0:
                    prepared_embed.title = None
                
                prepared_embed.description = discord.utils.escape_mentions(entry)
                prepared_embed.set_footer(text=f"Page {i + 1} of {len(text_splitter.words_list)}")
                some_channel = client.get_channel(id=712659793008918538)
                
                await some_channel.send(embed=prepared_embed)
    
    @commands.command(aliases=["chat-color", "color-chat", "chatcolor", "colorchat", "chat"], description="This command is used for chaning the color of your name in chat!")
    @commands.cooldown(1, 300, commands.BucketType.member)
    async def color(self, ctx):
        
        content_creators = client.get_guild(id=611227128020598805)

        sever_booster = discord.utils.get(content_creators.roles, id=712685506424471612)
        python_programmer = discord.utils.get(content_creators.roles, id=732377712286761001)
        game_designer = discord.utils.get(content_creators.roles, id=733281086913773599)
        threed_modeler = discord.utils.get(content_creators.roles, id=733281157872877629)
        csharp_programmer = discord.utils.get(content_creators.roles, id=732377857317142650)
        youtuber = discord.utils.get(content_creators.roles, id=738788543211634756)
        java_programmer = discord.utils.get(content_creators.roles, id=732379273100263464)
        roblox_studio_builder = discord.utils.get(content_creators.roles, id=733281281671954442)
        twitch_streamer = discord.utils.get(content_creators.roles, id=738814393663619182)
        js_programmer = discord.utils.get(content_creators.roles, id=732377955669508097)
        gfx_designer = discord.utils.get(content_creators.roles, id=733280979921141821)
        cpp_programmer = discord.utils.get(content_creators.roles, id=732377777772167188)
        translator = discord.utils.get(content_creators.roles, id=734527264657637416)
        c_programmer = discord.utils.get(content_creators.roles, id=732378157449216040)
        ui_designer = discord.utils.get(content_creators.roles, id=733274530524561430)
        php_programmer = discord.utils.get(content_creators.roles, id=732378321387520092)
        clothing_designer = discord.utils.get(content_creators.roles, id=734177621876801637)
        lua_programmer = discord.utils.get(content_creators.roles, id=732376072397783093)
        artist = discord.utils.get(content_creators.roles, id=734662196025360416)
        ruby_programmer = discord.utils.get(content_creators.roles, id=735147661430227025)
        music_composer = discord.utils.get(content_creators.roles, id=735497558855516161)
        html_programmer = discord.utils.get(content_creators.roles, id=735147383716970507)
        animator = discord.utils.get(content_creators.roles, id=734662028353994752)

    @commands.command(aliases=['suggestion'], description="This command is used for suggesting cool ideas!")
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