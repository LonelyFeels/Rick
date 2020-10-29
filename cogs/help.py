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
            url = 'https://hydrovanillasmp.com',
            colour = discord.Colour.from_rgb(12,235,241),
            )

        embedhelp.set_footer(text=f'@ Hydro Vanilla SMP', icon_url='https://hydrovanillasmp.com/wp-content/uploads/2019/06/HydroSMP_BaseLogo.png')
        embedhelp.set_thumbnail(url='https://hydrovanillasmp.com/wp-content/uploads/2019/03/HydroSMP_Discord-1.png')
        embedhelp.add_field(name='.help', value='Shows this message.', inline=False)
        embedhelp.add_field(name='.status', value='Shows Minecraft Server Status', inline=False)
        embedhelp.add_field(name='.donate', value='Shows information about how to donate.', inline=False)
        embedhelp.add_field(name='.invite', value='Get the invite link.', inline=False)
        embedhelp.add_field(name='.dynmap', value='Use this command to get the Official Hydro Vanilla SMP Dynmap!', inline=False)
        embedhelp.add_field(name='.8ball <your question>', value='Undecided about something? Ask our 8ball (:', inline=False)
        embedhelp.add_field(name='--------------------------------------------------------------', value='-------------------------------------------------------------, inline=False)
        embedhelp.add_field(name='.load <category>', value='Loads the category.', inline=False)
        embedhelp.add_field(name='.unload <category>', value='Unloads the category.', inline=False)
        embedhelp.add_field(name='.accept <@USER>', value='Use this to accept Applicants and give them Member role.', inline=False)
        embedhelp.add_field(name='.clear <amount=5>', value='Use this to clear messages.', inline=False)
        embedhelp.add_field(name='Categories:', value='Help: Help, Donate, Invite, Dynmap; Status: Status; Roles: Accept, Reaction Roles; Clear: Clear; Fun: 8ball', inline=False)

        await ctx.send(embed=embedhelp)
        
    @commands.command()
    async def dynmap(self, ctx):
        embeddynmap = discord.Embed(
            url = 'https://map.hydrovanillasmp.com',
            colour = discord.Colour.from_rgb(12,235,241)
        )

        embeddynmap.set_footer(text=f'@ Hydro Vanilla SMP', icon_url='https://hydrovanillasmp.com/wp-content/uploads/2019/06/HydroSMP_BaseLogo.png')
        embeddynmap.set_thumbnail(url='https://hydrovanillasmp.com/wp-content/uploads/2019/03/HydroSMP_Discord-1.png')
        embeddynmap.add_field(name='Dynmap Link', value='Here you go! The link to our Dynmap,\nhttps://map.hydrovanillasmp.com', inline=False)

        await ctx.send(embed=embeddynmap)

    @commands.command()
    async def donate(self, ctx):
        embeddonate = discord.Embed(
            url = 'https://www.paypal.me/HydroVanillaSMP',
            colour = discord.Color.from_rgb(12,235,241)
        )

        embeddonate.set_footer(text=f'@ Hydro Vanilla SMP', icon_url='https://hydrovanillasmp.com/wp-content/uploads/2019/06/HydroSMP_BaseLogo.png')
        embeddonate.set_thumbnail(url='https://hydrovanillasmp.com/wp-content/uploads/2019/03/HydroSMP_Discord-1.png')
        embeddonate.add_field(name='Here you go! The link to donate to Hydro Vanilla SMP!', value='Thanks in advance if you are donating! We really appreciate it :heart:', inline=False)
        embeddonate.add_field(name='https://www.paypal.me/HydroVanillaSMP', value='If you do not use PayPal, but are European and use iDeal you can message @Tehlo on Discord, I am Dutch too :smiley:', inline=False)

        await ctx.send(embed=embeddonate)

    @commands.command()
    async def invite(self, ctx):
        member = ctx.message.author
        await ctx.send(f'{member.mention}, You got mail! 📬')
        await member.send('Here you go, our Discord Invite!\nhttps://discordapp.com/invite/CAQ9p8y')


def setup(client):
    client.add_cog(Help(client))