import discord
from discord.ext import commands
import random


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
        embedhug = discord.Embed(
            colour = discord.Colour.from_rgb(12,235,241),
            )

        embedhug.set_footer(text=f'@ Hydro Vanilla SMP', icon_url='https://hydrovanillasmp.com/wp-content/uploads/2019/06/HydroSMP_BaseLogo.png')
        embedhug.set_image(url='https://imgur.com/kSWpxnG')
        embedhug.add_field(name='I just hugged you in my thoughts <3', value='Hope you felt the squeeze! :teddy_bear:', inline=False)

        await ctx.send(embed=embedhug)


def setup(client):
    client.add_cog(Fun(client))