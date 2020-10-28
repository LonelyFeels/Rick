import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb,
    activity=discord.Activity(type=discord.ActivityType.watching, name="Commands | !help"))
    print('Bot is ready.')

@client.event
async def on_member_join(ctx):
    role = discord.utils.get(ctx.guild.roles, name='Applicants')
    await ctx.add_roles(role)

@client.command()
@commands.has_role('Staff')
async def accept(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name='Members')
    applicants = discord.utils.get(ctx.guild.roles, name='Applicants')
    channel = client.get_channel(494184372258471938)
    info = '<#584773749497266199>'
    await member.remove_roles(applicants)
    await member.add_roles(role)
    await channel.send(f'Please welcome {member.mention} to **Hydro Vanilla SMP**! Our IP and Information can be found in {info}! :smiley:')


if __name__ == '__main__':
    import config
    client.run(config.token)