import discord
from discord.ext import commands
import datetime
import asyncio
from paginator import Paginator
import re


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.help_command.cog = self

    @commands.command(aliases=["for-hire", "forhire"],
                      description="Toggle Not For Hire role off, and For Hire on, that way everyone knows you are for hire.")
    @commands.cooldown(1, 300, commands.BucketType.member)
    async def fh(self, ctx):
        bot_commands = self.bot.get_channel(712659793008918538)

        if ctx.channel != bot_commands:
            return
        else:
            pass
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
        bot_commands = self.bot.get_channel(712659793008918538)

        if ctx.channel != bot_commands:
            return
        else:
            pass
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

    @commands.command()
    async def credits(self, ctx):
        malware = await ctx.bot.fetch_user(730082562868772924)
        markipro = await ctx.bot.fetch_user(530461779768377357)

        credits_embed = discord.Embed(
            title="**Credits**",
            description=f"Bot Creator: **{markipro}**\nHuge thank you to **{malware}**!\nWho contributed a lot!",
            timestamp=datetime.datetime.utcnow(),
            color=0x0064ff
        )
        await ctx.send(embed=credits_embed)

    @commands.command(description="This command is used for applying for appliable roles (STAFF ROLES NOT INCLUDED!).")
    @commands.cooldown(3, 10800, commands.BucketType.member)
    async def apply(self, ctx):
        bot_commands = self.bot.get_channel(712659793008918538)

        if ctx.channel != bot_commands:
            return
        else:
            pass
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
                
                `Roblox Studio Builder`;
                
                `Twitch Streamer`;
                
                `GFX Designer`;
                
                `Translator`;
                
                `UI Designer`;
                
                `Clothing Designer`;
                
                `Artist`;
                
                `Music Composer`;
                
                `Animator`;
                
            """,
            color=0x0064ff
        )
        categories.set_footer(text="React to this message within `16 minutes` • React with `cancel` to cancel.")
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
        if re.findall("cancel", category, re.IGNORECASE):
            cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
            await ctx.author.send(embed=cancel_prompt_embed)
            return

        if re.findall("programmer", category, re.IGNORECASE):
            programmer_categories = discord.Embed(
                title="**APPLICATION SETUP**",
                description="""
                Which Programmer role would you like to apply for? Reply with the number in front of the role you would like to apply for.

                `Python Programmer`;

                `C# Programmer`;

                `Java Programmer`;

                `JavaScript Programmer`;

                `CPP Programmer`;

                `C Programmer`;

                `PHP Programmer`;

                `Lua Programmer`;

                `Ruby Programmer`;

                `XML Programmer`;

                `CSS Programmer`;""",
                color=0x0064ff
            )
            programmer_categories.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
            await ctx.author.send(embed=categories)
            try:
                picked_programmer_category_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                programmer_category = picked_programmer_category_message.content
            except asyncio.TimeoutError:
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if re.findall("cancel", programmer_category, re.IGNORECASE):
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            elif re.findall("python programmer", programmer_category, re.IGNORECASE):
                programmer_embed1 = discord.Embed(
                    title="Python Programmer Post",
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
                if re.findall("cancel", programmer_work, re.IGNORECASE):
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_embed1 = discord.Embed(
                    title="Python Programmer Post",
                    description="***Do you have anything you would like to say about yourself here? If yes, please do so.***",
                    color=0x0064ff
                )
                programmer_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed1)
                try:
                    programmer_information_message = await self.bot.wait_for('message', check=check_dm,
                                                                      timeout=1000)
                    programmer_information = programmer_information_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if re.findall("cancel", programmer_information, re.IGNORECASE):
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
                if re.findall("cancel", programmer_other, re.IGNORECASE):
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
                                   title=title)
            elif re.findall("c# programmer", programmer_category, re.IGNORECASE):
                programmer_embed1 = discord.Embed(
                    title="C# Programmer Post",
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
                if re.findall("cancel", programmer_work, re.IGNORECASE):
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_embed1 = discord.Embed(
                    title="C# Programmer Post",
                    description="***Do you have anything you would like to say about yourself here? If yes, please do so.***",
                    color=0x0064ff
                )
                programmer_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed1)
                try:
                    programmer_information_message = await self.bot.wait_for('message', check=check_dm,
                                                                      timeout=1000)
                    programmer_information = programmer_information_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if re.findall("cancel", programmer_information, re.IGNORECASE):
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
                if re.findall("cancel", programmer_other, re.IGNORECASE):
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
                                   title=title)
            elif re.findall("java programmer", programmer_category, re.IGNORECASE):
                programmer_embed1 = discord.Embed(
                    title="Java Programmer Post",
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
                if re.findall("cancel", programmer_work, re.IGNORECASE):
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_embed1 = discord.Embed(
                    title="Java Programmer Post",
                    description="***Do you have anything you would like to say about yourself here? If yes, please do so.***",
                    color=0x0064ff
                )
                programmer_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed1)
                try:
                    programmer_information_message = await self.bot.wait_for('message', check=check_dm,
                                                                      timeout=1000)
                    programmer_information = programmer_information_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if re.findall("cancel", programmer_information, re.IGNORECASE):
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
                if re.findall("cancel", programmer_other, re.IGNORECASE):
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
                                   title=title)
            elif re.findall("javascript programmer", programmer_category, re.IGNORECASE):
                programmer_embed1 = discord.Embed(
                    title="JavaScript Programmer Post",
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
                if re.findall("cancel", programmer_work, re.IGNORECASE):
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_embed1 = discord.Embed(
                    title="JavaScript Programmer Post",
                    description="***Do you have anything you would like to say about yourself here? If yes, please do so.***",
                    color=0x0064ff
                )
                programmer_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed1)
                try:
                    programmer_information_message = await self.bot.wait_for('message', check=check_dm,
                                                                      timeout=1000)
                    programmer_information = programmer_information_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if re.findall("cancel", programmer_information, re.IGNORECASE):
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
                if re.findall("cancel", programmer_other, re.IGNORECASE):
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
                                   title=title)

            elif re.findall("cpp programmer", programmer_category, re.IGNORECASE):
                programmer_embed1 = discord.Embed(
                    title="CPP Programmer Post",
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
                if re.findall("cancel", programmer_work, re.IGNORECASE):
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_embed1 = discord.Embed(
                    title="CPP Programmer Post",
                    description="***Do you have anything you would like to say about yourself here? If yes, please do so.***",
                    color=0x0064ff
                )
                programmer_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed1)
                try:
                    programmer_information_message = await self.bot.wait_for('message', check=check_dm,
                                                                      timeout=1000)
                    programmer_information = programmer_information_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if re.findall("cancel", programmer_information, re.IGNORECASE):
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
                if re.findall("cancel", programmer_other, re.IGNORECASE):
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
                                   title=title)
            elif re.findall("c programmer", programmer_category, re.IGNORECASE):
                programmer_embed1 = discord.Embed(
                    title="C Programmer Post",
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
                if re.findall("cancel", programmer_work, re.IGNORECASE):
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_embed1 = discord.Embed(
                    title="C Programmer Post",
                    description="***Do you have anything you would like to say about yourself here? If yes, please do so.***",
                    color=0x0064ff
                )
                programmer_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed1)
                try:
                    programmer_information_message = await self.bot.wait_for('message', check=check_dm,
                                                                      timeout=1000)
                    programmer_information = programmer_information_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if re.findall("cancel", programmer_information, re.IGNORECASE):
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
                if re.findall("cancel", programmer_other, re.IGNORECASE):
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
                elif re.findall("cancel", programmer_other, re.IGNORECASE):
                    await ctx.author.send("Sent for approval!")
                    some_channel = self.bot.get_channel(739233448186609756)
                    some_role = discord.utils.get(ctx.guild.roles, id=732378157449216040)
                    title = "**C Programmer Application**"
                    pag = Paginator(
                        f"**Work:** {programmer_work}\n**Information:** {programmer_information}\n**Other:** {programmer_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                        1985)

                    await pag.send(bot=self.bot, channel=some_channel, role=some_role, member=ctx.author,
                                   title=title)
            elif re.findall("php programmer", programmer_category, re.IGNORECASE):
                programmer_embed1 = discord.Embed(
                    title="PHP Programmer Post",
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
                if re.findall("cancel", programmer_work, re.IGNORECASE):
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_embed1 = discord.Embed(
                    title="PHP Programmer Post",
                    description="***Do you have anything you would like to say about yourself here? If yes, please do so.***",
                    color=0x0064ff
                )
                programmer_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed1)
                try:
                    programmer_information_message = await self.bot.wait_for('message', check=check_dm,
                                                                      timeout=1000)
                    programmer_information = programmer_information_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if re.findall("cancel", programmer_information, re.IGNORECASE):
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
                if re.findall("cancel", programmer_other, re.IGNORECASE):
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
                                   title=title)
            elif re.findall("lua programmer", programmer_category, re.IGNORECASE):
                programmer_embed1 = discord.Embed(
                    title="Lua Programmer Post",
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
                if re.findall("cancel", programmer_work, re.IGNORECASE):
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_embed1 = discord.Embed(
                    title="Lua Programmer Post",
                    description="***Do you have anything you would like to say about yourself here? If yes, please do so.***",
                    color=0x0064ff
                )
                programmer_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed1)
                try:
                    programmer_information_message = await self.bot.wait_for('message', check=check_dm,
                                                                      timeout=1000)
                    programmer_information = programmer_information_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if re.findall("cancel", programmer_information, re.IGNORECASE):
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
                if re.findall("cancel", programmer_other, re.IGNORECASE):
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
                                   title=title)
            elif re.findall("ruby programmer", programmer_category, re.IGNORECASE):
                programmer_embed1 = discord.Embed(
                    title="Ruby Programmer Post",
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
                if re.findall("cancel", programmer_work, re.IGNORECASE):
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_embed1 = discord.Embed(
                    title="Ruby Programmer Post",
                    description="***Do you have anything you would like to say about yourself here? If yes, please do so.***",
                    color=0x0064ff
                )
                programmer_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed1)
                try:
                    programmer_information_message = await self.bot.wait_for('message', check=check_dm,
                                                                      timeout=1000)
                    programmer_information = programmer_information_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if re.findall("cancel", programmer_information, re.IGNORECASE):
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
                if re.findall("cancel", programmer_other, re.IGNORECASE):
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
                if re.findall("cancel", final_choice, re.IGNORECASE):
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                elif re.findall("cancel", final_choice, re.IGNORECASE):
                    await ctx.author.send("Sent for approval!")
                    some_channel = self.bot.get_channel(739233479098761307)
                    some_role = discord.utils.get(ctx.guild.roles, id=735147661430227025)
                    title = "**Ruby Programmer Application**"
                    pag = Paginator(
                        f"**Work:** {programmer_work}\n**Information:** {programmer_information}\n**Other:** {programmer_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                        1985)

                    await pag.send(bot=self.bot, channel=some_channel, role=some_role, member=ctx.author,
                                   title=title)
            elif re.findall("xml programmer", programmer_category, re.IGNORECASE):
                programmer_embed1 = discord.Embed(
                    title="XML Programmer Post",
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
                if re.findall("cancel", programmer_work, re.IGNORECASE):
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_embed1 = discord.Embed(
                    title="XML Programmer Post",
                    description="***Do you have anything you would like to say about yourself here? If yes, please do so.***",
                    color=0x0064ff
                )
                programmer_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed1)
                try:
                    programmer_information_message = await self.bot.wait_for('message', check=check_dm,
                                                                      timeout=1000)
                    programmer_information = programmer_information_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if re.findall("cancel", programmer_information, re.IGNORECASE):
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_embed3 = discord.Embed(
                    title="**XML Programmer Application**",
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
                if re.findall("cancel", programmer_other, re.IGNORECASE):
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
                    some_channel = self.bot.get_channel(739233397741715507)
                    some_role = discord.utils.get(ctx.guild.roles, id=735147383716970507)
                    title = "**XML Programmer Application**"
                    pag = Paginator(
                        f"**Work:** {programmer_work}\n**Information:** {programmer_information}\n**Other:** {programmer_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                        1985)

                    await pag.send(bot=self.bot, channel=some_channel, role=some_role, member=ctx.author,
                                   title=title)
            elif re.findall("css programmer", programmer_category, re.IGNORECASE):
                programmer_embed1 = discord.Embed(
                    title="CSS Programmer Post",
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
                if re.findall("cancel", programmer_work, re.IGNORECASE):
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_embed1 = discord.Embed(
                    title="CSS Programmer Post",
                    description="***Do you have anything you would like to say about yourself here? If yes, please do so.***",
                    color=0x0064ff
                )
                programmer_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=programmer_embed1)
                try:
                    programmer_information_message = await self.bot.wait_for('message', check=check_dm,
                                                                      timeout=1000)
                    programmer_information = programmer_information_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if re.findall("cancel", programmer_information, re.IGNORECASE):
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                programmer_embed3 = discord.Embed(
                    title="**CSS Programmer Application**",
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
                if re.findall("cancel", programmer_other, re.IGNORECASE):
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
                    title = "**CSS Programmer Application**"
                    pag = Paginator(
                        f"**Work:** {programmer_work}\n**Information:** {programmer_information}\n**Other:** {programmer_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                        1985)

                    await pag.send(bot=self.bot, channel=some_channel, role=some_role, member=ctx.author,
                                   title=title)

        elif re.findall("game designer", category, re.IGNORECASE):
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
            if re.findall("cancel", game_designer_work, re.IGNORECASE):
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
            if re.findall("cancel", game_designer_information, re.IGNORECASE):
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
            if re.findall("cancel", game_designer_other, re.IGNORECASE):
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
                               title=title)
        elif re.findall("3d modeler", category, re.IGNORECASE):
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
            if re.findall("cancel", threed_modeler_work, re.IGNORECASE):
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
            if re.findall("cancel", threed_modeler_information, re.IGNORECASE):
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
            if re.findall("cancel", threed_modeler_other, re.IGNORECASE):
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
                               title=title)
        elif re.findall("youtuber", category, re.IGNORECASE):
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
            if re.findall("cancel", youtuber_subs, re.IGNORECASE):
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
            if re.findall("cancel", youtuber_channel, re.IGNORECASE):
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
            if re.findall("cancel", youtuber_other, re.IGNORECASE):
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
                               title=title)

        elif re.findall("roblox studio builder", category, re.IGNORECASE):
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
            if re.findall("cancel", builder_work, re.IGNORECASE):
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
            if re.findall("cancel", builder_information, re.IGNORECASE):
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
            if re.findall("cancel", builder_other, re.IGNORECASE):
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
                               title=title)
        elif re.findall("twitch streamer", category, re.IGNORECASE):
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
            if re.findall("cancel", twitch_streamer_follows, re.IGNORECASE):
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
            if re.findall("cancel", twitch_streamer_channel, re.IGNORECASE):
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
            if re.findall("cancel", twitch_streamer_other, re.IGNORECASE):
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
                               title=title)
        elif re.findall("gfx designer", category, re.IGNORECASE):
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
            if re.findall("cancel", gfx_designer_work, re.IGNORECASE):
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
            if re.findall("cancel", gfx_designer_information, re.IGNORECASE):
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
                               title=title)
        elif re.findall("translator", category, re.IGNORECASE):
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
            if re.findall("cancel", translator_work, re.IGNORECASE):
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
            if re.findall("cancel", translator_information, re.IGNORECASE):
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
            if re.findall("cancel", translator_other, re.IGNORECASE):
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
                               title=title)
        elif re.findall("ui designer", category, re.IGNORECASE):
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
            if re.findall("cancel", ui_designer_work, re.IGNORECASE):
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
            if re.findall("cancel", ui_designer_information, re.IGNORECASE):
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
            if re.findall("cancel", ui_designer_other, re.IGNORECASE):
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
                               title=title)
        elif re.findall("clothing designer", category, re.IGNORECASE):
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
            if re.findall("cancel", clothing_designer_work, re.IGNORECASE):
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
            if re.findall("cancel", clothing_designer_information, re.IGNORECASE):
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
            if re.findall("cancel", clothing_designer_other, re.IGNORECASE):
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
                               title=title)
        elif re.findall("artist", category, re.IGNORECASE):
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
            if re.findall("cancel", artist_work, re.IGNORECASE):
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
            if re.findall("cancel", artist_information, re.IGNORECASE):
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
            if re.findall("cancel", artist_other, re.IGNORECASE):
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
                               title=title)
        elif re.findall("music composer", category, re.IGNORECASE):
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
            if re.findall("cancel", music_composer_work, re.IGNORECASE):
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
            if re.findall("cancel", music_composer_information, re.IGNORECASE):
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
            if re.findall("cancel", music_composer_other, re.IGNORECASE):
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
                               title=title)
        elif re.findall("animator", category, re.IGNORECASE):
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
            if re.findall("cancel", animator_work, re.IGNORECASE):
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
            if re.findall("cancel", animator_information, re.IGNORECASE):
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
            if re.findall("cancel", animator_other, re.IGNORECASE):
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
                some_role = discord.utils.get(ctx.guild.roles, id=729491617630912613)
                title = "**Animator Application**"
                pag = Paginator(
                    f"**Work:** {animator_work}\n**Information:** {animator_information}\n**Other:** {animator_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                    1985)

                await pag.send(bot=self.bot, channel=some_channel, role=some_role, member=ctx.author,
                               title=title)

    @commands.command(description="This command is used for posting.")
    @commands.cooldown(3, 10800, commands.BucketType.member)
    async def post(self, ctx):
        bot_commands = self.bot.get_channel(712659793008918538)

        if ctx.channel != bot_commands:
            return
        else:
            pass
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
            ***What would you like to do? React with the number in front of the category you would like to post in.***


                `hiring`;

                `for-hire`;

                `sell_creations`;

                `report`;

            """,
            color=0x0064ff
        )
        categories.set_footer(text="React to this message within `16 minutes` • Reply with `cancel` to cancel.")
        await ctx.send(embed=categories_embed)
        category_message = await ctx.author.send(embed=categories)

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
        if re.findall("cancel", category, re.IGNORECASE):
            cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
            await ctx.author.send(embed=cancel_prompt_embed)
            return
        elif re.findall("hiring", category, re.IGNORECASE):
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
            if re.findall("cancel", hiring_details, re.IGNORECASE):
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
            if re.findall("cancel", hiring_payment, re.IGNORECASE):
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
            if re.findall("cancel", hiring_image, re.IGNORECASE):
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
            if re.findall("cancel", hiring_other, re.IGNORECASE):
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
            if re.findall("no", category, re.IGNORECASE):
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            if re.findall("yes", category, re.IGNORECASE):
                await ctx.author.send("Sent for approval!")
                some_channel = self.bot.get_channel(739247560065024050)
                end_channel = self.bot.get_channel(727550350097252482)
                title = "**HIRING POST**"
                pag = Paginator(
                    f"**About the job:** {hiring_details}\n**Payment:** {hiring_payment}\n**Showcase:** {hiring_image}\n**Other:** {hiring_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                    1985)

                await pag.send(self.bot, some_channel, end_channel, ctx.author, title)
        elif re.findall("for_hire", category, re.IGNORECASE):
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
            if re.findall("cancel", for_hire_specialties, re.IGNORECASE):
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
            if re.findall("cancel", for_hire_showcase, re.IGNORECASE):
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
            if re.findall("cancel", for_hire_payment, re.IGNORECASE):
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
            if re.findall("cancel", for_hire_other, re.IGNORECASE):
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
            elif re.findall("no", final_choice, re.IGNORECASE):
                await ctx.author.send("Sent for approval!")
                some_channel = self.bot.get_channel(739247630193786900)
                end_channel = self.bot.get_channel(727550761801613393)
                title = "**FOR-HIRE POST**"
                pag = Paginator(
                    f"**Specialties:** {for_hire_specialties}\n**Showcase:** {for_hire_showcase}\n**Payment:** {for_hire_payment}\n**Other:** {for_hire_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                    1985)

                await pag.send(self.bot, some_channel, end_channel, ctx.author, title)
        elif re.findall("sell_creations", category, re.IGNORECASE):
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
            if re.findall("cancel", sell_creations_showcase, re.IGNORECASE):
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
            if re.findall("cancel", sell_creations_payment, re.IGNORECASE):
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
            if re.findall("cancel", sell_creations_other, re.IGNORECASE):
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

                await pag.send(self.bot, some_channel, end_channel, ctx.author, title)
        elif re.findall("report", category, re.IGNORECASE):
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
            if re.findall("cancel", reported_user, re.IGNORECASE):
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
            if re.findall("cancel", report_reason, re.IGNORECASE):
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
            if re.findall("cancel", report_evidence, re.IGNORECASE):
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
            if re.findall("cancel", report_other, re.IGNORECASE):
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

                await pag.send(bot=self.bot, channel=some_channel, member=ctx.author, title=title)

    @commands.command(
        aliases=["server-info", "si", "s-i", "guild-info", "guildinfo", "gi", "g-i", "server_info", "s_i", "guild_info",
                 "g_i"], description="Displays basic information about the server.")
    async def serverinfo(self, ctx):
        bot_commands = self.bot.get_channel(712659793008918538)

        if ctx.channel != bot_commands:
            return
        else:
            pass

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
        bot_commands = self.bot.get_channel(712659793008918538)

        if ctx.channel != bot_commands:
            return
        else:
            pass
        user = user or ctx.author

        join_pos = sum([m.joined_at < user.joined_at for m in ctx.guild.members if m.joined_at is not None])
        embed = discord.Embed(title=f"**Who is {user}**".upper(),
                              timestamp=datetime.datetime.utcnow(),
                              color=0x0064ff)
        if user.activities and user.activities == discord.ActivityType.custom:
            embed.description = f"{user.status}"
            pass
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
                 "devforum regular": 742333167133786124, "devforum top contributor": 742333168576888943,
                 "devforum community sage": 742333169423876106, "first server booster": 712685506424471612,
                 "server booster": 762172204628181023, "animator": 734662028353994752,
                 "music composer": 735497558855516161, "Artist": 734662196025360416,
                 "Clothing Designer": 734177621876801637, "UI Designer": 733274530524561430,
                 "Translator": 734527264657637416, "gfx designer": 733280979921141821,
                 "twitch streamer": 738814393663619182, "builder": 733281281671954442, "YouTuber": 738788543211634756,
                 "3d modeler": 733281157872877629, "game designer": 733281086913773599,
                 "css programmer": 741099963626422322, "xml programmer": 735147383716970507,
                 "ruby programmer": 735147661430227025, "lua programmer": 732376072397783093,
                 "php programmer": 732378321387520092, "c programmer": 732378157449216040,
                 "c++ programmer": 732377777772167188, "js programmer": 732377955669508097,
                 "java programmer": 732379273100263464, "c# programmer": 732377857317142650,
                 "python programmer": 732377712286761001}
        chat_color_roles = {"former staff": 743013368511594569, "roblox verified": 743013370588037191,
                            "verified": 732388199107657828, "devforum member": 743013366515236915,
                            "devforum regular": 743013366880272474, "devforum top contributor": 743013367840768072,
                            "devforum community sage": 743013368134107166, "server booster": 734527854871707762,
                            "animator": 734664243038912552, "music composer": 735497751978311681,
                            "Artist": 734664303327838230, "Clothing Designer": 734527130565738516,
                            "UI Designer": 734150445764837466, "Translator": 734527217350082672,
                            "gfx designer": 734150696944795698, "twitch streamer": 738814580712669214,
                            "builder": 734149969292034208, "YouTuber": 735557139984285706,
                            "3d modeler": 734527020905529375, "game designer": 732402691296198848,
                            "programmer": 732387788493946881}

        if role_name:
            if re.findall("former staff", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["former staff"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["former staff"])

                if role in ctx.author.roles:
                    for i in chat_color_roles:
                        another_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles[i])
                        if another_role in ctx.author.roles:
                            await ctx.author.remove_roles(another_role)
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send(
                        "You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.findall("roblox verified", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["roblox verified"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["roblox verified"])

                if role in ctx.author.roles:
                    for i in chat_color_roles:
                        another_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles[i])
                        if another_role in ctx.author.roles:
                            await ctx.author.remove_roles(another_role)
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send(
                        "You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.findall("verified", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["verified"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["verified"])

                if role in ctx.author.roles:
                    for i in chat_color_roles:
                        another_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles[i])
                        if another_role in ctx.author.roles:
                            await ctx.author.remove_roles(another_role)
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send(
                        "You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.findall("devforum member", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["devforum member"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["devforum member"])

                if role in ctx.author.roles:
                    for i in chat_color_roles:
                        another_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles[i])
                        if another_role in ctx.author.roles:
                            await ctx.author.remove_roles(another_role)
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send(
                        "You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.findall("devforum regular", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["devforum regular"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["devforum regular"])

                if role in ctx.author.roles:
                    for i in chat_color_roles:
                        another_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles[i])
                        if another_role in ctx.author.roles:
                            await ctx.author.remove_roles(another_role)
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send(
                        "You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.findall("devforum top contributor", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["devforum top contributor"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["devforum top contributor"])

                if role in ctx.author.roles:
                    for i in chat_color_roles:
                        another_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles[i])
                        if another_role in ctx.author.roles:
                            await ctx.author.remove_roles(another_role)
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send(
                        "You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.findall("devforum community sage", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["devforum community sage"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["devforum community sage"])

                if role in ctx.author.roles:
                    for i in chat_color_roles:
                        another_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles[i])
                        if another_role in ctx.author.roles:
                            await ctx.author.remove_roles(another_role)
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send(
                        "You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.findall("game designer", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["game designer"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["game designer"])

                if role in ctx.author.roles:
                    for i in chat_color_roles:
                        another_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles[i])
                        if another_role in ctx.author.roles:
                            await ctx.author.remove_roles(another_role)
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send(
                        "You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.findall("Roblox Studio Builder", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["builder"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["builder"])

                if role in ctx.author.roles:
                    for i in chat_color_roles:
                        another_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles[i])
                        if another_role in ctx.author.roles:
                            await ctx.author.remove_roles(another_role)
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send(
                        "You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.findall("ui designer", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["UI Designer"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["UI Designer"])

                if role in ctx.author.roles:
                    for i in chat_color_roles:
                        another_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles[i])
                        if another_role in ctx.author.roles:
                            await ctx.author.remove_roles(another_role)
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send(
                        "You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.findall("gfx designer", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["gfx designer"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["gfx designer"])

                if role in ctx.author.roles:
                    for i in chat_color_roles:
                        another_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles[i])
                        if another_role in ctx.author.roles:
                            await ctx.author.remove_roles(another_role)
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send(
                        "You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.findall("music composer", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["music composer"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["music composer"])

                if role in ctx.author.roles:
                    for i in chat_color_roles:
                        another_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles[i])
                        if another_role in ctx.author.roles:
                            await ctx.author.remove_roles(another_role)
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send(
                        "You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.findall("3d modeler", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["3d modeler"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["3d modeler"])

                if role in ctx.author.roles:
                    for i in chat_color_roles:
                        another_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles[i])
                        if another_role in ctx.author.roles:
                            await ctx.author.remove_roles(another_role)
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send(
                        "You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.findall("clothing designer", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["Clothing Designer"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["Clothing Designer"])

                if role in ctx.author.roles:
                    for i in chat_color_roles:
                        another_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles[i])
                        if another_role in ctx.author.roles:
                            await ctx.author.remove_roles(another_role)
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send(
                        "You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.findall("youtuber", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["YouTuber"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["YouTuber"])

                if role in ctx.author.roles:
                    for i in chat_color_roles:
                        another_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles[i])
                        if another_role in ctx.author.roles:
                            await ctx.author.remove_roles(another_role)
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send(
                        "You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.findall("twitch streamer", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["twitch streamer"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["twitch streamer"])

                if role in ctx.author.roles:
                    for i in chat_color_roles:
                        another_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles[i])
                        if another_role in ctx.author.roles:
                            await ctx.author.remove_roles(another_role)
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send(
                        "You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.findall("animator", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["animator"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["animator"])

                if role in ctx.author.roles:
                    for i in chat_color_roles:
                        another_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles[i])
                        if another_role in ctx.author.roles:
                            await ctx.author.remove_roles(another_role)
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send(
                        "You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.findall("translator", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["Translator"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["Translator"])

                if role in ctx.author.roles:
                    for i in chat_color_roles:
                        another_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles[i])
                        if another_role in ctx.author.roles:
                            await ctx.author.remove_roles(another_role)
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send(
                        "You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.findall("server booster", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["server booster"])
                role2 = discord.utils.get(ctx.guild.roles, id=roles["first server booster"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["server booster"])

                if role in ctx.author.roles or role2 in ctx.author.roles:
                    for i in chat_color_roles:
                        another_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles[i])
                        if another_role in ctx.author.roles:
                            await ctx.author.remove_roles(another_role)
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send(
                        "You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.findall("programmer", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["c programmer"])
                role2 = discord.utils.get(ctx.guild.roles, id=roles["python programmer"])
                role3 = discord.utils.get(ctx.guild.roles, id=roles["css programmer"])
                role4 = discord.utils.get(ctx.guild.roles, id=roles["java programmer"])
                role5 = discord.utils.get(ctx.guild.roles, id=roles["js programmer"])
                role6 = discord.utils.get(ctx.guild.roles, id=roles["lua programmer"])
                role7 = discord.utils.get(ctx.guild.roles, id=roles["php programmer"])
                role8 = discord.utils.get(ctx.guild.roles, id=roles["ruby programmer"])
                role9 = discord.utils.get(ctx.guild.roles, id=roles["xml programmer"])
                role10 = discord.utils.get(ctx.guild.roles, id=roles["c# programmer"])
                role11 = discord.utils.get(ctx.guild.roles, id=roles["c++ programmer"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["former staff"])

                if role in ctx.author.roles or role2 in ctx.author.roles or role3 in ctx.author.roles or role4 in ctx.author.roles or role5 in ctx.author.roles or role6 in ctx.author.roles or role7 in ctx.author.roles or role8 in ctx.author.roles or role9 in ctx.author.roles or role10 in ctx.author.roles or role11 in ctx.author.roles:
                    for i in chat_color_roles:
                        another_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles[i])
                        if another_role in ctx.author.roles:
                            await ctx.author.remove_roles(another_role)
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send(
                        "You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            else:
                await ctx.send("Role doesn't exist, or isn't provided in the dictionary.")
        else:
            await ctx.send("Get some help!")

    @commands.command()
    async def boosters(self, ctx):
        bot_commands = self.bot.get_channel(712659793008918538)

        if ctx.channel != bot_commands:
            return
        else:
            pass

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


def setup(bot):
    bot.add_cog(Misc(bot))
