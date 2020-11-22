import discord
from discord.ext import commands


class Admin(commands.Cog):

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

    @commands.command()
    @commands.has_role('Staff')
    async def count(self, ctx):
        guild = self.client.get_guild(494184372258471936)
        members = [m.status for m in guild.members]
        bots = [b.status for b in guild.members if b.bot]
        
        embedcount = discord.Embed(
            title = 'Hydro Member Counter',
            url = 'https://hydrovanillasmp.com',
            colour = discord.Colour.from_rgb(12,235,241)
        )

        embedcount.set_footer(text=f'@ Hydro Vanilla SMP', icon_url='https://hydrovanillasmp.com/wp-content/uploads/2019/06/HydroSMP_BaseLogo.png')
        embedcount.set_thumbnail(url='https://i.imgur.com/VkgebnW.png')
        embedcount.add_field(name='Online Members:', value=f'{members.count(discord.Status.online)}', inline=False)
        embedcount.add_field(name='Idle Members:', value=f'{members.count(discord.Status.idle)}', inline=False)
        embedcount.add_field(name='Do not disturb Members:', value=f'{members.count(discord.Status.do_not_disturb)}', inline=False)
        embedcount.add_field(name='Offline Members:', value=f'{members.count(discord.Status.offline)}', inline=False)
        embedcount.add_field(name='Total Members:', value=f'{len(self.client.users)}', inline=False)
        embedcount.add_field(name='Bots:', value=f'{bots.count(discord.Status.online)+bots.count(discord.Status.idle)+bots.count(discord.Status.do_not_disturb)}', inline=False)

        await ctx.send(embed=embedcount)

    @count.error
    async def count_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.send('You don\'t have the permissions to do that!')

def setup(client):
    client.add_cog(Admin(client))