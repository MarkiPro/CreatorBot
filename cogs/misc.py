import discord
from discord.ext import commands
import datetime

class Misc(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.client.help_command.cog = self


    @commands.command(description="This command is simply going to define the creators of this bot",
                      aliases=['cr'])
    @commands.cooldown(1, 60, commands.BucketType.member)
    async def credits(self, ctx):
        user_converter = commands.UserConverter()
        credit_users = {'malware': await user_converter.convert(ctx, "466591581286170624"),
                        'markipro': await user_converter.convert(ctx, "438333007036678155"),
                        'leaf': await user_converter.convert(ctx, "527945767059718154"),
                        'rama': await user_converter.convert(ctx, "561592624562044948")}

        credits_embed = discord.Embed(
            title=f"**CREDITS**",
            description=f"""
                Scripting: **{credit_users['malware'].mention}**

                Designing: **{credit_users['markipro'].mention}**

                GFX: **{credit_users['rama'].mention}**

                Special Thanks to:
                **{credit_users['leaf'].mention}**
                for helping beta test the bot!""",
            color=0x0064ff,
            timestamp=datetime.datetime.utcnow()
        )
        await ctx.send(embed=credits_embed)

    @commands.command(aliases=['who'],
                    description="Displays basic information about the supplied user. If the user is not provided, it would default to the command requester.")
    async def whois(self, ctx, user: discord.Member = None):
        if not user:
            user = ctx.message.author

        embed = discord.Embed(title=f"**Who is {user.name}**".upper(),
                              description="Displays basic information about the given user", colour=0xd9ac32)
        embed.set_author(name=f"{ctx.message.author}", icon_url=ctx.message.author.avatar_url)
        format = "%A, %d %B, %Y : %I:%M %p"
        delta_joined = datetime.datetime.utcnow() - user.joined_at
        delta_created = datetime.datetime.utcnow() - user.created_at
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="Joined on", value=f"{user.joined_at.strftime(format)} ({delta_joined.days} days)",
                        inline=True)
        embed.add_field(name="Account created on",
                        value=f"{user.created_at.strftime(format)} ({delta_created.days} days)", inline=True)
        embed.add_field(name="Nickname", value=f"{user.nick}", inline=True)
        roles = ", ".join([i.mention for i in user.roles if i.name != '@everyone']) or "No roles assigned."
        embed.add_field(name="Guild Roles", value=f"{roles}", inline=False)
        perms = ", ".join(list(i[0].title() for i in user.guild_permissions if i[1] == True)) or "No permissions in the guild."
        embed.add_field(name="Guild Permissions",
                        value=f"{perms}",
                        inline=False)
        await ctx.send(embed=embed)

    @commands.command(description="This command will remember MarkiPro, the original creator of the bot.")
    async def markipro(self, ctx):
        embed = discord.Embed(
            title="MarkiPro",
            description="We all know who you are, and what you did. We all know that you were an amazing mod, amazing friend, and an amazing programmer. We will always miss you, Marki...",
            color=0x0064ff,
            timestamp=datetime.datetime.utcnow()
        )

        await ctx.send(embed=embed)

    @commands.command(description="Invite link for RoDevs")
    async def rodevs(self, ctx):
        return await ctx.send("https://discord.gg/rodevs")

    @commands.command()
    async def boosters(self, ctx):

        boosters = "\n".join([i.mention for i in ctx.guild.premium_subscribers])

        embed = discord.Embed(
            title="**BOOSTERS**",
            description=f"***These are the boosters on the server:\n\n***{boosters}",
            color=0x0089ff,
            timestamp=datetime.datetime.utcnow()
            )

        if boosters is "":
            embed.description = "There are no boosters in this guild  :cry:"

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Misc(client))