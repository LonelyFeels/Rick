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


def setup(client):
    client.add_cog(Fun(client))