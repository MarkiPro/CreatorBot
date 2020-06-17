import discord
from discord.ext import commands
import mysql.connector
import datetime
import re

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def clear(self, ctx, amount=0):
        limit = 2000

        if amount > limit:
            if ctx.author.id == 438333007036678155:
                return await ctx.send("NO MARKI ARE YOU IDIOT")
            return await ctx.send(f"Sorry, the limit is {limit}")

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
    async def ban(self, ctx, member: discord.Member, *, reason=None):
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
            description=f"***:white_check_mark: *** {member.display_name} *** has been banned for: `{reason}`!***",
            color=0x00fa00,
            timestamp=datetime.datetime.now(tz=None)
        )
        embed2 = discord.Embed(
            title="**NOTIFICATION**",
            description=f":bell: *You have been banned in **{ctx.guild}** for:* `{reason}`!",
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
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def warn(self, ctx, member: discord.Member, *, reason):
        if member.id == 466591581286170624:
            return await ctx.send("Sorry bro, not gonna happen :D")
        connection = mysql.connector.connect(
            host="us-cdbr-east-06.cleardb.net",
            user="baba29035f4254",
            passwd="8a63c86d",
            database="heroku_daa9f1b493ff319"
        )
        cursor = connection.cursor()
        cursor.execute("INSERT INTO warns VALUES (%s, %s, %s, %s, %s)",
                       (None, ctx.guild.id, member.id, reason, ctx.author.id))
        connection.commit()
        embed1 = discord.Embed(
            title="**SUCCESS**",
            description=f":white_check_mark: ***{member} has been warned!***",
            color=0x00fa00,
            timestamp=datetime.datetime.now(tz=None)
        )
        await ctx.send(embed=embed1)

    @commands.command()
    async def warnings(self, ctx, member: discord.Member):
        connection = mysql.connector.connect(
            host="us-cdbr-east-06.cleardb.net",
            user="baba29035f4254",
            passwd="8a63c86d",
            database="heroku_daa9f1b493ff319"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM warns WHERE user_id = %s AND guild_id = %s", (member.id, ctx.guild.id))
        warns = cursor.fetchall()
        embed = discord.Embed(title=f"Warnings of {member}".upper(), description="Returns all the warns of a user")
        member_converter = commands.MemberConverter()
        for warn in warns:
            moderator = await member_converter.convert(ctx, warn[4])
            embed.add_field(name=f"Warning #{warn[0]} by {moderator}", value=f"{warn[3]}", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def removewarn(self, ctx, *, id):
        connection = mysql.connector.connect(
            host="us-cdbr-east-06.cleardb.net",
            user="baba29035f4254",
            passwd="8a63c86d",
            database="heroku_daa9f1b493ff319"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM warns WHERE id = %s", (int(id),))
        warn = cursor.fetchone()

        if warn == None:
            embed3 = discord.Embed(
                title="**ERROR**",
                description=f"""***:no_entry_sign: This warn doesn't exist!***""",
                color=0xff0000,
                timestamp=datetime.datetime.now(tz=None)
            )
            return await ctx.send(embed=embed3)
        if int(warn[1]) != ctx.guild.id:
            embed4 = discord.Embed(
                title="**ERROR**",
                description=f"""***:no_entry_sign: This warn doesn't exist in this guild!***""",
                color=0xff0000,
                timestamp=datetime.datetime.now(tz=None)
            )
            return await ctx.send(embed=embed4)

        cursor.execute("DELETE FROM warns WHERE id = %s", (int(id),))
        connection.commit()
        embed1 = discord.Embed(
            title="**SUCCESS**",
            description=f":white_check_mark: ***Removed warning #{id}***",
            color=0x00fa00,
            timestamp=datetime.datetime.now(tz=None)
        )
        await ctx.send(embed=embed1)

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

    @commands.command()
    @commands.bot_has_permissions(administrator=True, manage_guild=True)
    async def prefix(self, ctx, *, prefix):
        connection = mysql.connector.connect(
            host="us-cdbr-east-06.cleardb.net",
            user="baba29035f4254",
            passwd="8a63c86d",
            database="heroku_daa9f1b493ff319"
        )

        cursor = connection.cursor()

        cursor.execute("UPDATE guilds SET prefix = %s WHERE guild_id = %s", (prefix, ctx.guild.id))

        connection.commit()

        await ctx.send(f"Changed prefix of this server to `{prefix}`")


def setup(client):
    client.add_cog(Moderation(client))