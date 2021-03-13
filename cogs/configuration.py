import discord
from discord.ext import commands
import json


class Configuration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def add_config(self, ctx):
        bot_config_role = discord.utils.get(ctx.guild.roles, id=820246057991929878)
        if ctx.author in bot_config_role.members:
            pass
        else:
            return

    @add_config.command()
    async def banned_link(self, ctx, *, link):
        with open("configs/banned.json") as reader:
            banned_stuff = json.load(reader)
            banned_links = banned_stuff["banned_links"]

            added_link = str(link)

            if added_link not in banned_links:
                banned_links.append(added_link)
                with open("configs/banned.json", "w") as writer:
                    json.dump(banned_stuff, writer)
                await ctx.send("Listed the link!")
            else:
                return await ctx.send("That link is already listed!")

    @add_config.command()
    async def banned_word(self, ctx, *, word):
        with open("configs/banned.json", "r") as reader:
            banned_stuff = json.load(reader)
            banned_words = banned_stuff["banned_words"]

            added_word = str(word)

            random_list = {
                "blah": {},
                "blah again" : []
            }

            if added_word not in banned_words:
                banned_words.append(added_word)
                with open("configs/banned.json", "w") as writer:
                    json.dump(random_list, writer)
                await ctx.send("Listed the word!")
            else:
                return await ctx.send("That word is already listed!")


def setup(bot):
    bot.add_cog(Configuration(bot))
