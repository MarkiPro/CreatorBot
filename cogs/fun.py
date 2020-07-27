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

    @tasks.loop(seconds=3600)
    async def send_meme(ctx: commands.Context):
        try:
            channel = client.get_channel(id=712625666490761297)
            embed = discord.Embed(title="A nice meme for you!", color=0xe700ff)
            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                    res = await r.json()
                    embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                    await channel.send(embed=embed)
        except:
            return await channel.send("There was an issue with loading the meme.")

    @commands.command()
    @command.has_permissions(manage_messages=True)
    @command.cooldown(1, 3600, commands.BucketType.member)
    async def meme_config(ctx):
        send_meme.start(ctx=ctx)

def setup(client):
    client.add_cog(Fun(client))