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

    @commands.command(aliases=["for-hire", "forhire"], description="Toggle Not For Hire role off, and For Hire on, that way everyone knows you are for hire.")
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
            title="**POST SETUP**",
            description="***Please continue the setup in DMs.***",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
        )
        categories = discord.Embed(
            title="**APPLY SETUP**",
            description="""
            ***Which role would you like to apply for? Reply with the number in front of the role you would like to apply for.***


                **1** - `Programmer`;

                **2** - `Game Designer`;

                **3** - `3D Modeler`;

                **4** - `YouTuber`;
                
                **5** - `Roblox Studio Builder`;
                
                **6** - `Twitch Streamer`;
                
                **7** - `GFX Designer`;
                
                **8** - `Translator`;
                
                **9** - `UI Designer`;
                
                **10** - `Clothing Designer`;
                
                **11** - `Artist`;
                
                **12** - `Music Composer`;
                
                **13** - `Animator`;
                
            """,
            color=0x0064ff
        )
        categories.set_footer(text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
        await ctx.send(embed=pre_DM_embed)
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
            cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
            await ctx.author.send(embed=cancel_prompt_embed)
            return
        if category == "0":
            cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
            await ctx.author.send(embed=cancel_prompt_embed)
            return
        elif category == '1':
            programmer_categories = discord.Embed(
                title="**APPLY SETUP**",
                description="""
                Which Programmer role would you like to apply for? Reply with the number in front of the role you would like to apply for.
                
                **1** - `Python Programmer`;
                
                **2** - `C# Programmer`;
                
                **3** - `Java Programmer`;
                
                **4** - `JavaScript Programmer`;
                
                **5** - `C++ Programmer`;
                
                **6** - `C Programmer`;
                
                **7** - `Programmer`;
                
                **8** - `Programmer`;
                
                **9** - `Programmer`;
                
                **10** - `Programmer`;
                
                **11** - `Programmer`;"""
            )

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


                **1** - `hiring`;

                **2** - `for-hire`;

                **3** - `sell_creations`;

                **4** - `report`;

            """,
            color=0x0064ff
        )
        categories.set_footer(text="React to this message within `16 minutes` • Reply with `0` to cancel.")
        await ctx.send(embed=categories_embed)
        category_message = await ctx.author.send(embed=categories)
        await category_message.add_reaction("0\N{variation selector-16}\N{combining enclosing keycap}")
        await category_message.add_reaction("1\N{variation selector-16}\N{combining enclosing keycap}")
        await category_message.add_reaction("2\N{variation selector-16}\N{combining enclosing keycap}")
        await category_message.add_reaction("3\N{variation selector-16}\N{combining enclosing keycap}")
        await category_message.add_reaction("4\N{variation selector-16}\N{combining enclosing keycap}")

        def check_dm(m):
            if isinstance(m.channel, discord.DMChannel):
                if m.author == ctx.author:
                    return True
                else:
                    return False
            else:
                return False

        def check(reaction1, user1):
            return user1 and str(reaction1.emoji) in ["0\N{variation selector-16}\N{combining enclosing keycap}", "1\N{variation selector-16}\N{combining enclosing keycap}", "2\N{variation selector-16}\N{combining enclosing keycap}", "3\N{variation selector-16}\N{combining enclosing keycap}", "4\N{variation selector-16}\N{combining enclosing keycap}"]

        reaction1, user1 = await self.bot.wait_for("reaction_add", check=check)

        if str(user1) == str(self.bot.user):
            def check(reaction2, user2):
                return user1 and str(reaction1.emoji) in ["0\N{variation selector-16}\N{combining enclosing keycap}", "1\N{variation selector-16}\N{combining enclosing keycap}", "2\N{variation selector-16}\N{combining enclosing keycap}", "3\N{variation selector-16}\N{combining enclosing keycap}", "4\N{variation selector-16}\N{combining enclosing keycap}"]

            reaction2, user2 = await self.bot.wait_for("reaction_add", check=check)

            if str(reaction2.emoji) == "0\N{variation selector-16}\N{combining enclosing keycap}":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            elif str(reaction2.emoji) == "1\N{variation selector-16}\N{combining enclosing keycap}":
                hiring_embed1 = discord.Embed(
                    title="**HIRING POST**",
                    description="***Tell us more about the job, you may freely go into detail as much as you feel like is needed.***",
                    color=0x0064ff
                )
                hiring_embed1.set_footer(text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
                await ctx.author.send(embed=hiring_embed1)
                try:
                    hiring_details_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    hiring_details = hiring_details_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if hiring_details == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
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
                    hiring_payment_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    hiring_payment = hiring_payment_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if hiring_payment == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                hiring_embed3 = discord.Embed(
                    title="**HIRING POST**",
                    description="***Showcase some of your work here, could be a link to a portfolio. (ATTACHMENTS ARE CURRENTLY NOT SUPPORTED!)***",
                    color=0x0064ff
                )
                hiring_embed3.set_footer(text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
                await ctx.author.send(embed=hiring_embed3)
                try:
                    hiring_image_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    hiring_image = hiring_image_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if hiring_image == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
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
                    hiring_other_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    hiring_other = hiring_other_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if hiring_other == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                await ctx.author.send(
                    "Would you like to send this for Post Approval?\n Answer with: \n`1` - yes;\n`0` - no;")
                try:
                    final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    final_choice = final_choice_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if final_choice == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                elif final_choice == "1":
                    await ctx.author.send("Sent for approval!")
                    some_channel = self.bot.get_channel(739247560065024050)
                    end_channel = self.bot.get_channel(727550350097252482)
                    title = "**HIRING POST**"
                    pag = Paginator(
                        f"**About the job:** {hiring_details}\n**Payment:** {hiring_payment}\n**Showcase:** {hiring_image}\n**Other:** {hiring_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                        1985)

                    await pag.send(self.bot, some_channel, end_channel, ctx.author, title)
            elif str(reaction2.emoji) == "2\N{variation selector-16}\N{combining enclosing keycap}":
                for_hire_embed1 = discord.Embed(
                    title="**FOR-HIRE POST**",
                    description="***Define your specialties here, like for example a Java programmer, an Artist et cetera.***",
                    color=0x0064ff
                )
                for_hire_embed1.set_footer(text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
                await ctx.author.send(embed=for_hire_embed1)
                try:
                    for_hire_specialties_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    for_hire_specialties = for_hire_specialties_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if for_hire_specialties == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                for_hire_embed2 = discord.Embed(
                    title="**FOR-HIRE POST**",
                    description="***Showcase some of your previous work examples here, could be a link to a portfolio. (ATTACHMENTS ARE CURRENTLY NOT SUPPORTED!)***",
                    color=0x0064ff
                )
                for_hire_embed2.set_footer(text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
                await ctx.author.send(embed=for_hire_embed2)
                try:
                    for_hire_showcase_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    for_hire_showcase = for_hire_showcase_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if for_hire_showcase == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                for_hire_embed3 = discord.Embed(
                    title="**FOR-HIRE POST**",
                    description="***What is your desired payment for the job? Please define it here.***",
                    color=0x0064ff
                )
                for_hire_embed3.set_footer(text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
                await ctx.author.send(embed=for_hire_embed3)
                try:
                    for_hire_payment_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    for_hire_payment = for_hire_payment_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if for_hire_payment == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                for_hire_embed4 = discord.Embed(
                    title="**FOR-HIRE POST**",
                    description="***In case you have something else that you would like to add onto the previous statements, please provide it now.***",
                    color=0x0064ff
                )
                for_hire_embed4.set_footer(text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
                await ctx.author.send(embed=for_hire_embed4)
                try:
                    for_hire_other_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    for_hire_other = for_hire_other_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if for_hire_other == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                await ctx.author.send(
                    "Would you like to send this for Post Approval?\n Answer with: \n`1` - yes;\n`0` - no;")
                try:
                    final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    final_choice = final_choice_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if final_choice == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                elif final_choice == "1":
                    await ctx.author.send("Sent for approval!")
                    some_channel = self.bot.get_channel(739247630193786900)
                    end_channel = self.bot.get_channel(727550761801613393)
                    title = "**FOR-HIRE POST**"
                    pag = Paginator(
                        f"**Specialties:** {for_hire_specialties}\n**Showcase:** {for_hire_showcase}\n**Payment:** {for_hire_payment}\n**Other:** {for_hire_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                        1985)

                    await pag.send(self.bot, some_channel, end_channel, ctx.author, title)
            elif str(reaction2.emoji) == "3\N{variation selector-16}\N{combining enclosing keycap}":
                sell_creations_embed1 = discord.Embed(
                    title="**SELL-CREATIONS POST**",
                    description="***Showcase the creation here. (ATTACHMENTS ARE CURRENTLY NOT SUPPORTED!)***",
                    color=0x0064ff
                )
                sell_creations_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
                await ctx.author.send(embed=sell_creations_embed1)
                try:
                    sell_creations_showcase_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    sell_creations_showcase = sell_creations_showcase_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if sell_creations_showcase == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                sell_creations_embed2 = discord.Embed(
                    title="**SELL-CREATIONS POST**",
                    description="***What is your desired payment for your work? Please define it here.***",
                    color=0x0064ff
                )
                sell_creations_embed2.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
                await ctx.author.send(embed=sell_creations_embed2)
                try:
                    sell_creations_payment_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    sell_creations_payment = sell_creations_payment_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if sell_creations_payment == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                sell_creations_embed3 = discord.Embed(
                    title="**SELL-CREATIONS POST**",
                    description="***In case you have something else that you would like to add onto the previous statements, please provide it now.***",
                    color=0x0064ff
                )
                sell_creations_embed3.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
                await ctx.author.send(embed=sell_creations_embed3)
                try:
                    sell_creations_other_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    sell_creations_other = sell_creations_other_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if sell_creations_other == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                await ctx.author.send(
                    "Would you like to send this for Post Approval?\n Answer with: \n`1` - yes;\n`0` - no;")
                try:
                    final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    final_choice = final_choice_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if final_choice == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                elif final_choice == "1":
                    await ctx.author.send("Sent for approval!")
                    some_channel = self.bot.get_channel(739247602393940168)
                    end_channel = self.bot.get_channel(727550553806340197)
                    title = "**SELL-CREATIONS POST**"
                    pag = Paginator(
                        f"**Showcase:** {sell_creations_showcase}\n**Payment:** {sell_creations_payment}\n**Other:** {sell_creations_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                        1985)

                    await pag.send(self.bot, some_channel, end_channel, ctx.author, title)
            elif str(reaction2.emoji) == "4\N{variation selector-16}\N{combining enclosing keycap}":
                report_embed1 = discord.Embed(
                    title="**REPORT POST**",
                    description="***Who are you filing this report on? Please provide their Username and Discriminator/Tag. Example: Noob#1234 or MarkiPro#3753***",
                    color=0x0064ff
                )
                report_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
                await ctx.author.send(embed=report_embed1)
                try:
                    reported_user_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    reported_user = reported_user_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if reported_user == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                report_embed2 = discord.Embed(
                    title="**REPORT POST**",
                    description="***What did this person do?***",
                    color=0x0064ff
                )
                report_embed2.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
                await ctx.author.send(embed=report_embed2)
                try:
                    report_reason_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    report_reason = report_reason_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if report_reason == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                report_embed3 = discord.Embed(
                    title="**REPORT POST**",
                    description="***Do you have any evidence? If so, provide it here (ATTACHMENTS ARE NOT SUPPORTED!)***",
                    color=0x0064ff
                )
                report_embed3.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
                await ctx.author.send(embed=report_embed3)
                try:
                    report_evidence_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    report_evidence = report_evidence_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if report_evidence == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                report_embed4 = discord.Embed(
                    title="**REPORT POST**",
                    description="***In case you have something else you wanted to add onto your current statement, please do.***",
                    color=0x0064ff
                )
                report_embed4.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
                await ctx.author.send(embed=report_embed4)
                try:
                    report_other_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    report_other = report_other_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if report_other == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                await ctx.author.send(
                    "Would you like to send this for Post Approval?\n Answer with: \n`1` - yes;\n`0` - no;")
                try:
                    final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    final_choice = final_choice_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if final_choice == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                elif final_choice == "1":
                    await ctx.author.send("Sent!")
                    some_channel = self.bot.get_channel(773637163048239124)
                    title = "**REPORT POST**"
                    pag = Paginator(
                        f"**Subject Information:** {reported_user}\n**Report Reason:** {report_reason}\n**Evidence:** {report_evidence}\n**Other:** {report_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                        1985)

                    await pag.send(bot=self.bot, channel=some_channel, member=ctx.author, title=title)
        else:
            if str(reaction1.emoji) == "0\N{variation selector-16}\N{combining enclosing keycap}":
                cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                await ctx.author.send(embed=cancel_prompt_embed)
                return
            elif str(reaction1.emoji) == "1\N{variation selector-16}\N{combining enclosing keycap}":
                hiring_embed1 = discord.Embed(
                    title="**HIRING POST**",
                    description="***Tell us more about the job, you may freely go into detail as much as you feel like is needed.***",
                    color=0x0064ff
                )
                hiring_embed1.set_footer(text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
                await ctx.author.send(embed=hiring_embed1)
                try:
                    hiring_details_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    hiring_details = hiring_details_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if hiring_details == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
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
                    hiring_payment_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    hiring_payment = hiring_payment_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if hiring_payment == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                hiring_embed3 = discord.Embed(
                    title="**HIRING POST**",
                    description="***Showcase some of your work here, could be a link to a portfolio. (ATTACHMENTS ARE CURRENTLY NOT SUPPORTED!)***",
                    color=0x0064ff
                )
                hiring_embed3.set_footer(text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
                await ctx.author.send(embed=hiring_embed3)
                try:
                    hiring_image_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    hiring_image = hiring_image_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if hiring_image == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
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
                    hiring_other_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    hiring_other = hiring_other_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if hiring_other == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                await ctx.author.send(
                    "Would you like to send this for Post Approval?\n Answer with: \n`1` - yes;\n`0` - no;")
                try:
                    final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    final_choice = final_choice_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if final_choice == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                elif final_choice == "1":
                    await ctx.author.send("Sent for approval!")
                    some_channel = self.bot.get_channel(739247560065024050)
                    end_channel = self.bot.get_channel(727550350097252482)
                    title = "**HIRING POST**"
                    pag = Paginator(
                        f"**About the job:** {hiring_details}\n**Payment:** {hiring_payment}\n**Showcase:** {hiring_image}\n**Other:** {hiring_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                        1985)

                    await pag.send(self.bot, some_channel, end_channel, ctx.author, title)
            elif str(reaction1.emoji) == "2\N{variation selector-16}\N{combining enclosing keycap}":
                for_hire_embed1 = discord.Embed(
                    title="**FOR-HIRE POST**",
                    description="***Define your specialties here, like for example a Java programmer, an Artist et cetera.***",
                    color=0x0064ff
                )
                for_hire_embed1.set_footer(text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
                await ctx.author.send(embed=for_hire_embed1)
                try:
                    for_hire_specialties_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    for_hire_specialties = for_hire_specialties_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if for_hire_specialties == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                for_hire_embed2 = discord.Embed(
                    title="**FOR-HIRE POST**",
                    description="***Showcase some of your previous work examples here, could be a link to a portfolio. (ATTACHMENTS ARE CURRENTLY NOT SUPPORTED!)***",
                    color=0x0064ff
                )
                for_hire_embed2.set_footer(text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
                await ctx.author.send(embed=for_hire_embed2)
                try:
                    for_hire_showcase_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    for_hire_showcase = for_hire_showcase_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if for_hire_showcase == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                for_hire_embed3 = discord.Embed(
                    title="**FOR-HIRE POST**",
                    description="***What is your desired payment for the job? Please define it here.***",
                    color=0x0064ff
                )
                for_hire_embed3.set_footer(text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
                await ctx.author.send(embed=for_hire_embed3)
                try:
                    for_hire_payment_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    for_hire_payment = for_hire_payment_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if for_hire_payment == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                for_hire_embed4 = discord.Embed(
                    title="**FOR-HIRE POST**",
                    description="***In case you have something else that you would like to add onto the previous statements, please provide it now.***",
                    color=0x0064ff
                )
                for_hire_embed4.set_footer(text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
                await ctx.author.send(embed=for_hire_embed4)
                try:
                    for_hire_other_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    for_hire_other = for_hire_other_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if for_hire_other == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                await ctx.author.send(
                    "Would you like to send this for Post Approval?\n Answer with: \n`1` - yes;\n`0` - no;")
                try:
                    final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    final_choice = final_choice_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if final_choice == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                elif final_choice == "1":
                    await ctx.author.send("Sent for approval!")
                    some_channel = self.bot.get_channel(739247630193786900)
                    end_channel = self.bot.get_channel(727550761801613393)
                    title = "**FOR-HIRE POST**"
                    pag = Paginator(
                        f"**Specialties:** {for_hire_specialties}\n**Showcase:** {for_hire_showcase}\n**Payment:** {for_hire_payment}\n**Other:** {for_hire_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                        1985)

                    await pag.send(self.bot, some_channel, end_channel, ctx.author, title)
            elif str(reaction1.emoji) == "3\N{variation selector-16}\N{combining enclosing keycap}":
                sell_creations_embed1 = discord.Embed(
                    title="**SELL-CREATIONS POST**",
                    description="***Showcase some of your previous work examples here, could be a link portfolio. (ATTACHMENTS ARE CURRENTLY NOT SUPPORTED!)***",
                    color=0x0064ff
                )
                sell_creations_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
                await ctx.author.send(embed=sell_creations_embed1)
                try:
                    sell_creations_showcase_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    sell_creations_showcase = sell_creations_showcase_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if sell_creations_showcase == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                sell_creations_embed2 = discord.Embed(
                    title="**SELL-CREATIONS POST**",
                    description="***What is your desired payment for your work? Please define it here.***",
                    color=0x0064ff
                )
                sell_creations_embed2.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
                await ctx.author.send(embed=sell_creations_embed2)
                try:
                    sell_creations_payment_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    sell_creations_payment = sell_creations_payment_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if sell_creations_payment == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                sell_creations_embed3 = discord.Embed(
                    title="**SELL-CREATIONS POST**",
                    description="***In case you have something else that you would like to add onto the previous statements, please provide it now.***",
                    color=0x0064ff
                )
                sell_creations_embed3.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
                await ctx.author.send(embed=sell_creations_embed3)
                try:
                    sell_creations_other_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    sell_creations_other = sell_creations_other_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if sell_creations_other == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                await ctx.author.send(
                    "Would you like to send this for Post Approval?\n Answer with: \n`1` - yes;\n`0` - no;")
                try:
                    final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    final_choice = final_choice_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if final_choice == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                elif final_choice == "1":
                    await ctx.author.send("Sent for approval!")
                    some_channel = self.bot.get_channel(739247602393940168)
                    end_channel = self.bot.get_channel(727550553806340197)
                    title = "**SELL-CREATIONS POST**"
                    pag = Paginator(
                        f"**Showcase:** {sell_creations_showcase}\n**Payment:** {sell_creations_payment}\n**Other:** {sell_creations_other}\n**Contact:** {ctx.author.mention}({ctx.author})",
                        1985)

                    await pag.send(self.bot, some_channel, end_channel, ctx.author, title)
            elif str(reaction1.emoji) == "4\N{variation selector-16}\N{combining enclosing keycap}":
                report_embed1 = discord.Embed(
                    title="**REPORT POST**",
                    description="***Who are you filing this report on? Please provide their Username and Discriminator/Tag. Example: Noob#1234 or MarkiPro#3753***",
                    color=0x0064ff
                )
                report_embed1.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
                await ctx.author.send(embed=report_embed1)
                try:
                    reported_user_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    reported_user = reported_user_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if reported_user == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                report_embed2 = discord.Embed(
                    title="**REPORT POST**",
                    description="***What did this person do?***",
                    color=0x0064ff
                )
                report_embed2.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
                await ctx.author.send(embed=report_embed2)
                try:
                    report_reason_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    report_reason = report_reason_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if report_reason == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                report_embed3 = discord.Embed(
                    title="**REPORT POST**",
                    description="***Do you have any evidence? If so, provide it here (ATTACHMENTS ARE NOT SUPPORTED!)***",
                    color=0x0064ff
                )
                report_embed3.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
                await ctx.author.send(embed=report_embed3)
                try:
                    report_evidence_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    report_evidence = report_evidence_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if report_evidence == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                report_embed4 = discord.Embed(
                    title="**REPORT POST**",
                    description="***In case you have something else you wanted to add onto your current statement, please do.***",
                    color=0x0064ff
                )
                report_embed4.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `0` to cancel.")
                await ctx.author.send(embed=report_embed4)
                try:
                    report_other_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    report_other = report_other_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if report_other == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                await ctx.author.send(
                    "Would you like to send this for Post Approval?\n Answer with: \n`1` - yes;\n`0` - no;")
                try:
                    final_choice_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    final_choice = final_choice_message.content
                except asyncio.TimeoutError:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if final_choice == "0":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                elif final_choice == "1":
                    await ctx.author.send("Sent!")
                    some_channel = self.bot.get_channel(773637163048239124)
                    title = "**REPORT POST**"
                    pag = Paginator(f"**Subject Information:** {reported_user}\n**Report Reason:** {report_reason}\n**Evidence:** {report_evidence}\n**Other:** {report_other}\n**Contact:** {ctx.author.mention}({ctx.author})",1985)

                    await pag.send(bot=self.bot, channel=some_channel, member=ctx.author, title=title)

    @commands.command(aliases=["server-info", "si", "s-i", "guild-info", "guildinfo", "gi", "g-i", "server_info", "s_i", "guild_info", "g_i"], description="Displays basic information about the server.")
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
        embed.add_field(name="Member Count", value=f"Total: {guild.member_count}\n Humans: {human_member_count}\n Boosters: {boosters_amount}\nBots: {bots_amount}", inline=True)
        embed.add_field(name="Boost Level", value=f"{guild.premium_tier}")
        embed.add_field(name="Roles Amount", value=f"{roles_amount}", inline=True)
        embed.add_field(name="Categories Amount", value=f"{categoires_amount}")
        embed.add_field(name="Channels Amount", value=f"Text Channels: {text_channels_amount}\n Voice Channels: {voice_channels_amount}")
        embed.add_field(name="Server Region", value=f"{guild.region}", inline=True)
        embed.add_field(name="Verification Level", value=f"{guild.verification_level}", inline=True)
        if guild.banner:
            embed.set_image(url=guild.banner_url)
        embed.set_thumbnail(url=guild.icon_url)

        await ctx.send(embed=embed)

    @commands.command(aliases=["who", "user-info", "userinfo", "ui", "u-i", "who-is", "who_is", "profile"], description="Displays basic information about the supplied user. If the user is not provided, it would default to the command requester.")
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
        embed.add_field(name="Joined on", value=f"{user.joined_at.strftime(format)} ({delta_joined.days} days)", inline=True)
        embed.add_field(name="Status",
                        value=f"Desktop Status: {user.desktop_status}\nMobile Status: {user.mobile_status}\n Web Status: {user.web_status}")
        embed.add_field(name="Account created on", value=f"{user.created_at.strftime(format)} ({delta_created.days} days)", inline=True)
        embed.add_field(name="Nickname", value=f"{user.nick}", inline=True)
        embed.add_field(name="Join Position", value=f"#{join_pos}", inline=True)
        exculded_roles = [611227128020598805, 707957214995808296, 732375953203789965, 743590325448212651, 743013370588037191, 732388199107657828, 743013368511594569, 743013366515236915, 743013366880272474, 743013367840768072, 743013368134107166, 732387788493946881, 732402691296198848, 734149969292034208, 734150445764837466, 734150696944795698, 735497751978311681, 734527020905529375, 734664303327838230, 734527130565738516, 735557139984285706, 738814580712669214, 734664243038912552, 734527217350082672, 734527854871707762, 746758563703291938]
        roles = ", ".join(role.mention for role in user.roles if role.id not in exculded_roles) or 'No roles assigned.'
        embed.add_field(name="Guild Roles", value=f"{roles}", inline=False)
        notable_perms = ['administrator', 'manage_guild', 'view_audit_log', 'manage_roles', 'manage_channels', 'ban_members', 'kick_members', 'manage_messages', 'mention_everyone', 'manage_emojis', 'manage_webhooks', 'manage_nicknames', 'mute_members', 'deafen_members', 'move_members', 'priority_speaker']
        member_permissions = ", ".join(f"{i.title().replace('_', ' ')}" for i in notable_perms if getattr(user.permissions_in(ctx.channel), i, False)) or "No Permissions."
        embed.add_field(name="Guild Permissions", value=f"{member_permissions}", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def role(self, ctx, role_name=None):
        roles = {"former staff": 741728478721736755, "roblox verified": 741735258411499560, "verified": 695328817157373992, "devforum member": 742333164352962581, "devforum regular": 742333167133786124, "devforum top contributor": 742333168576888943, "devforum community champion": 742333169423876106, "first server booster": 712685506424471612, "server booster": 762172204628181023, "animator": 734662028353994752, "music composer": 735497558855516161, "Artist": 734662196025360416, "Clothing Designer": 734177621876801637, "UI Designer": 733274530524561430, "Translator": 734527264657637416, "gfx designer": 733280979921141821, "twitch streamer": 738814393663619182, "builder": 733281281671954442, "YouTuber": 738788543211634756, "3d modeler": 733281157872877629, "game designer": 733281086913773599, "css programmer": 741099963626422322, "xml programmer": 735147383716970507, "ruby programmer": 735147661430227025, "lua programmer": 732376072397783093, "php programmer": 732378321387520092, "c programmer": 732378157449216040, "c++ programmer": 732377777772167188, "js programmer": 732377955669508097, "java programmer": 732379273100263464, "c# programmer": 732377857317142650, "python programmer": 732377712286761001}
        chat_color_roles = {"former staff": 743013368511594569, "roblox verified": 743013370588037191, "verified": 732388199107657828, "devforum member": 743013366515236915, "devforum regular": 743013366880272474, "devforum top contributor": 743013367840768072, "devforum community champion": 743013368134107166, "server booster": 734527854871707762, "animator": 734664243038912552, "music composer": 735497751978311681, "Artist": 734664303327838230, "Clothing Designer": 734527130565738516, "UI Designer": 734150445764837466, "Translator": 734527217350082672, "gfx designer": 734150696944795698, "twitch streamer": 738814580712669214, "builder": 734149969292034208, "YouTuber": 735557139984285706, "3d modeler": 734527020905529375, "game designer": 732402691296198848, "programmer": 732387788493946881}

        if role_name:
            if re.match("former staff", ctx.message.content, re.IGNORECASE):
                await ctx.send("started")
                role = discord.utils.get(ctx.guild.roles, id=roles["former staff"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["former staff"])


                if role in ctx.author.roles:
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send("You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.match("roblox verified", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["roblox verified"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["roblox verified"])
                await ctx.send("started")

                if role in ctx.author.roles:
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send("You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.match("verified", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["verified"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["verified"])
                await ctx.send("started")

                if role in ctx.author.roles:
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send("You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.match("devforum member", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["devforum member"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["devforum member"])
                await ctx.send("started")

                if role in ctx.author.roles:
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send("You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.match("devforum regular", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["devforum regular"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["devforum regular"])
                await ctx.send("started")

                if role in ctx.author.roles:
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send("You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.match("devforum top contributor", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["devforum top contributor"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["devforum top contributor"])
                await ctx.send("started")

                if role in ctx.author.roles:
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send("You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.match("devforum community champion", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["devforum community champion"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["devforum community champion"])
                await ctx.send("started")

                if role in ctx.author.roles:
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send("You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.match("game designer", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["game designer"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["game designer"])
                await ctx.send("started")

                if role in ctx.author.roles:
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send("You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.match("Roblox Studio Builder", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["builder"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["builder"])
                await ctx.send("started")

                if role in ctx.author.roles:
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send("You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.match("ui designer", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["UI Designer"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["UI Designer"])
                await ctx.send("started")

                if role in ctx.author.roles:
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send("You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.match("gfx designer", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["gfx designer"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["gfx designer"])
                await ctx.send("started")

                if role in ctx.author.roles:
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send("You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.match("music composer", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["music composer"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["music composer"])
                await ctx.send("started")

                if role in ctx.author.roles:
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send("You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.match("3d modeler", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["3d modeler"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["3d modeler"])
                await ctx.send("started")

                if role in ctx.author.roles:
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send("You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.match("clothing designer", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["Clothing Designer"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["Clothing Designer"])
                await ctx.send("started")

                if role in ctx.author.roles:
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send("You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.match("youtuber", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["YouTuber"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["YouTuber"])
                await ctx.send("started")

                if role in ctx.author.roles:
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send("You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.match("twitch streamer", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["twitch streamer"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["twitch streamer"])
                await ctx.send("started")

                if role in ctx.author.roles:
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send("You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.match("animator", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["animator"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["animator"])
                await ctx.send("started")

                if role in ctx.author.roles:
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send("You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.match("translator", ctx.message.content, re.IGNORECASE):
                await ctx.send("started")
                role = discord.utils.get(ctx.guild.roles, id=roles["Translator"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["Translator"])


                if role in ctx.author.roles:
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send("You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.match("server booster", ctx.message.content, re.IGNORECASE):
                role = discord.utils.get(ctx.guild.roles, id=roles["server booster"])
                role2 = discord.utils.get(ctx.guild.roles, id=roles["first server booster"])
                chat_color_role = discord.utils.get(ctx.guild.roles, id=chat_color_roles["server booster"])
                await ctx.send("started")

                if role in ctx.author.roles or role2 in ctx.author.roles:
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send("You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
            elif re.match("programmer", ctx.message.content, re.IGNORECASE):
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
                await ctx.send("started")

                if role in ctx.author.roles or role2 in ctx.author.roles or role3 in ctx.author.roles or role4 in ctx.author.roles or role5 in ctx.author.roles or role6 in ctx.author.roles or role7 in ctx.author.roles or role8 in ctx.author.roles or role9 in ctx.author.roles or role10 in ctx.author.roles or role11 in ctx.author.roles:
                    await ctx.author.add_roles(chat_color_role)
                    await ctx.send("Added the chat color role!")
                    return
                else:
                    await ctx.send("You do not have the required role, please contact a staff member to assist you, or apply for the desired role using the `>apply` command.")
                    return
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

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Misc(bot))
