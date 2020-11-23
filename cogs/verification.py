import discord
from discord.ext import commands
import random
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageEnhance
import os
import asyncio
import datetime

class Verification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def verify(self, ctx):
        verified_role = ctx.guild.get_role(695328817157373992)

        if ctx in verified_role.members:
            return ctx.send("You are already verified!")
        else:
            pass

        choice_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                       "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D",
                       "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
                       "Y", "Z"]

        choice1 = choice_list[random.randint(0, 61)]
        choice2 = choice_list[random.randint(0, 61)]
        choice3 = choice_list[random.randint(0, 61)]
        choice4 = choice_list[random.randint(0, 61)]
        choice5 = choice_list[random.randint(0, 61)]
        choice6 = choice_list[random.randint(0, 61)]
        choice7 = choice_list[random.randint(0, 61)]
        choice8 = choice_list[random.randint(0, 61)]
        choice9 = choice_list[random.randint(0, 61)]
        choice10 = choice_list[random.randint(0, 61)]

        code = (choice1 + choice2 + choice3 + choice4 + choice5 + choice6 + choice7 + choice8 + choice9 + choice10)

        width = 150
        height = 100
        opacity = 1
        text = code
        filename = f"result{text}.png"
        blue_background = (95, 104, 222)
        blue_text = (1, 5, 48)
        transparent = (0, 0, 0, 0)

        font = ImageFont.truetype('verdana.ttf', 15)
        wm = Image.new('RGBA', (width, height), transparent)
        im = Image.new('RGBA', (width, height), transparent)  # Change this line too.

        draw = ImageDraw.Draw(wm)
        w, h = draw.textsize(text, font)
        draw.text(((width - w) / 2, (height - h) / 2), text, blue_text, font)

        en = ImageEnhance.Brightness(wm)
        # en.putalpha(mask)
        mask = en.enhance(1 - opacity)
        im.paste(wm, (25, 25), mask)

        im.save(filename)

        await ctx.send(content="**Welcome to Content Creators**!\nPlease send the captcha code here, you have 16 minutes to do so.\nHello! You are required to complete a captcha before entering the server.\n*NOTE: This is **Case Sensitive***.\n**Why?**\nThis is to protect the server against targeted attacks using automated user accounts.\n**Your Captcha:**", file=discord.File(filename))

        def check_dm(m):
            if isinstance(m.channel, discord.DMChannel):
                if m.author == ctx.author:
                    return True
                else:
                    return False
            else:
                return False
        try:
            answer_message = await self.bot.wait_for('message', check=check_dm, timeout=1000)
            answer = answer_message.content
        except asyncio.TimeoutError:
            return await ctx.author.send("You ran out of time, please call the `>verify` command again in <#745331129535561758> and try again.")
        if answer == code:
            await ctx.author.send("You did the captcha correctly! Good job! You now have the verified role and full access to the server.")
        elif answer != code:
            await ctx.author.send("You failed the captcha, please call the `>verify` command again in <#745331129535561758> and try again.")

        os.remove(filename)


def setup(bot):
    bot.add_cog(Verification(bot))
