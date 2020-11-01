import discord
from discord.ext import commands
from minecraft import Server
import rconcredentials


class RCON(commands.Cog):

    def __init__(self,client):
        self.client = client


    #Commands
    @commands.command()
    @commands.has_role('Staff')
    async def whitelist(self, ctx, ign):
        ip = rconcredentials.ip
        port = rconcredentials.port
        password = rconcredentials.password

        server = Server(ip, port, password, connect_on_send=True)
        print(await server.send(f'whitelist add {ign}'))
        await ctx.send(f'Added {ign} to the whitelist.')

        await server.close()

    @whitelist.error
    async def whitelist_error(self, ign, error):
        if isinstance(error, commands.MissingRole):
            await ign.send("You don't have the permissions to do that!")
        if isinstance(error, commands.MissingRequiredArgument):
            await ign.send('You have to put member\'s IGN that you want to whitelist!')

    @commands.command()
    @commands.has_role('Staff')
    async def unwhitelist(self, ctx, ign):
        ip = rconcredentials.ip
        port = rconcredentials.port
        password = rconcredentials.password

        server = Server(ip, port, password, connect_on_send=True)
        print(await server.send(f'whitelist remove {ign}'))
        await ctx.send(f'Removed {ign} to the whitelist.')

        await server.close()
    
    @unwhitelist.error
    async def unwhitelist_error(self, ign, error):
        if isinstance(error, commands.MissingRole):
            await ign.send("You don't have the permissions to do that!")
        if isinstance(error, commands.MissingRequiredArgument):
            await ign.send('You have to put member\'s IGN that you want to unwhitelist!')

    @commands.command()
    @commands.has_role('Staff')
    async def ban(self, ctx, member: discord.Member, ign):
        ip = rconcredentials.ip
        port = rconcredentials.port
        password = rconcredentials.password

        server = Server(ip, port, password, connect_on_send=True)
        print(await server.send(f'ban {ign}'))
        await member.ban(reason=None)

        await server.close()
        
        author = ctx.message.author
        author_icon = author.avatar_url
        embedban = discord.Embed(
            colour = discord.Colour.from_rgb(12,235,241)
            )

        embedban.set_footer(text=f'@ Hydro Vanilla SMP', icon_url='https://hydrovanillasmp.com/wp-content/uploads/2019/06/HydroSMP_BaseLogo.png')
        embedban.set_author(name=f'{author}', icon_url=f'{author_icon}')
        embedban.set_image(url='https://cdn.discordapp.com/attachments/586259382522609664/772449306560430110/tenor.gif')
        embedban.add_field(name=f'Successfully banned @{member}.', value='They\'ve been such a prick, innit?', inline=False)

        await ctx.send(embed=embedban)

    @ban.error
    async def ban_error(self, member, error):
        if isinstance(error, commands.MissingRole):
            await member.send('You don\'t have the permissions to do that!')
        if isinstance(error, commands.MissingRequiredArgument):
            await member.send('You have to mention the Member you want to ban and put down their IGN!')

    @commands.command()
    @commands.has_role('Staff')
    async def unban(self, ctx, ign):
        ip = rconcredentials.ip
        port = rconcredentials.port
        password = rconcredentials.password

        server = Server(ip, port, password, connect_on_send=True)
        print(await server.send(f'pardon {ign}'))

        await server.close()

        channel = ctx.channel
        await channel.send('Alright, now give me Username#Discriminator.')
        def check(message):
            return message.author == ctx.message.author
        member = await self.client.wait_for('message', check=check)

        banned_users = await ctx.guild.bans()
        print(tuple(member.content.split('#')))
        (member_name, member_discriminator) = tuple(member.content.split('#'))
        print(member_name)
        print(member_discriminator)

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                return
                
        author = ctx.message.author
        author_icon = author.avatar_url
        embedunban = discord.Embed(
            colour = discord.Colour.from_rgb(12,235,241)
            )

        embedunban.set_footer(text=f'@ Hydro Vanilla SMP', icon_url='https://hydrovanillasmp.com/wp-content/uploads/2019/06/HydroSMP_BaseLogo.png')
        embedunban.set_author(name=f'{author}', icon_url=f'{author_icon}')
        embedunban.set_image(url='https://cdn.discordapp.com/attachments/586259382522609664/772480429034569739/tenor.gif')
        embedunban.add_field(name=f'Successfully unbanned @{member}.', value='Maybe they haven\'t been such a prick?', inline=False)

        await ctx.send(embed=embedunban)

    @unban.error
    async def unban_error(self, member, error):
        if isinstance(error, commands.MissingRole):
            await member.send('You don\'t have the permissions to do that!')
        if isinstance(error, commands.MissingRequiredArgument):
            await member.send('You have put down Member\'s IGN and Username#Discriminator that you want to unban!')
    
    @commands.command()
    @commands.has_role('Staff')
    async def close(self, ctx):
        ip = rconcredentials.ip
        port = rconcredentials.port
        password = rconcredentials.password

        server = Server(ip, port, password, connect_on_send=True)

        await server.close()

    @close.error
    async def close_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.send("You don't have the permissions to do that!")


def setup(client):
    client.add_cog(RCON(client))