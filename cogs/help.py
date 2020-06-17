import discord
from discord.ext import commands
import mysql.connector
import datetime
import pbwrap

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.api_key = 'a69d904fff567bd3f6de8e146ec1e60e'

    @commands.command(description="NOT YET WORKING")
    @commands.has_any_role('Helper', 'Trial Mod', 'Head Admin', 'Admin', 'Mod')
    async def addtag(self, ctx):
        connection = mysql.connector.connect(
            host="us-cdbr-east-06.cleardb.net",
            user="baba29035f4254",
            passwd="8a63c86d",
            database="heroku_daa9f1b493ff319"
        )

        cursor = connection.cursor()

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.member)
    async def codeformat(self, ctx):
        code_block_embed = discord.Embed(
            title=f"**CODEBLOCK**",
            description=f"Continue this in dms.",
            color=0x0064ff,
            timestamp=datetime.datetime.utcnow()
        )
        await ctx.send(embed=code_block_embed)

        code_block_embed_2 = discord.Embed(
            title=f"**CODEBLOCK**",
            description=f"Is your code long or short? If it's longer and you can't post it, say `pastebin`, and if it's shorter, say `codeblock`.",
            color=0x0064ff,
            timestamp=datetime.datetime.utcnow()
        )
        code_block_embed_2.set_footer(
            text=f"Reply to this message within `16 minutes`. Say `cancel` to cancel this prompt.")

        await ctx.author.send(embed=code_block_embed_2)

        options = ['codeblock', 'pastebin']

        def check(m):
            if isinstance(m.channel, discord.DMChannel):
                if m.author == ctx.author:
                    return True
                else:
                    return False
            else:
                return False

        code_category_message = await self.client.wait_for('message', check=check, timeout=960)
        code_category = code_category_message.content

        is_valid = False

        for option in options:
            if code_category == 'cancel':
                return await ctx.author.send("Cancelled.")

            if option == code_category:
                is_valid = True

        if not is_valid:
            return await ctx.author.send("Category invalid.")

        if code_category == 'codeblock':

            code_block_embed_3 = discord.Embed(title='**CODEBLOCK**',
                                               description="Please send the code you want to be formatted.")

            await ctx.author.send(embed=code_block_embed_3)

            code_message = await self.client.wait_for('message', check=check, timeout=960)
            code = code_message.content

            formatted_code = f'\\```lua\n{code}```'

            return await ctx.author.send(f"Here is your formatted code!\n{formatted_code}")

        elif code_category == 'pastebin':

            code_block_embed_3 = discord.Embed(title='**CODEBLOCK**',
                                               description="Please send the link of your pastebin (If your link is pastebin.com/12313, then only send 12313")

            await ctx.author.send(embed=code_block_embed_3)

            code_message = await self.client.wait_for('message', check=check, timeout=960)
            code = code_message.content

            pastebin = pbwrap.Pastebin(api_dev_key=self.api_key)
            paste_text = pastebin.get_raw_paste(f"{code}")
            formatted_code = f"```lua\n{paste_text}```"
            new_paste = pastebin.create_paste(formatted_code)
            await ctx.author.send(f"I have created a new paste for you. Check it out here: {new_paste}")


def setup(client):
    client.add_cog(Help(client))