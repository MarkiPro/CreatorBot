import discord
from discord.ext import commands
#from discord.ext import buttons


#class ReactionsPaginator(buttons.Paginator):
 #   def __init__(self, *args, **kwargs) -> None:
  #      super().__init__(*args, **kwargs)

class TextSplitter:
    def __init__(self, char_per_page, text):
        self.char_per_page = char_per_page
        self.words_list = []
        self.text = text

    async def make_text(self):
        n = self.char_per_page
        self.words_list = [self.text[i:i + n] for i in range(0, len(self.text), n)]


class EmbedDescriptionSplitter(TextSplitter):
    def __init__(self, embed: discord.Embed, description, char_per_page=1000) -> None:
        super().__init__(char_per_page=char_per_page, text=description)
        self.embed = embed

    async def send(self, ctx):
        await super().make_text()
        for entry in self.words_list:
            prepared_embed = self.embed

            prepared_embed.description = entry

            await ctx.send(embed=prepared_embed)
