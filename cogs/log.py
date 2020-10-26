import discord
from discord import Embed
from discord.ext.commands import Cog
from discord.ext.commands import command

class Log(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @Cog.listener()
    async def on_ready(self):
        self.bot.cogs_ready.ready_up("log")

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
        pass

    @Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(767416354700918814)
        message = channel.fetch_message(767422159270182922)
        guild = channel.guild

        await message.edit(content=f"Currently, there are a total **{guild.member_count}** Members in this server!!!")

    @Cog.listener()
    async def on_member_remove(self, ember):
        channel = self.bot.get_channel(767416354700918814)
        message = channel.fetch_message(767422159270182922)
        guild = channel.guild

        await message.edit(content=f"Currently, there are a total **{guild.member_count}** Members in this server!!!")

def setup(bot):
    bot.add_cog(Log(bot))