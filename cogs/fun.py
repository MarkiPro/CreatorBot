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

    @commands.command()
    async def cat(self, ctx):
        await ctx.send("Generating a cat image for you!")
        request = requests.get("https://api.thecatapi.com/v1/images/search", params={'limit': 1})
        data = request.json()
        request.close()
        embed = discord.Embed(title=f"A nice cat, for you!", colour=discord.Color.blurple())
        embed.set_image(url=data[0]['url'])
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Fun(client))