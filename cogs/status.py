import discord
from discord.ext import commands
from mcsrvstat import ServerStatus


class Status(commands.Cog):

    def __init__(self,client):
        self.client = client


    #Commands
    @commands.command()
    async def status(self, ctx):
        status = ServerStatus()
        online_players = status.online_players
        max_players = status.max_players
        motd = status.motd
        version = status.version
        players_list = status.players_list

        if online_players == None:
            embedstatus = discord.Embed(
                url = 'https://hydrovanillasmp.com',
                colour = discord.Color.from_rgb(12,235,241)
            )

            embedstatus.set_footer(text=f'@ Hydro Vanilla SMP', icon_url='https://hydrovanillasmp.com/wp-content/uploads/2019/06/HydroSMP_BaseLogo.png')
            embedstatus.set_thumbnail(url='https://i.imgur.com/VkgebnW.png')
            embedstatus.add_field(name='Hydro Vanilla SMP Season 6 is online!', value=f'Currently there are 0 / {max_players} playing.', inline=False)
            embedstatus.add_field(name='_ _', value='_ _', inline=False)
            embedstatus.add_field(name='Playerlist:', value='_ _')
            embedstatus.add_field(name='_ _', value='_ _', inline=False)
            embedstatus.add_field(name='Message of the day:', value=f'{motd}', inline=False)
            embedstatus.add_field(name='_ _', value='_ _', inline=False)
            embedstatus.add_field(name='Current Minecraft Version:', value=f'{version}', inline=False)

            await ctx.send(embed=embedstatus)
        else:
            embedstatus = discord.Embed(
                url = 'https://hydrovanillasmp.com',
                colour = discord.Color.from_rgb(12,235,241)
            )

            embedstatus.set_footer(text=f'@ Hydro Vanilla SMP', icon_url='https://hydrovanillasmp.com/wp-content/uploads/2019/06/HydroSMP_BaseLogo.png')
            embedstatus.set_thumbnail(url='https://i.imgur.com/VkgebnW.png')
            embedstatus.add_field(name='Hydro Vanilla SMP Season 6 is online!', value=f'Currently there are {online_players} / {max_players} playing.', inline=False)
            embedstatus.add_field(name='_ _', value='_ _', inline=False)
            embedstatus.add_field(name='Playerlist:', value=f'{players_list}')
            embedstatus.add_field(name='_ _', value='_ _', inline=False)
            embedstatus.add_field(name='Message of the day:', value=f'{motd}', inline=False)
            embedstatus.add_field(name='_ _', value='_ _', inline=False)
            embedstatus.add_field(name='Current Minecraft Version:', value=f'{version}', inline=False)

            await ctx.send(embed=embedstatus)


def setup(client):
    client.add_cog(Status(client))