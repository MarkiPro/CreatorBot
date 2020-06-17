import discord
from discord.ext import commands
import requests
import json
import random

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dog(self, ctx):
        message = await ctx.send("Generating a dog image for you!")
        request = requests.get('https://dog.ceo/api/breeds/image/random')
        data = request.json()
        request.close()
        embed = discord.Embed(title=f"A nice dog, for you!", colour=discord.Color.blurple())
        embed.set_image(url=data['message'])
        await ctx.send(embed=embed)
        await message.edit("Here is a dog image for you")

    @commands.command()
    async def cat(self, ctx):
        await ctx.send("Generating a cat image for you!")
        request = requests.get("https://api.thecatapi.com/v1/images/search", params={'limit': 1})
        data = request.json()
        request.close()
        embed = discord.Embed(title=f"A nice cat, for you!", colour=discord.Color.blurple())
        embed.set_image(url=data[0]['url'])
        await ctx.send(embed=embed)


    @commands.command()
    async def mushroom(self, ctx, member: discord.Member, *, reason):
        await ctx.send(f"{member.mention} has been mushroomed for `{reason}`")

        def check(m):
            if m.author.id == member.id:
                return True
            else:
                return False

        message = await self.client.wait_for('message', check=check)

        await message.add_reaction(":timthemushroom:716208401675452437")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def bean(self, ctx, member: discord.Member, *, reason=None):

        await ctx.send(f"{member} were beaned for `{reason}`")

        await member.send("https://tenor.com/EQmg.gif")

        def check(m):
            if m.author == member:
                return True
            else:
                return False


        message = await self.client.wait_for("message", check=check)

        await message.add_reaction(":bean:721246373957074984")

    @commands.command(name="8ball")
    async def ball(self, ctx, *, question):
        random_answers = ['yes', 'no', 'maybe']

        await ctx.send(random.choice(random_answers))


def setup(client):
    client.add_cog(Fun(client))