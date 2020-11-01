import discord
from discord.ext import commands
from mctools import RCONClient


class Rcon(commands.Cog):

    def __init__(self,client):
        self.client = client


    #Commands
    @commands.command()
    async def whitelist(self, ctx):
        HOST = '46.4.13.165'
        PORT = 25567

        rcon = RCONClient(HOST, port=PORT)
        if rcon.login('@LdY%U430G8NVS8sqsJAR$z#m08763'):
            rcon.command(f'whitelist add {ctx}')
            await ctx.say(f'Added {ctx} to the whitelist.')

    @commands.command()
    async def unwhitelist(self, ctx):
        HOST = '46.4.13.165'
        PORT = 25567

        rcon = RCONClient(HOST, port=PORT)
        if rcon.login('@LdY%U430G8NVS8sqsJAR$z#m08763'):
            rcon.command(f'whitelist add {ctx}')
            await ctx.say(f'Removed {ctx} from the whitelist.')


def setup(client):
    client.add_cog(Rcon(client))