import discord
from discord.ext import commands
import aiohttp

class Serverstatus:
        @classmethod
        async def new(cls):
            async with aiohttp.ClientSession() as session:
                async with session.get('https://api.mcsrvstat.us/1/148.251.236.239:25565') as resp:
                    data = await resp.json()
                    players_list = data['players'].get('list') if 'list' in data['players'] else None
            return type(cls, (), {'online_players': data['players']['online'], 'max_players': data['players']['max'], 'motd': data['motd']['clean'][0].strip(), 'version': data['version'], 'players_list': players_list})

class Status(commands.Cog):

    def __init__(self,client):
        self.client = client

    #Commands
    @commands.command()
    async def status(self, ctx):
        server = await Serverstatus.new()
        embedstatus = discord.Embed(
            url = 'https://hydrovanillasmp.com',
            colour = discord.Color.from_rgb(12,235,241)
        )

        embedstatus.set_footer(text=f'@ Hydro Vanilla SMP', icon_url='https://hydrovanillasmp.com/wp-content/uploads/2019/06/HydroSMP_BaseLogo.png')
        embedstatus.set_thumbnail(url='https://i.imgur.com/VkgebnW.png')
        embedstatus.add_field(name='Hydro Vanilla SMP Season 6 is online!', value=f'Currently there are {server.online_players} / {server.max_players} playing.', inline=False)
        embedstatus.add_field(name='_ _', value='_ _', inline=False)
        pl1 = server.players_list
        if pl1:
            pl2 = '\n'.join(pl1)
            embedstatus.add_field(name='Playerlist:', value=f'{pl2}')
        else:
            embedstatus.add_field(name='Playerlist:', value='No online players.')
        embedstatus.add_field(name='_ _', value='_ _', inline=False)
        embedstatus.add_field(name='Message of the day:', value=f'{server.motd}', inline=False)
        embedstatus.add_field(name='_ _', value='_ _', inline=False)
        embedstatus.add_field(name='Current Minecraft Version:', value=f'{server.version}', inline=False)

        await ctx.send(embed=embedstatus)

def setup(client):
    client.add_cog(Status(client))