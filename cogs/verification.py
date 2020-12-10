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
                       "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        choice1 = choice_list[random.randint(0, 36)]
        rand_choice1 = random.randint(1, 2)
        if rand_choice1 == 1:
            choice1.lower()
        elif rand_choice1 == 2:
            choice1.upper()
        choice2 = choice_list[random.randint(0, 36)]
        rand_choice2 = random.randint(1, 2)
        if rand_choice2 == 1:
            choice2.lower()
        elif rand_choice2 == 2:
            choice2.upper()
        choice3 = choice_list[random.randint(0, 36)]
        rand_choice3 = random.randint(1, 2)
        if rand_choice3 == 1:
            choice3.lower()
        elif rand_choice3 == 2:
            choice3.upper()
        choice4 = choice_list[random.randint(0, 36)]
        rand_choice4 = random.randint(1, 2)
        if rand_choice4 == 1:
            choice4.lower()
        elif rand_choice4 == 2:
            choice4.upper()
        choice5 = choice_list[random.randint(0, 36)]
        rand_choice5 = random.randint(1, 2)
        if rand_choice5 == 1:
            choice5.lower()
        elif rand_choice5 == 2:
            choice5.upper()
        choice6 = choice_list[random.randint(0, 36)]
        rand_choice6 = random.randint(1, 2)
        if rand_choice6 == 1:
            choice6.lower()
        elif rand_choice6 == 2:
            choice6.upper()
        choice7 = choice_list[random.randint(0, 36)]
        rand_choice7 = random.randint(1, 2)
        if rand_choice7 == 1:
            choice7.lower()
        elif rand_choice7 == 2:
            choice7.upper()
        choice8 = choice_list[random.randint(0, 36)]
        rand_choice8 = random.randint(1, 2)
        if rand_choice8 == 1:
            choice8.lower()
        elif rand_choice8 == 2:
            choice8.upper()
        choice9 = choice_list[random.randint(0, 36)]
        rand_choice9 = random.randint(1, 2)
        if rand_choice9 == 1:
            choice9.lower()
        elif rand_choice9 == 2:
            choice9.upper()
        choice10 = choice_list[random.randint(0, 36)]
        rand_choice10 = random.randint(1, 2)
        if rand_choice10 == 1:
            choice10.lower()
        elif rand_choice10 == 2:
            choice10.upper()

        code = (choice1 + choice2 + choice3 + choice4 + choice5 + choice6 + choice7 + choice8 + choice9 + choice10)

        width = 300
        height = 100
        opacity = 1
        text = code
        filename = f"result{text}.png"
        blue_background = (95, 104, 222)
        blue_text = (1, 5, 48)
        # transparent = (0, 0, 0, 0)

        font = ImageFont.truetype(fm.findfont(fm.FontProperties(family='Computer Modern')), 25)
        wm = Image.new('RGBA', (width, height))
        im = Image.new('RGBA', (width, height), blue_background)

        draw = ImageDraw.Draw(im)
        w, h = draw.textsize(text, font)
        draw.text(((width - w)/2, (height - h)/2), text, blue_text, font)

        en = ImageEnhance.Brightness(wm)
        # en.putalpha(mask)
        mask = en.enhance(1 - opacity)
        im.paste(wm, (25, 25), mask)

        im.save(filename)

        f = discord.File(filename, filename=filename)

        verif_embed = discord.Embed(
            title="**Welcome to Content Creators**",
            description="Please send the captcha code here, you have 16 minutes to do so.\n\nHello! You are required to complete a captcha before entering the server.\n\n*NOTE: This is **Case Sensitive***.\n\n**Why?**\nThis is to protect the server against targeted attacks using automated user accounts.\n\n**Your Captcha:**",
            timestamp=datetime.datetime.utcnow(),
            color=0x0064ff
        )

        verif_embed.set_image(url=f"attachment://{filename}")

        await ctx.author.send(embed=verif_embed, file=f)

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
        except asyncio.TimeoutError:
            await ctx.author.send("You ran out of time, please call the `>verify` command again in <#745331129535561758> and try again.")
            log_embed1 = discord.Embed(
                title="**Verification Failed**",
                description=f"Verification for {ctx.author.mention}({ctx.author})",
                color=0xff0000,
                timestamp=datetime.datetime.utcnow()
            )
            log_embed1.add_field(name="Looking for", value=f"{code}", inline=True)
            log_embed1.add_field(name="Reason", value=f"Ran out of time!", inline=True)
            await log_channel.send(embed=log_embed1)
        os.remove(filename)


def setup(bot):
    bot.add_cog(Verification(bot))
