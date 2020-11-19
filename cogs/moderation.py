import asyncio
import datetime

import discord
from discord.ext import commands
from discord.utils import parse_time


class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def clear(self, ctx, amount: int = 0, *, channel: discord.TextChannel = None):
        channel = channel or ctx.channel

        await ctx.message.delete()
        await channel.purge(limit=amount)

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(kick_members=True)
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if member.id == ctx.me.id:
            embed1 = discord.Embed(
                title="**OOPS**",
                description=f"***Sorry bro, not gonna happen :) ***",
                color=0xffbd00,
                timestamp=datetime.datetime.utcnow()
            )
            await ctx.send(embed=embed1)
        embed1 = discord.Embed(
            title="**SUCCESS**",
            description=f"***:white_check_mark: *** {member.display_name} *** has been kicked for: `{reason}`!***",
            color=0x00fa00,
            timestamp=datetime.datetime.utcnow()
        )
        embed2 = discord.Embed(
            title="**NOTIFICATION**",
            description=f":bell: *You have been kicked in **{ctx.guild}** for:* `{reason}`!",
            color=0x0064ff,
            timestamp=datetime.datetime.utcnow()
        )
        async with ctx.typing():
            try:
                await member.send(embed=embed2)
            except discord.Forbidden:
                pass
            await member.kick(reason=reason)
            await ctx.send(embed=embed1)

    @commands.command(aliases=['perm-ban'], description="This command is used for permanently banning.")
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def permban(self, ctx, member: discord.Member, *, reason=None):
        if member.id == ctx.me.id:
            embed1 = discord.Embed(
                title="**OOPS**",
                description=f"***Sorry bro, not gonna happen! :) ***",
                color=0xffbd00,
                timestamp=datetime.datetime.utcnow()
            )
            await ctx.send(embed=embed1)
        embed1 = discord.Embed(
            title="**SUCCESS**",
            description=f"***:white_check_mark: *** {member.display_name} *** has been perm-banned for: `{reason}`!***",
            color=0x00fa00,
            timestamp=datetime.datetime.utcnow()
        )
        embed2 = discord.Embed(
            title="**NOTIFICATION**",
            description=f":bell: ***You have been perm-banned in **{ctx.guild}** for: `{reason}`***",
            color=0x0064ff,
            timestamp=datetime.datetime.utcnow()
        )
        embed2.add_field(name="**In case you would like to appeal your ban, go here:**", value=f"https://forms.gle/zs9vRAz5Fw1SFgvR6", inline=False)
        async with ctx.typing():
            try:
                await member.send(embed=embed2)
            except discord.Forbidden:
                pass
            await member.ban(reason=reason)
            await ctx.send(embed=embed1)

    @commands.command(aliases=['temp-ban'], description="This command is used for temporarily banning.")
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def tempban(self, ctx, member: discord.Member, *args):
        time = []
        time_fields = []

        possible_time = args[:2]

        available_options = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400, 'w': 604800}

        if member.id == ctx.me.id:
            embed1 = discord.Embed(
                title="**OOPS**",
                description=f"***Sorry bro, not gonna happen! :) ***",
                color=0xffbd00,
                timestamp=datetime.datetime.utcnow()
            )
            await ctx.send(embed=embed1)
        i = 0
        for arg in possible_time:
            if arg.endswith(available_options):
                try:
                    int(arg[:-1])
                    time.append(arg)
                    time_fields.append(i)
                    i = i + 1
                except ValueError:
                    break
            else:
                break

        args_list = list(args)

        for element in time_fields:
            args_list[element] = None

        reason = " ".join([i for i in args_list if i is not None])

        embed1 = discord.Embed(
            title="**SUCCESS**",
            description=f"***:white_check_mark: *** {member.display_name} *** has been temp-banned for: `{reason}`, for: {time}!***",
            color=0x00fa00,
            timestamp=datetime.datetime.utcnow()
        )
        embed2 = discord.Embed(
            title="**NOTIFICATION**",
            description=f":bell: ***You have been temp-banned in **{ctx.guild}** for: `{reason}`, for: {time}!***",
            color=0x0064ff,
            timestamp=datetime.datetime.utcnow()
        )
        embed2.add_field(name="**In case you would like to appeal your ban, go here:**", value=f"https://forms.gle/zs9vRAz5Fw1SFgvR6", inline=False)

        await ctx.send(embed=embed2)
        try:
            await member.send(embed=embed2)
        except Exception:
            pass
        await ctx.send(embed=embed1)
        await member.ban(reason=reason)

        parsed_time = await parse_time(time)

        if parsed_time != 0:
            await asyncio.sleep(parsed_time)
            await member.unban(reason=" ended.")

    @commands.command(aliases=['soft-ban'],
                      description="This command is used for banning and immediate unbanning, mostly used for clearing out user's messages.")
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def softban(self, ctx, member: discord.Member, *, reason=None):
        if member.id == ctx.me.id:
            embed1 = discord.Embed(
                title="**OOPS**",
                description=f"***Sorry bro, not gonna happen :) ***",
                color=0xffbd00,
                timestamp=datetime.datetime.utcnow()
            )
            await ctx.send(embed=embed1)
        embed1 = discord.Embed(
            title="**SUCCESS**",
            description=f"***:white_check_mark: *** {member.display_name} *** has been soft-banned for: `{reason}`!***",
            color=0x00fa00,
            timestamp=datetime.datetime.utcnow()
        )
        embed2 = discord.Embed(
            title="**NOTIFICATION**",
            description=f":bell: ***You have been soft-banned in **{ctx.guild}** for: `{reason}`!***",
            color=0x0064ff,
            timestamp=datetime.datetime.utcnow()
        )
        async with ctx.typing():
            try:
                await member.send(embed=embed2)
            except discord.Forbidden:
                pass
            await member.ban(reason=reason)
            await member.unban(reason=reason)
            await ctx.send(embed=embed1)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def unban(self, ctx, member, *, reason=None):
        ban_list = await ctx.guild.bans()
        for ban_entry in ban_list:
            user = ban_entry.user
            id = member
            embed1 = discord.Embed(
                title="**SUCCESS**",
                description=f"***:white_check_mark: *** {user.display_name} *** has been unbanned for: `{reason}`!***",
                color=0x00fa00,
                timestamp=datetime.datetime.utcnow()
            )
            try:
                user_name, user_discriminator = member.split('#')
            except ValueError:
                user_name = ''
                user_discriminator = ''
            pass

            try:
                int_id = int(id)
            except ValueError:
                int_id = None

            if (user.name, user.discriminator) == (user_name, user_discriminator) or int_id == user.id:
                await ctx.guild.unban(user, reason=reason)
                await ctx.send(embed=embed1)
                try:
                    embed2 = discord.Embed(
                        title="**NOTIFICATION**",
                        description=f":bell: ***You have been unbanned from {ctx.guild}, for: `{reason}`!***",
                        timestamp=datetime.datetime.utcnow()
                    )
                    await user.send(embed=embed2)
                except discord.Forbidden:
                    break

    @commands.command(alises=["av", "pfp"], description="Sends the provided user's, or the command caller's avatar.")
    async def avatar(self, ctx, *, user: discord.Member = None):
        user = user or ctx.author

        embed = discord.Embed(
            title=f"{user} AVATAR",
            timestamp=datetime.datetime.utcnow(),
            color=0x0064ff
        )

        embed.set_image(url=user.avatar_url)

        await ctx.channel.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def say(self, ctx, *, text, channel: discord.TextChannel):
        channel = channel or ctx.channel

        await ctx.message.delete()
        await channel.send(text)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def slowmode(self, ctx, time: int = 0, channel: discord.TextChannel = None):
        channel = channel or ctx.channel

        await channel.edit(slowmode_delay=time)

    @commands.group()
    async def add(self, ctx):
        staff_role = discord.utils.get(ctx.guild.roles, id=756565123350659385)
        if ctx.author in staff_role.members:
            pass
        else:
            return

    @add.command()
    @commands.has_permissions(manage_roles=True)
    async def role(self, ctx, member: discord.Member, *, role: discord.Role):
        if ctx.author.top_role < member.top_role:
            return

        if ctx.author.top_role == member.top_role:
            return

        await member.add_roles(role)
        embed = discord.Embed(
            title=f"**ROLE GIVEN**",
            description=f"✅ ***You have successfully given {role.mention} to {member.mention}!***",
            timestamp=datetime.datetime.utcnow(),
            color=0x3aff00
        )
        await ctx.send(embed=embed)

    @add.command()
    @commands.has_permissions(manage_channels=True)
    async def category(self, ctx, *, name):
        await ctx.guild.create_category(name, position=0)
        embed = discord.Embed(
            title=f"**CATEGORY CREATED**",
            description=f"✅ ***You have successfully created the `{name}` category!***",
            timestamp=datetime.datetime.utcnow(),
            color=0x3aff00
        )
        await ctx.send(embed=embed)

    @add.command()
    @commands.has_permissions(manage_channels=True)
    async def text_channel(self, ctx, category: discord.CategoryChannel = None, *, name):
        await ctx.guild.create_text_channel(name, category=category)
        embed = discord.Embed(
            title=f"**CHANNEL CREATED**",
            description=f"✅ ***You have successfully created the `{name}` channel!***",
            timestamp=datetime.datetime.utcnow(),
            color=0x3aff00
        )
        await ctx.send(embed=embed)

    @add.command()
    @commands.has_permissions(manage_channels=True)
    async def voice_channel(self, ctx, category: discord.CategoryChannel = None, *, name):
        await ctx.guild.create_voice_channel(name, category=category)
        embed = discord.Embed(
            title=f"**VOICE CHANNEL CREATED**",
            description=f"✅ ***You have successfully created the `{name}` channel!***",
            timestamp=datetime.datetime.utcnow(),
            color=0x3aff00
        )
        await ctx.send(embed=embed)

    @add.command()
    @commands.has_permissions(manage_emojis=True)
    async def emoji(self, ctx, image, *, name):
        await ctx.guild.create_custom_emoji(name, image=image)
        embed = discord.Embed(
            title=f"**EMOJI ADDED**",
            description=f"✅ ***You have successfully added the `{name}` emoji!***",
            timestamp=datetime.datetime.utcnow(),
            color=0x3aff00
        )
        await ctx.send(embed=embed)

    @commands.group(aliases=['rem'])
    async def remove(self, ctx):
        staff_role = discord.utils.get(ctx.guild.roles, id=756565123350659385)
        if ctx.author in staff_role.members:
            pass
        else:
            return

    @remove.command(name='role')
    @commands.has_permissions(manage_roles=True)
    async def rem_role(self, ctx, member: discord.Member, *, role: discord.Role):
        if ctx.author.top_role < member.top_role:
            return

        if ctx.author.top_role == member.top_role:
            return

        await member.remove_roles(role)
        embed = discord.Embed(
            title=f"**ROLE REMOVED**",
            description=f"✅ ***You have successfully removed the `{role}` role from `{member}`!***",
            timestamp=datetime.datetime.utcnow(),
            color=0x3aff00
        )
        await ctx.send(embed=embed)

    @remove.command(name="category")
    @commands.has_permissions(manage_channels=True)
    async def rem_category(self, ctx, *, category: discord.CategoryChannel):
        await category.delete()
        embed = discord.Embed(
            title=f"**CATEGORY DELETED**",
            description=f"✅ ***You have successfully deleted the `{category}` category!***",
            timestamp=datetime.datetime.utcnow(),
            color=0x3aff00
        )
        await ctx.send(embed=embed)

    @remove.command(name="text_channel")
    @commands.has_permissions(manage_channels=True)
    async def rem_text_channel(self, ctx, *, channel: discord.TextChannel):
        await channel.delete()
        embed = discord.Embed(
            title=f"**CHANNEL DELETED**",
            description=f"✅ ***You have successfully deleted the `{channel}` channel!***",
            timestamp=datetime.datetime.utcnow(),
            color=0x3aff00
        )
        await ctx.send(embed=embed)

    @remove.command(name="voice_channel")
    @commands.has_permissions(manage_channels=True)
    async def rem_voice_channel(self, ctx,  *, channel: discord.VoiceChannel):
        await channel.delete()
        embed = discord.Embed(
            title=f"**CHANNEL DELETED**",
            description=f"✅ ***You have successfully deleted the `{channel}` channel!***",
            timestamp=datetime.datetime.utcnow(),
            color=0x3aff00
        )
        await ctx.send(embed=embed)

    @remove.command(name="emoji")
    @commands.has_permissions(manage_emojis=True)
    async def rem_emoji(self, ctx, *, emoji: discord.Emoji):
        await emoji.delete()
        embed = discord.Embed(
            title=f"**EMOJI REMOVED**",
            description=f"✅ ***You have successfully removed the `{emoji}` emoji!***",
            timestamp=datetime.datetime.utcnow(),
            color=0x3aff00
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Moderation(bot))
