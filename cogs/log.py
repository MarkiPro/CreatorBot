import datetime
import re
from discord.ext import tasks
import discord
from discord.ext.commands import Cog
from paginator import Paginator
import asyncio


class Log(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.muteable_offence = 0
        self.kickable_offence = 0
        self.invite_muteable_offence = 0
        self.invite_kickable_offence = 0

    @Cog.listener()
    async def on_guild_channel_update(self, before, after):
        server_management_logs_channel = self.bot.get_channel(771465807276277810)
        channel = before
        cc_guild = self.bot.get_guild(id=611227128020598805)

        if before and after:
            if before.guild != cc_guild or after.guild != cc_guild:
                return
            else:
                pass
        else:
            pass
        if before.position != after.position:
            return
        if before.permissions != after.permissions:
            log_embed = discord.Embed(
                title="**Role Updated**",
                description=f"***{channel.mention}`({channel.name})`** was just updated!*",
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )

            log_embed.add_field(name="**Before**", value=f"{before}", inline=True)
            log_embed.add_field(name="**After**", value=f"{after}", inline=True)

            await server_management_logs_channel.send(embed=log_embed)

    @Cog.listener()
    async def on_guild_channel_delete(self, channel):
        server_management_logs_channel = self.bot.get_channel(771465807276277810)
        cc_guild = self.bot.get_guild(id=611227128020598805)

        if channel.guild != cc_guild:
            return
        else:
            pass
        log_embed = discord.Embed(
            title="**Role Deletion**",
            description=f"***`{channel.name}`** was just deleted!*",
            timestamp=datetime.datetime.utcnow(),
            color=0x0064ff
        )

        await server_management_logs_channel.send(embed=log_embed)

    @Cog.listener()
    async def on_guild_channel_create(self, channel):
        server_management_logs_channel = self.bot.get_channel(771465807276277810)
        cc_guild = self.bot.get_guild(id=611227128020598805)

        if channel.guild != cc_guild:
            return
        else:
            pass
        log_embed = discord.Embed(
            title="**Channel Creation**",
            description=f"***{channel.mention}`({channel.name})`** was just created!*",
            timestamp=datetime.datetime.utcnow(),
            color=0x0064ff
        )

        await server_management_logs_channel.send(embed=log_embed)

    @Cog.listener()
    async def on_guild_role_create(self, role):
        server_management_logs_channel = self.bot.get_channel(771465807276277810)
        cc_guild = self.bot.get_guild(id=611227128020598805)

        if role.guild != cc_guild:
            return
        else:
            pass
        log_embed = discord.Embed(
            title="**Role Creation**",
            description=f"***{role.mention}`({role.name})`** was just created!*",
            timestamp=datetime.datetime.utcnow(),
            color=0x0064ff
        )

        await server_management_logs_channel.send(embed=log_embed)

    @Cog.listener()
    async def on_guild_role_update(self, before, after):
        server_management_logs_channel = self.bot.get_channel(771465807276277810)
        role = before
        cc_guild = self.bot.get_guild(id=611227128020598805)

        if before and after:
            if before.guild != cc_guild and after.guild != cc_guild:
                print("returned!")
                return
            else:
                pass
        else:
            pass
        if before.position != after.position:
            return
        if before.permissions != after.permissions:
            log_embed = discord.Embed(
                title="**Role Updated**",
                description=f"***{role.mention}`({role.name})`** was just updated!*",
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )

            log_embed.add_field(name="**Before**", value=f"{before}", inline=True)
            log_embed.add_field(name="**After**", value=f"{after}", inline=True)

            await server_management_logs_channel.send(embed=log_embed)

    @Cog.listener()
    async def on_reaction_add(self, reaction, user):
        staff_role = discord.utils.get(reaction.message.guild.roles, id=756565123350659385)
        message = reaction.message
        suggestions_channel = self.bot.get_channel(712655570737299567)
        top_suggestions_channel = self.bot.get_channel(771822991256059905)
        reactions = message.reactions

        if str(user) == str(self.bot.user):
            return

        if not message.author.bot:
            if len(reactions) >= 1:
                reaction1 = reactions[0]
                if reaction1 and message.channel == suggestions_channel and reaction == reaction1:
                    if user in staff_role.members:
                        pass
                    else:
                        await user.send("This is staff-only!")
                        await reaction.remove(user)
                        return
                    await message.delete()

        if len(reactions) >= 2:
            reaction1 = reactions[0]
            reaction2 = reactions[1]

            if reaction == reaction1 and message.channel == suggestions_channel:
                async for some_user in reaction2.users():
                    if some_user.id == user.id:
                        await reaction.remove(user)
                        await user.send(
                            "You've already disliked this suggestion, if you wanna change your vote, you have to remove your previous reaction.")
                        return
                if reaction1.count > reaction2.count and reaction1.count >= 10:
                    suggest_embed = discord.Embed(
                        title="**Top Suggestion**",
                        description=f"**[Message link]({message.jump_url})**",
                        timestamp=datetime.datetime.utcnow(),
                        color=0x0064ff
                    )

                    await top_suggestions_channel.send(embed=suggest_embed)

            elif reaction == reaction2 and message.channel == suggestions_channel:
                async for some_user in reaction1.users():
                    if some_user.id == user.id:
                        await reaction.remove(user)
                        await user.send(
                            "You've already liked this suggestion, if you wanna change your vote, you have to remove your previous reaction.")
                        return
                if reaction2.count > reaction1.count and reaction2.count >= 10:
                    await message.delete()
        else:
            return

        if len(reactions) >= 3:
            reaction1 = reactions[2]

            if reaction == reaction1 and message.channel == suggestions_channel:
                if user in staff_role.members and user is not self.bot.user:
                    pass
                else:
                    await user.send("This is staff-only!")
                    await reaction.remove(user)
                    return
                await message.delete()
        else:
            return

    @tasks.loop(seconds=600)
    async def clear_muteable_offences(self):
        if self.muteable_offence > 0:
            self.muteable_offence = 0
        if self.invite_muteable_offence > 0:
            self.invite_muteable_offence = 0

    @tasks.loop(seconds=2000)
    async def clear_kickable_offences(self):
        if self.kickable_offence > 0:
            self.kickable_offence = 0
        if self.invite_kickable_offence > 0:
            self.invite_kickable_offence = 0

    @Cog.listener()
    async def on_message(self, message):
        suggestions_channel = self.bot.get_channel(712655570737299567)
        banned_racial_words = ["nigger", "nig", "nigor", "nigra", "nigre", "nigar", "niggur", "nigga", "niggah",
                               "niggar", "nigguh", "niggress", "nigette", "negro", "nibba", "niba", "n1gger", "n1ger",
                               "n1g", "n1gor", "n1gra", "n1gre", "n1gar", "n1ggur", "n1gga", "n1ggah", "n1ggar",
                               "n1gguh", "n1ggress", "n1gette", "negro", "n1bba", "n1ba"]
        banned_links = ["https://pornhub.com", "https://porn.com", "https://fuq.com", "https://brazzers.com"]
        log_channel = self.bot.get_channel(712761128895381676)
        cc_guild = self.bot.get_guild(id=611227128020598805)
        staff_role = discord.utils.get(cc_guild.roles, id=756565123350659385)
        banned_words = ["porn", "fuck", "dick", "pussy", "bitch", "bollocks", "cunt", "bugger",
                        "cock", "blowjob", "choad", "twat", "shag", "wanker", "bint", "balls", "tit", "boob", "sex",
                        "seggz", "segz", "cnut", "fcuk", "penis", "fück", "cünt", "fúck", "cúnt", "fùck", "cùnt",
                        "fŭck", "cŭnt", "fûck", "cûnt", "fǔck", "cǔnt", "fůck", "cůnt", "fǘck", "cǘnt", "fǜck", "cǜnt",
                        "fǚck", "cǚnt", "fǖck", "cǖnt", "fűck", "cűnt", "fũck", "cũnt", "fṹck", "cṹnt", "fųck", "cųnt",
                        "fų́ck", "cų́nt", "fų̃ck", "cų̃nt", "fūck", "cūnt", "fṻck", "cṻnt", "fū̀ck", "cū̀nt", "fū́ck",
                        "cū́nt", "fū̃ck", "cū̃nt", "fủck", "củnt", "fȕck", "cȕnt", "fȗck", "cȗnt", "fưck", "cưnt",
                        "fứck", "cứnt", "fừck", "cừnt", "fữck", "cữnt", "fửck", "cửnt", "fựck", "cựnt", "fụck", "cụnt",
                        "fṳck", "cṳnt", "fṷck", "cṷnt", "fṵck", "cṵnt", "fʉck", "cʉnt", "fᶙck", "cᶙnt", "fꭒck", "cꭒnt",
                        "fcük", "cnüt", "fcúk", "cnút", "fcùk", "cnùt", "fcŭk", "cnŭt", "fcûk", "cnût", "fcǔk", "cnǔt",
                        "fcůk", "cnůt", "fcǘk", "cnǘt", "fcǜk", "cnǜt", "fcǚk", "cnǚt", "fcǖk", "cnǖt", "fcűk", "cnűt",
                        "fcũk", "cnũt", "fcṹk", "cnṹt", "fcųk", "cnųt", "fcų́k", "cnų́t", "fcų̃k", "cnų̃t", "fcūk",
                        "cnūt", "fcṻk", "cnṻt", "fcū̀k", "cnū̀t", "fcū́k", "cnū́t", "fcū̃k", "cnū̃t", "fcủk", "cnủt",
                        "fcȕk", "cnȕt", "fcȗk", "cnȗt", "fcưk", "cnưt", "fcứk", "cnứt", "fcừk", "cnừt", "fcữk", "cnữt",
                        "fcửk", "cnửt", "fcựk", "cnựt", "fcụk", "cnụt", "fcṳk", "cnṳt", "fcṷk", "cnṷt", "fcṵk", "cnṵt",
                        "fcʉk", "cnʉt", "fcᶙk", "cnᶙt", "fcꭒk", "cnꭒt"]
        mute_role = discord.utils.get(cc_guild.roles, id=712730274412232807)

        if message.author in staff_role.members:
            return
        else:
            pass
        if any(re.findall("|".join(banned_links), message.content, re.IGNORECASE)):
            await message.delete()
            ban_embed = discord.Embed(
                title="**NOTIFICATION**",
                description=f":bell: *You have been banned in **{message.guild}** because you've sent an inappropriate link!*",
                color=0x0064ff,
                timestamp=datetime.datetime.utcnow()
            )
            ban_embed.add_field(name="**In case you would like to appeal your ban, go here:**",
                                value=f"https://forms.gle/zs9vRAz5Fw1SFgvR6", inline=False)
            try:
                await message.author.send(embed=ban_embed)
            except:
                pass
            try:
                await message.author.ban(reason="Sent something inappropriate!")
            except:
                return
        elif any(re.findall("|".join(banned_racial_words), message.content, re.IGNORECASE)):
            ban_embed = discord.Embed(
                title="**Member Banned**",
                description=f"***{message.author}** has been banned for sending a racial slur/banned word!*",
                color=0x0064ff,
                timestamp=datetime.datetime.utcnow()
            )
            ban_embed.add_field(name="**In case you would like to appeal your ban, go here:**",
                                value=f"https://forms.gle/zs9vRAz5Fw1SFgvR6", inline=False)
            try:
                ban_embed.set_thumbnail(url=message.author.avatar_url)
            except:
                pass
            await log_channel.send(embed=ban_embed)
        elif re.findall("https://web.roblox.com", message.content, re.IGNORECASE):
            ban_embed = discord.Embed(
                title="**Member Banned**",
                description=f"***{message.author}** has been banned for sending an underage version of a roblox link!*",
                color=0x0064ff,
                timestamp=datetime.datetime.utcnow()
            )
            ban_embed.add_field(name="**In case you would like to appeal your ban, go here:**",
                                value=f"https://forms.gle/zs9vRAz5Fw1SFgvR6", inline=False)
            try:
                ban_embed.set_thumbnail(url=message.author.avatar_url)
            except:
                pass
            await log_channel.send(embed=ban_embed)
        elif any(re.findall("|".join(banned_words), message.content, re.IGNORECASE)):
            banned_word = re.findall("|".join(banned_words), message.content, re.IGNORECASE)
            matches = re.findall("`|```", message.content)
            if len(matches) >= 0:
                pre_message_content = message.content.replace("```", "")
                message_content = pre_message_content.replace("`", "")
            else:
                pass
            new_message_content = message_content or message.content
            await message.author.send(
                "Greetings! I've detected a banned word in your message, right now, it is up to our wonderful staff members to decide whether or not this is well-deserved of a punishment.")
            await message.author.send(
                f"The word(s) in particular is/are **`{banned_word}`**, in the following message content:\n\n ```{new_message_content}```")
            auto_reports = cc_guild.get_channel(786007666329124874)
            pag = Paginator(f"Word(s) **`{banned_word}`** found in:\n\n```{new_message_content}```", 1985)
            await pag.send(bot=self.bot, channel=auto_reports, member=message.author, end_channel=message.author,
                           another_channel=log_channel, title="**AUTO-REPORTED MESSAGE**", autoreport=True,
                           messagee=message)
        if message.channel == suggestions_channel:
            if message.content.startswith("//"):
                await message.add_reaction("🚫")
                return
            else:
                suggestion_embed = discord.Embed(
                    title="**Suggestion**",
                    description=f"{message.content}",
                    color=0x0064ff,
                    timestamp=datetime.datetime.utcnow()
                )

                suggestion_embed.set_footer(text=f"Suggestion by: {message.author}", icon_url=message.author.avatar_url)

                await message.delete()
                another_message = await suggestions_channel.send(embed=suggestion_embed)

                await another_message.add_reaction("👍")
                await another_message.add_reaction("👎")
                await another_message.add_reaction("🚫")
        matched_inv = re.findall("discord.gg/|discord.com/invite/", message.content, re.IGNORECASE)
        if matched_inv:
            matched_invite = re.search("discord.gg/\w+|discord.com/invite/\w+", message.content).group()
            invite = await self.bot.fetch_invite(matched_invite)
            if invite.guild is not cc_guild and message.author != self.bot.user:
                await message.author.send("No advertising allowed!")
                log_embed_punished = discord.Embed(
                    title="**Member Advertising**",
                    description=f"*{message.author.mention} **`({message.author})`** has just advertised another server in {message.channel.mention}!*",
                    timestamp=datetime.datetime.utcnow(),
                    color=0x0064ff
                )
                try:
                    log_embed_punished.set_thumbnail(url=message.author.avatar_url)
                except:
                    pass
                await log_channel.send(embed=log_embed_punished)
                self.invite_muteable_offence += 1
                await message.delete()
        if self.invite_muteable_offence >= 3 and message.author != self.bot.user:
            self.invite_kickable_offence += 1
            log_embed_muted = discord.Embed(
                title="**Member Auto-Muted**",
                description=f"*{message.author.mention} **`({message.author})`** has just been auto-muted for advertising other servers in {message.channel.mention}!*",
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )
            try:
                log_embed_muted.set_thumbnail(url=message.author.avatar_url)
            except:
                pass
            await log_channel.send(embed=log_embed_muted)
            await message.author.add_roles(mute_role)
            self.invite_muteable_offence = 0
            await asyncio.sleep(1800)
            await message.author.remove_roles(mute_role)

        if self.invite_kickable_offence >= 3 and message.author != self.bot.user:
            kick_embed = discord.Embed(
                title="**NOTIFICATION**",
                description=f":bell: *You have been kicked in **{log_channel.guild}** for advertising other servers!*",
                color=0x0064ff,
                timestamp=datetime.datetime.utcnow()
            )
            try:
                await message.author.send(embed=kick_embed)
            except:
                pass
            log_embed_kicked = discord.Embed(
                title="**Member Kicked**",
                description=f"*{message.author.mention} **`({message.author})`** has just been kicked for advertising other servers in {message.channel.mention}!*",
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )
            try:
                log_embed_kicked.set_thumbnail(url=message.author.avatar_url)
            except:
                pass
            await log_channel.send(embed=log_embed_kicked)
            self.invite_kickable_offence = 0
            await message.author.kick(reason=f"Sending Invite links to other servers!")

    @Cog.listener()
    async def on_message_delete(self, message):
        log_channel = self.bot.get_channel(771471454629003314)
        cc_guild = self.bot.get_guild(id=611227128020598805)

        if message.guild != cc_guild:
            return
        else:
            pass
        if not message.author.bot:
            matches = re.findall("```", message.content)
            if len(matches) >= 0:
                pre_message_content = message.content.replace("```", "")
                message_content = pre_message_content.replace("`", "")
            else:
                pass
            new_message_content = message_content or message.content
            log_embed = discord.Embed(
                title="**Message Deletion**",
                description=f"Message sent by **{message.author.mention}** deleted in **{message.channel.mention}**!",
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )
            log_embed.set_thumbnail(url=message.author.avatar_url)
            log_embed.add_field(name="**Message Content**", value=f"```{new_message_content}```", inline=True)
            await log_channel.send(embed=log_embed)

    @Cog.listener()
    async def on_bulk_message_delete(self, messages):
        log_channel = self.bot.get_channel(771471454629003314)
        cc_guild = self.bot.get_guild(id=611227128020598805)
        first_message = messages[0]

        if first_message.guild != cc_guild:
            return
        else:
            pass
        log_embed = discord.Embed(
            title="**Message Bulk Deletion**",
            description=f'*Deleted **{len(messages)}** message(s) in **{first_message.channel.mention}***!',
            timestamp=datetime.datetime.utcnow(),
            color=0x0064ff
        )
        await log_channel.send(embed=log_embed)

    @Cog.listener()
    async def on_message_edit(self, before, after):
        messages_log_channel = self.bot.get_channel(771471454629003314)
        message = after
        banned_links = ["https://pornhub.com", "https://porn.com", "https://fuq.com", "https://brazzers.com"]
        banned_racial_words = ["nigger", "nig", "nigor", "nigra", "nigre", "nigar", "niggur", "nigga", "niggah",
                               "niggar", "nigguh", "niggress", "nigette", "negro", "nibba", "niba", "n1gger", "n1ger",
                               "n1g", "n1gor", "n1gra", "n1gre", "n1gar", "n1ggur", "n1gga", "n1ggah", "n1ggar",
                               "n1gguh", "n1ggress", "n1gette", "negro", "n1bba", "n1ba"]
        log_channel = self.bot.get_channel(712761128895381676)
        cc_guild = self.bot.get_guild(id=611227128020598805)
        staff_role = discord.utils.get(cc_guild.roles, id=756565123350659385)
        banned_words = ["porn", "fuck", "dick", "pussy", "bitch", "bollocks", "cunt", "bugger", "chode",
                        "cock", "blowjob", "choad", "twat", "shag", "wanker", "bint", "balls", "tit", "boob", "sex",
                        "seggz", "segz", "cnut", "fcuk", "penis", "fück", "cünt", "fúck", "cúnt", "fùck", "cùnt",
                        "fŭck", "cŭnt", "fûck", "cûnt", "fǔck", "cǔnt", "fůck", "cůnt", "fǘck", "cǘnt", "fǜck", "cǜnt",
                        "fǚck", "cǚnt", "fǖck", "cǖnt", "fűck", "cűnt", "fũck", "cũnt", "fṹck", "cṹnt", "fųck", "cųnt",
                        "fų́ck", "cų́nt", "fų̃ck", "cų̃nt", "fūck", "cūnt", "fṻck", "cṻnt", "fū̀ck", "cū̀nt", "fū́ck",
                        "cū́nt", "fū̃ck", "cū̃nt", "fủck", "củnt", "fȕck", "cȕnt", "fȗck", "cȗnt", "fưck", "cưnt",
                        "fứck", "cứnt", "fừck", "cừnt", "fữck", "cữnt", "fửck", "cửnt", "fựck", "cựnt", "fụck", "cụnt",
                        "fṳck", "cṳnt", "fṷck", "cṷnt", "fṵck", "cṵnt", "fʉck", "cʉnt", "fᶙck", "cᶙnt", "fꭒck", "cꭒnt"]
        mute_role = discord.utils.get(cc_guild.roles, id=712730274412232807)

        if message.author in staff_role.members:
            return
        else:
            pass
        if any(re.findall("|".join(banned_links), message.content, re.IGNORECASE)):
            await message.delete()
            ban_embed = discord.Embed(
                title="**NOTIFICATION**",
                description=f":bell: *You have been banned in **{message.guild}** because you've sent an inappropriate link!*",
                color=0x0064ff,
                timestamp=datetime.datetime.utcnow()
            )
            ban_embed.add_field(name="**In case you would like to appeal your ban, go here:**",
                                value=f"https://forms.gle/zs9vRAz5Fw1SFgvR6", inline=False)
            try:
                await message.author.send(embed=ban_embed)
            except:
                pass
            try:
                await message.author.ban(reason="Sent something inappropriate!")
            except:
                return
        elif any(re.findall("|".join(banned_racial_words), message.content, re.IGNORECASE)):
            ban_embed = discord.Embed(
                title="**Member Banned**",
                description=f"***{message.author}** has been banned for sending a racial slur/banned word!*",
                color=0x0064ff,
                timestamp=datetime.datetime.utcnow()
            )
            ban_embed.add_field(name="**In case you would like to appeal your ban, go here:**",
                                value=f"https://forms.gle/zs9vRAz5Fw1SFgvR6", inline=False)
            try:
                ban_embed.set_thumbnail(url=message.author.avatar_url)
            except:
                pass
            await log_channel.send(embed=ban_embed)
        elif re.findall("https://web.roblox.com", message.content, re.IGNORECASE):
            ban_embed = discord.Embed(
                title="**Member Banned**",
                description=f"***{message.author}** has been banned for sending an underage version of a roblox link!*",
                color=0x0064ff,
                timestamp=datetime.datetime.utcnow()
            )
            ban_embed.add_field(name="**In case you would like to appeal your ban, go here:**",
                                value=f"https://forms.gle/zs9vRAz5Fw1SFgvR6", inline=False)
            try:
                ban_embed.set_thumbnail(url=message.author.avatar_url)
            except:
                pass
            await log_channel.send(embed=ban_embed)
        elif any(re.findall("|".join(banned_words), message.content, re.IGNORECASE)):
            banned_word = re.findall("|".join(banned_words), message.content, re.IGNORECASE)
            matches = re.findall("`|```", message.content)
            if len(matches) >= 0:
                pre_message_content = message.content.replace("```", "")
                message_content = pre_message_content.replace("`", "")
            else:
                pass
            new_message_content = message_content or message.content
            await message.author.send(
                "Greetings! I've detected a banned word in your message, right now, it is up to our wonderful staff members to decide whether or not this is well-deserved of a punishment.")
            await message.author.send(
                f"The word(s) in particular is/are **`{banned_word}`**, in the following message content:\n\n ```{new_message_content}```")
            auto_reports = cc_guild.get_channel(786007666329124874)
            pag = Paginator(f"Word(s) **`{banned_word}`** found in:\n\n```{new_message_content}```", 1985)
            await pag.send(bot=self.bot, channel=auto_reports, member=message.author, end_channel=message.author,
                           another_channel=log_channel, title="**AUTO-REPORTED MESSAGE**", autoreport=True,
                           messagee=message)
        if before.content != after.content:
            matches1 = re.findall("```|`", before.content)
            if len(matches1) >= 0:
                pre_before_message_content = before.content.replace("```", "")
                before_message_content = pre_before_message_content.replace("`", "")
            else:
                pass
            before_new_message_content = before_message_content or before.content
            matches2 = re.findall("```|`", after.content)
            if len(matches2) >= 0:
                pre_after_message_content = after.content.replace("```", "")
                after_message_content = pre_after_message_content.replace("`", "")
            else:
                pass
            after_new_message_content = after_message_content or after.content
            log_embed = discord.Embed(
                title="**Message Edit**",
                description=f'**{message.author.mention}** Edited The **[Message]({message.jump_url})** in **{message.channel.mention}**!',
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )
            log_embed.add_field(name="**Before**", value=f"```{before_new_message_content}```", inline=False)
            log_embed.add_field(name="**After**", value=f"```{after_new_message_content}```", inline=False)
            log_embed.set_thumbnail(url=before.author.avatar_url)
            await messages_log_channel.send(embed=log_embed)
        matched_inv = re.findall("discord.gg/|discord.com/invite/", message.content, re.IGNORECASE)
        if matched_inv:
            matched_invite = re.search("discord.gg/\w+|discord.com/invite/\w+", message.content).group()
            invite = await self.bot.fetch_invite(matched_invite)
            if invite.guild is not cc_guild:
                await message.author.send("No advertising allowed!")
                log_embed_punished = discord.Embed(
                    title="**Member Advertising**",
                    description=f"*{message.author.mention} **`({message.author})`** has just advertised another server in {message.channel.mention}!*",
                    timestamp=datetime.datetime.utcnow(),
                    color=0x0064ff
                )
                try:
                    log_embed_punished.set_thumbnail(url=message.author.avatar_url)
                except:
                    pass
                await log_channel.send(embed=log_embed_punished)
                self.invite_muteable_offence += 1
                await message.delete()
        if self.invite_muteable_offence >= 3 and message.author != self.bot.user:
            self.invite_kickable_offence += 1
            log_embed_muted = discord.Embed(
                title="**Member Auto-Muted**",
                description=f"*{message.author.mention} **`({message.author})`** has just been auto-muted for advertising other servers in {message.channel.mention}!*",
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )
            try:
                log_embed_muted.set_thumbnail(url=message.author.avatar_url)
            except:
                pass
            await log_channel.send(embed=log_embed_muted)
            await message.author.add_roles(mute_role)
            self.invite_muteable_offence = 0
            await asyncio.sleep(1800)
            await message.author.remove_roles(mute_role)

        if self.invite_kickable_offence >= 3 and message.author != self.bot.user:
            kick_embed = discord.Embed(
                title="**NOTIFICATION**",
                description=f":bell: *You have been kicked in **{log_channel.guild}** for advertising other servers!*",
                color=0x0064ff,
                timestamp=datetime.datetime.utcnow()
            )
            try:
                await message.author.send(embed=kick_embed)
            except:
                pass
            log_embed_kicked = discord.Embed(
                title="**Member Kicked**",
                description=f"*{message.author.mention} **`({message.author})`** has just been kicked for advertising other servers in {message.channel.mention}!*",
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )
            try:
                log_embed_kicked.set_thumbnail(url=message.author.avatar_url)
            except:
                pass
            await log_channel.send(embed=log_embed_kicked)
            self.invite_kickable_offence = 0
            await message.author.kick(reason=f"Sending Invite links to other servers!")

    @Cog.listener()
    async def on_member_update(self, before, after):
        sum_channel = self.bot.get_channel(767416354700918814)
        message = await sum_channel.fetch_message(770695658318463007)
        guild = sum_channel.guild
        booster_role = discord.utils.get(guild.roles, id=762172204628181023)
        excluded_roles = [611227128020598805, 707957214995808296, 732375953203789965, 743590325448212651,
                          743013370588037191, 732388199107657828, 743013368511594569, 743013366515236915,
                          743013366880272474, 743013367840768072, 743013368134107166, 732387788493946881,
                          732402691296198848, 734149969292034208, 734150445764837466, 734150696944795698,
                          735497751978311681, 734527020905529375, 734664303327838230, 734527130565738516,
                          735557139984285706, 738814580712669214, 734664243038912552, 734527217350082672,
                          734527854871707762, 746758563703291938, 695328817157373992, 741735258411499560,
                          722793289119432736, 734638949162811470, 734639357360603166, 734639430828032061,
                          734639586038513716, 734639664606085133, 742333164352962581, 742333167133786124,
                          742333168576888943, 742333169423876106, 745347527209123871]
        role_update_log_channel = self.bot.get_channel(770368850679169075)
        nick_update_log_channel = self.bot.get_channel(771465528618254347)

        if before.top_role.guild == guild:
            pass
        else:
            return

        if before.nick != after.nick and after.nick != before.nick:
            nick_log_embed = discord.Embed(
                title="**Nickname Update**",
                description=f"Nickname Update for **{after.mention}**!",
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )
            nick_log_embed.add_field(name="**Before**", value=f"```{before.nick}```", inline=False)
            nick_log_embed.add_field(name="**After**", value=f"```{after.nick}```", inline=False)

            await nick_update_log_channel.send(embed=nick_log_embed)
        if len(after.roles) > len(before.roles):
            role_difference_set = set(after.roles).difference(set(before.roles))
            for first_role in role_difference_set:
                actual_role = discord.utils.get(guild.roles, name=str(first_role))
                if actual_role.id not in excluded_roles:
                    role_log_embed = discord.Embed(
                        title="**Role Update**",
                        description=f"*Role Added for **{after.mention}***!",
                        timestamp=datetime.datetime.utcnow(),
                        color=0x0064ff
                    )
                    role_log_embed.add_field(name="**Added Role**", value=f":white_check_mark: {actual_role.mention}",
                                             inline=False)
                    role_log_embed.set_thumbnail(url=before.avatar_url)
                    await role_update_log_channel.send(embed=role_log_embed)
        elif len(before.roles) > len(after.roles):
            role_difference_set = set(before.roles).difference(set(after.roles))
            for first_role in role_difference_set:
                actual_role = discord.utils.get(guild.roles, name=str(first_role))
                if actual_role.id not in excluded_roles:
                    role_log_embed = discord.Embed(
                        title="**Role Update**",
                        description=f"*Role removed for **{after.mention}***!",
                        timestamp=datetime.datetime.utcnow(),
                        color=0x0064ff
                    )
                    role_log_embed.add_field(name="**Removed Role**", value=f":no_entry_sign: {actual_role.mention}",
                                             inline=False)
                    role_log_embed.set_thumbnail(url=before.avatar_url)
                    await role_update_log_channel.send(embed=role_log_embed)
        if booster_role in before.roles and booster_role not in after.roles:
            await message.edit(
                content=f"Currently, there are a total of **{guild.member_count}** Members in this server,\n**{guild.premium_subscription_count}** Boosters,\nBoosting Level for this server is currently **{guild.premium_tier}**.")

    @Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        log_channel = self.bot.get_channel(736234713940754432)
        cc_guild = self.bot.get_guild(id=611227128020598805)

        try:
            if before.channel:
                if before.channel.guild != cc_guild and after.channel.guild != cc_guild:
                    return
                else:
                    pass
            else:
                pass
        except:
            pass
        if after.channel and not before.channel:
            member_joined_vc_log_embed = discord.Embed(
                title="**Member Joined Voice Channel**",
                description=f"**{member.mention}** just joined the voice channel **`{after.channel}`**!",
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )

            member_joined_vc_log_embed.set_thumbnail(url=member.avatar_url)
            await log_channel.send(embed=member_joined_vc_log_embed)
        elif before.channel and not after.channel:
            member_left_vc_log_embed = discord.Embed(
                title="**Member Left Voice Channel**",
                description=f"**{member.mention}** just left the voice channel **`{before.channel}`**!",
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )

            member_left_vc_log_embed.set_thumbnail(url=member.avatar_url)
            await log_channel.send(embed=member_left_vc_log_embed)
        elif before.channel and after.channel and before.channel != after.channel:
            member_switched_vc_log_embed = discord.Embed(
                title="**Member Switched Voice Channels**",
                description=f"**{member.mention}** just left **`{before.channel}`** and joined **`{after.channel}`**!",
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )

            member_switched_vc_log_embed.set_thumbnail(url=member.avatar_url)
            await log_channel.send(embed=member_switched_vc_log_embed)
        if after.self_mute:
            member_self_muted_log_embed1 = discord.Embed(
                title="**Member Self-Muted**",
                description=f"**{member.mention}** just self-muted themselves in **`{after.channel}`**!",
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )

            member_self_muted_log_embed1.set_thumbnail(url=member.avatar_url)
            await log_channel.send(embed=member_self_muted_log_embed1)
        elif after.mute:
            member_muted_log_embed1 = discord.Embed(
                title="**Member Muted**",
                description=f"**{member.mention}** just got muted in **`{after.channel}`**!",
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )

            member_muted_log_embed1.set_thumbnail(url=member.avatar_url)
            await log_channel.send(embed=member_muted_log_embed1)
        elif after.deaf:
            member_deaf_log_embed1 = discord.Embed(
                title="**Member Deafened**",
                description=f"**{member.mention}** just got deafened in **`{after.channel}`**!",
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )

            member_deaf_log_embed1.set_thumbnail(url=member.avatar_url)
            await log_channel.send(embed=member_deaf_log_embed1)
        elif after.self_deaf:
            member_self_deaf_log_embed1 = discord.Embed(
                title="**Member Self-Deafened**",
                description=f"**{member.mention}** just self-deafened in **`{after.channel}`**!",
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )

            member_self_deaf_log_embed1.set_thumbnail(url=member.avatar_url)
            await log_channel.send(embed=member_self_deaf_log_embed1)
        elif after.self_stream:
            member_self_stream_log_embed1 = discord.Embed(
                title="**Member Started Streaming**",
                description=f"**{member.mention}** just started streaming in **`{after.channel}`**!",
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )

            member_self_stream_log_embed1.set_thumbnail(url=member.avatar_url)
            await log_channel.send(embed=member_self_stream_log_embed1)
        elif after.self_video:
            member_self_video_log_embed1 = discord.Embed(
                title="**Member Turned Camera On**",
                description=f"**{member.mention}** just turned their camera on in **`{after.channel}`**!",
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )

            member_self_video_log_embed1.set_thumbnail(url=member.avatar_url)
            await log_channel.send(embed=member_self_video_log_embed1)
        elif before.self_mute:
            member_self_muted_log_embed2 = discord.Embed(
                title="**Member Un-Self-Muted**",
                description=f"**{member.mention}** just un-self-muted themselves in **`{after.channel}`**!",
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )

            member_self_muted_log_embed2.set_thumbnail(url=member.avatar_url)
            await log_channel.send(embed=member_self_muted_log_embed2)
        elif before.mute:
            member_muted_log_embed2 = discord.Embed(
                title="**Member Un-Muted**",
                description=f"**{member.mention}** just got un-muted in **`{after.channel}`**!",
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )

            member_muted_log_embed2.set_thumbnail(url=member.avatar_url)
            await log_channel.send(embed=member_muted_log_embed2)
        elif before.deaf:
            member_deaf_log_embed2 = discord.Embed(
                title="**Member Un-Deafened**",
                description=f"**{member.mention}** just got un-deafened in **`{after.channel}`**!",
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )

            member_deaf_log_embed2.set_thumbnail(url=member.avatar_url)
            await log_channel.send(embed=member_deaf_log_embed2)
        elif before.self_deaf:
            member_self_deaf_log_embed2 = discord.Embed(
                title="**Member Un-Self-Deafened**",
                description=f"**{member.mention}** just un-self-deafened in **`{after.channel}`**!",
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )

            member_self_deaf_log_embed2.set_thumbnail(url=member.avatar_url)
            await log_channel.send(embed=member_self_deaf_log_embed2)
        elif before.self_stream:
            member_self_stream_log_embed2 = discord.Embed(
                title="**Member Stopped Streaming**",
                description=f"**{member.mention}** just stopped streaming in **`{after.channel}`**!",
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )

            member_self_stream_log_embed2.set_thumbnail(url=member.avatar_url)
            await log_channel.send(embed=member_self_stream_log_embed2)
        elif before.self_video:
            member_self_video_log_embed2 = discord.Embed(
                title="**Member Turned Camera Off**",
                description=f"**{member.mention}** just turned their camera off in **`{after.channel}`**!",
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )

            member_self_video_log_embed2.set_thumbnail(url=member.avatar_url)
            await log_channel.send(embed=member_self_video_log_embed2)

    @Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(767416354700918814)
        message = await channel.fetch_message(770695658318463007)
        guild = channel.guild
        log_channel = self.bot.get_channel(736234502816399422)
        delta_created = datetime.datetime.utcnow() - member.created_at
        format = "%A, %d %B, %Y : %I:%M %p"
        cc_guild = self.bot.get_guild(id=611227128020598805)

        if member.guild != cc_guild:
            return
        else:
            pass
        if delta_created.days < 7:
            kick_embed = discord.Embed(
                title="**NOTIFICATION**",
                description=f":bell: *You have been kicked in **{guild}** because your account is not even a week old. You may join back once your account is at least one week old*!",
                color=0x0064ff,
                timestamp=datetime.datetime.utcnow()
            )
            try:
                await member.send(embed=kick_embed)
            except discord.Forbidden:
                pass
            await member.kick(reason="Account Age is less than a week.")
            return
        else:
            log_embed = discord.Embed(
                title="**Member Joined**",
                description=f"**{member.mention}** Joined The Server!\n Account Created **{member.created_at.strftime(format)}**.",
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )

            log_embed.set_thumbnail(url=member.avatar_url)

            await log_channel.send(embed=log_embed)

            await message.edit(
                content=f"Currently, there are a total of **{guild.member_count}** Members in this server,\n**{guild.premium_subscription_count}** Boosters,\nBoosting Level for this server is currently **{guild.premium_tier}**.")

    @Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(767416354700918814)
        message = await channel.fetch_message(770695658318463007)
        guild = channel.guild
        log_channel = self.bot.get_channel(736234502816399422)
        format = "%A, %d %B, %Y : %I:%M %p"
        excluded_roles = [611227128020598805, 707957214995808296, 732375953203789965, 743590325448212651,
                          743013370588037191, 732388199107657828, 743013368511594569, 743013366515236915,
                          743013366880272474, 743013367840768072, 743013368134107166, 732387788493946881,
                          732402691296198848, 734149969292034208, 734150445764837466, 734150696944795698,
                          735497751978311681, 734527020905529375, 734664303327838230, 734527130565738516,
                          735557139984285706, 738814580712669214, 734664243038912552, 734527217350082672,
                          734527854871707762, 746758563703291938]
        member_roles = ", ".join(
            role.mention for role in member.roles if role.id not in excluded_roles) or "No roles assigned."
        cc_guild = self.bot.get_guild(id=611227128020598805)

        if member.guild != cc_guild:
            return
        else:
            pass
        try:
            if await guild.fetch_ban(user=member):
                return
            else:
                pass
        except:
            pass

        log_embed = discord.Embed(
            title="**Member Left**",
            description=f"**{member.mention}** Left The Server!\n Account Created **{member.created_at.strftime(format)}**.\n Member Joined **{member.joined_at.strftime(format)}**.",
            timestamp=datetime.datetime.utcnow(),
            color=0x0064ff
        )

        log_embed.add_field(name="Roles:", value=f"{member_roles}", inline=False)
        log_embed.set_thumbnail(url=member.avatar_url)

        await log_channel.send(embed=log_embed)

        await message.edit(
            content=f"""Currently, there are a total of **{guild.member_count}** Members in this server,\n**{guild.premium_subscription_count}** Boosters,\nBoosting Level for this server is currently **{guild.premium_tier}**.""")


def setup(bot):
    bot.add_cog(Log(bot))
