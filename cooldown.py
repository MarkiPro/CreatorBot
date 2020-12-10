import datetime
import discord


class Cooldown:
    def __init__(self, time, message_count=None):
        self.cooldown_start_time = time
        self.message_count = message_count
        self.muteable_offence = 0

    async def time_it(self, user, message=None, channel=None, mute_role=None):
        current_time = datetime.datetime.utcnow()

        if self.muteable_offence >= 3:
            await user.add_roles(mute_role)
            self.muteable_offence = 0

        if message and channel:
            self.message_count += 1
            time_difference = (current_time - self.cooldown_start_time).total_seconds()
            if time_difference < 5 < self.message_count:
                await user.send(f"{user.mention} you've sent over 5 messages in under 2.5 seconds!")
                log_embed = discord.Embed(
                    title="**Message Spam**",
                    description=f"*{user.mention} **`({user})`** has just sent over 5 messages in under 2.5 seconds in {message.channel.mention}!*",
                    timestamp=datetime.datetime.utcnow(),
                    color=0x0064ff
                )

                try:
                    log_embed.set_thumbnail(url=user.avatar_url)
                except:
                    pass
                await channel.send(embed=log_embed)
                self.message_count = 0
                self.muteable_offence += 1
            elif self.message_count > 5 and not time_difference < 2.5:
                self.message_count = 0
        else:
            pass

        if not message:
            time_difference = (current_time - self.cooldown_start_time).total_seconds()
            if time_difference < 3600:
                await user.send("You are on cooldown for this category which lasts for 1 hour!")
