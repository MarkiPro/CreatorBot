import discord
from discord.ext import commands
import datetime
import re
import asyncio

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def clear(self, ctx, amount=None):
        await ctx.channel.purge(limit=amount + 1)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if member.id == ctx.me.id:
            embed1 = discord.Embed(
                title="**OOPS**",
                description=f"***Sorry bro, not gonna happen :) ***",
                color=0xffbd00,
                timestamp=datetime.datetime.now(tz=None)
            )
            await ctx.send(embed=embed1)
        embed1 = discord.Embed(
            title="**SUCCESS**",
            description=f"***:white_check_mark: *** {member.display_name} *** has been kicked for: `{reason}`!***",
            color=0x00fa00,
            timestamp=datetime.datetime.now(tz=None)
        )
        embed2 = discord.Embed(
            title="**NOTIFICATION**",
            description=f":bell: *You have been kicked in **{ctx.guild}** for:* `{reason}`!",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
        )
        async with ctx.typing():
            await member.send(embed=embed2)
            await member.kick(reason=reason)
            await ctx.send(embed=embed1)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def permban(self, ctx, member: discord.Member, *, reason=None):
        if member.id == ctx.me.id:
            embed1 = discord.Embed(
                title="**OOPS**",
                description=f"***Sorry bro, not gonna happen :) ***",
                color=0xffbd00,
                timestamp=datetime.datetime.now(tz=None)
            )
            await ctx.send(embed=embed1)
        embed1 = discord.Embed(
            title="**SUCCESS**",
            description=f"***:white_check_mark: *** {member.display_name} *** has been perm-banned for: `{reason}`!***",
            color=0x00fa00,
            timestamp=datetime.datetime.now(tz=None)
        )
        embed2 = discord.Embed(
            title="**NOTIFICATION**",
            description=f":bell: *You have been perm-banned in **{ctx.guild}** for: `{reason}`*",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
        )
        async with ctx.typing():
            await member.ban(reason=reason)
            await ctx.send(embed=embed1)
            await member.send(embed=embed2)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def tempban(self, ctx, member: discord.Member, *args):
        time = []
        time_fields = []

        possible_time = args[:2]

        if member.id == ctx.me.id:
            embed1 = discord.Embed(
                title="**OOPS**",
                description=f"***Sorry bro, not gonna happen :) ***",
                color=0xffbd00,
                timestamp=datetime.datetime.now(tz=None)
            )
            await ctx.send(embed=embed1)
        embed1 = discord.Embed(
            title="**SUCCESS**",
            description=f"***:white_check_mark: *** {member.display_name} *** has been temp-banned for: `{reason}`, for: {time}!***",
            color=0x00fa00,
            timestamp=datetime.datetime.now(tz=None)
        )
        embed2 = discord.Embed(
            title="**NOTIFICATION**",
            description=f":bell: *You have been temp-banned in **{ctx.guild}** for: `{reason}`, for: {time}!*",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
        )

        available_options = ['s' , 'm', 'h', 'd', 'w']

        async with ctx.typing():
            await member.ban(reason=reason)
            await ctx.send(embed=embed1)
            await member.send(embed=embed2):
            await asyncio.sleep(time)
            await member.unban(reason=reason)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def softban(self, ctx, member: discord.Member, *, reason=None):
        if member.id == ctx.me.id:
            embed1 = discord.Embed(
                title="**OOPS**",
                description=f"***Sorry bro, not gonna happen :) ***",
                color=0xffbd00,
                timestamp=datetime.datetime.now(tz=None)
            )
            await ctx.send(embed=embed1)
        embed1 = discord.Embed(
            title="**SUCCESS**",
            description=f"***:white_check_mark: *** {member.display_name} *** has been soft-banned for: `{reason}`!***",
            color=0x00fa00,
            timestamp=datetime.datetime.now(tz=None)
        )
        embed2 = discord.Embed(
            title="**NOTIFICATION**",
            description=f":bell: *You have been soft-banned in **{ctx.guild}** for: `{reason}`!*",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
        )
        async with ctx.typing():
            await member.ban(reason=reason)
            await ctx.send(embed=embed1)
            await member.unban(reason=reason)
            await member.send(embed=embed2)

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
                timestamp=datetime.datetime.now(tz=None)
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
                break

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def say(self, ctx, *, text):
        await ctx.message.delete()
        await ctx.send(text)

    @commands.group()
    @commands.has_permissions(manage_roles=True)
    async def add(self, ctx):
        pass

    @add.command()
    async def role(self, ctx, member: discord.Member, *, role: discord.Role):
        if ctx.author.top_role < member.top_role:
            return

        if ctx.author.top_role == member.top_role:
            return

        await member.add_roles(role)
        embed = discord.Embed(
            title=f"**ROLE GIVEN**",
            description=f"✅ ***You have successfully given `{role}` to `{member}`!***",
            timestamp=datetime.datetime.utcnow(),
            color=0x3aff00
        )
        await ctx.send(embed=embed)

    @add.command()
    async def text_channel(self, ctx, category: discord.CategoryChannel = None, *, name):
        await ctx.guild.create_text_channel(name, category=category)
        embed = discord.Embed(
            title=f"**CHANNEL CREATED**",
            description=f"✅ ***You have successfully created `{name}` channel!***",
            timestamp=datetime.datetime.utcnow(),
            color=0x3aff00
        )
        await ctx.send(embed=embed)

    @add.command()
    async def voice_channel(self, ctx, category: discord.CategoryChannel = None, *, name):
        await ctx.guild.create_voice_channel(name, category=category)
        embed = discord.Embed(
            title=f"**VOICE CHANNEL CREATED**",
            description=f"✅ ***You have successfully created `{name}` channel!***",
            timestamp=datetime.datetime.utcnow(),
            color=0x3aff00
        )
        await ctx.send(embed=embed)

    @commands.group(aliases=['rem'])
    async def remove(self, ctx):
        pass

    @remove.command(name='role')
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

    @remove.command(name="text_channel")
    async def rem_text_channel(self, ctx, channel: discord.TextChannel, *, reason=None):
        await channel.delete(reason=reason)
        embed = discord.Embed(
            title=f"**CHANNEL DELETED**",
            description=f"✅ ***You have successfully deleted the `{channel}` channel!***",
            timestamp=datetime.datetime.utcnow(),
            color=0x3aff00
        )
        await ctx.send(embed=embed)

    @remove.command(name="voice_channel")
    async def rem_voice_channel(self, ctx, channel: discord.VoiceChannel, *, reason=None):
        await channel.delete(reason=reason)
        embed = discord.Embed(
            title=f"**CHANNEL DELETED**",
            description=f"✅ ***You have successfully deleted the `{channel}` channel!***",
            timestamp=datetime.datetime.utcnow(),
            color=0x3aff00
        )
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Moderation(client))