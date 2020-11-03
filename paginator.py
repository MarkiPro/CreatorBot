import datetime

import discord


# from discord.ext import buttons


# class ReactionsPaginator(buttons.Paginator):
#    def __init__(self, *args, **kwargs) -> None:
#        super().__init__(*args, **kwargs)

# class TextSplitter:
#    def __init__(self, char_per_page, text):
#       self.char_per_page = char_per_page
#        self.words_list = []
#        self.text = text

#    async def make_text(self):
#        n = self.char_per_page
#        self.words_list = [self.text[i:i + n] for i in range(0, len(self.text), n)]


# class EmbedDescriptionSplitter(TextSplitter):
#    def __init__(self, embed: discord.Embed, description, char_per_page=1000) -> None:
#        super().__init__(char_per_page=char_per_page, text=description)
#        self.embed = embed
#
#    async def send(self, ctx):
#        await super().make_text()
#        for entry in self.words_list:
#            prepared_embed = self.embed

#            prepared_embed.description = entry

#            await ctx.send(embed=prepared_embed)
class Paginator:
    def __init__(self, text, char_per_page):
        self.text = text
        self.char_per_page = char_per_page
        self.messages = []

    def paginate(self):
        n = self.char_per_page
        self.words_list = [self.text[i:i + n] for i in range(0, len(self.text), n)]

    async def send(self, bot, channel, end_channel):
        self.paginate()
        for i, entry in enumerate(self.words_list):
            prepared_embed = discord.Embed(description=entry, color=0x0064ff)

            if i == 0:
                prepared_embed.title = "**Post**"
            if (i + 1) == len(self.words_list):
                prepared_embed.timestamp = datetime.datetime.utcnow()

            prepared_embed.set_footer(text=f"Page {i + 1}/{len(self.words_list)}")

            message = await channel.send(embed=prepared_embed)

            self.messages.append(message)

            if (i + 1) == len(self.words_list):
                await message.add_reaction("👍")
                await message.add_reaction("👎")

                def check(reaction, user):
                    return user == message.author and str(reaction.emoji) in ["👍", "👎"]

                reaction, user = await bot.wait_for("reaction_add", check=check)

                if str(reaction.emoji) == "👍":
                    reaction = discord.utils.get(message.reactions, emoji=reaction.emoji)
                    if reaction.count >= 2:
                        for v, ok in enumerate(self.messages):
                            await end_channel.send(ok)
                            await ok.delete()

                elif str(reaction.emoji) == "👎":
                    reaction = discord.utils.get(message.reactions, emoji=reaction.emoji)
                    if reaction.count >= 2:
                        for v, ok in enumerate(self.messages):
                            await ok.delete()