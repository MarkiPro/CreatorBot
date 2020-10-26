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
        if not after.author.bot:
            pass

    @Cog.listener()
    async def on_member_update(self, before, after):
        channel = self.bot.get_channel(767416354700918814)
        message = await channel.fetch_message(767422159270182922)
        guild = channel.guild
        booster_role = discord.utils.get(guild.roles, id=762172204628181023)
        before_roles = ", ".join([i.mention for i in before.roles if i.name != '@everyone' or i.name != '­@­━━­━━━━ SKILLS ­━━­━━━━' or i.name != '­@━━━━━ ATTAINMENTS ━━━━­' or i.name != '@­━━━━━   ESTABLISHED  ━━━━­']) or "No roles assigned."
        after_roles = ", ".join([i.mention for i in after.roles if i.name != '@everyone' or i.name != '­@­━━­━━━━ SKILLS ­━━­━━━━' or i.name != '­@━━━━━ ATTAINMENTS ━━━━­' or i.name != '@­━━━━━   ESTABLISHED  ━━━━­']) or "No roles assigned."
        role_update_log_channel = self.bot.get_channel(712761099401035799)

        if before_roles != after_roles:
            log_embed = discord.Embed(
                title="Role Update",
                description=f"Role Update for {before}",
                timestamp=datetime.datetime.utcnow()
            )
            log_embed.add_field(name="**Before**", value=f"{before_roles}", inline=True)
            log_embed.add_field(name="**After**", value=f"{after_roles}", inline=True)
            await role_update_log_channel.send(embed=log_embed)

        if booster_role in before.roles and booster_role not in after.roles:
            await message.edit(content=f"""Currently, there are a total of **{guild.member_count}** Members in this server,
                **{guild.premium_subscription_count}** Boosters,
                Boosting Level for this server is currently **{guild.premium_tier}**.""")



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