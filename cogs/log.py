import asyncio
import datetime
from typing import Optional, Any
import re

import discord
from discord.ext.commands import Cog


class Log(Cog):
    def __init__(self, bot):
        self.bot = bot

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
            description=f"{role.mention} was just created!",
            timestamp=datetime.datetime.utcnow(),
            color=0x0064ff
        )

        await server_management_logs_channel.send(embed=log_embed)

    @Cog.listener()
    async def on_guild_role_update(self, before, after):
        server_management_logs_channel = self.bot.get_channel(771465807276277810)
        role = before
        cc_guild = self.bot.get_guild(id=611227128020598805)

        if before.guild != cc_guild and after.guild != cc_guild:
            return
        else:
            pass
        if before.position != after.position:
            return

        if before.permissions != after.permissions:
            log_embed = discord.Embed(
                title="**Role Updated**",
                description=f"**{role.mention}** was just updated!",
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
                if reaction1 and message.channel == suggestions_channel and reaction == reaction1 and user in staff_role.members:
                    await message.delete()

        if len(reactions) >= 2:
            reaction1 = reactions[0]
            reaction2 = reactions[1]

            if reaction == reaction1 and message.channel == suggestions_channel:
                async for some_user in reaction2.users():
                    if some_user.id == user.id:
                        await reaction.remove(user)
                        await user.send("You've already disliked this suggestion, if you wanna change your vote, you have to remove your previous reaction.")
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
                        await user.send("You've already liked this suggestion, if you wanna change your vote, you have to remove your previous reaction.")
                        return
                if reaction2.count > reaction1.count and reaction2.count >= 10:
                    await message.delete()
        else:
            return

        if len(reactions) >= 3:
            reaction1 = reactions[2]

            if reaction == reaction1 and user in staff_role.members:
                if message.channel == suggestions_channel:
                    await message.delete()
        else:
            return

    @Cog.listener()
    async def on_message(self, message):
        suggestions_channel = self.bot.get_channel(712655570737299567)
        banned_links = ["https://pornhub.com", "https://porn.com", "https://fuq.com", "https://web.roblox.com", "https://brazzers.com"]
        banned_words = ["nigger", "nig", "nigor", "nigra", "nigre", "nigar", "niggur", "nigga", "niggah", "niggar", "nigguh", "niggress", "nigette", "negro", "nibba", "niba", "n1gger", "n1ger", "n1g", "n1gor", "n1gra", "n1gre", "n1gar", "n1ggur", "n1gga", "n1ggah", "n1ggar", "n1gguh", "n1ggress", "n1gette", "negro", "n1bba", "n1ba"]
        banned_links_v2 = ["https://pornhub.com", "https://porn.com", "https://fuq.com"]
        log_channel = self.bot.get_channel(712761128895381676)
        cc_guild = self.bot.get_guild(id=611227128020598805)

        if message.guild != cc_guild:
            return
        else:
            pass
        if not message.author.bot and message.channel == suggestions_channel:
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

        if any(re.findall("|".join(banned_words), message.content, re.IGNORECASE)) or any(re.findall("|".join(banned_links), message.content, re.IGNORECASE)):
            if message.author.top_role < self.bot.top_role:
                ban_embed = discord.Embed(
                    title="**NOTIFICATION**",
                    description=f":bell: *You have been banned in **{message.guild}** because you've sent something inappropriate, or turned out to be underage!*",
                    color=0x0064ff,
                    timestamp=datetime.datetime.utcnow()
                )

                ban_embed.add_field(name="**In case you would like to appeal your ban, go here:**", value=f"https://forms.gle/zs9vRAz5Fw1SFgvR6", inline=False)

                try:
                    await message.author.send(embed=ban_embed)
                except Exception:
                    pass

                try:
                    await message.author.ban(reason="Sent something inappropriate, or turned out to be underage!")
                except:
                    return
            else:
                return
            if any(re.findall("|".join(banned_words), message.content, re.IGNORECASE)):
                ban_embed_reason = discord.Embed(
                    title="**Member Banned**",
                    description=f"***{message.author}** has been banned for sending a racial slur/banned word!*",
                    color=0x0064ff,
                    timestamp=datetime.datetime.utcnow()
                )
                await log_channel.send(embed=ban_embed_reason)
            if re.match("https://web.roblox.com", message.content, re.IGNORECASE):
                ban_embed_reason = discord.Embed(
                    title="**Member Banned**",
                    description=f"***{message.author}** has been banned for sending an underage version of a roblox link!*",
                    color=0x0064ff,
                    timestamp=datetime.datetime.utcnow()
                )
                await log_channel.send(embed=ban_embed_reason)
            if any(re.findall("|".join(banned_links_v2), message.content, re.IGNORECASE)):
                ban_embed_reason = discord.Embed(
                    title="**Member Banned**",
                    description=f"***{message.author}** has been banned for sending an inappropriate link!*",
                    color=0x0064ff,
                    timestamp=datetime.datetime.utcnow()
                )
                await log_channel.send(embed=ban_embed_reason)

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
        if not messages.author.bot:
            log_embed = discord.Embed(
                title="**Message Bulk Deletion**",
                description=f'*Deleted **{len(messages)}** in **{messages.channel.mention}***!',
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )
            await log_channel.send(embed=log_embed)

    @Cog.listener()
    async def on_message_edit(self, before, after):
        log_channel = self.bot.get_channel(771471454629003314)
        message = before
        cc_guild = self.bot.get_guild(id=611227128020598805)

        if message.guild != cc_guild:
            return
        else:
            pass
        if not message.author.bot and before.content != after.content:
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
            await log_channel.send(embed=log_embed)

    @Cog.listener()
    async def on_member_update(self, before, after):
        sum_channel = self.bot.get_channel(767416354700918814)
        message = await sum_channel.fetch_message(770695658318463007)
        guild = sum_channel.guild
        booster_role = discord.utils.get(guild.roles, id=762172204628181023)
        excluded_roles = [611227128020598805, 707957214995808296, 732375953203789965, 743590325448212651, 743013370588037191, 732388199107657828, 743013368511594569, 743013366515236915, 743013366880272474, 743013367840768072, 743013368134107166, 732387788493946881, 732402691296198848, 734149969292034208, 734150445764837466, 734150696944795698, 735497751978311681, 734527020905529375, 734664303327838230, 734527130565738516, 735557139984285706, 738814580712669214, 734664243038912552, 734527217350082672, 734527854871707762, 746758563703291938]
        before_roles = [(role.mention for role in before.roles if role.id not in excluded_roles) or "No roles assigned."]
        after_roles = [(role.mention for role in after.roles if role.id not in excluded_roles) or "No roles assigned."]
        role_update_log_channel = self.bot.get_channel(770368850679169075)
        nick_update_log_channel = self.bot.get_channel(771465528618254347)
        cc_guild = self.bot.get_guild(id=611227128020598805)

        if before.guild != cc_guild and after.guild != cc_guild:
            return
        else:
            pass
        if before.display_name != after.display_name and after.display_name != before.display_name:
            nick_log_embed = discord.Embed(
                title="**Nickname Update**",
                description=f"Nickname Update for **{after.mention}**!",
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )
            nick_log_embed.add_field(name="**Before**", value=f"```{before.display_name}```", inline=False)
            nick_log_embed.add_field(name="**After**", value=f"```{after.display_name}```", inline=False)

            await nick_update_log_channel.send(embed=nick_log_embed)
        if str(after_roles) == "No roles assigned." or str(after_roles) == "No roles assigned." and str(before_roles) == "No roles assigned.":
            print("returned!")
            return
        else:
            pass
        for role in list(set(after.roles)):
            if role not in before.roles:
                actual_role = discord.utils.get(cc_guild.roles, name=f"{role}")
                role_log_embed = discord.Embed(
                    title="**Role Update**",
                    description=f"*Role Added for **{after.mention}***!",
                    timestamp=datetime.datetime.utcnow(),
                    color=0x0064ff
                )
                role_log_embed.add_field(name="**Added Role**", value=f":white_check_mark: {actual_role.mention}", inline=False)
                role_log_embed.set_thumbnail(url=before.avatar_url)
                await role_update_log_channel.send(embed=role_log_embed)
        for role in list(set(before.roles)):
            if role not in after.roles:
                actual_role = discord.utils.get(cc_guild.roles, name=f"{role}")
                role_log_embed = discord.Embed(
                    title="**Role Update**",
                    description=f"*Role removed for **{after.mention}***!",
                    timestamp=datetime.datetime.utcnow(),
                    color=0x0064ff
                )
                role_log_embed.add_field(name="**Removed Role**", value=f":no_entry_sign: {actual_role.mention}", inline=False)
                role_log_embed.set_thumbnail(url=before.avatar_url)
                await role_update_log_channel.send(embed=role_log_embed)
        if booster_role in before.roles and booster_role not in after.roles:
            await message.edit(content=f"Currently, there are a total of **{guild.member_count}** Members in this server,\n**{guild.premium_subscription_count}** Boosters,\nBoosting Level for this server is currently **{guild.premium_tier}**.")

    @Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        log_channel = self.bot.get_channel(736234713940754432)
        cc_guild = self.bot.get_guild(id=611227128020598805)

        if before.guild != cc_guild and after.guild != cc_guild:
            return
        else:
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

            await message.edit(content=f"Currently, there are a total of **{guild.member_count}** Members in this server,\n**{guild.premium_subscription_count}** Boosters,\nBoosting Level for this server is currently **{guild.premium_tier}**.")

    @Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(767416354700918814)
        message = await channel.fetch_message(770695658318463007)
        guild = channel.guild
        log_channel = self.bot.get_channel(736234502816399422)
        format = "%A, %d %B, %Y : %I:%M %p"
        delta_created = datetime.datetime.utcnow() - member.created_at
        delta_joined = datetime.datetime.utcnow() - member.joined_at
        excluded_roles = [611227128020598805, 707957214995808296, 732375953203789965, 743590325448212651, 743013370588037191, 732388199107657828, 743013368511594569, 743013366515236915, 743013366880272474, 743013367840768072, 743013368134107166, 732387788493946881, 732402691296198848, 734149969292034208, 734150445764837466, 734150696944795698, 735497751978311681, 734527020905529375, 734664303327838230, 734527130565738516, 735557139984285706, 738814580712669214, 734664243038912552, 734527217350082672, 734527854871707762, 746758563703291938]
        member_roles = ", ".join(role.mention for role in member.roles if role.id not in excluded_roles) or "No roles assigned."
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
        except Exception:
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

        await message.edit(content=f"""Currently, there are a total of **{guild.member_count}** Members in this server,\n**{guild.premium_subscription_count}** Boosters,\nBoosting Level for this server is currently **{guild.premium_tier}**.""")


def setup(bot):
    bot.add_cog(Log(bot))
