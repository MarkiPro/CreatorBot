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
import matplotlib.font_manager as fm


class Verification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def verify(self, ctx):
        verified_role = ctx.guild.get_role(695328817157373992)
        log_channel = ctx.guild.get_channel(745904248461590549)
        verification_channel = ctx.guild.get_channel(745331129535561758)

        if ctx.author in verified_role.members:
            return await ctx.send("You are already verified!")
        else:
            pass
        if ctx.channel != verification_channel:
            return await ctx.send("Please go to verify in <@#745331129535561758>, and if you need assistance, you should first read over <@#713020247543906368>!")
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

        width = 300
        height = 200
        opacity = 1
        text = code
        filename = f"result{text}.png"
        blue_background = (95, 104, 222)
        blue_text = (1, 5, 48)
        transparent = (0, 0, 0, 0)

        wm = Image.new('RGBA', (width, height))
        im = Image.new('RGBA', (width, height), blue_background)  # Change this line too.

        draw = ImageDraw.Draw(wm)
        w, h = draw.textsize(text)
        draw.text(((width - w)/2, (height - h)/2), text, blue_text)

        en = ImageEnhance.Brightness(wm)
        # en.putalpha(mask)
        mask = en.enhance(1 - opacity)
        im.paste(wm, (25, 25), mask)

        im.save(filename)

        await ctx.author.send(content="**Welcome to Content Creators**!\nPlease send the captcha code here, you have 16 minutes to do so.\nHello! You are required to complete a captcha before entering the server.\n*NOTE: This is **Case Sensitive***.\n**Why?**\nThis is to protect the server against targeted attacks using automated user accounts.\n**Your Captcha:**", file=discord.File(filename))

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
            await ctx.author.send("You ran out of time, please call the `>verify` command again in <#745331129535561758> and try again.")
            log_embed1 = discord.Embed(
                title="**Verification Failed**",
                description=f"Verification for {ctx.author.mention}({ctx.author})",
                color=0xff0000,
                timestamp=datetime.datetime.utcnow()
            )
            log_embed1.add_field(name="Looking for", value=f"{code}", inline=True)
            log_embed1.add_field(name="Given", value=f"{answer}", inline=True)
            log_embed1.add_field(name="Reason", value=f"Ran out of time!", inline=True)
            await log_channel.send(embed=log_embed1)
            os.remove(filename)
            return
        if answer == code:
            await ctx.author.send("You did the captcha correctly! Good job! You now have the verified role and full access to the server.")
            log_embed2 = discord.Embed(
                title="**Verification Success**",
                description=f"Verification for {ctx.author.mention}({ctx.author})",
                color=0x00fa00,
                timestamp=datetime.datetime.utcnow()
            )
            log_embed2.add_field(name="Looking for", value=f"{code}", inline=True)
            log_embed2.add_field(name="Given", value=f"{answer}", inline=True)
            await ctx.author.add_roles(verified_role)
            await log_channel.send(embed=log_embed2)
        elif answer != code:
            await ctx.author.send("You failed the captcha, please call the `>verify` command again in <#745331129535561758> and try again.")
            log_embed3 = discord.Embed(
                title="**Verification Failed**",
                description=f"Verification for {ctx.author.mention}({ctx.author})",
                color=0xff0000,
                timestamp=datetime.datetime.utcnow()
            )
            log_embed3.add_field(name="Looking for", value=f"{code}", inline=True)
            log_embed3.add_field(name="Given", value=f"{answer}", inline=True)
            log_embed3.add_field(name="Reason", value=f"Sent the wrong code!", inline=True)
            await log_channel.send(embed=log_embed3)
        os.remove(filename)


def setup(bot):
    bot.add_cog(Verification(bot))
