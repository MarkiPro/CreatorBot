import discord
from discord.ext import commands
import datetime
import asyncio
from cogs.paginator import TextSplitter


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.help_command.cog = self

    @commands.command(aliases=["for-hire", "forhire"],
                      description="Toggle Not For Hire role off, and For Hire on, that way everyone knows you are for hire.")
    @commands.cooldown(1, 300, commands.BucketType.member)
    async def fh(self, ctx):
        cc_guild = self.bot.get_guild(id=611227128020598805)

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

    @commands.command(aliases=["not-for-hire", "notforhire"],
                      description="Toggle Not For Hire role off, and For Hire on, that way everyone knows you are for hire.")
    @commands.cooldown(1, 300, commands.BucketType.member)
    async def nfh(self, ctx):
        cc_guild = self.bot.get_guild(id=611227128020598805)

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
            category_message = await self.bot.wait_for('message', check=check, timeout=1000)
            category = category_message.content
        except asyncio.TimeoutError:
            await ctx.author.send(embed=cancel_prompt_embed)
            return
        if category == ['0']:
            await ctx.author.send(embed=cancel_prompt_embed)
            return
        elif category == "1":
            hiring_embed1 = discord.Embed(
                title="**HIRING POST**",
                description="***Tell us more about the job, you may freely go into detail as much as you feel like is needed.***",
                color=0x0064ff
            )
            hiring_embed1.set_footer(text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
            await ctx.author.send(embed=hiring_embed1)
            try:
                hiring_details_message = await self.bot.wait_for('message', check=check, timeout=1000)
                hiring_details = hiring_details_message.content
            except asyncio.TimeoutError:
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if hiring_details == ['0']:
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            hiring_embed2 = discord.Embed(
                title="**HIRING POST**",
                description="***Describe the payment to this job.***",
                color=0x0064ff
            )
            hiring_embed2.set_footer(text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
            await ctx.author.send(embed=hiring_embed2)
            try:
                hiring_payment_message = await self.bot.wait_for('message', check=check, timeout=1000)
                hiring_payment = hiring_payment_message.content
            except asyncio.TimeoutError:
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if hiring_payment == ['0']:
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            hiring_embed3 = discord.Embed(
                title="**HIRING POST**",
                description="***You may send links leading to the project ideas/screenshots, anything really.***",
                color=0x0064ff
            )
            hiring_embed3.set_footer(text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
            await ctx.author.send(embed=hiring_embed3)
            try:
                hiring_image_message = await self.bot.wait_for('message', check=check, timeout=1000)
                hiring_image = hiring_image_message.content
            except asyncio.TimeoutError:
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if hiring_image == ['0']:
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            hiring_embed4 = discord.Embed(
                title="**HIRING POST**",
                description="***In case you have something else that you would like to add onto the previous statements, please provide it now.***",
                color=0x0064ff
            )
            hiring_embed4.set_footer(text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
            await ctx.author.send(embed=hiring_embed4)
            try:
                hiring_other_message = await self.bot.wait_for('message', check=check, timeout=1000)
                hiring_other = hiring_other_message.content
            except asyncio.TimeoutError:
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if hiring_other == ['0']:
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            some_long_text = "blah blah blah blah test"
            text_splitter = TextSplitter(char_per_page=11, text=some_long_text)

            for i, entry in enumerate(text_splitter.words_list):
                prepared_embed = discord.Embed(
                    title="A simple Paginated thing")  # do not set the footer and descriping they get overriden.

                if i != 0:
                    prepared_embed.title = None

                prepared_embed.description = discord.utils.escape_mentions(entry)
                prepared_embed.set_footer(text=f"Page {i + 1} of {len(text_splitter.words_list)}")
                some_channel = self.bot.get_channel(id=712625020567814157)
                await some_channel.send(embed=hiring_embed4)

    #            await sent.add_reaction('👍')
    #            await sent.add_reaction('👎')

    @commands.command(aliases=['who'],
                      description="Displays basic information about the supplied user. If the user is not provided, it would default to the command requester.")
    async def whois(self, ctx, user: discord.Member = None):
        user = user or ctx.author

        join_pos = sum([m.joined_at < user.joined_at for m in ctx.guild.members if m.joined_at is not None])
        embed = discord.Embed(title=f"**Who is {user.name}**".upper(),
                              description="Displays basic information about the given user",
                              timestamp=datetime.datetime.utcnow(),
                              colour=0x0064ff)
        format = "%A, %d %B, %Y : %I:%M %p"
        delta_joined = datetime.datetime.utcnow() - user.joined_at
        delta_created = datetime.datetime.utcnow() - user.created_at
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="Joined on", value=f"{user.joined_at.strftime(format)} ({delta_joined.days} days)", inline=True)
        embed.add_field(name="Join Position", value=f"#{join_pos}", inline=True)
        embed.add_field(name="Account created on", value=f"{user.created_at.strftime(format)} ({delta_created.days} days)", inline=True)
        embed.add_field(name="Nickname", value=f"{user.nick}", inline=True)
        exculded_roles = [611227128020598805, 707957214995808296, 732375953203789965, 743590325448212651, 743013370588037191, 732388199107657828, 743013368511594569, 743013366515236915, 743013366880272474, 743013367840768072, 743013368134107166, 732387788493946881, 732402691296198848, 734149969292034208, 734150445764837466, 734150696944795698, 735497751978311681, 734527020905529375, 734664303327838230, 734527130565738516, 735557139984285706, 738814580712669214, 734664243038912552, 734527217350082672, 734527854871707762, 746758563703291938]
        roles = ", ".join(role.mention for role in user.roles if role.id not in exculded_roles) or 'No roles assigned.'
        embed.add_field(name="Guild Roles", value=f"{roles}", inline=False)
        notable_perms = ['administrator', 'manage_guild', 'view_audit_log', 'manage_roles', 'manage_channels', 'ban_members', 'kick_members', 'manage_messages', 'mention_everyone', 'manage_emojis', 'manage_webhooks', 'manage_nicknames', 'mute_members', 'deafen_members', 'move_members', 'priority_speaker']
        member_permissions = ", ".join(f"{i.title().replace('_', ' ')}" for i in notable_perms if getattr(ctx.author.permissions_in(ctx.channel), i, False)) or "No Permissions."
        embed.add_field(name="Guild Permissions", value=f"{member_permissions}", inline=False)
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


def setup(bot):
    bot.add_cog(Misc(bot))
