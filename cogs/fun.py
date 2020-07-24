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
        message1 = await ctx.send("Generating a dog image for you!")
        embed = discord.Embed(title="A nice dog for you!", color=0xe700ff)
        async with aiohttp.ClientSession() as do:
            async with do.get('https://dog.ceo/api/breeds/image/random') as d:
                res1 = await d.json()
                embed.set_image(url=res1['data'])
                await ctx.send(embed=embed)
                print(res1)

    @commands.command()
    async def cat(self, ctx):
        message = await ctx.send("Generating a cat image for you!")
        embed = discord.Embed(title="A nice cat for you!", color=0xe700ff)
        async with aiohttp.ClientSession() as ca:
            async with ca.get('https://api.thecatapi.com/v1/images/search') as c:
                res2 = await c.json()
                embed.set_image(url=res2[0]['url'])
                await ctx.send(embed=embed)
                print(res2)

def setup(client):
    client.add_cog(Fun(client))