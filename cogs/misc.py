import discord
from discord.ext import commands
import datetime
import asyncio
from paginator import Paginator
import re
from cooldown import Cooldown
import mystbin


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.formats_list = ["python", "lua", "c++", "csharp", "cpp", "cs", "css", "html", "json", "go", "js", "javascript", "java", "py", "c"]
        self.bot.help_command.cog = self
        self.hiring_cool = Cooldown(time=datetime.datetime.utcfromtimestamp(0))
        self.for_hire_cool = Cooldown(time=datetime.datetime.utcfromtimestamp(0))
        self.sell_creations_cool = Cooldown(time=datetime.datetime.utcfromtimestamp(0))
        self.report_cool = Cooldown(time=datetime.datetime.utcfromtimestamp(0))
        self.cpp_programmer_cool = Cooldown(time=datetime.datetime.utcfromtimestamp(0))
        self.lua_programer_cool = Cooldown(time=datetime.datetime.utcfromtimestamp(0))
        self.csharp_programmer_cool = Cooldown(time=datetime.datetime.utcfromtimestamp(0))
        self.java_programmer_cool = Cooldown(time=datetime.datetime.utcfromtimestamp(0))
        self.python_programmer_cool = Cooldown(time=datetime.datetime.utcfromtimestamp(0))
        self.javascript_programmer_cool = Cooldown(time=datetime.datetime.utcfromtimestamp(0))
        self.html_and_css_programmer_cool = Cooldown(time=datetime.datetime.utcfromtimestamp(0))
        self.ruby_programmer_cool = Cooldown(time=datetime.datetime.utcfromtimestamp(0))
        self.c_programmer_cool = Cooldown(time=datetime.datetime.utcfromtimestamp(0))
        self.php_programmer_cool = Cooldown(time=datetime.datetime.utcfromtimestamp(0))
        self.music_composer_cool = Cooldown(time=datetime.datetime.utcfromtimestamp(0))
        self.artist_cool = Cooldown(time=datetime.datetime.utcfromtimestamp(0))
        self.twitch_streamer_cool = Cooldown(time=datetime.datetime.utcfromtimestamp(0))
        self.youtuber_cool = Cooldown(time=datetime.datetime.utcfromtimestamp(0))
        self.translator_cool = Cooldown(time=datetime.datetime.utcfromtimestamp(0))
        self.roblox_studio_builder_cool = Cooldown(time=datetime.datetime.utcfromtimestamp(0))
        self.ui_designer_cool = Cooldown(time=datetime.datetime.utcfromtimestamp(0))
        self.animator_cool = Cooldown(time=datetime.datetime.utcfromtimestamp(0))
        self.game_designer_cool = Cooldown(time=datetime.datetime.utcfromtimestamp(0))
        self.threed_modeler_cool = Cooldown(time=datetime.datetime.utcfromtimestamp(0))
        self.clothing_designer_cool = Cooldown(time=datetime.datetime.utcfromtimestamp(0))
        self.gfx_designer_cool = Cooldown(time=datetime.datetime.utcfromtimestamp(0))

    @commands.command(aliases=["for-hire", "forhire"],
                      description="Toggle Not For Hire role off, and For Hire on, that way everyone knows you are for hire.")
    @commands.cooldown(1, 300, commands.BucketType.member)
    async def fh(self, ctx):
        allowed_channels = [712659793008918538, 712624774479740931, 712624686399225907, 722898958996865035]

        if ctx.channel.id not in allowed_channels:
            await ctx.send("Run the command again in <#712659793008918538>")
            return
        cc_guild = self.bot.get_guild(id=611227128020598805)

        nfh_role = discord.utils.get(cc_guild.roles, id=729491617630912613)
        fh_role = discord.utils.get(cc_guild.roles, id=738814225614635100)

        member = ctx.author

        embed1 = discord.Embed(
            title="**ERROR**",
            description="***:no_entry_sign: You already have the `For Hire` role.***",
            color=0xff0000,
            timestamp=datetime.datetime.utcnow()
        )

        embed3 = discord.Embed(
            title="**SUCCESS**",
            description="***:white_check_mark: Removed the `Not For Hire` role.***",
            color=0x00fa00,
            timestamp=datetime.datetime.utcnow()
        )

        embed2 = discord.Embed(
            title="**SUCCESS**",
            description="***:white_check_mark: You now have the `For Hire` role.***",
            color=0x00fa00,
            timestamp=datetime.datetime.utcnow()
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
        allowed_channels = [712659793008918538, 712624774479740931, 712624686399225907, 722898958996865035]

        if ctx.channel.id not in allowed_channels:
            await ctx.send("Run the command again in <#712659793008918538>")
            return
        cc_guild = self.bot.get_guild(id=611227128020598805)

        nfh_role = discord.utils.get(cc_guild.roles, id=729491617630912613)
        fh_role = discord.utils.get(cc_guild.roles, id=738814225614635100)

        member = ctx.author

        embed1 = discord.Embed(
            title="**ERROR**",
            description="***:no_entry_sign: You already have the `Not For Hire` role.***",
            color=0xff0000,
            timestamp=datetime.datetime.utcnow()
        )

        embed3 = discord.Embed(
            title="**SUCCESS**",
            description="***:white_check_mark: Removed the `For Hire` role.***",
            color=0x00fa00,
            timestamp=datetime.datetime.utcnow()
        )

        embed2 = discord.Embed(
            title="**SUCCESS**",
            description="***:white_check_mark: You now have the `Not For Hire` role.***",
            color=0x00fa00,
            timestamp=datetime.datetime.utcnow()
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

    @commands.command()
    async def credits(self, ctx):
        malware = await ctx.bot.fetch_user(730082562868772924)
        markipro = await ctx.bot.fetch_user(530461779768377357)

        credits_embed = discord.Embed(
            title="**Credits**",
            description=f"Bot Creator: **{markipro}**\nHuge thank you to **{malware}**!",
            timestamp=datetime.datetime.utcnow(),
            color=0x0064ff
        )
        await ctx.send(embed=credits_embed)

    @commands.command(description="This command is used for applying for appliable roles (STAFF ROLES NOT INCLUDED!).")
    async def apply(self, ctx):
        allowed_channels = [712659793008918538, 712624774479740931, 712624686399225907, 722898958996865035]
        applications_muted = ctx.guild.get_role(780494171730477086)

        if ctx.author in applications_muted.members:
            return await ctx.send("You are restricted from using this command, you have the `Applications Muted` role. Please consult with a staff member about it.")
        else:
            pass
        if ctx.channel.id not in allowed_channels:
            await ctx.send("Run the command again in <#712659793008918538>")
            return
        cancel_prompt_embed = discord.Embed(
            title="**CANCELLED**",
            description="***The setup has been cancelled.***",
            color=0xff0000,
            timestamp=datetime.datetime.utcnow()
        )
        pre_DM_embed = discord.Embed(
            title="**APPLICATION SETUP**",
            description="***Please continue the setup in DMs.***",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
        )
        categories = discord.Embed(
            title="**APPLICATION SETUP**",
            description="""
            ***Which role would you like to apply for? Reply below with the name of the role you would like to apply for.***


                `Programmer`;

                `Game Designer`;

                `3D Modeler`;

                `YouTuber`;
                
                `Roblox Builder`;
                
                `Twitch Streamer`;
                
                `GFX Designer`;
                
                `Translator`;
                
                `UI Designer`;
                
                `Clothing Designer`;
                
                `Artist`;
                
                `Music Composer`;
                
                `Animator`;
                
            """,
            color=0x0064ff,
            timestamp=datetime.datetime.utcnow()
        )
        categories.set_footer(text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
        await ctx.send(embed=pre_DM_embed)
        await ctx.author.send(embed=categories)

        def check_dm(m):
            if isinstance(m.channel, discord.DMChannel):
                if m.author == ctx.author:
                    return True
                else:
                    return False
            else:
                return False
        try:
            picked_category_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
            category = picked_category_message.content
        except asyncio.TimeoutError:
            cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
            await ctx.author.send(embed=cancel_prompt_embed)
            return
        if category.lower() == "cancel":
            cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
            await ctx.author.send(embed=cancel_prompt_embed)
            return

        if re.findall("programmer", category, re.IGNORECASE):
            programmer_categories = discord.Embed(
                title="**APPLICATION SETUP**",
                description="""
                Which Programmer role would you like to apply for? Reply with the name of the role you would like to apply for.

                `Python Programmer`;

                `C# Programmer`;

                `Java Programmer`;

                `JavaScript Programmer`;

                `CPP Programmer`;

                `C Programmer`;

                `PHP Programmer`;

                `Lua Programmer`;

                `Ruby Programmer`;

                `HTML & CSS Programmer`;

                `CSS Programmer`;""",
                color=0x0064ff,
                timestamp=datetime.datetime.utcnow()
            )
            programmer_categories.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=programmer_categories)
            try:
                picked_programmer_category_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                programmer_category = picked_programmer_category_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if programmer_category.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            elif re.findall("python programmer", programmer_category, re.IGNORECASE):
                if self.python_programmer_cool.cooldown_start_time != 0 and (
                        datetime.datetime.utcnow() - self.python_programmer_cool.cooldown_start_time).total_seconds() < 3600:
                    await self.python_programmer_cool.time_it(user=ctx.author)
                    return
                programmer_embed1 = discord.Embed(
                    title="**Python Programmer Post**",
                    description="***Provide some work examples you've done in the past. You could link a portfolio. (ATTACHMENTS ARE CURRENTLY NOT SUPPORTED!)***",
                    color=0x0064ff
                )
                programmer_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed1)
                try:
                    programmer_work_message = await self.bot.wait_for('message', check=check_dm,
                                                                      timeout=1000)
                    programmer_work = programmer_work_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if programmer_work.lower() == "cancel":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_embed1 = discord.Embed(
                    title="**Python Programmer Post**",
                    description="***Do you have anything you would like to say about yourself here? If yes, please do so.***",
                    color=0x0064ff
                )
                programmer_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed1)
                try:
                    programmer_information_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    programmer_information = programmer_information_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if programmer_information.lower() == "cancel":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_embed3 = discord.Embed(
                    title="**Python Programmer Application**",
                    description="***Anything that you've missed that you would like to add onto your current statement?***",
                    color=0x0064ff
                )
                programmer_embed3.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed3)
                try:
                    programmer_other_message = await self.bot.wait_for('message', check=check_dm,
                                                                       timeout=1000)
                    programmer_other = programmer_other_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if programmer_other.lower() == "cancel":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                await ctx.author.send(
                    "Would you like to send this for Application Approval?\n Reply with `yes` or `no`")
                try:
                    final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    final_choice = final_choice_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if re.findall("no", final_choice, re.IGNORECASE):
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                elif re.findall("yes", final_choice, re.IGNORECASE):
                    await ctx.author.send("Sent for approval!")
                    some_channel = self.bot.get_channel(739229509240225842)
                    some_role = discord.utils.get(ctx.guild.roles, id=732377712286761001)
                    title = "**Python Programmer Application**"
                    pag = Paginator(
                        f"**Work:** {programmer_work}\n**Information:** {programmer_information}\n**Other:** {programmer_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                        1985)

                    await pag.send(bot=self.bot, channel=some_channel, role=some_role, member=ctx.author,
                                   title=title, mute_role=applications_muted)
                    self.python_programmer_cool = Cooldown(time=datetime.datetime.utcnow())
            elif re.findall("c# programmer", programmer_category, re.IGNORECASE):
                if self.csharp_programmer_cool.cooldown_start_time != 0 and (
                        datetime.datetime.utcnow() - self.csharp_programmer_cool.cooldown_start_time).total_seconds() < 3600:
                    await self.csharp_programmer_cool.time_it(user=ctx.author)
                    return
                programmer_embed1 = discord.Embed(
                    title="**C# Programmer Post**",
                    description="***Provide some work examples you've done in the past. You could link a portfolio. (ATTACHMENTS ARE CURRENTLY NOT SUPPORTED!)***",
                    color=0x0064ff
                )
                programmer_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed1)
                try:
                    programmer_work_message = await self.bot.wait_for('message', check=check_dm,
                                                                      timeout=1000)
                    programmer_work = programmer_work_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if programmer_work.lower() == "cancel":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_embed1 = discord.Embed(
                    title="**C# Programmer Post**",
                    description="***Do you have anything you would like to say about yourself here? If yes, please do so.***",
                    color=0x0064ff
                )
                programmer_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed1)
                try:
                    programmer_information_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    programmer_information = programmer_information_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if programmer_information.lower() == "cancel":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_embed3 = discord.Embed(
                    title="**C# Programmer Application**",
                    description="***Anything that you've missed that you would like to add onto your current statement?***",
                    color=0x0064ff
                )
                programmer_embed3.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed3)
                try:
                    programmer_other_message = await self.bot.wait_for('message', check=check_dm,
                                                                       timeout=1000)
                    programmer_other = programmer_other_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if programmer_other.lower() == "cancel":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                await ctx.author.send(
                    "Would you like to send this for Application Approval?\n Answer with: \n`1` - yes;\n`cancel` - no;")
                try:
                    final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    final_choice = final_choice_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if re.findall("no", final_choice, re.IGNORECASE):
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                elif re.findall("yes", final_choice, re.IGNORECASE):
                    await ctx.author.send("Sent for approval!")
                    some_channel = self.bot.get_channel(739229541964185772)
                    some_role = discord.utils.get(ctx.guild.roles, id=732377857317142650)
                    title = "**C# Programmer Application**"
                    pag = Paginator(
                        f"**Work:** {programmer_work}\n**Information:** {programmer_information}\n**Other:** {programmer_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                        1985)

                    await pag.send(bot=self.bot, channel=some_channel, role=some_role, member=ctx.author,
                                   title=title, mute_role=applications_muted)
                    self.csharp_programmer_cool = Cooldown(time=datetime.datetime.utcnow())
            elif re.findall("java programmer", programmer_category, re.IGNORECASE):
                if self.java_programmer_cool.cooldown_start_time != 0 and (
                        datetime.datetime.utcnow() - self.java_programmer_cool.cooldown_start_time).total_seconds() < 3600:
                    await self.java_programmer_cool.time_it(user=ctx.author)
                    return
                programmer_embed1 = discord.Embed(
                    title="**Java Programmer Post**",
                    description="***Provide some work examples you've done in the past. You could link a portfolio. (ATTACHMENTS ARE CURRENTLY NOT SUPPORTED!)***",
                    color=0x0064ff
                )
                programmer_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed1)
                try:
                    programmer_work_message = await self.bot.wait_for('message', check=check_dm,
                                                                      timeout=1000)
                    programmer_work = programmer_work_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if programmer_work.lower() == "cancel":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_embed1 = discord.Embed(
                    title="**Java Programmer Post**",
                    description="***Do you have anything you would like to say about yourself here? If yes, please do so.***",
                    color=0x0064ff
                )
                programmer_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed1)
                try:
                    programmer_information_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    programmer_information = programmer_information_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if programmer_information.lower() == "cancel":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_embed3 = discord.Embed(
                    title="**Java Programmer Application**",
                    description="***Anything that you've missed that you would like to add onto your current statement?***",
                    color=0x0064ff
                )
                programmer_embed3.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed3)
                try:
                    programmer_other_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    programmer_other = programmer_other_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if programmer_other.lower() == "cancel":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                await ctx.author.send(
                    "Would you like to send this for Application Approval?\n Reply with `yes` or `no`")
                try:
                    final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    final_choice = final_choice_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if re.findall("no", final_choice, re.IGNORECASE):
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                elif re.findall("yes", final_choice, re.IGNORECASE):
                    await ctx.author.send("Sent for approval!")
                    some_channel = self.bot.get_channel(739233043533004820)
                    some_role = discord.utils.get(ctx.guild.roles, id=732379273100263464)
                    title = "**Java Programmer Application**"
                    pag = Paginator(
                        f"**Work:** {programmer_work}\n**Information:** {programmer_information}\n**Other:** {programmer_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                        1985)

                    await pag.send(bot=self.bot, channel=some_channel, role=some_role, member=ctx.author,
                                   title=title, mute_role=applications_muted)
                    self.java_programmer_cool = Cooldown(time=datetime.datetime.utcnow())
            elif re.findall("javascript programmer", programmer_category, re.IGNORECASE):
                if self.javascript_programmer_cool.cooldown_start_time != 0 and (
                        datetime.datetime.utcnow() - self.javascript_programmer_cool.cooldown_start_time).total_seconds() < 3600:
                    await self.javascript_programmer_cool.time_it(user=ctx.author)
                    return
                programmer_embed1 = discord.Embed(
                    title="**JavaScript Programmer Post**",
                    description="***Provide some work examples you've done in the past. You could link a portfolio. (ATTACHMENTS ARE CURRENTLY NOT SUPPORTED!)***",
                    color=0x0064ff
                )
                programmer_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed1)
                try:
                    programmer_work_message = await self.bot.wait_for('message', check=check_dm,
                                                                      timeout=1000)
                    programmer_work = programmer_work_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if programmer_work.lower() == "cancel":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_embed1 = discord.Embed(
                    title="**JavaScript Programmer Post**",
                    description="***Do you have anything you would like to say about yourself here? If yes, please do so.***",
                    color=0x0064ff
                )
                programmer_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed1)
                try:
                    programmer_information_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    programmer_information = programmer_information_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if programmer_information.lower() == "cancel":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_embed3 = discord.Embed(
                    title="**JavaScript Programmer Application**",
                    description="***Anything that you've missed that you would like to add onto your current statement?***",
                    color=0x0064ff
                )
                programmer_embed3.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed3)
                try:
                    programmer_other_message = await self.bot.wait_for('message', check=check_dm,
                                                                       timeout=1000)
                    programmer_other = programmer_other_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if programmer_other.lower() == "cancel":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                await ctx.author.send(
                    "Would you like to send this for Application Approval?\n Reply with `yes` or `no`")
                try:
                    final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    final_choice = final_choice_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if re.findall("no", final_choice, re.IGNORECASE):
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                elif re.findall("yes", final_choice, re.IGNORECASE):
                    await ctx.author.send("Sent for approval!")
                    some_channel = self.bot.get_channel(739233060091985951)
                    some_role = discord.utils.get(ctx.guild.roles, id=732377955669508097)
                    title = "**JavaScript Programmer Application**"
                    pag = Paginator(
                        f"**Work:** {programmer_work}\n**Information:** {programmer_information}\n**Other:** {programmer_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                        1985)

                    await pag.send(bot=self.bot, channel=some_channel, role=some_role, member=ctx.author,
                                   title=title, mute_role=applications_muted)
                    self.javascript_programmer_cool = Cooldown(time=datetime.datetime.utcnow())
            elif re.findall("cpp programmer", programmer_category, re.IGNORECASE):
                if self.cpp_programmer_cool.cooldown_start_time != 0 and (
                        datetime.datetime.utcnow() - self.cpp_programmer_cool.cooldown_start_time).total_seconds() < 3600:
                    await self.cpp_programmer_cool.time_it(user=ctx.author)
                    return
                programmer_embed1 = discord.Embed(
                    title="**CPP Programmer Post**",
                    description="***Provide some work examples you've done in the past. You could link a portfolio. (ATTACHMENTS ARE CURRENTLY NOT SUPPORTED!)***",
                    color=0x0064ff
                )
                programmer_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed1)
                try:
                    programmer_work_message = await self.bot.wait_for('message', check=check_dm,
                                                                      timeout=1000)
                    programmer_work = programmer_work_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if programmer_work.lower() == "cancel":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_embed1 = discord.Embed(
                    title="**CPP Programmer Post**",
                    description="***Do you have anything you would like to say about yourself here? If yes, please do so.***",
                    color=0x0064ff
                )
                programmer_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed1)
                try:
                    programmer_information_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    programmer_information = programmer_information_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if programmer_information.lower() == "cancel":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_embed3 = discord.Embed(
                    title="**CPP Programmer Application**",
                    description="***Anything that you've missed that you would like to add onto your current statement?***",
                    color=0x0064ff
                )
                programmer_embed3.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed3)
                try:
                    programmer_other_message = await self.bot.wait_for('message', check=check_dm,
                                                                       timeout=1000)
                    programmer_other = programmer_other_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if programmer_other.lower() == "cancel":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                await ctx.author.send(
                    "Would you like to send this for Application Approval?\n Reply with `yes` or `no`")
                try:
                    final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    final_choice = final_choice_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if re.findall("no", final_choice, re.IGNORECASE):
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                elif re.findall("yes", final_choice, re.IGNORECASE):
                    await ctx.author.send("Sent for approval!")
                    some_channel = self.bot.get_channel(739229568296157184)
                    some_role = discord.utils.get(ctx.guild.roles, id=732377777772167188)
                    title = "**C++ Programmer Application**"
                    pag = Paginator(
                        f"**Work:** {programmer_work}\n**Information:** {programmer_information}\n**Other:** {programmer_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                        1985)

                    await pag.send(bot=self.bot, channel=some_channel, role=some_role, member=ctx.author,
                                   title=title, mute_role=applications_muted)
                    self.cpp_programmer_cool = Cooldown(time=datetime.datetime.utcnow())
            elif re.findall("c programmer", programmer_category, re.IGNORECASE):
                if self.c_programmer_cool.cooldown_start_time != 0 and (
                        datetime.datetime.utcnow() - self.c_programmer_cool.cooldown_start_time).total_seconds() < 3600:
                    await self.c_programmer_cool.time_it(user=ctx.author)
                    return
                programmer_embed1 = discord.Embed(
                    title="**C Programmer Post**",
                    description="***Provide some work examples you've done in the past. You could link a portfolio. (ATTACHMENTS ARE CURRENTLY NOT SUPPORTED!)***",
                    color=0x0064ff
                )
                programmer_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed1)
                try:
                    programmer_work_message = await self.bot.wait_for('message', check=check_dm,
                                                                      timeout=1000)
                    programmer_work = programmer_work_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if programmer_work.lower() == "cancel":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_embed1 = discord.Embed(
                    title="**C Programmer Post**",
                    description="***Do you have anything you would like to say about yourself here? If yes, please do so.***",
                    color=0x0064ff
                )
                programmer_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed1)
                try:
                    programmer_information_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    programmer_information = programmer_information_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if programmer_information.lower() == "cancel":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_embed3 = discord.Embed(
                    title="**C Programmer Application**",
                    description="***Anything that you've missed that you would like to add onto your current statement?***",
                    color=0x0064ff
                )
                programmer_embed3.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed3)
                try:
                    programmer_other_message = await self.bot.wait_for('message', check=check_dm,
                                                                       timeout=1000)
                    programmer_other = programmer_other_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if programmer_other.lower() == "cancel":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                await ctx.author.send(
                    "Would you like to send this for Application Approval?\n Reply with `yes` or `no`")
                try:
                    final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    final_choice = final_choice_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if re.findall("no", final_choice, re.IGNORECASE):
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                elif re.findall("yes", final_choice, re.IGNORECASE):
                    await ctx.author.send("Sent for approval!")
                    some_channel = self.bot.get_channel(739233448186609756)
                    some_role = discord.utils.get(ctx.guild.roles, id=732378157449216040)
                    title = "**C Programmer Application**"
                    pag = Paginator(
                        f"**Work:** {programmer_work}\n**Information:** {programmer_information}\n**Other:** {programmer_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                        1985)

                    await pag.send(bot=self.bot, channel=some_channel, role=some_role, member=ctx.author,
                                   title=title, mute_role=applications_muted)
                    self.c_programmer_cool = Cooldown(time=datetime.datetime.utcnow())
            elif re.findall("php programmer", programmer_category, re.IGNORECASE):
                if self.php_programmer_cool.cooldown_start_time != 0 and (
                        datetime.datetime.utcnow() - self.php_programmer_cool.cooldown_start_time).total_seconds() < 3600:
                    await self.php_programmer_cool.time_it(user=ctx.author)
                    return
                programmer_embed1 = discord.Embed(
                    title="**PHP Programmer Post**",
                    description="***Provide some work examples you've done in the past. You could link a portfolio. (ATTACHMENTS ARE CURRENTLY NOT SUPPORTED!)***",
                    color=0x0064ff
                )
                programmer_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed1)
                try:
                    programmer_work_message = await self.bot.wait_for('message', check=check_dm,
                                                                      timeout=1000)
                    programmer_work = programmer_work_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if programmer_work.lower() == "cancel":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_embed1 = discord.Embed(
                    title="**PHP Programmer Post**",
                    description="***Do you have anything you would like to say about yourself here? If yes, please do so.***",
                    color=0x0064ff
                )
                programmer_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed1)
                try:
                    programmer_information_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    programmer_information = programmer_information_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if programmer_information.lower() == "cancel":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_embed3 = discord.Embed(
                    title="**PHP Programmer Application**",
                    description="***Anything that you've missed that you would like to add onto your current statement?***",
                    color=0x0064ff
                )
                programmer_embed3.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed3)
                try:
                    programmer_other_message = await self.bot.wait_for('message', check=check_dm,
                                                                       timeout=1000)
                    programmer_other = programmer_other_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if programmer_other.lower() == "cancel":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                await ctx.author.send(
                    "Would you like to send this for Application Approval?\n Reply with `yes` or `no`")
                try:
                    final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    final_choice = final_choice_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if re.findall("no", final_choice, re.IGNORECASE):
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                elif re.findall("yes", final_choice, re.IGNORECASE):
                    await ctx.author.send("Sent for approval!")
                    some_channel = self.bot.get_channel(739233420827295875)
                    some_role = discord.utils.get(ctx.guild.roles, id=732378321387520092)
                    title = "**PHP Programmer Application**"
                    pag = Paginator(
                        f"**Work:** {programmer_work}\n**Information:** {programmer_information}\n**Other:** {programmer_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                        1985)

                    await pag.send(bot=self.bot, channel=some_channel, role=some_role, member=ctx.author,
                                   title=title, mute_role=applications_muted)
                    self.php_programmer_cool = Cooldown(time=datetime.datetime.utcnow())
            elif re.findall("lua programmer", programmer_category, re.IGNORECASE):
                if self.lua_programer_cool.cooldown_start_time != 0 and (
                        datetime.datetime.utcnow() - self.lua_programer_cool.cooldown_start_time).total_seconds() < 3600:
                    await self.lua_programer_cool.time_it(user=ctx.author)
                    return
                programmer_embed1 = discord.Embed(
                    title="**Lua Programmer Post**",
                    description="***Provide some work examples you've done in the past. You could link a portfolio. (ATTACHMENTS ARE CURRENTLY NOT SUPPORTED!)***",
                    color=0x0064ff
                )
                programmer_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed1)
                try:
                    programmer_work_message = await self.bot.wait_for('message', check=check_dm,
                                                                      timeout=1000)
                    programmer_work = programmer_work_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if programmer_work.lower() == "cancel":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_embed1 = discord.Embed(
                    title="**Lua Programmer Post**",
                    description="***Do you have anything you would like to say about yourself here? If yes, please do so.***",
                    color=0x0064ff
                )
                programmer_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed1)
                try:
                    programmer_information_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    programmer_information = programmer_information_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if programmer_information.lower() == "cancel":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_embed3 = discord.Embed(
                    title="**Lua Programmer Application**",
                    description="***Anything that you've missed that you would like to add onto your current statement?***",
                    color=0x0064ff
                )
                programmer_embed3.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed3)
                try:
                    programmer_other_message = await self.bot.wait_for('message', check=check_dm,
                                                                       timeout=1000)
                    programmer_other = programmer_other_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if programmer_other.lower() == "cancel":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                await ctx.author.send(
                    "Would you like to send this for Application Approval?\n Reply with: `yes` or `no`")
                try:
                    final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    final_choice = final_choice_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if re.findall("no", final_choice, re.IGNORECASE):
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                elif re.findall("yes", final_choice, re.IGNORECASE):
                    await ctx.author.send("Sent for approval!")
                    some_channel = self.bot.get_channel(739233077879898123)
                    some_role = discord.utils.get(ctx.guild.roles, id=732376072397783093)
                    title = "**Lua Programmer Application**"
                    pag = Paginator(
                        f"**Work:** {programmer_work}\n**Information:** {programmer_information}\n**Other:** {programmer_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                        1985)

                    await pag.send(bot=self.bot, channel=some_channel, role=some_role, member=ctx.author,
                                   title=title, mute_role=applications_muted)
                    self.lua_programer_cool = Cooldown(time=datetime.datetime.utcnow())
            elif re.findall("ruby programmer", programmer_category, re.IGNORECASE):
                if self.ruby_programmer_cool.cooldown_start_time != 0 and (
                        datetime.datetime.utcnow() - self.ruby_programmer_cool.cooldown_start_time).total_seconds() < 3600:
                    await self.ruby_programmer_cool.time_it(user=ctx.author)
                    return
                programmer_embed1 = discord.Embed(
                    title="**Ruby Programmer Post**",
                    description="***Provide some work examples you've done in the past. You could link a portfolio. (ATTACHMENTS ARE CURRENTLY NOT SUPPORTED!)***",
                    color=0x0064ff
                )
                programmer_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed1)
                try:
                    programmer_work_message = await self.bot.wait_for('message', check=check_dm,
                                                                      timeout=1000)
                    programmer_work = programmer_work_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if programmer_work.lower() == "cancel":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_embed1 = discord.Embed(
                    title="**Ruby Programmer Post**",
                    description="***Do you have anything you would like to say about yourself here? If yes, please do so.***",
                    color=0x0064ff
                )
                programmer_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed1)
                try:
                    programmer_information_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    programmer_information = programmer_information_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if programmer_information.lower() == "cancel":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_embed3 = discord.Embed(
                    title="**Ruby Programmer Application**",
                    description="***Anything that you've missed that you would like to add onto your current statement?***",
                    color=0x0064ff
                )
                programmer_embed3.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed3)
                try:
                    programmer_other_message = await self.bot.wait_for('message', check=check_dm,
                                                                       timeout=1000)
                    programmer_other = programmer_other_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if programmer_other.lower() == "cancel":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                await ctx.author.send(
                    "Would you like to send this for Application Approval?\n Answer with: \n`1` - yes;\n`cancel` - no;")
                try:
                    final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    final_choice = final_choice_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if re.findall("no", final_choice, re.IGNORECASE):
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                elif re.findall("yes", final_choice, re.IGNORECASE):
                    await ctx.author.send("Sent for approval!")
                    some_channel = self.bot.get_channel(739233479098761307)
                    some_role = discord.utils.get(ctx.guild.roles, id=735147661430227025)
                    title = "**Ruby Programmer Application**"
                    pag = Paginator(
                        f"**Work:** {programmer_work}\n**Information:** {programmer_information}\n**Other:** {programmer_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                        1985)

                    await pag.send(bot=self.bot, channel=some_channel, role=some_role, member=ctx.author,
                                   title=title, mute_role=applications_muted)
                    if self.ruby_programmer_cool.cooldown_start_time != 0 and (
                            datetime.datetime.utcnow() - self.ruby_programmer_cool.cooldown_start_time).total_seconds() < 3600:
                        await self.ruby_programmer_cool.time_it(user=ctx.author)
                        return
            elif re.findall("html & css programmer", programmer_category, re.IGNORECASE):
                if self.html_and_css_programmer_cool.cooldown_start_time != 0 and (
                        datetime.datetime.utcnow() - self.html_and_css_programmer_cool.cooldown_start_time).total_seconds() < 3600:
                    await self.html_and_css_programmer_cool.time_it(user=ctx.author)
                    return
                programmer_embed1 = discord.Embed(
                    title="**HTML & CSS Programmer Application**",
                    description="***Provide some work examples you've done in the past. You could link a portfolio. (ATTACHMENTS ARE CURRENTLY NOT SUPPORTED!)***",
                    color=0x0064ff
                )
                programmer_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed1)
                try:
                    programmer_work_message = await self.bot.wait_for('message', check=check_dm,
                                                                      timeout=1000)
                    programmer_work = programmer_work_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if programmer_work.lower() == "cancel":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_embed1 = discord.Embed(
                    title="**HTML & CSS Programmer Application**",
                    description="***Do you have anything you would like to say about yourself here? If yes, please do so.***",
                    color=0x0064ff
                )
                programmer_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed1)
                try:
                    programmer_information_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    programmer_information = programmer_information_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if programmer_information.lower() == "cancel":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_embed3 = discord.Embed(
                    title="**HTML & CSS Programmer Application**",
                    description="***Anything that you've missed that you would like to add onto your current statement?***",
                    color=0x0064ff
                )
                programmer_embed3.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed3)
                try:
                    programmer_other_message = await self.bot.wait_for('message', check=check_dm,
                                                                       timeout=1000)
                    programmer_other = programmer_other_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if programmer_other.lower() == "cancel":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                await ctx.author.send(
                    "Would you like to send this for Application Approval?\n Reply with `yes` or `no`")
                try:
                    final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    final_choice = final_choice_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if re.findall("no", final_choice, re.IGNORECASE):
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                elif re.findall("yes", final_choice, re.IGNORECASE):
                    await ctx.author.send("Sent for approval!")
                    some_channel = self.bot.get_channel(778686711810490379)
                    some_role = discord.utils.get(ctx.guild.roles, id=741099963626422322)
                    title = "**HTML & CSS Programmer Application**"
                    pag = Paginator(
                        f"**Work:** {programmer_work}\n**Information:** {programmer_information}\n**Other:** {programmer_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                        1985)

                    await pag.send(bot=self.bot, channel=some_channel, role=some_role, member=ctx.author,
                                   title=title, mute_role=applications_muted)
                    self.html_and_css_programmer_cool = Cooldown(time=datetime.datetime.utcnow())
        elif re.findall("game designer", category, re.IGNORECASE):
            if self.game_designer_cool.cooldown_start_time != 0 and (datetime.datetime.utcnow() - self.game_designer_cool.cooldown_start_time).total_seconds() < 3600:
                await self.game_designer_cool.time_it(user=ctx.author)
                return
            game_designer_embed1 = discord.Embed(
                title="**Game Designer Application**",
                description="***Provide some work examples you've done in the past. You could link a portfolio. (ATTACHMENTS ARE CURRENTLY NOT SUPPORTED!)***",
                color=0x0064ff
            )
            game_designer_embed1.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=game_designer_embed1)
            try:
                game_designer_work_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                game_designer_work = game_designer_work_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if game_designer_work.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            game_designer_embed2 = discord.Embed(
                title="**Game Designer Application**",
                description="***Do you have anything you would like to say about yourself here? If yes, please do so.***",
                color=0x0064ff
            )
            game_designer_embed2.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=game_designer_embed2)
            try:
                game_designer_information_message = await self.bot.wait_for('message', check=check_dm,
                                                                            timeout=1000)
                game_designer_information = game_designer_information_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if game_designer_information.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            game_designer_embed3 = discord.Embed(
                title="**Game Designer Application**",
                description="***Anything that you've missed that you would like to add onto your current statement?***",
                color=0x0064ff
            )
            game_designer_embed3.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=game_designer_embed3)
            try:
                game_designer_other_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                game_designer_other = game_designer_other_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if game_designer_other.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            await ctx.author.send(
                "Would you like to send this for Application Approval?\n Reply with `yes` or `no`")
            try:
                final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                final_choice = final_choice_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if re.findall("no", final_choice, re.IGNORECASE):
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            elif re.findall("yes", final_choice, re.IGNORECASE):
                await ctx.author.send("Sent for approval!")
                some_channel = self.bot.get_channel(739233876446281778)
                some_role = discord.utils.get(ctx.guild.roles, id=733281086913773599)
                title = "**Game Designer Application**"
                pag = Paginator(
                    f"**Work:** {game_designer_work}\n**Information:** {game_designer_information}\n**Other:** {game_designer_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                    1985)

                await pag.send(bot=self.bot, channel=some_channel, role=some_role, member=ctx.author,
                               title=title, mute_role=applications_muted)
                self.game_designer_cool = Cooldown(time=datetime.datetime.utcnow())
        elif re.findall("3d modeler", category, re.IGNORECASE):
            if self.threed_modeler_cool.cooldown_start_time != 0 and (datetime.datetime.utcnow() - self.threed_modeler_cool.cooldown_start_time).total_seconds() < 3600:
                await self.threed_modeler_cool.time_it(user=ctx.author)
                return
            threed_modeler_embed1 = discord.Embed(
                title="**3D Modeler Application**",
                description="***Provide some work examples you've done in the past. You could link a portfolio. (ATTACHMENTS ARE CURRENTLY NOT SUPPORTED!)***",
                color=0x0064ff
            )
            threed_modeler_embed1.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=threed_modeler_embed1)
            try:
                threed_modeler_work_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                threed_modeler_work = threed_modeler_work_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if threed_modeler_work.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            threed_modeler_embed2 = discord.Embed(
                title="**3D Modeler Application**",
                description="***Do you have anything you would like to say about yourself here? If yes, please do so.***",
                color=0x0064ff
            )
            threed_modeler_embed2.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=threed_modeler_embed2)
            try:
                threed_modeler_information_message = await self.bot.wait_for('message', check=check_dm,
                                                                             timeout=1000)
                threed_modeler_information = threed_modeler_information_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if threed_modeler_information.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            threed_modeler_embed3 = discord.Embed(
                title="**3D Modeler Application**",
                description="***Anything that you've missed that you would like to add onto your current statement?***",
                color=0x0064ff
            )
            threed_modeler_embed3.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=threed_modeler_embed3)
            try:
                threed_modeler_other_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                threed_modeler_other = threed_modeler_other_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if threed_modeler_other.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            await ctx.author.send(
                "Would you like to send this for Application Approval?\n Reply with `yes` or `no`")
            try:
                final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                final_choice = final_choice_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if re.findall("no", final_choice, re.IGNORECASE):
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            elif re.findall("yes", final_choice, re.IGNORECASE):
                await ctx.author.send("Sent for approval!")
                some_channel = self.bot.get_channel(739233640596111411)
                some_role = discord.utils.get(ctx.guild.roles, id=733281157872877629)
                title = "**3D Modeler Application**"
                pag = Paginator(
                    f"**Work:** {threed_modeler_work}\n**Information:** {threed_modeler_information}\n**Other:** {threed_modeler_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                    1985)

                await pag.send(bot=self.bot, channel=some_channel, role=some_role, member=ctx.author,
                               title=title, mute_role=applications_muted)
                self.threed_modeler_cool = Cooldown(time=datetime.datetime.utcnow())
        elif re.findall("youtuber", category, re.IGNORECASE):
            if self.youtuber_cool.cooldown_start_time != 0 and (datetime.datetime.utcnow() - self.youtuber_cool.cooldown_start_time).total_seconds() < 3600:
                await self.youtuber_cool.time_it(user=ctx.author)
                return
            youtuber_embed1 = discord.Embed(
                title="**YouTuber Application**",
                description="***How many subscribers does your channel have? Minimum needed to apply is 1, 000***",
                color=0x0064ff
            )
            youtuber_embed1.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=youtuber_embed1)
            try:
                youtuber_subs_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                youtuber_subs = youtuber_subs_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if youtuber_subs.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            youtuber_embed2 = discord.Embed(
                title="**YouTuber Application**",
                description="***Provide us with the link of your YouTube channel here. Also, please make sure you have the YouTube account connected with your discord account. To do that, go to User Settings > Connections, and connect.***",
                color=0x0064ff
            )
            youtuber_embed2.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=youtuber_embed2)
            try:
                youtuber_channel_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                youtuber_channel = youtuber_channel_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if youtuber_channel.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            youtuber_embed3 = discord.Embed(
                title="**YouTuber Application**",
                description="***Anything that you've missed that you would like to add onto your current statement?***",
                color=0x0064ff
            )
            youtuber_embed3.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=youtuber_embed3)
            try:
                youtuber_other_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                youtuber_other = youtuber_other_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if youtuber_other.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            await ctx.author.send(
                "Would you like to send this for Application Approval?\n Reply with `yes` or `no`")
            try:
                final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                final_choice = final_choice_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if re.findall("no", final_choice, re.IGNORECASE):
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            elif re.findall("yes", final_choice, re.IGNORECASE):
                await ctx.author.send("Sent for approval!")
                some_channel = self.bot.get_channel(778689200350167123)
                some_role = discord.utils.get(ctx.guild.roles, id=738788543211634756)
                title = "**YouTuber Application**"
                pag = Paginator(
                    f"**Subscriber Count:** {youtuber_subs}\n**YouTube Channel:** {youtuber_channel}\n**Other:** {youtuber_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                    1985)

                await pag.send(bot=self.bot, channel=some_channel, role=some_role, member=ctx.author,
                               title=title, mute_role=applications_muted)
                self.youtuber_cool = Cooldown(time=datetime.datetime.utcnow())
        elif re.findall("roblox builder", category, re.IGNORECASE):
            if self.roblox_studio_builder_cool.cooldown_start_time != 0 and (datetime.datetime.utcnow() - self.roblox_studio_builder_cool.cooldown_start_time).total_seconds() < 3600:
                await self.roblox_studio_builder_cool.time_it(user=ctx.author)
                return
            builder_embed1 = discord.Embed(
                title="**Roblox Builder Application**",
                description="***Provide some work examples you've done in the past. You could link a portfolio. (ATTACHMENTS ARE CURRENTLY NOT SUPPORTED!)***",
                color=0x0064ff
            )
            builder_embed1.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=builder_embed1)
            try:
                builder_work_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                builder_work = builder_work_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if builder_work.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            builder_embed2 = discord.Embed(
                title="**Roblox Builder Application**",
                description="***Do you have anything you would like to say about yourself here? If yes, please do so.***",
                color=0x0064ff
            )
            builder_embed2.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=builder_embed2)
            try:
                builder_information_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                builder_information = builder_information_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if builder_information.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            builder_embed3 = discord.Embed(
                title="**Roblox Builder Application**",
                description="***Anything that you've missed that you would like to add onto your current statement?***",
                color=0x0064ff
            )
            builder_embed3.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=builder_embed3)
            try:
                builder_other_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                builder_other = builder_other_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if builder_other.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            await ctx.author.send(
                "Would you like to send this for Application Approval?\n Reply with `yes` or `no`")
            try:
                final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                final_choice = final_choice_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if re.findall("no", final_choice, re.IGNORECASE):
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            elif re.findall("yes", final_choice, re.IGNORECASE):
                await ctx.author.send("Sent for approval!")
                some_channel = self.bot.get_channel(739233671730561124)
                some_role = discord.utils.get(ctx.guild.roles, id=733281281671954442)
                title = "**Roblox Builder Application**"
                pag = Paginator(
                    f"**Work:** {builder_work}\n**Information:** {builder_information}\n**Other:** {builder_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                    1985)

                await pag.send(bot=self.bot, channel=some_channel, role=some_role, member=ctx.author,
                               title=title, mute_role=applications_muted)
                self.roblox_studio_builder_cool = Cooldown(time=datetime.datetime.utcnow())
        elif re.findall("twitch streamer", category, re.IGNORECASE):
            if self.twitch_streamer_cool.cooldown_start_time != 0 and (datetime.datetime.utcnow() - self.twitch_streamer_cool.cooldown_start_time).total_seconds() < 3600:
                await self.twitch_streamer_cool.time_it(user=ctx.author)
                return
            twitch_streamer_embed1 = discord.Embed(
                title="**Twitch Streamer Application**",
                description="***How many followers does your channel have? Minimum needed to apply is 1, 000***",
                color=0x0064ff
            )
            twitch_streamer_embed1.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=twitch_streamer_embed1)
            try:
                twitch_streamer_follows_message = await self.bot.wait_for('message', check=check_dm,
                                                                          timeout=1000)
                twitch_streamer_follows = twitch_streamer_follows_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if twitch_streamer_follows.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            twitch_streamer_embed2 = discord.Embed(
                title="**Twitch Streamer Application**",
                description="***Provide us with the link of your YouTube channel here. Also, please make sure you have the YouTube account connected with your discord account. To do that, go to User Settings > Connections, and connect.***",
                color=0x0064ff
            )
            twitch_streamer_embed2.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=twitch_streamer_embed2)
            try:
                twitch_streamer_channel_message = await self.bot.wait_for('message', check=check_dm,
                                                                          timeout=1000)
                twitch_streamer_channel = twitch_streamer_channel_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if twitch_streamer_channel.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            twitch_streamer_embed3 = discord.Embed(
                title="**Twitch Streamer Application**",
                description="***Anything that you've missed that you would like to add onto your current statement?***",
                color=0x0064ff
            )
            twitch_streamer_embed3.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=twitch_streamer_embed3)
            try:
                twitch_streamer_other_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                twitch_streamer_other = twitch_streamer_other_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if twitch_streamer_other.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            await ctx.author.send(
                "Would you like to send this for Application Approval?\n Reply with `yes` or `no`")
            try:
                final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                final_choice = final_choice_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if re.findall("no", final_choice, re.IGNORECASE):
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            elif re.findall("yes", final_choice, re.IGNORECASE):
                await ctx.author.send("Sent for approval!")
                some_channel = self.bot.get_channel(778689246729863228)
                some_role = discord.utils.get(ctx.guild.roles, id=738814393663619182)
                title = "**Twitch Streamer Application**"
                pag = Paginator(
                    f"**Followers Count:** {twitch_streamer_follows}\n**Twitch Channel:** {twitch_streamer_channel}\n**Other:** {twitch_streamer_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                    1985)

                await pag.send(bot=self.bot, channel=some_channel, role=some_role, member=ctx.author,
                               title=title, mute_role=applications_muted)
                self.twitch_streamer_cool = Cooldown(time=datetime.datetime.utcnow())
        elif re.findall("gfx designer", category, re.IGNORECASE):
            if self.gfx_designer_cool.cooldown_start_time != 0 and (datetime.datetime.utcnow() - self.gfx_designer_cool.cooldown_start_time).total_seconds() < 3600:
                await self.gfx_designer_cool.time_it(user=ctx.author)
                return
            gfx_designer_embed1 = discord.Embed(
                title="**GFX Designer Application**",
                description="***Provide some work examples you've done in the past. You could link a portfolio. (ATTACHMENTS ARE CURRENTLY NOT SUPPORTED!)***",
                color=0x0064ff
            )
            gfx_designer_embed1.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=gfx_designer_embed1)
            try:
                gfx_designer_work_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                gfx_designer_work = gfx_designer_work_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if gfx_designer_work.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            gfx_designer_embed2 = discord.Embed(
                title="**GFX Designer Application**",
                description="***Do you have anything you would like to say about yourself here? If yes, please do so.***",
                color=0x0064ff
            )
            gfx_designer_embed2.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=gfx_designer_embed2)
            try:
                gfx_designer_information_message = await self.bot.wait_for('message', check=check_dm,
                                                                           timeout=1000)
                gfx_designer_information = gfx_designer_information_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if gfx_designer_information.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            gfx_designer_embed3 = discord.Embed(
                title="**GFX Designer Application**",
                description="***Anything that you've missed that you would like to add onto your current statement?***",
                color=0x0064ff
            )
            gfx_designer_embed3.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=gfx_designer_embed3)
            try:
                gfx_designer_other_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                gfx_designer_other = gfx_designer_other_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if re.findall("no", gfx_designer_other, re.IGNORECASE):
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            await ctx.author.send(
                "Would you like to send this for Application Approval?\n Reply with `yes` or `no`")
            try:
                final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                final_choice = final_choice_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if re.findall("no", final_choice, re.IGNORECASE):
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            elif re.findall("yes", final_choice, re.IGNORECASE):
                await ctx.author.send("Sent for approval!")
                some_channel = self.bot.get_channel(739233658556383262)
                some_role = discord.utils.get(ctx.guild.roles, id=733280979921141821)
                title = "**GFX Designer Application**"
                pag = Paginator(
                    f"**Work:** {gfx_designer_work}\n**Information:** {gfx_designer_information}\n**Other:** {gfx_designer_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                    1985)

                await pag.send(bot=self.bot, channel=some_channel, role=some_role, member=ctx.author,
                               title=title, mute_role=applications_muted)
                self.gfx_designer_cool = Cooldown(time=datetime.datetime.utcnow())
        elif re.findall("translator", category, re.IGNORECASE):
            if self.translator_cool.cooldown_start_time != 0 and (datetime.datetime.utcnow() - self.translator_cool.cooldown_start_time).total_seconds() < 3600:
                await self.translator_cool.time_it(user=ctx.author)
                return
            translator_embed1 = discord.Embed(
                title="**Translator Application**",
                description="***Provide some work examples you've done in the past. You could link a portfolio. (ATTACHMENTS ARE CURRENTLY NOT SUPPORTED!)***",
                color=0x0064ff
            )
            translator_embed1.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=translator_embed1)
            try:
                translator_work_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                translator_work = translator_work_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if translator_work.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            translator_embed2 = discord.Embed(
                title="**Translator Application**",
                description="***Do you have anything you would like to say about yourself here? If yes, please do so.***",
                color=0x0064ff
            )
            translator_embed2.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=translator_embed2)
            try:
                translator_information_message = await self.bot.wait_for('message', check=check_dm,
                                                                         timeout=1000)
                translator_information = translator_information_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if translator_information.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            translator_embed3 = discord.Embed(
                title="**Translator Application**",
                description="***Anything that you've missed that you would like to add onto your current statement?***",
                color=0x0064ff
            )
            translator_embed3.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=translator_embed3)
            try:
                translator_other_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                translator_other = translator_other_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if translator_other.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            await ctx.author.send(
                "Would you like to send this for Application Approval?\n Reply with `yes` or `no`")
            try:
                final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                final_choice = final_choice_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if re.findall("no", final_choice, re.IGNORECASE):
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            elif re.findall("yes", final_choice, re.IGNORECASE):
                await ctx.author.send("Sent for approval!")
                some_channel = self.bot.get_channel(778690032630235157)
                some_role = discord.utils.get(ctx.guild.roles, id=734527264657637416)
                title = "**Translator Application**"
                pag = Paginator(
                    f"**Work:** {translator_work}\n**Information:** {translator_information}\n**Other:** {translator_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                    1985)

                await pag.send(bot=self.bot, channel=some_channel, role=some_role, member=ctx.author,
                               title=title, mute_role=applications_muted)
                self.translator_cool = Cooldown(time=datetime.datetime.utcnow())
        elif re.findall("ui designer", category, re.IGNORECASE):
            if self.ui_designer_cool.cooldown_start_time != 0 and (datetime.datetime.utcnow() - self.ui_designer_cool.cooldown_start_time).total_seconds() < 3600:
                await self.ui_designer_cool.time_it(user=ctx.author)
                return
            ui_designer_embed1 = discord.Embed(
                title="**UI Designer Application**",
                description="***Provide some work examples you've done in the past. You could link a portfolio. (ATTACHMENTS ARE CURRENTLY NOT SUPPORTED!)***",
                color=0x0064ff
            )
            ui_designer_embed1.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=ui_designer_embed1)
            try:
                ui_designer_work_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                ui_designer_work = ui_designer_work_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if ui_designer_work.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            ui_designer_embed2 = discord.Embed(
                title="**UI Designer Application**",
                description="***Do you have anything you would like to say about yourself here? If yes, please do so.***",
                color=0x0064ff
            )
            ui_designer_embed2.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=ui_designer_embed2)
            try:
                ui_designer_information_message = await self.bot.wait_for('message', check=check_dm,
                                                                          timeout=1000)
                ui_designer_information = ui_designer_information_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if ui_designer_information.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            ui_designer_embed3 = discord.Embed(
                title="**UI Designer Application**",
                description="***Anything that you've missed that you would like to add onto your current statement?***",
                color=0x0064ff
            )
            ui_designer_embed3.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=ui_designer_embed3)
            try:
                ui_designer_other_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                ui_designer_other = ui_designer_other_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if ui_designer_other.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            await ctx.author.send(
                "Would you like to send this for Application Approval?\n Reply with `yes` or `no`")
            try:
                final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                final_choice = final_choice_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if re.findall("no", final_choice, re.IGNORECASE):
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            elif re.findall("yes", final_choice, re.IGNORECASE):
                await ctx.author.send("Sent for approval!")
                some_channel = self.bot.get_channel(739233732342579210)
                some_role = discord.utils.get(ctx.guild.roles, id=733274530524561430)
                title = "**UI Designer Application**"
                pag = Paginator(
                    f"**Work:** {ui_designer_work}\n**Information:** {ui_designer_information}\n**Other:** {ui_designer_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                    1985)

                await pag.send(bot=self.bot, channel=some_channel, role=some_role, member=ctx.author,
                               title=title, mute_role=applications_muted)
                self.ui_designer_cool = Cooldown(time=datetime.datetime.utcnow())
        elif re.findall("clothing designer", category, re.IGNORECASE):
            if self.clothing_designer_cool.cooldown_start_time != 0 and (datetime.datetime.utcnow() - self.clothing_designer_cool.cooldown_start_time).total_seconds() < 3600:
                await self.clothing_designer_cool.time_it(user=ctx.author)
                return
            clothing_designer_embed1 = discord.Embed(
                title="**Clothing Designer Application**",
                description="***Provide some work examples you've done in the past. You could link a portfolio. (ATTACHMENTS ARE CURRENTLY NOT SUPPORTED!)***",
                color=0x0064ff
            )
            clothing_designer_embed1.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=clothing_designer_embed1)
            try:
                clothing_designer_work_message = await self.bot.wait_for('message', check=check_dm,
                                                                         timeout=1000)
                clothing_designer_work = clothing_designer_work_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if clothing_designer_work.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            clothing_designer_embed2 = discord.Embed(
                title="**Clothing Designer Application**",
                description="***Do you have anything you would like to say about yourself here? If yes, please do so.***",
                color=0x0064ff
            )
            clothing_designer_embed2.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=clothing_designer_embed2)
            try:
                clothing_designer_information_message = await self.bot.wait_for('message', check=check_dm,
                                                                                timeout=1000)
                clothing_designer_information = clothing_designer_information_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if clothing_designer_information.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            clothing_designer_embed3 = discord.Embed(
                title="**Clothing Designer Application**",
                description="***Anything that you've missed that you would like to add onto your current statement?***",
                color=0x0064ff
            )
            clothing_designer_embed3.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=clothing_designer_embed3)
            try:
                clothing_designer_other_message = await self.bot.wait_for('message', check=check_dm,
                                                                          timeout=1000)
                clothing_designer_other = clothing_designer_other_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if clothing_designer_other.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            await ctx.author.send(
                "Would you like to send this for Application Approval?\n Reply with `yes` or `no`")
            try:
                final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                final_choice = final_choice_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if re.findall("no", final_choice, re.IGNORECASE):
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            elif re.findall("yes", final_choice, re.IGNORECASE):
                await ctx.author.send("Sent for approval!")
                some_channel = self.bot.get_channel(739233957417189547)
                some_role = discord.utils.get(ctx.guild.roles, id=734177621876801637)
                title = "**Clothing Designer Application**"
                pag = Paginator(
                    f"**Work:** {clothing_designer_work}\n**Information:** {clothing_designer_information}\n**Other:** {clothing_designer_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                    1985)

                await pag.send(bot=self.bot, channel=some_channel, role=some_role, member=ctx.author,
                               title=title, mute_role=applications_muted)
                self.clothing_designer_cool = Cooldown(time=datetime.datetime.utcnow())
        elif re.findall("artist", category, re.IGNORECASE):
            if self.artist_cool.cooldown_start_time != 0 and (datetime.datetime.utcnow() - self.artist_cool.cooldown_start_time).total_seconds() < 3600:
                await self.artist_cool.time_it(user=ctx.author)
                return
            artist_embed1 = discord.Embed(
                title="**Artist Application**",
                description="***Provide some work examples you've done in the past. You could link a portfolio. (ATTACHMENTS ARE CURRENTLY NOT SUPPORTED!)***",
                color=0x0064ff
            )
            artist_embed1.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=artist_embed1)
            try:
                artist_work_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                artist_work = artist_work_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if artist_work.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            artist_embed2 = discord.Embed(
                title="**Artist Application**",
                description="***Do you have anything you would like to say about yourself here? If yes, please do so.***",
                color=0x0064ff
            )
            artist_embed2.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=artist_embed2)
            try:
                artist_information_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                artist_information = artist_information_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if artist_information.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            artist_embed3 = discord.Embed(
                title="**Artist Application**",
                description="***Anything that you've missed that you would like to add onto your current statement?***",
                color=0x0064ff
            )
            artist_embed3.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=artist_embed3)
            try:
                artist_other_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                artist_other = artist_other_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if artist_other.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            await ctx.author.send(
                "Would you like to send this for Application Approval?\n Reply with `yes` or `no`")
            try:
                final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                final_choice = final_choice_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if re.findall("no", final_choice, re.IGNORECASE):
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            elif re.findall("yes", final_choice, re.IGNORECASE):
                await ctx.author.send("Sent for approval!")
                some_channel = self.bot.get_channel(739233626960691221)
                some_role = discord.utils.get(ctx.guild.roles, id=734662196025360416)
                title = "**Artist Application**"
                pag = Paginator(
                    f"**Work:** {artist_work}\n**Information:** {artist_information}\n**Other:** {artist_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                    1985)

                await pag.send(bot=self.bot, channel=some_channel, role=some_role, member=ctx.author,
                               title=title, mute_role=applications_muted)
                self.artist_cool = Cooldown(time=datetime.datetime.utcnow())
        elif re.findall("music composer", category, re.IGNORECASE):
            if self.music_composer_cool.cooldown_start_time != 0 and (datetime.datetime.utcnow() - self.music_composer_cool.cooldown_start_time).total_seconds() < 3600:
                await self.music_composer_cool.time_it(user=ctx.author)
                return
            music_composer_embed1 = discord.Embed(
                title="**Music Composer Application**",
                description="***Provide some work examples you've done in the past. You could link a portfolio. (ATTACHMENTS ARE CURRENTLY NOT SUPPORTED!)***",
                color=0x0064ff
            )
            music_composer_embed1.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=music_composer_embed1)
            try:
                music_composer_work_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                music_composer_work = music_composer_work_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if music_composer_work.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            music_composer_embed2 = discord.Embed(
                title="**Music Composer Application**",
                description="***Do you have anything you would like to say about yourself here? If yes, please do so.***",
                color=0x0064ff
            )
            music_composer_embed2.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=music_composer_embed2)
            try:
                music_composer_information_message = await self.bot.wait_for('message', check=check_dm,
                                                                             timeout=1000)
                music_composer_information = music_composer_information_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if music_composer_information.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            music_composer_embed3 = discord.Embed(
                title="**Music Composer Application**",
                description="***Anything that you've missed that you would like to add onto your current statement?***",
                color=0x0064ff
            )
            music_composer_embed3.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=music_composer_embed3)
            try:
                music_composer_other_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                music_composer_other = music_composer_other_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if music_composer_other.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            await ctx.author.send(
                "Would you like to send this for Application Approval?\n Reply with `yes` or `no`")
            try:
                final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                final_choice = final_choice_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if re.findall("no", final_choice, re.IGNORECASE):
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            elif re.findall("yes", final_choice, re.IGNORECASE):
                await ctx.author.send("Sent for approval!")
                some_channel = self.bot.get_channel(739233898600595597)
                some_role = discord.utils.get(ctx.guild.roles, id=735497558855516161)
                title = "**Music Composer Application**"
                pag = Paginator(
                    f"**Work:** {music_composer_work}\n**Information:** {music_composer_information}\n**Other:** {music_composer_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                    1985)

                await pag.send(bot=self.bot, channel=some_channel, role=some_role, member=ctx.author,
                               title=title, mute_role=applications_muted)
                self.music_composer_cool = Cooldown(time=datetime.datetime.utcnow())
        elif re.findall("animator", category, re.IGNORECASE):
            if self.animator_cool.cooldown_start_time != 0 and (datetime.datetime.utcnow() - self.animator_cool.cooldown_start_time).total_seconds() < 3600:
                await self.animator_cool.time_it(user=ctx.author)
                return
            animator_embed1 = discord.Embed(
                title="**Animator Application**",
                description="***Provide some work examples you've done in the past. You could link a portfolio. (ATTACHMENTS ARE CURRENTLY NOT SUPPORTED!)***",
                color=0x0064ff
            )
            animator_embed1.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=animator_embed1)
            try:
                animator_work_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                animator_work = animator_work_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if animator_work.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            animator_embed2 = discord.Embed(
                title="**Animator Application**",
                description="***Do you have anything you would like to say about yourself here? If yes, please do so.***",
                color=0x0064ff
            )
            animator_embed2.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=animator_embed2)
            try:
                animator_information_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                animator_information = animator_information_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if animator_information.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            animator_embed3 = discord.Embed(
                title="**Animator Application**",
                description="***Anything that you've missed that you would like to add onto your current statement?***",
                color=0x0064ff
            )
            animator_embed3.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=animator_embed3)
            try:
                animator_other_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                animator_other = animator_other_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if animator_other.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            await ctx.author.send(
                "Would you like to send this for Application Approval?\n Reply with `yes` or `no`")
            try:
                final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                final_choice = final_choice_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if re.findall("no", final_choice, re.IGNORECASE):
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            elif re.findall("yes", final_choice, re.IGNORECASE):
                await ctx.author.send("Sent for approval!")
                some_channel = self.bot.get_channel(739233745197858855)
                some_role = discord.utils.get(ctx.guild.roles, id=734662028353994752)
                title = "**Animator Application**"
                pag = Paginator(
                    f"**Work:** {animator_work}\n**Information:** {animator_information}\n**Other:** {animator_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                    1985)

                await pag.send(bot=self.bot, channel=some_channel, role=some_role, member=ctx.author,
                               title=title, mute_role=applications_muted)
                self.animator_cool = Cooldown(time=datetime.datetime.utcnow())

    @commands.command(aliases=['code-format', "codeformat", "code format"], description="This command is used for assisting you with formatting your code!")
    async def code_format(self, ctx):
        cancel_prompt_embed = discord.Embed(
            title="**CANCELLED**",
            description="***The setup has been cancelled.***",
            color=0xff0000
        )
        starting_embed = discord.Embed(
            title="**CODE FORMAT**",
            description="***Please continue the setup in DMs.***",
            color=0x0064ff,
            timestamp=datetime.datetime.utcnow()
        )
        question_embed = discord.Embed(
            title="**CODE FORMAT**",
            description="Is your code longer or shorter? Can it fit in a single message? (yes/no)",
            color=0x0064ff
        )
        question_embed.set_footer(text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
        await ctx.send(embed=starting_embed)
        await ctx.author.send(embed=question_embed)

        def check_dm(m):
            if isinstance(m.channel, discord.DMChannel):
                if m.author == ctx.author:
                    return True
                else:
                    return False
            else:
                return False
        try:
            answer_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
            answer = answer_message.content
        except:
            cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
            await ctx.author.send(embed=cancel_prompt_embed)
            return
        if answer == "no":
            for x in range(11):
                code_request_embed = discord.Embed(
                    title="**CODE FORMAT**",
                    description="Please paste your code!",
                    color=0x0064ff
                )
                code_request_embed.set_footer(text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=code_request_embed)
                try:
                    code_request_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    if x == 0:
                        code = code_request_message.content
                    else:
                        code += "\n" + code_request_message.content
                except:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if code.lower() == "cancel":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                more_code_question_embed = discord.Embed(
                    title="**CODE FORMAT**",
                    description="Is there more code? (yes/no)",
                    color=0x0064ff
                )
                more_code_question_embed.set_footer(text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=more_code_question_embed)
                try:
                    more_code_answer_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    more_code_answer = more_code_answer_message.content
                except:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if more_code_answer == "cancel":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if more_code_answer == "no":
                    break
        if answer == "yes":
            code_request_embed = discord.Embed(
                title="**CODE FORMAT**",
                description="Please paste your code!",
                color=0x0064ff
            )
            code_request_embed.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=code_request_embed)
            try:
                code_requesting_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                code_answer = code_requesting_message.content
            except:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if code_answer.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
        code_format_request_embed = discord.Embed(
            title="**CODE FORMAT**",
            description="Please tell us what format you want for your code! Examples: `python`, `lua`, `c`, `csharp`, `c++` and so on",
            color=0x0064ff
        )
        code_format_request_embed.set_footer(text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
        await ctx.author.send(embed=code_format_request_embed)
        try:
            code_format_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
            code_format_answer = code_format_message.content
        except:
            cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
            await ctx.author.send(embed=cancel_prompt_embed)
            return
        if code_format_answer.lower() == "cancel":
            cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
            await ctx.author.send(embed=cancel_prompt_embed)
            return
        if code_format_answer not in self.formats_list:
            return await ctx.author.send("Unknown format!")
        try:
            formated_code = f"\`\`\`{code_format_answer}\n{code_answer or code}\n\`\`\`"
            await ctx.author.send(formated_code)
            await ctx.author.send("Copy the message content above and paste it where you need to!")
        except:
            try:
                mystbin_client = mystbin.Client()

                paste = await mystbin_client.post(code_answer or code, syntax=code_format_answer)

                paste_url = paste.url
                print(paste_url)

                await ctx.author.send(f"This is the link to your code! Copy and paste it where you need to!\n\n{paste_url}")
            except:
                await ctx.author.send("Something went wrong!")

    @commands.command(description="This command is used for posting.")
    async def post(self, ctx):
        allowed_channels = [712659793008918538, 712624774479740931, 712624686399225907, 722898958996865035]

        post_muted = ctx.guild.get_role(780494155075420262)

        if ctx.author in post_muted.members:
            return await ctx.send("You are restricted from using this command, you have the `Post Muted` role. Please consult with a staff member about it.")
        else:
            pass
        if ctx.channel.id not in allowed_channels:
            await ctx.send("Run the command again in <#712659793008918538>")
            return
        cancel_prompt_embed = discord.Embed(
            title="**CANCELLED**",
            description="***The setup has been cancelled.***",
            color=0xff0000
        )
        categories_embed = discord.Embed(
            title="**POST SETUP**",
            description="***Please continue the setup in DMs.***",
            color=0x0064ff,
            timestamp=datetime.datetime.utcnow()
        )
        categories = discord.Embed(
            title="**POST SETUP**",
            description="""
            ***What would you like to do? Reply with the name of the category you would like to post in.***


                `hiring`;

                `for_hire`;

                `sell_creations`;

                `report`;

            """,
            color=0x0064ff,
            timestamp=datetime.datetime.utcnow()
        )
        categories.set_footer(text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
        await ctx.send(embed=categories_embed)
        await ctx.author.send(embed=categories)

        def check_dm(m):
            if isinstance(m.channel, discord.DMChannel):
                if m.author == ctx.author:
                    return True
                else:
                    return False
            else:
                return False
        try:
            picked_category_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
            category = picked_category_message.content
        except asyncio.TimeoutError:
            cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
            await ctx.author.send(embed=cancel_prompt_embed)
            return
        if category.lower() == "cancel":
            cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
            await ctx.author.send(embed=cancel_prompt_embed)
            return
        elif re.findall("hiring", category, re.IGNORECASE):
            if self.hiring_cool.cooldown_start_time != 0 and (datetime.datetime.utcnow() - self.hiring_cool.cooldown_start_time).total_seconds() < 3600:
                await self.hiring_cool.time_it(user=ctx.author)
                return
            hiring_embed1 = discord.Embed(
                title="**HIRING POST**",
                description="***Tell us more about the job, you may freely go into detail as much as you feel like is needed.***",
                color=0x0064ff
            )
            hiring_embed1.set_footer(text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=hiring_embed1)
            try:
                hiring_details_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                hiring_details = hiring_details_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if hiring_details.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            hiring_embed2 = discord.Embed(
                title="**HIRING POST**",
                description="***Describe the payment to this job.***",
                color=0x0064ff
            )
            hiring_embed2.set_footer(text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=hiring_embed2)
            try:
                hiring_payment_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                hiring_payment = hiring_payment_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if hiring_payment.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            hiring_embed3 = discord.Embed(
                title="**HIRING POST**",
                description="***Showcase some of your work here, could be a link to a portfolio. (ATTACHMENTS ARE CURRENTLY NOT SUPPORTED!)***",
                color=0x0064ff
            )
            hiring_embed3.set_footer(text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=hiring_embed3)
            try:
                hiring_image_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                hiring_image = hiring_image_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if hiring_image.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            hiring_embed4 = discord.Embed(
                title="**HIRING POST**",
                description="***In case you have something else that you would like to add onto the previous statements, please provide it now.***",
                color=0x0064ff
            )
            hiring_embed4.set_footer(text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=hiring_embed4)
            try:
                hiring_other_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                hiring_other = hiring_other_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if hiring_other.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            await ctx.author.send(
                "Would you like to send this for Post Approval?\n Reply with `yes` or `no`")
            try:
                final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                final_choice = final_choice_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if re.findall("no", final_choice, re.IGNORECASE):
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if re.findall("yes", final_choice, re.IGNORECASE):
                await ctx.author.send("Sent for approval!")
                some_channel = self.bot.get_channel(739247560065024050)
                end_channel = self.bot.get_channel(727550350097252482)
                title = "**HIRING POST**"
                pag = Paginator(
                    f"**About the job:** {hiring_details}\n**Payment:** {hiring_payment}\n**Showcase:** {hiring_image}\n**Other:** {hiring_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                    1985)

                await pag.send(self.bot, some_channel, end_channel, ctx.author, title, mute_role=post_muted)
                self.hiring_cool = Cooldown(time=datetime.datetime.utcnow())
        elif re.findall("for_hire|for hire|for-hire|forhire", category, re.IGNORECASE):
            if self.for_hire_cool.cooldown_start_time != 0 and (datetime.datetime.utcnow() - self.for_hire_cool.cooldown_start_time).total_seconds() < 3600:
                await self.for_hire_cool.time_it(user=ctx.author)
                return
            for_hire_embed1 = discord.Embed(
                title="**FOR-HIRE POST**",
                description="***Define your specialties here, like for example a Java programmer, an Artist et cetera.***",
                color=0x0064ff
            )
            for_hire_embed1.set_footer(text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=for_hire_embed1)
            try:
                for_hire_specialties_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                for_hire_specialties = for_hire_specialties_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if for_hire_specialties.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            for_hire_embed2 = discord.Embed(
                title="**FOR-HIRE POST**",
                description="***Showcase some of your previous work examples here, could be a link to a portfolio. (ATTACHMENTS ARE CURRENTLY NOT SUPPORTED!)***",
                color=0x0064ff
            )
            for_hire_embed2.set_footer(text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=for_hire_embed2)
            try:
                for_hire_showcase_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                for_hire_showcase = for_hire_showcase_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if for_hire_showcase.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            for_hire_embed3 = discord.Embed(
                title="**FOR-HIRE POST**",
                description="***What is your desired payment for the job? Please define it here.***",
                color=0x0064ff
            )
            for_hire_embed3.set_footer(text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=for_hire_embed3)
            try:
                for_hire_payment_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                for_hire_payment = for_hire_payment_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if for_hire_payment.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            for_hire_embed4 = discord.Embed(
                title="**FOR-HIRE POST**",
                description="***In case you have something else that you would like to add onto the previous statements, please provide it now.***",
                color=0x0064ff
            )
            for_hire_embed4.set_footer(text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=for_hire_embed4)
            try:
                for_hire_other_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                for_hire_other = for_hire_other_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if for_hire_other.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            await ctx.author.send(
                "Would you like to send this for Post Approval?\n Reply with `yes` or `no`")
            try:
                final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                final_choice = final_choice_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if re.findall("no", final_choice, re.IGNORECASE):
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            elif re.findall("yes", final_choice, re.IGNORECASE):
                await ctx.author.send("Sent for approval!")
                some_channel = self.bot.get_channel(739247630193786900)
                end_channel = self.bot.get_channel(727550761801613393)
                title = "**FOR-HIRE POST**"
                pag = Paginator(
                    f"**Specialties:** {for_hire_specialties}\n**Showcase:** {for_hire_showcase}\n**Payment:** {for_hire_payment}\n**Other:** {for_hire_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                    1985)

                await pag.send(self.bot, some_channel, end_channel, ctx.author, title, mute_role=post_muted)
                self.for_hire_cool = Cooldown(time=datetime.datetime.utcnow())
        elif re.findall("sell_creations|sell creations|sell-creations|sellcreations", category, re.IGNORECASE):
            if self.sell_creations_cool.cooldown_start_time != 0 and (datetime.datetime.utcnow() - self.sell_creations_cool.cooldown_start_time).total_seconds() < 3600:
                await self.sell_creations_cool.time_it(user=ctx.author)
                return
            sell_creations_embed1 = discord.Embed(
                title="**SELL-CREATIONS POST**",
                description="***Showcase the creation here. (ATTACHMENTS ARE CURRENTLY NOT SUPPORTED!)***",
                color=0x0064ff
            )
            sell_creations_embed1.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=sell_creations_embed1)
            try:
                sell_creations_showcase_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                sell_creations_showcase = sell_creations_showcase_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if sell_creations_showcase.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            sell_creations_embed2 = discord.Embed(
                title="**SELL-CREATIONS POST**",
                description="***What is your desired payment for your work? Please define it here.***",
                color=0x0064ff
            )
            sell_creations_embed2.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=sell_creations_embed2)
            try:
                sell_creations_payment_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                sell_creations_payment = sell_creations_payment_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if sell_creations_payment.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            sell_creations_embed3 = discord.Embed(
                title="**SELL-CREATIONS POST**",
                description="***In case you have something else that you would like to add onto the previous statements, please provide it now.***",
                color=0x0064ff
            )
            sell_creations_embed3.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=sell_creations_embed3)
            try:
                sell_creations_other_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                sell_creations_other = sell_creations_other_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if sell_creations_other.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            await ctx.author.send(
                "Would you like to send this for Post Approval?\n Reply with `yes` or `no`")
            try:
                final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                final_choice = final_choice_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if re.findall("no", final_choice, re.IGNORECASE):
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            elif re.findall("yes", final_choice, re.IGNORECASE):
                await ctx.author.send("Sent for approval!")
                some_channel = self.bot.get_channel(739247602393940168)
                end_channel = self.bot.get_channel(727550553806340197)
                title = "**SELL-CREATIONS POST**"
                pag = Paginator(
                    f"**Showcase:** {sell_creations_showcase}\n**Payment:** {sell_creations_payment}\n**Other:** {sell_creations_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                    1985)

                await pag.send(self.bot, some_channel, end_channel, ctx.author, title, mute_role=post_muted)
                self.sell_creations_cool = Cooldown(time=datetime.datetime.utcnow())
        elif re.findall("report", category, re.IGNORECASE):
            if self.report_cool.cooldown_start_time != 0 and (datetime.datetime.utcnow() - self.report_cool.cooldown_start_time).total_seconds() < 3600:
                await self.report_cool.time_it(user=ctx.author)
                return
            report_embed1 = discord.Embed(
                title="**REPORT POST**",
                description="***Who are you filing this report on? Please provide their Username and Discriminator/Tag. Example: Noob#1234 or MarkiPro#3753***",
                color=0x0064ff
            )
            report_embed1.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=report_embed1)
            try:
                reported_user_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                reported_user = reported_user_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if reported_user.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            report_embed2 = discord.Embed(
                title="**REPORT POST**",
                description="***What did this person do?***",
                color=0x0064ff
            )
            report_embed2.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=report_embed2)
            try:
                report_reason_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                report_reason = report_reason_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if report_reason.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            report_embed3 = discord.Embed(
                title="**REPORT POST**",
                description="***Do you have any evidence? If so, provide it here (ATTACHMENTS ARE NOT SUPPORTED!)***",
                color=0x0064ff
            )
            report_embed3.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=report_embed3)
            try:
                report_evidence_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                report_evidence = report_evidence_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if report_evidence.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            report_embed4 = discord.Embed(
                title="**REPORT POST**",
                description="***In case you have something else you wanted to add onto your current statement, please do.***",
                color=0x0064ff
            )
            report_embed4.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=report_embed4)
            try:
                report_other_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                report_other = report_other_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if report_other.lower() == "cancel":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            await ctx.author.send(
                "Would you like to send this for Post Approval?\n Reply with `yes` or `no`")
            try:
                final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                final_choice = final_choice_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if re.findall("no", final_choice, re.IGNORECASE):
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            elif re.findall("yes", final_choice, re.IGNORECASE):
                await ctx.author.send("Sent!")
                some_channel = self.bot.get_channel(773637163048239124)
                title = "**REPORT POST**"
                pag = Paginator(
                    f"**Subject Information:** {reported_user}\n**Report Reason:** {report_reason}\n**Evidence:** {report_evidence}\n**Other:** {report_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                    1985)

                await pag.send(bot=self.bot, channel=some_channel, member=ctx.author, title=title, mute_role=post_muted)
                self.report_cool = Cooldown(time=datetime.datetime.utcnow())

    @commands.command(
        aliases=["server-info", "si", "s-i", "guild-info", "guildinfo", "gi", "g-i", "server_info", "s_i", "guild_info",
                 "g_i"], description="Displays basic information about the server.")
    async def serverinfo(self, ctx):
        allowed_channels = [712659793008918538, 712624774479740931, 712624686399225907, 722898958996865035]

        if ctx.channel.id not in allowed_channels:
            return
        guild = ctx.guild
        embed = discord.Embed(
            title=f"Server Information for {guild.name}",
            description=f"{guild.description}",
            timestamp=datetime.datetime.utcnow(),
            color=0x0064ff
        )

        bot_role = discord.utils.get(guild.roles, id=712623235807838258)
        bots_amount = len(bot_role.members)
        boosters_amount = len(guild.premium_subscribers)
        human_member_count = ctx.guild.member_count - bots_amount
        roles_amount = len(guild.roles)
        text_channels_amount = len(guild.text_channels)
        voice_channels_amount = len(guild.voice_channels)
        categoires_amount = len(guild.categories)

        embed.add_field(name="Server ID", value=f"{guild.id}", inline=True)
        embed.add_field(name="Server Created", value=f"{guild.created_at}", inline=True)
        embed.add_field(name="Member Count",
                        value=f"Total: {guild.member_count}\n Humans: {human_member_count}\n Boosters: {boosters_amount}\nBots: {bots_amount}",
                        inline=True)
        embed.add_field(name="Boost Level", value=f"{guild.premium_tier}")
        embed.add_field(name="Roles Amount", value=f"{roles_amount}", inline=True)
        embed.add_field(name="Categories Amount", value=f"{categoires_amount}")
        embed.add_field(name="Channels Amount",
                        value=f"Text Channels: {text_channels_amount}\n Voice Channels: {voice_channels_amount}")
        embed.add_field(name="Server Region", value=f"{guild.region}", inline=True)
        embed.add_field(name="Verification Level", value=f"{guild.verification_level}", inline=True)
        if guild.banner:
            embed.set_image(url=guild.banner_url)
        embed.set_thumbnail(url=guild.icon_url)

        await ctx.send(embed=embed)

    @commands.command(aliases=["who", "user-info", "userinfo", "ui", "u-i", "who-is", "who_is", "profile"],
                      description="Displays basic information about the supplied user. If the user is not provided, it would default to the command requester.")
    async def whois(self, ctx, user: discord.Member = None):
        allowed_channels = [712659793008918538, 712624774479740931, 712624686399225907, 722898958996865035]

        if ctx.channel.id not in allowed_channels:
            await ctx.send("Run the command again in <#712659793008918538>")
            return
        user = user or ctx.author

        join_pos = sum([m.joined_at < user.joined_at for m in ctx.guild.members if m.joined_at is not None])
        embed = discord.Embed(title=f"**Who is {user}**",
                              timestamp=datetime.datetime.utcnow(),
                              color=0x0064ff)
        format = "%A, %d %B, %Y : %I:%M %p"
        delta_joined = datetime.datetime.utcnow() - user.joined_at
        delta_created = datetime.datetime.utcnow() - user.created_at
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="Joined on", value=f"{user.joined_at.strftime(format)} ({delta_joined.days} days)",
                        inline=True)
        embed.add_field(name="Status",
                        value=f"Desktop Status: {user.desktop_status}\nMobile Status: {user.mobile_status}\n Web Status: {user.web_status}")
        embed.add_field(name="Account created on",
                        value=f"{user.created_at.strftime(format)} ({delta_created.days} days)", inline=True)
        embed.add_field(name="Nickname", value=f"{user.nick}", inline=True)
        embed.add_field(name="Join Position", value=f"#{join_pos}", inline=True)
        exculded_roles = [611227128020598805, 707957214995808296, 732375953203789965, 743590325448212651,
                          743013370588037191, 732388199107657828, 743013368511594569, 743013366515236915,
                          743013366880272474, 743013367840768072, 743013368134107166, 732387788493946881,
                          732402691296198848, 734149969292034208, 734150445764837466, 734150696944795698,
                          735497751978311681, 734527020905529375, 734664303327838230, 734527130565738516,
                          735557139984285706, 738814580712669214, 734664243038912552, 734527217350082672,
                          734527854871707762, 746758563703291938]
        roles = ", ".join(role.mention for role in user.roles if role.id not in exculded_roles) or 'No roles assigned.'
        embed.add_field(name="Guild Roles", value=f"{roles}", inline=False)
        notable_perms = ['administrator', 'manage_guild', 'view_audit_log', 'manage_roles', 'manage_channels',
                         'ban_members', 'kick_members', 'manage_messages', 'mention_everyone', 'manage_emojis',
                         'manage_webhooks', 'manage_nicknames', 'mute_members', 'deafen_members', 'move_members',
                         'priority_speaker']
        member_permissions = ", ".join(f"{i.title().replace('_', ' ')}" for i in notable_perms if
                                       getattr(user.permissions_in(ctx.channel), i, False)) or "No Permissions."
        embed.add_field(name="Guild Permissions", value=f"{member_permissions}", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def role(self, ctx, *, role_name=None):
        roles = {"former staff": 741728478721736755, "roblox verified": 741735258411499560,
                 "verified": 695328817157373992, "devforum member": 742333164352962581,
                 "devforum regular": 742333167133786124, "devforum editor": 742333168576888943,
                 "devforum leader": 742333169423876106, "first server booster": 712685506424471612,
                 "server booster": 762172204628181023, "animator": 734662028353994752,
                 "music composer": 735497558855516161, "artist": 734662196025360416,
                 "clothing designer": 734177621876801637, "ui designer": 733274530524561430,
                 "translator": 734527264657637416, "gfx designer": 733280979921141821,
                 "twitch streamer": 738814393663619182, "builder": 733281281671954442, "youtuber": 738788543211634756,
                 "3d modeler": 733281157872877629, "game designer": 733281086913773599,
                 "css programmer": 741099963626422322, "html & css programmer": 735147383716970507,
                 "ruby programmer": 735147661430227025, "lua programmer": 732376072397783093,
                 "php programmer": 732378321387520092, "c programmer": 732378157449216040,
                 "c++ programmer": 732377777772167188, "js programmer": 732377955669508097,
                 "java programmer": 732379273100263464, "c# programmer": 732377857317142650,
                 "python programmer": 732377712286761001}
        chat_color_roles = {"former staff": 743013368511594569, "roblox verified": 743013370588037191,
                            "verified": 732388199107657828, "devforum member": 743013366515236915,
                            "devforum regular": 743013366880272474, "devforum editor": 743013367840768072,
                            "devforum leader": 743013368134107166, "server booster": 734527854871707762,
                            "animator": 734664243038912552, "music composer": 735497751978311681,
                            "artist": 734664303327838230, "clothing designer": 734527130565738516,
                            "ui designer": 734150445764837466, "translator": 734527217350082672,
                            "gfx designer": 734150696944795698, "twitch streamer": 738814580712669214,
                            "builder": 734149969292034208, "youtuber": 735557139984285706,
                            "3d modeler": 734527020905529375, "game designer": 732402691296198848,
                            "html & css programmer": 732387788493946881, "css programmer": 732387788493946881, "js programmer": 732387788493946881, "java programmer": 732387788493946881, "php programmer": 732387788493946881, "lua programmer": 732387788493946881, "python programmer": 732387788493946881, "c++ programmer": 732387788493946881, "c# programmer": 732387788493946881, "c programmer": 732387788493946881, "ruby programmer": 732387788493946881}
        if role_name:
            desired_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles[role_name])
            needed_role = discord.utils.get(ctx.guild.roles, id=roles[role_name])

            if needed_role in ctx.author.roles:
                await ctx.author.add_roles(desired_role)
                await ctx.send(f"Successfully given you the chat color role!")

                for role in chat_color_roles:
                    check_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles[role])

                    if check_role in ctx.author.roles:
                        await ctx.author.remove_roles(check_role)

            elif needed_role not in ctx.author.roles:
                await ctx.send("You do not have the required role! Please run `>apply`!")
        else:
            await ctx.send("Role not listed or doesn't exist, please run `/tag chat color roles` to see which roles are listed.")

    @commands.command()
    async def boosters(self, ctx):
        allowed_channels = [712659793008918538, 712624774479740931, 712624686399225907, 722898958996865035]

        if ctx.channel.id not in allowed_channels:
            await ctx.send("Run the command again in <#712659793008918538>")
            return
        boosters = "\n".join([i.mention for i in ctx.guild.premium_subscribers])

        embed = discord.Embed(
            title="**BOOSTERS**",
            description=f"***These are the boosters on the server:\n\n***{boosters}",
            color=0x0089ff,
            timestamp=datetime.datetime.utcnow()
        )

        if boosters is "":
            embed.description = "There are no boosters in this guild.  :cry:"
            pass

        await ctx.send(embed=embed)

    @commands.command()
    async def members(self, ctx, *, role: discord.Role = None):
        role_members = "\n".join([i.mention for i in role.members])
        allowed_channels = [712659793008918538, 712624774479740931, 712624686399225907, 722898958996865035]

        if ctx.channel.id not in allowed_channels:
            await ctx.send("Run the command again in <#712659793008918538>")
            return
        else:
            pass
        if role_members == "":
            await ctx.send("There are no members with this role!")
            return
        else:
            pass
        pag = Paginator(f"Members with the role {role} are displayed below:\n\n {role_members}", 1985)
        await pag.send(bot=self.bot, channel=ctx.channel, members_thing=True, title=f"Members of Role **{role}**")


def setup(bot):
    bot.add_cog(Misc(bot))
