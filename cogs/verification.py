import discord
from discord.ext import commands
import random
from PIL import Image, ImageDraw, ImageFont
import os
import asyncio
import datetime
import string
import robloxpy
import aiohttp


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
            return await ctx.send(
                "Please go to verify in <@#745331129535561758>, and if you need assistance, you should first read over <@#713020247543906368>!")
        else:
            pass

        getit = lambda: (random.randrange(5, 295), random.randrange(5, 95))

        color = (200, 200, 200)
        shadow_color = (0, 0, 0)

        def random_string():
            N = 8
            s = string.ascii_uppercase + string.ascii_lowercase + string.digits
            random_string = ''.join(random.choices(s, k=N))
            return random_string

        captcha_str = random_string()
        file_name = f"{ctx.message.id}.png"

        img = Image.new('RGB', (300, 100), color=(95, 104, 222))
        draw = ImageDraw.Draw(img)

        text_color = color
        font = "langar.ttf"
        font_name = f'fonts/{font}'
        font = ImageFont.truetype(font=font_name, size=50)
        w, h = draw.textsize(captcha_str, font)
        draw.text(((300 - w) / 2 + 5, (100 - h) / 2 + 5), captcha_str, fill=shadow_color, font=font)
        draw.text(((300 - w) / 2, (100 - h) / 2), captcha_str, fill=text_color, font=font)

        for i in range(5, random.randrange(10, 20)):
            start = (0, (100 - random.randrange(0, 101)))
            end = (300, (100 - random.randrange(0, 101)))
            draw.line((start, end), fill=shadow_color, width=2)

        for i in range(50, random.randrange(100, 300)):
            draw.point((random.randrange(0, 300), random.randrange(0, 100)), fill=color)

        img.save(file_name)

        f = discord.File(file_name, filename=file_name)

        verif_embed = discord.Embed(
            title="**Welcome to Content Creators**",
            description="Please send the captcha code here, you have 5 minutes to do so.\n\nHello! You are required to complete a captcha before entering the server.\n\n*NOTE: This is **Case Sensitive***.\n\n**Why?**\nThis is to protect the server against targeted attacks using automated user accounts.\n\n**Your Captcha:**",
            timestamp=datetime.datetime.utcnow(),
            color=0x0064ff
        )

        verif_embed.set_image(url=f"attachment://{file_name}")

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
            answer_message = await self.bot.wait_for('message', check=check_dm, timeout=300)
            answer = answer_message.content
            if answer == captcha_str:
                await ctx.author.send(
                    "You did the captcha correctly! Good job! You now have the verified role and full access to the server.")
                log_embed2 = discord.Embed(
                    title="**Verification Success**",
                    description=f"Verification for {ctx.author.mention}({ctx.author})",
                    color=0x00fa00,
                    timestamp=datetime.datetime.utcnow()
                )
                log_embed2.add_field(name="Looking for", value=f"{captcha_str}", inline=True)
                log_embed2.add_field(name="Given", value=f"{answer}", inline=True)
                await ctx.author.add_roles(verified_role)
                await log_channel.send(embed=log_embed2)
            elif answer != captcha_str:
                await ctx.author.send(
                    "You failed the captcha, please run the `>verify` command again in <#745331129535561758> and try again.")
                log_embed3 = discord.Embed(
                    title="**Verification Failed**",
                    description=f"Verification for {ctx.author.mention}({ctx.author})",
                    color=0xff0000,
                    timestamp=datetime.datetime.utcnow()
                )
                log_embed3.add_field(name="Looking for", value=f"{captcha_str}", inline=True)
                log_embed3.add_field(name="Given", value=f"{answer}", inline=True)
                log_embed3.add_field(name="Reason", value=f"Sent the wrong code!", inline=True)
                await log_channel.send(embed=log_embed3)
        except asyncio.TimeoutError:
            await ctx.author.send(
                "You ran out of time, please run the `>verify` command again in <#745331129535561758> and try again.")
            log_embed1 = discord.Embed(
                title="**Verification Failed**",
                description=f"Verification for {ctx.author.mention}({ctx.author})",
                color=0xff0000,
                timestamp=datetime.datetime.utcnow()
            )
            log_embed1.add_field(name="Looking for", value=f"{captcha_str}", inline=True)
            log_embed1.add_field(name="Reason", value=f"Ran out of time!", inline=True)
            await log_channel.send(embed=log_embed1)
        os.remove(file_name)

    @commands.command()
    async def rblx_verify(self, ctx):
        command_caller = ctx.author
        call_embed = discord.Embed(
            title="**Welcome to Content Creators**",
            description="Please respond in under 5 minutes!\n\nHello, please respond with your Roblox Username!\n\n*NOTE: This is **Case Sensitive!***",
            timestamp=datetime.datetime.utcnow(),
            color=0x0064ff
        )
        await command_caller.send(embed=call_embed)

        def check_dm(m):
            if isinstance(m.channel, discord.DMChannel):
                if m.author == ctx.author:
                    return True
                else:
                    return False
            else:
                return False

        try:
            roblox_name_message = await self.bot.wait_for('message', check=check_dm, timeout=300)
            roblox_name = roblox_name_message.content
        except asyncio.TimeoutError:
            await ctx.author.send("You ran out of time, please run the `>rblx_verify` command again in <#741733794536751114> and try again.")
        if robloxpy.DoesNameExist(roblox_name):

            user = robloxpy.GetUserInfo
            N = 30
            s = string.ascii_uppercase + string.ascii_lowercase + string.digits
            code = ''.join(random.choices(s, k=N))
            code_embed = discord.Embed(
                title="**Welcome to Content Creators**",
                description=f"Please respond in under 5 minutes!\n\nHello, please copy the given code, and paste it in your Roblox Bio/Description, and once you're done, respond with `done`!\n\n*NOTE: This is **Case Sensitive!***\n\n\n**Your Code:***\n**{code}**",
                timestamp=datetime.datetime.utcnow(),
                color=0x0064ff
            )
            await command_caller.send(embed=code_embed)
            try:
                roblox_desc_message = await self.bot.wait_for('message', check=check_dm, timeout=300)
                roblox_desc = roblox_desc_message.content
            except asyncio.TimeoutError:
                await ctx.author.send(
                    "You ran out of time, please run the `>rblx_verify` command again in <#741733794536751114> and try again.")
            if str(roblox_desc).lower() == "done" or str(roblox_desc).lower() == "yes" or str(roblox_desc).lower() == "ok":
                pass
            else:
                return await ctx.send("Prompt Cancelled. Reason: User hadn't responded appropriately.")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get('https://users.roblox.com/v1/users/1239087921/') as user:
                    user_desc = await user.json()
                    print(user_desc)
                    print(user_desc['description'])

        except:
            return await ctx.send("Could not find the description!")


def setup(bot):
    bot.add_cog(Verification(bot))
