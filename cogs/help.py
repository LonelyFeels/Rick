import discord
from discord.ext import commands


class Help(commands.Cog):

    def __init__(self,client):
        self.client = client


    #Commands
    @commands.command()
    async def help(self, ctx):
        embedhelp = discord.Embed(
            title = 'All Hydro Accept commands',
            url = 'https://hydrovanillasmp.com',
            colour = discord.Colour.from_rgb(12,235,241)
            )

        embedhelp.set_footer(text=f'@ Hydro Vanilla SMP', icon_url='https://i.imgur.com/VkgebnW.png')
        embedhelp.set_thumbnail(url='https://i.imgur.com/VkgebnW.png')
        embedhelp.add_field(name='!help', value='Shows this message.', inline=False)
        embedhelp.add_field(name='!status', value='Shows Minecraft Server Status', inline=False)
        embedhelp.add_field(name='!donate', value='Shows information about how to donate.', inline=False)
        embedhelp.add_field(name='!invite', value='Get the invite link.', inline=False)
        embedhelp.add_field(name='!dynmap', value='Use this command to get the Official Hydro Vanilla SMP Dynmap!', inline=False)
        embedhelp.add_field(name='!suggest <suggestion>', value='Suggest something you think it would be a cool addition to the server.', inline=False)
        embedhelp.add_field(name='!colorlist', value='Shows you the list of available colors for Donators.', inline=False)
        embedhelp.add_field(name='!color', value='Use this command to change your donator IGN color. Make sure you\'re in-game. For colors check #rules-and-info.', inline=False)
        embedhelp.add_field(name='!trail', value='Use this command to change your donator trail color. You can use any Minecraft color or any HEX color.', inline=False)
        embedhelp.add_field(name='!hug <@USER>', value='Show someone how much you love them :heart:', inline=False)
        embedhelp.add_field(name='!8ball <question>', value='Undecided about something? Ask our 8ball (:', inline=False)
        embedhelp.add_field(name='!dogfact', value='Woof Woof 🐕', inline=False)
        embedhelp.add_field(name='!catfact', value='Meow 🐈‍⬛', inline=False)
        embedhelp.add_field(name='!pandafact', value='Squeak? 🐼', inline=False)
        embedhelp.add_field(name='!foxfact', value='What does the fox say? 🦊', inline=False)
        embedhelp.add_field(name='!birdfact', value='Tweet 🐦', inline=False)
        embedhelp.add_field(name='!koalafact', value='Tweet 🐨', inline=False)
        embedhelp.add_field(name='_ _', value='_ _', inline=False)
        embedhelp.add_field(name='!load <category>', value='Loads the category.', inline=False)
        embedhelp.add_field(name='!unload <category>', value='Unloads the category.', inline=False)
        embedhelp.add_field(name='!close', value='Close accidentally opened RCON.', inline=False)
        embedhelp.add_field(name='!accept <@USER>', value='Use this to accept Applicants and give them Member role.', inline=False)
        embedhelp.add_field(name='!permdeny <@USER>', value='Use this to permanently deny Applicants.', inline=False)
        embedhelp.add_field(name='!whitelist <IGN>', value='Use this to whitelist the member.', inline=False)
        embedhelp.add_field(name='!unwhitelist <IGN>', value='Use this to unwhitelist the member.', inline=False)
        embedhelp.add_field(name='!ban <@USER> <IGN> <REASON>', value='Use this to ban the member both from Discord and Minecraft server.', inline=False)
        embedhelp.add_field(name='!unban <IGN> -> <USER#DISCRIMINATOR>', value='Use this to unban the member both from Discord and Minecraft server.', inline=False)
        embedhelp.add_field(name='!kick <IGN>', value='Use this to kick the member from Discord server.', inline=False)
        embedhelp.add_field(name='!clear <amount=5>', value='Use this to clear messages.', inline=False)
        embedhelp.add_field(name='!count', value='Returns amounts of members.', inline=False)
        embedhelp.add_field(name='_ _', value='_ _', inline=False)
        embedhelp.add_field(name='Categories:', value='Help: Help, Donate, Invite, Dynmap; Status: Status; Roles: Accept, PermDeny, Reaction Roles; RCON: Whitelist, Unwhitelist, Ban, Unban, Kick, Close; Suggestions: Suggest; Admin: Clear, Count; Fun:  Hug, 8ball, Waifu, DogFact, CatFact, PandaFact, FoxFact, BirdFact, Koalafact', inline=False)

        await ctx.send(embed=embedhelp)
        
    @commands.command()
    async def dynmap(self, ctx):
        embeddynmap = discord.Embed(
            url = 'http://hydrovanillasmp.dedimc.io:25599/',
            colour = discord.Colour.from_rgb(12,235,241)
        )

        embeddynmap.set_footer(text=f'@ Hydro Vanilla SMP', icon_url='https://i.imgur.com/VkgebnW.png')
        embeddynmap.set_thumbnail(url='https://i.imgur.com/VkgebnW.png')
        embeddynmap.add_field(name='Dynmap Link', value='Here you go! The link to our Dynmap,\nhttp://148.251.211.70:25599', inline=False)

        await ctx.send(embed=embeddynmap)

    @commands.command()
    async def plan(self, ctx):
        embedplan = discord.Embed(
            url = 'http://148.251.211.70:25553',
            colour = discord.Colour.from_rgb(12,235,241)
        )

        embedplan.set_footer(text=f'@ Hydro Vanilla SMP', icon_url='https://i.imgur.com/VkgebnW.png')
        embedplan.set_thumbnail(url='https://i.imgur.com/VkgebnW.png')
        embedplan.add_field(name='PLAN Link', value='Here you go! The link to our PLAN,\nhttp://148.251.211.70:25553', inline=False)

        await ctx.send(embed=embedplan)

    @commands.command()
    async def docs(self, ctx):
        embeddocs = discord.Embed(
            url = 'https://lonelyfeels1.gitbook.io/hydro-guide/',
            colour = discord.Colour.from_rgb(12,235,241)
        )

        embeddocs.set_footer(text=f'@ Hydro Vanilla SMP', icon_url='https://i.imgur.com/VkgebnW.png')
        embeddocs.set_thumbnail(url='https://i.imgur.com/VkgebnW.png')
        embeddocs.add_field(name='Docs Website', value='Here you go! The link to our Docs,\nhttps://lonelyfeels1.gitbook.io/hydro-guide/', inline=False)

        await ctx.send(embed=embeddocs)

    @commands.command()
    async def donate(self, ctx):
        embeddonate = discord.Embed(
            colour = discord.Color.from_rgb(12,235,241)
        )

        embeddonate.set_footer(text=f'@ Hydro Vanilla SMP', icon_url='https://i.imgur.com/VkgebnW.png')
        embeddonate.set_thumbnail(url='https://i.imgur.com/VkgebnW.png')
        embeddonate.add_field(name='Here you go! The link to donate to Hydro Vanilla SMP!', value='Thanks in advance if you are donating! We really appreciate it :heart:', inline=False)
        embeddonate.add_field(name='We are being sponsored from **DedicatedMC** 🙏', value='We are thankful from the bottom of the heart ❤️', inline=False)

        await ctx.send(embed=embeddonate)

    @commands.command()
    async def invite(self, ctx):
        member = ctx.message.author
        await ctx.send(f'{member.mention}, You got mail! 📬')
        await member.send('Here you go, our Discord Invite!\nhttps://discordapp.com/invite/CAQ9p8y')

    @commands.command()
    async def colorlist(self, ctx):
        embedcolorlist = discord.Embed(
            title = 'All In-Game Available Colors',
            url = 'https://hydrovanillasmp.com',
            colour = discord.Colour.from_rgb(12,235,241)
            )

        embedcolorlist.set_footer(text=f'@ Hydro Vanilla SMP', icon_url='https://i.imgur.com/VkgebnW.png')
        embedcolorlist.set_thumbnail(url='https://i.imgur.com/VkgebnW.png')
        embedcolorlist.add_field(name='How to use !color and !trail', value='It\'s simple. Your Discord nickname must match your IGN in order for the command to work. Check commands syntax in !help and follow them. Available colors are stated below.', inline=False)
        embedcolorlist.add_field(name='IGN COLORS', value='GOLD, DARK_GREEN, GREEN, DARK_PURPLE, LIGHT_PURPLE, DARK_AQUA, AQUA, DARK_BLUE', inline=False)
        embedcolorlist.add_field(name='TRAIL COLORS', value='AQUA, BLACK, BLUE, DARK_AQUA, DARK_BLUE, DARK_GRAY, DARK_GREEN, DARK_PURPLE, DARK_RED, GOLD, GRAY, GREEN, LIGHT_PURPLE, RED, WHITE, YELLOW, remove, any HEX color', inline=False)

        await ctx.send(embed=embedcolorlist)


def setup(client):
    client.add_cog(Help(client))