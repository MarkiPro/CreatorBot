import discord
from discord.ext import commands, tasks
import aiohttp
import json
import random
import asyncio

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dog(self, ctx):
        message = await ctx.send("Generating a dog image for you!")
        embed = discord.Embed(title="A nice dog for you!", color=0xe700ff)
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://dog.ceo/api/breeds/image/random') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)

    @commands.command()
    async def cat(self, ctx):
        message = await ctx.send("Generating a cat image for you!")
        embed = discord.Embed(title="A nice dog for you!", color=0xe700ff)
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://api.thecatapi.com/v1/images/search') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Fun(client))