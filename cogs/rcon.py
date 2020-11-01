import discord
from discord.ext import commands
from mcrcon import MCRcon


class Rcon(commands.Cog):

    def __init__(self,client):
        self.client = client


    #Commands
    @commands.command()
    async def whitelist(self, ctx):
        mcr = MCRcon('46.4.13.165:25567', '@LdY%U430G8NVS8sqsJAR$z\#m08763')
        mcr.connect()
        wh = mcr.command(f'/whitelist add {ctx}')
        print(wh)
        mcr.disconnect

        await ctx.send(f'Added {ctx} to the whitelist.')

    @commands.command()
    async def unwhitelist(self, ctx):
        mcr = MCRcon('46.4.13.165:25567', '@LdY%U430G8NVS8sqsJAR$z\#m08763')
        mcr.connect()
        unwh = mcr.command(f'/whitelist remove {ctx}')
        print(unwh)
        mcr.disconnect

        await ctx.send(f'Removed {ctx} to the whitelist.')


def setup(client):
    client.add_cog(Rcon(client))