import discord
from discord.ext import commands
from minecraft import Server


class Rcon(commands.Cog):

    def __init__(self,client):
        self.client = client


    #Commands
    @commands.command()
    async def whitelist(self, ctx, player):
        ip = '46.4.13.165'
        port = 25567
        password = '@LdY%U430G8NVS8sqsJAR$z#m08763'

        server = Server(ip, port, password, connect_on_send=True)
        print(await server.send(f'whitelist add {player}'))

        await server.close()

    @commands.command()
    async def unwhitelist(self, ctx, player):
        ip = '46.4.13.165'
        port = 25567
        password = '@LdY%U430G8NVS8sqsJAR$z#m08763'

        server = Server(ip, port, password, connect_on_send=True)
        print(await server.send(f'whitelist add {player}'))

        await server.close()
    
    @commands.command()
    async def close(self, ctx):
        ip = '46.4.13.165'
        port = 25567
        password = '@LdY%U430G8NVS8sqsJAR$z#m08763'

        server = Server(ip, port, password, connect_on_send=True)

        await server.close()


def setup(client):
    client.add_cog(Rcon(client))