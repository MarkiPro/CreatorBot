import discord
from discord.ext import commands
import datetime
import pbwrap

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.api_key = 'a69d904fff567bd3f6de8e146ec1e60e'

def setup(client):
    client.add_cog(Help(client))