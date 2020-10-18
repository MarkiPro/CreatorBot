from discord import Forbidden
from discord.ext.commands import Cog
from discord.ext.commands import command

class Log(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("log")

    @Cog.listener()
    async def on_member_join(member):
        message = discord.utils.get()

    @Cog.listener()
    async def on_member_remove(member):


def setup(bot):
    bot.add_cog(Log(bot))