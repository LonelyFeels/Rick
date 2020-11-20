import discord
import os
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '!', intents=intents, help_command=None)


@client.event
async def on_ready():
    member_count = sum(1 for _ in client.get_all_members())
    await client.change_presence(status=discord.Status.do_not_disturb,
    activity=discord.Activity(type=discord.ActivityType.watching, name=f'{member_count} Hydro Members'))
    print('Bot is ready.')

@client.event
async def on_member_join(member: discord.Member):
    total_users = sum(1 for _ in client.get_all_members())
    total_channel = client.get_channel(615522151742701590)
    await total_channel.edit(name = f'Total Users: {total_users}')

@client.event
async def on_member_remove(member: discord.Member):
    total_users = sum(1 for _ in client.get_all_members())
    total_channel = client.get_channel(615522151742701590)
    await total_channel.edit(name = f'Total Users: {total_users}')

@client.event
async def on_member_update(member: discord.Member):
    online_users = sum(member.status!=discord.Status.offline and not member.bot for member in client.get_all_members)
    online_channel = client.get_channel(615522198073114625)
    await online_channel.edit(name = f'Online Users: {online_users}')

@client.command()
@commands.has_role('botadmin')
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'You have loaded {extension}')

@client.command()
@commands.has_role('botadmin')
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'You have unloaded {extension} category.')

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