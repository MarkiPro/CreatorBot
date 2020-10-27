import discord
from discord.ext.commands import Cog
from discord.ext.commands import command
import datetime


class Log(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_message_delete(self, before, after):
        if not after.author.bot:
            pass

    @Cog.listener()
    async def on_message_edit(self, before, after):
        channel = self.bot.get_channel(767416354700918814)
        message = await channel.fetch_message(767422159270182922)
        log_channel = self.bot.get_channel(712624826463813753)

        if not after.author.bot:
            log_embed = discord.Embed(
                title="**Message Edit**",
                description=f"{before.author} Edited The Message",
                timestamp=datetime.datetime.utcnow()
            )
            log_embed.add_field(name="**Before**", value=f"{before.content}", inline=True)
            log_embed.add_field(name="**After**", value=f"{after.content}", inline=True)
            await log_channel.send(embed=log_embed)

    @Cog.listener()
    async def on_member_update(self, before, after):
        sum_channel = self.bot.get_channel(767416354700918814)
        message = await sum_channel.fetch_message(767422159270182922)
        guild = sum_channel.guild
        booster_role = discord.utils.get(guild.roles, id=762172204628181023)
        exculded_roles = [611227128020598805, 707957214995808296, 732375953203789965, 743590325448212651, 743013370588037191, 732388199107657828, 743013368511594569, 743013366515236915, 743013366880272474, 743013367840768072, 743013368134107166, 732387788493946881, 732402691296198848, 734149969292034208, 734150445764837466, 734150696944795698, 735497751978311681, 734527020905529375, 734664303327838230, 734527130565738516, 735557139984285706, 738814580712669214, 734664243038912552, 734527217350082672, 734527854871707762, 746758563703291938]
        before_roles = ", ".join(role.mention for role in before.roles if role.id not in exculded_roles) or "No roles assigned."
        after_roles = ", ".join(role.mention for role in after.roles if role.id not in exculded_roles) or "No roles assigned."
        role_update_log_channel = self.bot.get_channel(770368850679169075)

        if booster_role in before.roles and booster_role not in after.roles:
            await message.edit(
                content=f"""Currently, there are a total of **{guild.member_count}** Members in this server,
                **{guild.premium_subscription_count}** Boosters,
                Boosting Level for this server is currently **{guild.premium_tier}**.""")

        log_embed = discord.Embed(
            title="Role Update",
            description=f"Role Update for {before}",
            timestamp=datetime.datetime.utcnow()
        )
        log_embed.add_field(name="**Before**", value=f"{before_roles}", inline=True)
        log_embed.add_field(name="**After**", value=f"{after_roles}", inline=True)
        await role_update_log_channel.send(embed=log_embed)

    @Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(767416354700918814)
        message = await channel.fetch_message(767422159270182922)
        guild = channel.guild



        await message.edit(content=f"""Currently, there are a total of **{guild.member_count}** Members in this server,
            **{guild.premium_subscription_count}** Boosters,
            Boosting Level for this server is currently **{guild.premium_tier}**.""")

    @Cog.listener()
    async def on_member_remove(self, ember):
        channel = self.bot.get_channel(767416354700918814)
        message = await channel.fetch_message(767422159270182922)
        guild = channel.guild

        await message.edit(content=f"""Currently, there are a total of **{guild.member_count}** Members in this server,
            **{guild.premium_subscription_count}** Boosters,
            Boosting Level for this server is currently **{guild.premium_tier}**.""")


def setup(bot):
    bot.add_cog(Log(bot))
