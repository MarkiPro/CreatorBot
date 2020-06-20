import discord
from discord.ext import commands
import datetime

class Misc(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.client.help_command.cog = self

    @commands.command(aliases=['suggestion'], description="This command is used for suggesting useful ideas!")
    async def suggest(ctx):
        suggestionsChannel = client.get_channel(id=712655570737299567)
        startedEmbed = discord.Embed(
            title="**SUGGESTION SETUP**",
            description="Please continue the setup in dms.",
            color=0x0064ff,
            set_footer=f"{datetime.datetime.now(tz=None)} Reply to this message within `16 minutes`. Say `cancel` to cancel this prompt."
        )
        furstEmbed = discord.Embed(
            title="**SUGGESTION SETUP**",
            description="What would you like to name your suggestion?",
            color=0x0064ff,
            timestamp={datetime.datetime.now(tz=None)}
        )
        furstEmbed.set_footer(text=f"Reply to this message within `16 minutes`. Say `cancel` to cancel this prompt.")
        await ctx.send(embed=startedEmbed)
        await ctx.author.send(embed=furstEmbed)
        def check(m):
            if isinstance(m.channel, discord.DMChannel):
                if m.author == ctx.author:
                    return True
                else:
                    return False
            else:
                return False
        title_message = await client.wait_for('message', check=check, timeout=1000)
        title = title_message.content
        startEmbed = discord.Embed(
            title="**SUGGESTION SETUP**",
            description="Please write down your suggestion in detail.",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
        )
        startEmbed.set_footer(text=f"Reply to this message within `16 minutes`. Say `cancel` to cancel this prompt.")
        await ctx.author.send(embed=startEmbed)
        body_message = await client.wait_for('message', check=check, timeout=1000)
        body = body_message.content
        suggestedEmbed2 = discord.Embed(
            title=f"**FINISHED PRODUCT**",
            description=f"""*Say `done` to post.*""",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
        )
        suggestedEmbed2.set_footer(text=f"Reply to this message within `16 minutes`. Say `cancel` to cancel this prompt.")
        suggestedEmbed1 = discord.Embed(
            title=f"**{title}**",
            description=f"{body}",
            color=0x0064ff,
            timestamp=datetime.datetime.now(tz=None)
        )
        suggestedEmbed1.set_footer(text=f"by: {ctx.author}")
        await ctx.author.send(embed=suggestedEmbed2)
        await ctx.author.send(embed=suggestedEmbed1)
        body_message2 = await client.wait_for('message', check=check, timeout=1000)
        body2 = body_message2.content
        if(body2 == "done"):
            finalEmbed = discord.Embed(
                title="**SUGGESTION SETUP**",
                description="Your suggestion has been posted.",
                color=0x0064ff,
                timestamp=datetime.datetime.now(tz=None)
                )
            await ctx.author.send(embed=finalEmbed)
            suggestedEmbed = discord.Embed(
                title=f"**{title}**",
                description=f"{body}",
                color=0x0064ff,
                timestamp=datetime.datetime.now(tz=None)
                )
            suggestedEmbed.set_footer(text=f"by: {ctx.author}")
            sent = await suggestionsChannel.send(embed=suggestedEmbed)
            await sent.add_reaction('👍')
            await sent.add_reaction('👎')

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