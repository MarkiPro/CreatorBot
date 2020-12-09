import datetime
import discord


class Paginator:
    def __init__(self, text, char_per_page):
        self.text = text
        self.char_per_page = char_per_page
        self.messages = []

    def paginate(self):
        n = self.char_per_page
        self.words_list = [self.text[i:i + n] for i in range(0, len(self.text), n)]

    async def send(self, bot, channel, end_channel=None, member=None, title=None, role=None, mute_role=None, autoreport=None):
        self.paginate()
        for i, entry in enumerate(self.words_list):
            prepared_embed = discord.Embed(description=entry, color=0x0064ff)

            if i == 0:
                prepared_embed.title = f"{title}"
                prepared_embed.set_thumbnail(url=member.avatar_url)
            if (i + 1) == len(self.words_list):
                prepared_embed.timestamp = datetime.datetime.utcnow()

            prepared_embed.set_footer(text=f"Page {i + 1}/{len(self.words_list)}")

            message = await channel.send(embed=prepared_embed)

            self.messages.append(message)

            if (i + 1) == len(self.words_list):
                await message.add_reaction("👍")
                await message.add_reaction("👎")

                if autoreport:
                    def check(reaction1, user1):
                        return user1 and str(reaction1.emoji) in ["👍", "👎"]

                    reaction1, user1 = await bot.wait_for("reaction_add", check=check)

                    if str(user1) == str(bot.user):
                        def check(reaction2, user2):
                            return user2 and str(reaction2.emoji) in ["👍", "👎"]

                        reaction2, user2 = await bot.wait_for("reaction_add", check=check)

                        if str(reaction2.emoji) == "👍":
                            for _, msgs in enumerate(self.messages):
                                await msgs.delete()
                                await member.send(
                                    "The action taken against you was claimed to be the right thing, and soon enough, you will recieve your punishment!")
                                return

                        elif str(reaction2.emoji) == "👎":
                            for _, msgs in enumerate(self.messages):
                                await msgs.delete()
                                await member.send(
                                    "The action was claimed to be mistaken, and without further punishments, you may continue on with your day!")
                                return
                    else:
                        if str(reaction1.emoji) == "👍":
                            for _, msgs in enumerate(self.messages):
                                await msgs.delete()
                                await member.send(
                                    "The action taken against you was claimed to be the right thing, and soon enough, you will recieve your punishment!")
                                return

                        elif str(reaction1.emoji) == "👎":
                            for _, msgs in enumerate(self.messages):
                                await msgs.delete()
                                await member.send(
                                    "The action was claimed to be mistaken, and without further punishments, you may continue on with your day!")
                                return


                if role and not autoreport:
                    await message.add_reaction("🔇")
                    def check(reaction1, user1):
                        return user1 and str(reaction1.emoji) in ["👍", "👎", "🔇"]

                    reaction1, user1 = await bot.wait_for("reaction_add", check=check)

                    if str(user1) == str(bot.user):
                        def check(reaction2, user2):
                            return user2 and str(reaction2.emoji) in ["👍", "👎", "🔇"]

                        reaction2, user2 = await bot.wait_for("reaction_add", check=check)
                        if str(reaction2.emoji) == "👍":
                            for _, msgs in enumerate(self.messages):
                                await msgs.delete()
                                await member.send("Your application has been approved!")
                                await member.add_roles(role)
                                return

                        elif str(reaction2.emoji) == "👎":
                            for _, msgs in enumerate(self.messages):
                                await msgs.delete()
                                await member.send("Your application has been declined!")
                                return
                        elif str(reaction2.emoji) == "🔇":
                            for _, msgs in enumerate(self.messages):
                                await msgs.delete()
                                await member.send("Your application has been denied and you have been muted!")
                                await member.add_roles(mute_role)
                                return
                    else:
                        if str(reaction1.emoji) == "👍":
                            for _, msgs in enumerate(self.messages):
                                await msgs.delete()
                                await member.send("Your application has been approved!")
                                await member.add_roles(role)
                                return

                        elif str(reaction1.emoji) == "👎":
                            for _, msgs in enumerate(self.messages):
                                await msgs.delete()
                                await member.send("Your application has been declined!")
                                return
                        elif str(reaction2.emoji) == "🔇":
                            for _, msgs in enumerate(self.messages):
                                await msgs.delete()
                                await member.send("Your application has been denied and you have been muted!")
                                await member.add_roles(mute_role)
                                return
                    return

                if not end_channel and mute_role is not None and not autoreport:
                    await message.add_reaction("🔇")
                    def check(reaction1, user1):
                        return user1 and str(reaction1.emoji) in ["👍", "👎", "🔇"]

                    reaction1, user1 = await bot.wait_for("reaction_add", check=check)

                    if str(user1) == str(bot.user):
                        def check(reaction2, user2):
                            return user2 and str(reaction2.emoji) in ["👍", "👎", "🔇"]

                        reaction2, user2 = await bot.wait_for("reaction_add", check=check)
                        if str(reaction2.emoji) == "👍":
                            for _, msgs in enumerate(self.messages):
                                await msgs.delete()
                                await member.send("Your report has been approved!")
                                return

                        elif str(reaction2.emoji) == "👎":
                            for _, msgs in enumerate(self.messages):
                                await msgs.delete()
                                await member.send("Your report has been declined!")
                                return
                        elif str(reaction2.emoji) == "🔇":
                            for _, msgs in enumerate(self.messages):
                                await msgs.delete()
                                await member.send("Your report has been denied and you have been muted!")
                                await member.add_roles(mute_role)
                                return
                    else:
                        if str(reaction1.emoji) == "👍":
                            for _, msgs in enumerate(self.messages):
                                await end_channel.send(embed=msgs.embeds[0])
                                await msgs.delete()
                                await member.send("Your post has been approved!")
                                return
                        elif str(reaction1.emoji) == "👎":
                            for _, msgs in enumerate(self.messages):
                                await msgs.delete()
                                await member.send("Your post has been declined!")
                                return
                        elif str(reaction2.emoji) == "🔇":
                            for _, msgs in enumerate(self.messages):
                                await msgs.delete()
                                await member.send("Your report has been denied and you have been muted!")
                                await member.add_roles(mute_role)
                                return
                    return
                if end_channel and not autoreport:
                    await message.add_reaction("🔇")
                    def check(reaction1, user1):
                        return user1 and str(reaction1.emoji) in ["👍", "👎", "🔇"]

                    reaction1, user1 = await bot.wait_for("reaction_add", check=check)

                    if str(user1) == str(bot.user):
                        def check(reaction2, user2):
                            return user2 and str(reaction2.emoji) in ["👍", "👎", "🔇"]

                        reaction2, user2 = await bot.wait_for("reaction_add", check=check)
                        if str(reaction2.emoji) == "👍":
                            for _, msgs in enumerate(self.messages):
                                await end_channel.send(embed=msgs.embeds[0])
                                await msgs.delete()
                                await member.send("Your post has been approved!")
                                return

                        elif str(reaction2.emoji) == "👎":
                            for _, msgs in enumerate(self.messages):
                                await msgs.delete()
                                await member.send("Your post has been declined!")
                                return
                        elif str(reaction2.emoji) == "🔇":
                            for _, msgs in enumerate(self.messages):
                                await msgs.delete()
                                await member.send("Your post has been denied and you have been muted!")
                                await member.add_roles(mute_role)
                                return
                    else:
                        if str(reaction1.emoji) == "👍":
                            for _, msgs in enumerate(self.messages):
                                await end_channel.send(embed=msgs.embeds[0])
                                await msgs.delete()
                                await member.send("Your post has been approved!")
                                return

                        elif str(reaction1.emoji) == "👎":
                            for _, msgs in enumerate(self.messages):
                                await msgs.delete()
                                await member.send("Your post has been declined!")
                                return
                        elif str(reaction2.emoji) == "🔇":
                            for _, msgs in enumerate(self.messages):
                                await msgs.delete()
                                await member.send("Your post has been denied and you have been muted!")
                                await member.add_roles(mute_role)
                                return
