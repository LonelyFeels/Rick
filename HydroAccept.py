import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '!', intents=intents)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb,
    activity=discord.Activity(type=discord.ActivityType.watching, name="Commands | !help"))
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name='Members')
    welcome = client.get_channel(621326188555796481)
    applications = client.get_channel(494184460275941377)
    info = '<#584777370557349898>'
    await member.add_roles(role)
    await welcome.send(f'Welcome {member.mention} to **Hydro Vanilla SMP!** :hydrosmp:')
    await applications.send(f'Welcome {member.mention} to **Hydro Vanilla SMP** :hydrosmp:! \n**Make sure to read** {info} **to check on how to Apply!**')
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


if __name__ == '__main__':
    import config
    client.run(config.token)