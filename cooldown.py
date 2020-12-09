import datetime


class Cooldown:
    def __init__(self, time):
        self.cooldown_start_time = datetime.datetime.utcfromtimestamp(time)

    async def time_it(self, user):
        current_time = datetime.datetime.utcnow()

        time_difference = (current_time - self.cooldown_start_time).total_seconds()
        if time_difference < 3600:
            await user.send("You are on cooldown for this category which lasts for 1 hour!")
