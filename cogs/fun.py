import random

import aiohttp
import discord
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def dog(self, ctx):
        try:
            await ctx.send("Generating a dog image for you!")
            embed = discord.Embed(title="A nice dog for you!", color=0xe700ff)
            async with aiohttp.ClientSession() as session:
                async with session.get('https://dog.ceo/api/breeds/image/random') as image:
                    res_json = await image.json()
                    embed.set_image(url=res_json['message'])
                    await ctx.send(embed=embed)
        except:
            return await ctx.send("There was an issue with loading the image.")

    @commands.command()
    async def print(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://devforum.roblox.com/u/markipr0.json') as j:
                res_j = await j.json()
                trust_level = res_j['trust_level']
                print(trust_level)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def cat(self, ctx):
        await ctx.send("Generating a cat image for you!")
        try:
            embed = discord.Embed(title="A nice cat for you!", color=0xe700ff)
            async with aiohttp.ClientSession() as ca:
                async with ca.get('https://api.thecatapi.com/v1/images/search') as c:
                    res2 = await c.json()
                    embed.set_image(url=res2[0]['url'])
                    await ctx.send(embed=embed)
        except:
            return await ctx.send("There was an issue with loading the image.")

    @commands.command(pass_context=True)
    async def meme(self, ctx):
        await ctx.send("Generating a meme for you!")
        try:
            embed = discord.Embed(title="A funny meme for you!", color=0xe700ff)

            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                    res = await r.json()
                    embed.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
                    await ctx.send(embed=embed)
        except:
            return await ctx.send("There was an issue with loading the image.")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def rps(self, ctx, *, choice):

        choice = choice.lower()

        choices = {"rock": {
            "loose": ["scissors"],
        }, "paper": {
            "loose": ['rock']
        }, "scissors": {
            "loose": ['paper']
        }, "marki": {
            "loose": ['rock', 'paper', 'scissors']
        }}

        options = [i for i in choices.keys()]

        if choice not in options:
            return await ctx.send("Please use a valid choice")

        bot_choice = random.choice([i for i in choices.keys() if i != "marki"])

        if f"{choice}" == bot_choice:
            return await ctx.send(f"I chose {bot_choice}\nIt is a draw.")

        if f"{choice}" in choices[bot_choice]['loose']:
            return await ctx.send(f"I chose {bot_choice}\nI won!")
        else:
            return await ctx.send(f"I chose {bot_choice}\nYou won!")

    @commands.command()
    async def rate(self, ctx, user: discord.User = None):
        markipro = await ctx.bot.fetch_user(530461779768377357)
        if user is None or user.id == ctx.author.id:
            await ctx.send(f"In my eyes, you're a **{random.randint(0, 10)}/10**! :eyes:")
        elif user == self.bot.user:
            await ctx.send("Well, obviously, I'm a **10/10**! :wink: :wink:")
        elif user == markipro:
            await ctx.send("He's my creator!!! If I don't say he's a **10/10** which he is, I'm a goner! :eyes:")
        else:
            await ctx.send(f"I see them as a solid **{random.randint(0, 10)}/10**! :eyes:")

    @commands.command()
    async def spellout(self, ctx, *, msg: str):
        await ctx.send(" ".join(list(msg.upper())))
        await ctx.send("Duh!")

    @commands.command()
    async def reverse(self, ctx, *, msg: str):
        await ctx.send(msg[::-1])

    @commands.command()
    async def randomnumber(self, ctx, *, digits: int = 1):
        number = ""
        if digits > 250:
            return await ctx.send("Cannot go higher than 250, as it slows the bot down when it is too high!")
        for i in range(digits):
            number += str(random.randint(0, 9))
        await ctx.send(number)

    @commands.command()
    async def rolldice(self, ctx):
        await ctx.send(f"You rolled a {random.randint(1, 6)}!")

    @commands.command()
    async def fortune(self, ctx):
        fortunes = ["You are not meant to live any more, begone thot!", "Your life is short, therefore use it wisely!", "Seems like your children will hate you... hope you're not expecting any!", "Someone is looking up to you. Don't let that person down.", "RUN!!!", "No snowflake in an avalanche ever feels responsible", "If you eat something, and nobody sees you eat it, it has no calories!", "Your heart will skip a beat!", "A new romance is in the future!", "Ignore the previous fortune. You did this to yourself!", "You will marry a professional athlete - if competitive eating can be considered a sport.", "You don't have to be faster than the bear, you just have to be faster than the slowest guy running from it.", "You look pretty!", "In youth and beauty, wisdom is rare.", "Enjoy yourself while you can.", "You are not illiterate.", "If you think we're going to sum up your whole life here, you're crazy!", "I see money in your future... it is not yours though.", "Three can keep a secret, if you get rid of two.", "Death.", "Avoid taking unnecessary gambles. Lucky Numbers: 12, 14, 17, 20, 28, 36", "This fortune is never gonna give you up, never gonna let you down.", "You laugh now, wait till you get home."]
        await ctx.send(f"```{random.choice(fortunes)}```")

    @commands.command(name="8ball", alises=['8ball'])
    async def askbot(self, ctx):
        random_choices = ["Yes!", "Yessir!", "No!", "No sir!", "Nope, but that's dope!", "Ew! Ew! Ew! What is going through your mind?!", "I would love to, but unfortunately... no.", "I believe there's someone a lot stupider who would enjoy doing that instead", "Such a task is no match for my incompetency", "Maybe!", "Maybeh!", "Yeah well, sorry to let you down, but no.", "Perhaps another time...", "Why, Heavens, no.", "Has Hell frozen over? Then, sure.", "Frankly my dear, no.", "I think not.", "My advisors have come to an unanimous decision of **\"NO\"** on that.", "I would... but I'm a bot.", "Give me a \"Y\"! Give me an \"E\"! Give me an \"S\"! GIVE ME A \"YES\"!!!", "Sure thing, bud.", "Better luck next time!", "Yeah... no... I'm out man!", "Perhaps another time.", "Too busy! Try your luck next time around!", "Okie dokie!", "Hell no!", "wHaT tHe AcTuAl HeCk?", "I mean... sure.", "What would **your mom** say to that?", "What about your family?", "Alright well... you do you!", "Ehhhh.....", "Sounds good!", "Seems like a plan!", "Glad to be a part of it!", "I'll trust you on this one.", "Ya ya ya ya ya!", "Took you long enough to ask!", "Good God, I was getting impatient!", "Mmmm... alright sure."]
        await ctx.send(f"{random.choice(random_choices)}")


def setup(bot):
    bot.add_cog(Fun(bot))
