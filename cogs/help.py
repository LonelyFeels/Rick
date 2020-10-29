import discord
from discord.ext import commands


class Help(commands.Cog):

    def __init__(self,client):
        self.client = client


    #Commands
    @commands.command()
    async def help(self, ctx):
        embedhelp = discord.Embed(
            title = '**All Hydro Accept commands**',
            colour = discord.Colour.blue(),
            icon_url = 'https://hydrovanillasmp.com/wp-content/uploads/2019/06/HydroSMP_BaseLogo.png'
            )

        embedhelp.set_footer(text=f'@ Hydro Vanilla SMP')
        embedhelp.add_field(name='.help', value='Shows this message.', inline=False)
        embedhelp.add_field(name='!status', value='Shows Minecraft Server Status', inline=False)
        embedhelp.add_field(name='!donate', value='Shows information about how to donate.', inline=False)
        embedhelp.add_field(name='!invite', value='Get the invite link.', inline=False)
        embedhelp.add_field(name='!dynmap', value='Use this command to get the Official Hydro Vanilla SMP Dynmap!', inline=False)
        embedhelp.add_field(name='.8ball <your question>', value='Undecided about something? Ask our 8ball (:', inline=False)
        embedhelp.add_field(name='.load <category>', value='Loads the category.', inline=False)
        embedhelp.add_field(name='.unload <category>', value='Unloads the category.', inline=False)
        embedhelp.add_field(name='.accept <@USER>', value='Use this to accept Applicants and give them Member role.', inline=False)
        embedhelp.add_field(name='.clear <amount=5>', value='Use this to clear messages.', inline=False)
        embedhelp.add_field(name='Categories:', value='Roles: Accept, Reaction Roles; Clear: Clear, Fun: 8ball')

        await ctx.send(embed=embedhelp)
        

def setup(client):
    client.add_cog(Help(client))