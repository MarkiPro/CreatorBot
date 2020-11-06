import asyncio
import datetime
from typing import Optional, Any

import discord
from discord.ext.commands import Cog


class Log(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_guild_role_create(self, role):
        server_management_logs_channel = self.bot.get_channel(771465807276277810)

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
        role = before or after

        log_embed = discord.Embed(
            title="**Role Creation**",
            description=f"{role.mention} was just created!",
            timestamp=datetime.datetime.utcnow(),
            color=0x0064ff
        )

        log_embed.add_field(name="**Before**", value=f"{before.permissions}", inline=True)
        log_embed.add_field(name="**After**", value=f"{after.permissions}", inline=True)

        await server_management_logs_channel.send(embed=log_embed)

    @Cog.listener()
    async def on_reaction_add(self, reaction, user):
        message = reaction.message
        suggestions_channel = self.bot.get_channel(712655570737299567)
        top_suggestions_channel = self.bot.get_channel(771822991256059905)
        reactions = message.reactions
        reaction1 = reactions[0]
        reaction2 = reactions[1]

        if reaction == reaction1 and reaction1.count > reaction2.count and reaction1.count >= 2:
            if message.channel == suggestions_channel:
                suggest_embed = discord.Embed(
                    title="**Top Suggestion**",
                    description=f"[Message link]({message.jump_url})",
                    timestamp=datetime.datetime.utcnow(),
                    color=0x0064ff
                )

                await top_suggestions_channel.send(embed=suggest_embed)
        elif reaction == reaction2 and reaction2.count > reaction1.count and reaction2.count >= 2:
            if message.channel == suggestions_channel:
                await message.delete()

    @Cog.listener()
    async def on_message(self, message):
        suggestions_channel = self.bot.get_channel(712655570737299567)
        banned_links = ["https://pornhub.com/", "https://porn.com/", "https://fuq.com/", "https://web.roblox.com/"]
        banned_words = ["nigger", "nig", "nigor", "nigra", "nigre", "nigar", "niggur", "nigga", "niggah", "niggar", "nigguh", "niggress", "nigette", "negro", "nibba", "niba", "n1gger", "n1ger", "n1g", "n1gor", "n1gra", "n1gre", "n1gar", "n1ggur", "n1gga", "n1ggah", "n1ggar", "n1gguh", "n1ggress", "n1gette", "negro", "n1bba", "n1ba"]

        if not message.author.bot and message.channel == suggestions_channel:
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

        if str(tuple(banned_links)) in message.content or str(tuple(banned_words)) in message.content:
            ban_embed = discord.Embed(
                title="**NOTIFICATION**",
                description=f":bell: *You have been banned in **{message.guild}** because you've sent something inappropriate, or turned out to be underage!*!",
                color=0x0064ff,
                timestamp=datetime.datetime.now(tz=None)
            )

            ban_embed.add_field(name="**In case you would like to appeal your ban, go here:**", value=f"https://forms.gle/zs9vRAz5Fw1SFgvR6", inline=False)

            await message.author.ban(embed=ban_embed)

    @Cog.listener()
    async def on_message_delete(self, message):
        log_channel = self.bot.get_channel(771471454629003314)

        if not message.author.bot:
            log_embed = discord.Embed(
                title="**Message Deletion**",
                description=f"{message.author.mention} Deleted a Message in {message.channel.mention}!",
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )
            log_embed.set_thumbnail(url=message.author.avatar_url)
            log_embed.add_field(name="**Message Content**", value=f"```{message.content}```", inline=True)
            await log_channel.send(embed=log_embed)

    @Cog.listener()
    async def on_message_edit(self, before, after):
        log_channel = self.bot.get_channel(771471454629003314)
        message = before

        if not message.author.bot:
            log_embed = discord.Embed(
                title="**Message Edit**",
                description=f'{message.author.mention} Edited The [Message]({message.jump_url}) in {message.channel.mention}!',
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )
            log_embed.add_field(name="**Before**", value=f"```{before.content}```", inline=False)
            log_embed.add_field(name="**After**", value=f"```{after.content}```", inline=False)
            log_embed.set_thumbnail(url=before.author.avatar_url)
            await log_channel.send(embed=log_embed)

    @Cog.listener()
    async def on_member_update(self, before, after):
        sum_channel = self.bot.get_channel(767416354700918814)
        message = await sum_channel.fetch_message(770695658318463007)
        guild = sum_channel.guild
        booster_role = discord.utils.get(guild.roles, id=762172204628181023)
        exculded_roles = [611227128020598805, 707957214995808296, 732375953203789965, 743590325448212651, 743013370588037191, 732388199107657828, 743013368511594569, 743013366515236915, 743013366880272474, 743013367840768072, 743013368134107166, 732387788493946881, 732402691296198848, 734149969292034208, 734150445764837466, 734150696944795698, 735497751978311681, 734527020905529375, 734664303327838230, 734527130565738516, 735557139984285706, 738814580712669214, 734664243038912552, 734527217350082672, 734527854871707762, 746758563703291938]
        before_roles = ", ".join(role.mention for role in before.roles if role.id not in exculded_roles) or "No roles assigned."
        after_roles = ", ".join(role.mention for role in after.roles if role.id not in exculded_roles) or "No roles assigned."
        role_update_log_channel = self.bot.get_channel(770368850679169075)
        nick_update_log_channel = self.bot.get_channel(771465528618254347)

        if before.display_name != after.display_name and after.display_name != before.display_name:
            nick_log_embed = discord.Embed(
                title="Nickname Update",
                description=f"Nickname Update for {after.mention}!",
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )
            nick_log_embed.add_field(name="**Before**", value=f"```{before.display_name}```", inline=False)
            nick_log_embed.add_field(name="**After**", value=f"```{after.display_name}```", inline=False)

            await nick_update_log_channel.send(embed=nick_log_embed)

        if before_roles != after_roles and after_roles != before_roles and str(before_roles) != "No roles assigned." and str(after_roles) != "No roles assigned.":
            role_log_embed = discord.Embed(
                title="Role Update",
                description=f"Role Update for {after.mention}!",
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )
            role_log_embed.add_field(name="**Before**", value=f"{before_roles}", inline=False)
            role_log_embed.add_field(name="**After**", value=f"{after_roles}", inline=False)
            role_log_embed.set_thumbnail(url=before.avatar_url)
            await role_update_log_channel.send(embed=role_log_embed)
            await asyncio.sleep(60)

        if booster_role in before.roles and booster_role not in after.roles:
            await message.edit(content=f"""Currently, there are a total of **{guild.member_count}** Members in this server,\n**{guild.premium_subscription_count}** Boosters,\nBoosting Level for this server is currently **{guild.premium_tier}**.""")

    @Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        log_channel = self.bot.get_channel(736234713940754432)

        if after.channel and not before.channel:
            member_joined_vc_log_embed = discord.Embed(
                title="Member Joined Voice Channel",
                description=f"{member.mention} just joined the voice channel `{after.channel}`!",
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )

            member_joined_vc_log_embed.set_thumbnail(url=member.avatar_url)
            await log_channel.send(embed=member_joined_vc_log_embed)

        elif before.channel and not after.channel:
            member_left_vc_log_embed = discord.Embed(
                title="Member Left Voice Channel",
                description=f"{member.mention} just left the voice channel `{after.channel}`!",
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )

            member_left_vc_log_embed.set_thumbnail(url=member.avatar_url)
            await log_channel.send(embed=member_left_vc_log_embed)

        elif before.channel and after.channel and before.channel != after.channel:
            member_switched_vc_log_embed = discord.Embed(
                title="Member Switched Voice Channels",
                description=f"{member.mention} just left {before.channel.mention} and joined {after.channel.mention}!",
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

        if delta_created.days < 7:
            kick_embed = discord.Embed(
                title="**NOTIFICATION**",
                description=f":bell: *You have been kicked in **{guild}** because your account is not even a week old. You may join back once your account is at least one week old*!",
                color=0x0064ff,
                timestamp=datetime.datetime.now(tz=None)
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
                description=f"{member.mention} Joined The Server!\n Account Created {delta_created.days} days ago.",
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
        delta_created = datetime.datetime.utcnow() - member.created_at

        log_embed = discord.Embed(
            title="**Member Left**",
            description=f"{member.mention} Left The Server!\n Account Created {delta_created.days} days ago.",
            timestamp=datetime.datetime.utcnow(),
            color=0x0064ff
        )

        log_embed.set_thumbnail(url=member.avatar_url)

        await log_channel.send(embed=log_embed)

        await message.edit(content=f"""Currently, there are a total of **{guild.member_count}** Members in this server,\n**{guild.premium_subscription_count}** Boosters,\nBoosting Level for this server is currently **{guild.premium_tier}**.""")


def setup(bot):
    bot.add_cog(Log(bot))
