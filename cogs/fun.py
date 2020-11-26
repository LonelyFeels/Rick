import discord
from discord.ext import commands
import random
from bs4 import BeautifulSoup as bs
import requests
import urllib.request
import json


class Fun(commands.Cog):

    def __init__(self,client):
        self.client = client


    #Commands
    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ['It is certain.',
                    'It is decidedly so.',
                    'Without a douubt.',
                    'Yes - definitely.',
                    'You may rely on it.',
                    'As I see it, yes',
                    'Most likely.',
                    'Outlook good.',
                    'Yes.',
                    'Signs point to yes.',
                    'Reply hazy, try again.',
                    'Ask again later.',
                    'Better not tell you now.',
                    'Cannot predict now.',
                    'Concentrate and ask again.',
                    "Don't count on it.",
                    'My reply is no.',
                    'My sources say no.',
                    'Outlook not so good',
                    'Very doubtful.']
        await ctx.send(f'{random.choice(responses)}')

    @commands.command()
    async def hug(self, ctx, member: discord.Member):
        author = ctx.message.author
        author_icon = author.avatar_url
        embedhug = discord.Embed(
            colour = discord.Colour.from_rgb(12,235,241)
            )

        embedhug.set_footer(text=f'@ Hydro Vanilla SMP', icon_url='https://hydrovanillasmp.com/wp-content/uploads/2019/06/HydroSMP_BaseLogo.png')
        embedhug.set_author(name=f'{author}', icon_url=f'{author_icon}')
        embedhug.set_image(url='https://i.imgur.com/kSWpxnG.gif')
        embedhug.add_field(name=f'@{member} I just hugged you in my thoughts :heart:', value='Hope you felt the squeeze! :teddy_bear:', inline=False)

        await ctx.send(embed=embedhug)

    @hug.error
    async def hug_error(self, member, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await member.send('You have to mention the Member you want to hug.')

    @commands.command()
    async def waifu(self, ctx):
        page = requests.get('http://randomwaifu.altervista.org')
        soup = bs(page.content, features='html.parser')
        url = str(soup.find_all(class_="center-fit")[0])[-18:][:15]
        name = str(soup.find_all(align="center")[0]).split(' from')[0][55:]
        channel = self.client.get_channel(771725747480035358)

        if ctx.channel.id == channel.id:
            embedwaifu = discord.Embed(
                title = f'{name}',
                url = f'http://randomwaifu.altervista.org/{url}',
                colour = discord.Colour.from_rgb(12,235,241)
            )

            embedwaifu.set_footer(text=f'@ Hydro Vanilla SMP', icon_url='https://hydrovanillasmp.com/wp-content/uploads/2019/06/HydroSMP_BaseLogo.png')
            embedwaifu.set_image(url=f'http://randomwaifu.altervista.org/{url}')
            embedwaifu.add_field(name='_ _', value='If the picutre doesn\'t load, that means it\'s too big.\nClick the name and it will open on your browser.', inline=False)

            await ctx.send(embed=embedwaifu)
        else:
            await ctx.send(f'You can only use this command in {channel.mention}.')

    @commands.command()
    async def dogfact(self, ctx):
        response = urllib.request.urlopen("https://some-random-api.ml/facts/dog")
        data = json.load(response)
        fact = data['fact']

        embeddog = discord.Embed(
            title = 'Dog Fact',
            colour = discord.Colour.from_rgb(12,235,241)
        )
        
        embeddog.set_footer(text=f'@ Hydro Vanilla SMP', icon_url='https://hydrovanillasmp.com/wp-content/uploads/2019/06/HydroSMP_BaseLogo.png')
        embeddog.set_thumbnail(url='https://i.imgur.com/VkgebnW.png')
        embeddog.add_field(name='Woof woof 🐕', value=f'{fact}', inline=False)

        await ctx.send(embed=embeddog)

    @commands.command()
    async def catfact(self, ctx):
        response = urllib.request.urlopen("https://some-random-api.ml/facts/cat")
        data = json.load(response)
        fact = data['fact']
        
        embedcat = discord.Embed(
            title = 'Dog Fact',
            colour = discord.Colour.from_rgb(12,235,241)
        )
        
        embedcat.set_footer(text=f'@ Hydro Vanilla SMP', icon_url='https://hydrovanillasmp.com/wp-content/uploads/2019/06/HydroSMP_BaseLogo.png')
        embedcat.set_thumbnail(url='https://i.imgur.com/VkgebnW.png')
        embedcat.add_field(name='Meow 🐈‍⬛', value=f'{fact}', inline=False)

        await ctx.send(embed=embedcat)

def setup(client):
    client.add_cog(Fun(client))