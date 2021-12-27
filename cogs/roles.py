import discord
from discord.ext import commands


class Roles(commands.Cog):

    def __init__(self,client):
        self.client = client


    #Events
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        role = discord.utils.get(member.guild.roles, name='Applicants')
        welcome = self.client.get_channel(621326188555796481)
        applications = self.client.get_channel(494184460275941377)
        info = '<#584777370557349898>'
        await member.add_roles(role)
        await welcome.send(f'Welcome {member.mention} to **Hydro Vanilla SMP!** <:hydrosmp:579754809272434695>')
        await applications.send(f'Welcome {member.mention} to **Hydro Vanilla SMP** <:hydrosmp:579754809272434695>! \n**Make sure to read** {info} **to check on how to Apply!**')
        await applications.send('```IGN?:\nLocation?:\nWhat year were you born?:\n\nHow long have you been playing Minecraft SMP?:\nWhat do you primarily do while playing Minecraft?:\nHow many past servers have you played on?:\nWill you be active in Discord and do you want to participate in group events?:\nHow much time can you play a week? (estimated):\nBriefly explain your plans for this server:\n\nWhere did you find out about Hydro SMP? (If it is a website, post the link):\nIf it was on Reddit, what is your Reddit username?```')
        await applications.send('Copy this template ^ and post it in this channel when you are done filling it in! :white_check_mark:')

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        welcome = self.client.get_channel(621326188555796481)
        await welcome.send(f'Goodbye @{member}... May we meet again :sob:')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id
        if message_id == 771114709603713035:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)

            if payload.emoji.name == 'blamenate':
                role = discord.utils.get(guild.roles, name='#PraiseNate')
            elif payload.emoji.name == '🛒':
                role = discord.utils.get(guild.roles, name='Shopaholics')
            elif payload.emoji.name == 'HydroSubway':
                role = discord.utils.get(guild.roles, name='Weebs')
            elif payload.emoji.name == '🇳🇱':
                role = discord.utils.get(guild.roles, name='Dutchie')
            elif payload.emoji.name == '🍰':
                role = discord.utils.get(guild.roles, name='Food Addicts')
            elif payload.emoji.name == '🎨':
                role = discord.utils.get(guild.roles, name='Art')
            elif payload.emoji.name == '🔞':
                role = discord.utils.get(guild.roles, name='NSFW')
            elif payload.emoji.name == 'HydroPing1':
                role = discord.utils.get(guild.roles, name='Survey')
            elif payload.emoji.name == 'HydroTwitch':
                role = discord.utils.get(guild.roles, name='Stream Fans')
            elif payload.emoji.name == 'Hydrohypers':
                role = discord.utils.get(guild.roles, name='Memester')
            elif payload.emoji.name == '1️⃣':
                role = discord.utils.get(guild.roles, name='Season 1 OG')
            elif payload.emoji.name == '2️⃣':
                role = discord.utils.get(guild.roles, name='Season 2 OG')
            elif payload.emoji.name == '3️⃣':
                role = discord.utils.get(guild.roles, name='Season 3 OG')
            elif payload.emoji.name == '4️⃣':
                role = discord.utils.get(guild.roles, name='Season 4 OG')
            elif payload.emoji.name == '5️⃣':
                role = discord.utils.get(guild.roles, name='Season 5 OG')
            elif payload.emoji.name == '6️⃣':
                role = discord.utils.get(guild.roles, name='Season 6 OG')
            elif payload.emoji.name == 'Hydro69':
                role = discord.utils.get(guild.roles, name='Season 6.9 OG')
            elif payload.emoji.name == '7️⃣':
                role = discord.utils.get(guild.roles, name='Season 7 OG')
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role in member.roles:
                await member.send(f"You already have {role} role.")
            else:
                if role is not None:
                    if member is not None:
                        await member.add_roles(role)
                        await member.send(f"You've been given {role} role")
                    else:
                        pass
                else:
                    await member.send('Role not found.')

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        message_id = payload.message_id
        if message_id == 771114709603713035:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.client.guilds)
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)

            if payload.emoji.name == 'blamenate':
                role = discord.utils.get(guild.roles, name='#PraiseNate')
            elif payload.emoji.name == '🛒':
                role = discord.utils.get(guild.roles, name='Shopaholics')
            elif payload.emoji.name == 'HydroSubway':
                role = discord.utils.get(guild.roles, name='Weebs')
            elif payload.emoji.name == '🇳🇱':
                role = discord.utils.get(guild.roles, name='Dutchie')
            elif payload.emoji.name == '🍰':
                role = discord.utils.get(guild.roles, name='Food Addicts')
            elif payload.emoji.name == '🎨':
                role = discord.utils.get(guild.roles, name='Art')
            elif payload.emoji.name == '🔞':
                role = discord.utils.get(guild.roles, name='NSFW')
            elif payload.emoji.name == 'HydroPing1':
                role = discord.utils.get(guild.roles, name='Survey')
            elif payload.emoji.name == 'HydroTwitch':
                role = discord.utils.get(guild.roles, name='Stream Fans')
            elif payload.emoji.name == 'Hydrohypers':
                role = discord.utils.get(guild.roles, name='Memester')
            elif payload.emoji.name == '1️⃣':
                role = discord.utils.get(guild.roles, name='Season 1 OG')
            elif payload.emoji.name == '2️⃣':
                role = discord.utils.get(guild.roles, name='Season 2 OG')
            elif payload.emoji.name == '3️⃣':
                role = discord.utils.get(guild.roles, name='Season 3 OG')
            elif payload.emoji.name == '4️⃣':
                role = discord.utils.get(guild.roles, name='Season 4 OG')
            elif payload.emoji.name == '5️⃣':
                role = discord.utils.get(guild.roles, name='Season 5 OG')
            elif payload.emoji.name == '6️⃣':
                role = discord.utils.get(guild.roles, name='Season 6 OG')
            elif payload.emoji.name == 'Hydro69':
                role = discord.utils.get(guild.roles, name='Season 6.9 OG')
            elif payload.emoji.name == '7️⃣':
                role = discord.utils.get(guild.roles, name='Season 7 OG')
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role in member.roles:
                if role is not None:
                    if member is not None:
                        await member.remove_roles(role)
                        await member.send(f"{role} role has been taken from you.")
                    else:
                        pass
                else:
                    await member.send('Role not found.')
            else:
                if role is not None:
                    await member.send(f"You don't have {role} role.")    
                else:
                    await member.send('Role not found.')

    #Commands
    @commands.command()
    @commands.has_role('Staff')
    async def accept(self, ctx, member: discord.Member):
        members = discord.utils.get(ctx.guild.roles, name='Members')
        applicants = discord.utils.get(ctx.guild.roles, name='Applicants')
        channel = self.client.get_channel(494184372258471938)
        info = '<#584773749497266199>'
        await member.remove_roles(applicants)
        await member.add_roles(members)
        await channel.send(f'Please welcome {member.mention} to **Hydro Vanilla SMP**! Our IP and Information can be found in {info}! :smiley:\nAnd no, @W1ckeDMetaL is not an admin... he is just an asshole with too much income 💸')

    @accept.error
    async def accept_error(self, member, error):
        if isinstance(error, commands.MissingRole):
            await member.send('You don\'t have the permissions to do that!')
        if isinstance(error, commands.MissingRequiredArgument):
            await member.send('You have to mention the Applicant you want to accept!')

    @commands.command()
    @commands.has_role('Staff')
    async def permdeny(self, ctx, member: discord.Member):
        applicants = discord.utils.get(ctx.guild.roles, name='Applicants')
        permdenied = discord.utils.get(ctx.guild.roles, name='Permanently Denied')
        channel = self.client.get_channel(494184460275941377)
        await member.remove_roles(applicants)
        await member.add_roles(permdenied)
        await channel.send(f'Permanently denied {member.mention}.')

    @permdeny.error
    async def permdeny_error(self, member, error):
        if isinstance(error, commands.MissingRole):
            await member.send('You don\'t have the permission to do that!')
        if isinstance(error, commands.MissingRequiredArgument):
            await member.send('You have to mention the Applicant you want to permanently denied!')


def setup(client):
    client.add_cog(Roles(client))