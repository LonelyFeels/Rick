import discord
import os
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '.', intents=intents)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb,
    activity=discord.Activity(type=discord.ActivityType.listening, name="to Hydro Applications"))
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name='Applicants')
    welcome = client.get_channel(621326188555796481)
    applications = client.get_channel(494184460275941377)
    info = '<#584777370557349898>'
    await member.add_roles(role)
    await welcome.send(f'Welcome {member.mention} to **Hydro Vanilla SMP!** <:hydrosmp:579754809272434695>')
    await applications.send(f'Welcome {member.mention} to **Hydro Vanilla SMP** <:hydrosmp:579754809272434695>! \n**Make sure to read** {info} **to check on how to Apply!**')
    await applications.send('```IGN?:\nLocation?:\nWhat year were you born?:\n\nHow long have you been playing Minecraft SMP?:\nWhat do you primarily do while playing Minecraft?:\nHow many past servers have you played on?:\nWill you be active in Discord and do you want to participate in group events?:\nHow much time can you play a week? (estimated):\nBriefly explain your plans for this server:\n\nWhere did you find out about Hydro SMP? (If it is a website, post the link):\nIf it was on Reddit, what is your Reddit username?```')
    await applications.send('Copy this template ^ and post it in this channel when you are done filling it in! :white_check_mark:')

@client.event
async def on_member_remove(member):
    welcome = client.get_channel(621326188555796481)
    await welcome.send(f'Goodbye {member.mention}... May we meet again :sob:')

@client.command()
@commands.has_role('Staff')
async def accept(ctx, member: discord.Member):
    members = discord.utils.get(ctx.guild.roles, name='Members')
    applicants = discord.utils.get(ctx.guild.roles, name='Applicants')
    channel = client.get_channel(494184372258471938)
    info = '<#584773749497266199>'
    await member.remove_roles(applicants)
    await member.add_roles(members)
    await channel.send(f'Please welcome {member.mention} to **Hydro Vanilla SMP**! Our IP and Information can be found in {info}! :smiley:')

@accept.error
async def accept_error(member, error):
    if isinstance(error, commands.MissingRole):
        await member.send("You don't have the permissions to do that!")

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 771114709603713035:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
        member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)

        if payload.emoji.name == 'Hydropepecglock':
            role = discord.utils.get(guild.roles, name='True Server Crasher...')
        elif payload.emoji.name == 'tehlo':
            role = discord.utils.get(guild.roles, name="'Story of Teflon'")
        elif payload.emoji.name == 'blamenate':
            role = discord.utils.get(guild.roles, name='#PraiseNate')
        elif payload.emoji.name == '🛒':
            role = discord.utils.get(guild.roles, name='Shopaholics')
        elif payload.emoji.name == '🇳🇱':
            role = discord.utils.get(guild.roles, name='Dutchie')
        elif payload.emoji.name == '🍰':
            role = discord.utils.get(guild.roles, name='Food Addicts')
        elif payload.emoji.name == 'reddit':
            role = discord.utils.get(guild.roles, name='Subreddit Member')
        elif payload.emoji.name == 'HydroTwitch':
            role = discord.utils.get(guild.roles, name='Stream Fans')
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

@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 771114709603713035:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
        member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)

        if payload.emoji.name == 'Hydropepecglock':
            role = discord.utils.get(guild.roles, name='True Server Crasher...')
        elif payload.emoji.name == 'tehlo':
            role = discord.utils.get(guild.roles, name="'Story of Teflon'")
        elif payload.emoji.name == 'blamenate':
            role = discord.utils.get(guild.roles, name='#PraiseNate')
        elif payload.emoji.name == '🛒':
            role = discord.utils.get(guild.roles, name='Shopaholics')
        elif payload.emoji.name == '🇳🇱':
            role = discord.utils.get(guild.roles, name='Dutchie')
        elif payload.emoji.name == '🍰':
            role = discord.utils.get(guild.roles, name='Food Addicts')
        elif payload.emoji.name == 'reddit':
            role = discord.utils.get(guild.roles, name='Subreddit Member')
        elif payload.emoji.name == 'HydroTwitch':
            role = discord.utils.get(guild.roles, name='Stream Fans')
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

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
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

@client.command()
@commands.has_role('botadmin')
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
@commands.has_role('botadmin')
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("You don't have the permissions to do that!")

@unload.error
async def unload_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("You don't have the permissions to do that!")

for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


if __name__ == '__main__':
    import config
    client.run(config.token)