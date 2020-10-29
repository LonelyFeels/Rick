import discord
from discord.ext import commands


class Clear(commands.Cog):

    def __init__(self,client):
        self.client = client

    #Commands
    @commands.command()
    async def clear(self, ctx, amount=5):
        authorperms_clear = ctx.author.permissions_in(ctx.channel)
        if authorperms_clear.manage_messages:
          await ctx.channel.purge(limit=amount+1)
        else:
         await ctx.send("You don't have the permissions to do that!")

def setup(client):
    client.add_cog(Clear(client))