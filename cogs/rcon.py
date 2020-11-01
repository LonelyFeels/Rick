import discord
from discord.ext import commands
from minecraft import Server


class Rcon(commands.Cog):

    def __init__(self,client):
        self.client = client


    #Commands
    @commands.command()
    async def whitelist(self, ctx):
        ip = '46.4.13.165'
        port = 25567
        password = '@LdY%U430G8NVS8sqsJAR$z#m08763'

        server = Server(ip, port, password, connect_on_send=True)
        print(await server.send(f'whitelist add {ctx}'))

        await Server.close(self)

    @commands.command()
    async def unwhitelist(self, ctx):
        ip = '46.4.13.165'
        port = 25567
        password = '@LdY%U430G8NVS8sqsJAR$z#m08763'

        server = Server(ip, port, password, connect_on_send=True)
        print(await server.send(f'whitelist add {ctx}'))

        await Server.close(self)


def setup(client):
    client.add_cog(Rcon(client))