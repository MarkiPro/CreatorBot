import discord
from discord.ext import commands
import datetime
import asyncio
from paginator import Paginator
from cooldown import Cooldown
import mystbin
import json


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.formats_list = ["python", "lua", "c++", "csharp", "cpp", "cs", "css", "html", "json", "go", "js",
                             "javascript", "java", "py", "c"]
        self.bot.help_command.cog = self
        self.hiring_cool = Cooldown(time=datetime.datetime.utcfromtimestamp(0))
        self.for_hire_cool = Cooldown(time=datetime.datetime.utcfromtimestamp(0))
        self.sell_creations_cool = Cooldown(time=datetime.datetime.utcfromtimestamp(0))
        self.report_cool = Cooldown(time=datetime.datetime.utcfromtimestamp(0))
        self.cpp_programmer_cool = Cooldown(time=datetime.datetime.utcfromtimestamp(0))
        self.lua_programmer_cool = Cooldown(time=datetime.datetime.utcfromtimestamp(0))
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

    @commands.command(description="This command converts Roblox Currency (Robux) into USD.")
    async def convert(self, ctx, robux):
        robux_amount = int(robux)
        usd_amount = robux_amount * 0.0035

        usd_string = str(usd_amount)
        robux_string = str(robux_amount)

        times_of_iteration_for_usd = int(len(usd_string) / 3)
        times_of_iteration_for_robux = int(len(robux_string) / 3)

        if times_of_iteration_for_robux >= 1:
            for iteration in range(times_of_iteration_for_robux):
                robux_string = robux_string[:-int(3 * iteration)] + ", " + robux_string[-int(3 * iteration):]

        if times_of_iteration_for_usd >= 1:
            for iteration in range(times_of_iteration_for_usd):
                usd_string = usd_string[:-int(3 * iteration)] + ", " + usd_string[-int(3 * iteration):]

        return await ctx.channel.send(f"**{robux_string}** Robux is equivalent to **{usd_string}** USD.")

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

    @commands.command(description="This command is used for applying for applicable roles (STAFF ROLES NOT INCLUDED!).")
    async def apply(self, ctx):
        application_text = ""
        allowed_channels = [712659793008918538, 712624774479740931, 712624686399225907, 722898958996865035]
        applications_muted = ctx.guild.get_role(780494171730477086)

        if ctx.author in applications_muted.members:
            return await ctx.send(
                "You are restricted from using this command, you have the `Applications Muted` role. Please consult with a staff member about it.")
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
        pre_dm_embed = discord.Embed(
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
        await ctx.send(embed=pre_dm_embed)
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
            category = picked_category_message.content.lower()
        except asyncio.TimeoutError:
            cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
            await ctx.author.send(embed=cancel_prompt_embed)
            return
        if category.lower() == "cancel":
            cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
            await ctx.author.send(embed=cancel_prompt_embed)
            return
        else:
            with open("configs/apps.json", "r") as apps:
                apps = json.load(apps)
                if category == "programmer":
                    starter_embed = discord.Embed(
                        title="**APPLICATION SETUP**",
                        description=apps["programmer"]["Categories"],
                        color=0x0064ff,
                        timestamp=datetime.datetime.utcnow()
                    )
                    starter_embed.set_footer(text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                    await ctx.author.send(embed=starter_embed)
                    try:
                        category_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                        category = category_message.content
                    except asyncio.TimeoutError:
                        cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                        return await ctx.author.send(embed=cancel_prompt_embed)
                    if category.lower() == "cancel":
                        cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                        return await ctx.author.send(embed=cancel_prompt_embed)
                try:
                    category_json = apps[f"{category}"]
                except:
                    try:
                        category_json = apps["programmer"]["category"][f"{category}"]
                    except:
                        return await ctx.author.send("There is no such category!")

                cooldown_name = f"{category.replace(' ', '_')}_cool"
                if vars(self)[cooldown_name].cooldown_start_time != 0 and (datetime.datetime.utcnow() - vars(self)[cooldown_name].cooldown_start_time).total_seconds() < 3600:
                    print("cooldown")
                    await vars(self)[cooldown_name].time_it(user=ctx.author)
                    return

                questions = category_json["questions"]
                title = category_json["title"]

                channel_id = category_json["channel"]
                role_id = category_json["role"]

                channel = self.bot.get_channel(channel_id)
                role = ctx.guild.get_role(role_id)

                position = 1
                for question in questions:
                    new_embed = discord.Embed(
                        title=title,
                        description=f"{questions[question]}\n\nQuestion: {position}/{len(questions)}",
                        color=0x0064ff
                    )
                    new_embed.set_footer(
                        text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                    await ctx.author.send(embed=new_embed)
                    try:
                        details_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                        details = details_message.content
                    except asyncio.TimeoutError:
                        cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                        return await ctx.author.send(embed=cancel_prompt_embed)
                    if details.lower() == "cancel":
                        cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                        return await ctx.author.send(embed=cancel_prompt_embed)
                    if position == len(questions):
                        if details.lower() == "yes":
                            pag = Paginator(application_text, 1985)

                            await ctx.author.send("Your post has been sent for approval!")
                            await pag.send(bot=self.bot, channel=channel, member=ctx.author, title=title, role=role, mute_role=applications_muted)
                            vars(self)[cooldown_name] = Cooldown(time=datetime.datetime.utcnow())
                            return
                        else:
                            cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                            return await ctx.author.send(embed=cancel_prompt_embed)
                    application_text += f"**{question}:** {details}\n"
                    position += 1

    @commands.command(description="This command is used for posting.")
    async def post(self, ctx):
        post_text = ""
        allowed_channels = [712659793008918538, 712624774479740931, 712624686399225907, 722898958996865035]

        mute_role = ctx.guild.get_role(780494155075420262)

        if ctx.author in mute_role.members:
            return await ctx.send(
                "You are restricted from using this command, you have the `Post Muted` role. Please consult with a staff member about it.")
        else:
            pass
        if ctx.channel.id not in allowed_channels:
            return await ctx.send("Run the command again in <#712659793008918538>")
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
            category = picked_category_message.content.lower()
        except asyncio.TimeoutError:
            cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
            return await ctx.author.send(embed=cancel_prompt_embed)
        if category == "cancel":
            cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
            return await ctx.author.send(embed=cancel_prompt_embed)
        else:
            with open("configs/posts.json", "r") as posts:
                posts = json.load(posts)
                try:
                    category_json = posts[f"{category}"]
                except:
                    return await ctx.author.send("There is no such category!")

                cooldown_name = f"{category}_cool"
                if vars(self)[cooldown_name].cooldown_start_time != 0 and (datetime.datetime.utcnow() - vars(self)[cooldown_name].cooldown_start_time).total_seconds() < 3600:
                    print("cooldown")
                    await vars(self)[cooldown_name].time_it(user=ctx.author)
                    return

                questions = category_json["questions"]
                title = category_json["title"]

                channel_id = category_json["channel"]
                try:
                    final_channel_id = category_json["end_channel"]
                except:
                    pass

                channel = self.bot.get_channel(channel_id)
                try:
                    final_channel = self.bot.get_channel(final_channel_id)
                except:
                    pass

                position = 1
                for question in questions:
                    new_embed = discord.Embed(
                        title=title,
                        description=f"{questions[question]}\n\nQuestion: {position}/{len(questions)}",
                        color=0x0064ff
                    )
                    new_embed.set_footer(
                        text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                    await ctx.author.send(embed=new_embed)
                    try:
                        details_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                        details = details_message.content
                    except asyncio.TimeoutError:
                        cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                        return await ctx.author.send(embed=cancel_prompt_embed)
                    if details.lower() == "cancel":
                        cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                        return await ctx.author.send(embed=cancel_prompt_embed)
                    if position == len(questions):
                        if details.lower() == "yes":
                            pag = Paginator(post_text, 1985)

                            try:
                                await ctx.author.send("Your post has been sent for approval!")
                                await pag.send(bot=self.bot, channel=channel, end_channel=final_channel, member=ctx.author, title=title, mute_role=mute_role)
                            except:
                                await ctx.author.send("Your report has been sent!")
                                await pag.send(bot=self.bot, channel=channel, member=ctx.author, title=title, mute_role=mute_role)
                            vars(self)[cooldown_name] = Cooldown(time=datetime.datetime.utcnow())
                            return
                        else:
                            cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                            return await ctx.author.send(embed=cancel_prompt_embed)
                    post_text += f"**{question}:** {details}\n"
                    position += 1

    @commands.command(aliases=['code-format', "codeformat", "code format"],
                      description="This command is used for assisting you with formatting your code!")
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
                code_request_embed.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
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
                more_code_question_embed.set_footer(
                    text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
                await ctx.author.send(embed=more_code_question_embed)
                try:
                    more_code_answer_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
                    more_code_answer = more_code_answer_message.content
                except:
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                if more_code_answer.lower() == "cancel":
                    cancel_prompt_embed.timestamp = datetime.datetime.utcnow()
                    await ctx.author.send(embed=cancel_prompt_embed)
                    return
                elif more_code_answer == "no":
                    code_format_request_embed = discord.Embed(
                        title="**CODE FORMAT**",
                        description="Please tell us what format you want for your code! Examples: `python`, `lua`, `c`, `csharp`, `c++` and so on",
                        color=0x0064ff
                    )
                    code_format_request_embed.set_footer(
                        text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
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
                        formated_code = f"\`\`\`{code_format_answer}\n{code}\n\`\`\`"
                        await ctx.author.send(formated_code)
                        await ctx.author.send("Copy the message content above and paste it where you need to!")
                    except:
                        try:
                            mystbin_client = mystbin.Client()

                            paste = await mystbin_client.post(code, syntax=code_format_answer)

                            paste_url = paste.url

                            await ctx.author.send(
                                f"This is the link to your code! Copy and paste it where you need to!\n\n{paste_url}")
                        except:
                            await ctx.author.send("Something went wrong!")
                    break

        elif answer == "yes":
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
            code_format_request_embed.set_footer(
                text="Reply to this message within `16 minutes` • Reply with `cancel` to cancel.")
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
                formated_code = f"\`\`\`{code_format_answer}\n{code_answer}\n\`\`\`"
                await ctx.author.send(formated_code)
                await ctx.author.send("Copy the message content above and paste it where you need to!")
            except:
                try:
                    mystbin_client = mystbin.Client()

                    paste = await mystbin_client.post(code_answer, syntax=code_format_answer)

                    paste_url = paste.url

                    await ctx.author.send(
                        f"This is the link to your code! Copy and paste it where you need to!\n\n{paste_url}")
                except:
                    await ctx.author.send("Something went wrong!")

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
        excluded_roles = [611227128020598805, 707957214995808296, 732375953203789965, 743590325448212651,
                          743013370588037191, 732388199107657828, 743013368511594569, 743013366515236915,
                          743013366880272474, 743013367840768072, 743013368134107166, 732387788493946881,
                          732402691296198848, 734149969292034208, 734150445764837466, 734150696944795698,
                          735497751978311681, 734527020905529375, 734664303327838230, 734527130565738516,
                          735557139984285706, 738814580712669214, 734664243038912552, 734527217350082672,
                          734527854871707762, 746758563703291938]
        roles = ", ".join(role.mention for role in user.roles if role.id not in excluded_roles) or 'No roles assigned.'
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
        with open("configs/role.json", "r") as json_roles:
            roles = json_roles["roles"]
            chat_color_roles = json_roles["chat_color_roles"]

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
                await ctx.send(
                    "Role not listed or doesn't exist, please run `/tag chat color roles` to see which roles are listed.")

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
