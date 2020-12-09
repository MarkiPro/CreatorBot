import datetime
import asyncio


class Cooldown:
    def __init__(self, time):
        self.cooldown_start_time = time

    async def time_it(self, user, message=None):
        current_time = datetime.datetime.utcnow()

        if message:
            time_difference = (current_time - self.cooldown_start_time).total_seconds()
            if time_difference < 0.25:
                system_message = await message.channel.send(f"{user.mention}, you are sending messages too quickly!")
                await message.delete()
                await asyncio.sleep(10)
                await system_message.delete()
        else:
            pass

        time_difference = (current_time - self.cooldown_start_time).total_seconds()
        if time_difference < 3600:
            await user.send("You are on cooldown for this category which lasts for 1 hour!")
