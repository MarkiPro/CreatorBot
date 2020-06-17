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
    async def Magic8Ball(self, ctx, *, question):
        random_answers = ['Is Einstein bold? I think not!', 'Can we time travel? Science says yes!', 'Ahh, maybe.', 'That is a yes.', 'Nah, I am good', 'I would love to, but unfortunately... no.', 'The idea is not compatible with myself.', 'I think I will go find a lake of piranhas to jump in instead.', 'My schedule is packed with better things', 'There are worse things I could agree to, I just cannot think of any at the moment.', 'There are many cool things to do. ***Your idea does not fall into such a category.***', 'You\’re not giving me that much of a choice, huh?', 'Then, let’s seal it with a kiss.', 'Just be sure to pay me back later.', 'Just be sure that we won’t get caught.', 'Life\’s too short to be saying no.', 'Who put you up to this? Tell me!', 'Kiss my butt first.', 'Have you forgotten? I’m a yes-man!', 'Thought you\’d never ask!', 'Hell, you bet-cha, matey!', 'I\’ll even kiss you!', 'Even my dog is saying yes.', 'Let\’s say I agreed to this. But, can I still change my mind later?', 'My answer would probably be yes, but I totally forgot—I have another appointment!', 'You should know my answer by the way I\’m nodding my head up and down.', 'Just be sure that we won\’t go to jail for this.', 'If I say yes, will you give me a million bucks?', 'Abso-f*kin-lutely!', 'Preach!', 'What are we waiting for? Let\’s close the deal!', 'Probably yes, but I\’ll have my people call your people to discuss.', 'Well then, what are we waiting for?', 'There\’s a chance that I might regret this, but—YOLO—let\’s do it!', 'Even if I hate you, I would say yes to this one.', 'Say no more!', 'It would take a whole army to keep me from saying yes.', 'Right on the money!', 'Yes, yes, and yes!', 'If there\’s a reward, I\’m in!', 'Hallelujah!', 'You get my vote.', 'I\’m here to the rescue!', 'It\’s fine now. Why? Because I\’m here!', 'I love you, so yeah.', 'I don\’t have a choice, do I?', 'Let me check my schedule first. Oh, I\’m available.', 'Take off your clothes because you\’ve hit the spot!', 'Why, that\'s the nicest offer I\'ve had all day!', 'Give me a \‘ **Y**.\’ Give me an \‘ **E**.\’ Give me an \‘ **S**.\’ Give me a \‘ **Y-E-S!**\’', 'May-be!', 'Do aliens even exist? Maybe!', '**M**y **A**rt **Y**ikes **B**asketball **E**ar!', 'I.... don\'t know! 😢']

        await ctx.send(random.choice(random_answers))


def setup(client):
    client.add_cog(Fun(client))