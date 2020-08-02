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
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def dog(self, ctx):
        try:
            message = await ctx.send("Generating a dog image for you!")
            embed = discord.Embed(title="A nice dog for you!", color=0xe700ff)
            async with aiohttp.ClientSession() as session:
                async with session.get('https://dog.ceo/api/breeds/image/random') as image:
                    res_json = await image.json()
                    embed.set_image(url=res_json['message'])
                    await ctx.send(embed=embed)
        except:
            return await ctx.send("There was an issue with loading the image.")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def cat(self, ctx):
        message = await ctx.send("Generating a cat image for you!")
        try:
            embed = discord.Embed(title="A nice cat for you!", color=0xe700ff)
            async with aiohttp.ClientSession() as ca:
                async with ca.get('https://api.thecatapi.com/v1/images/search') as c:
                    res2 = await c.json()
                    embed.set_image(url=res2[0]['url'])
                    await ctx.send(embed=embed)
        except:
            return await ctx.send("There was an issue with loading the image.")

def setup(client):
    client.add_cog(Fun(client))