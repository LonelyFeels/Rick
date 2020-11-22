import discord
import os
from discord.ext import commands
import asyncio


intents = discord.Intents.default()
intents.members = True
intents.presences = True
client = commands.Bot(command_prefix = '!', intents=intents, help_command=None)


@client.event
async def on_ready():
    guild = client.get_guild(494184372258471936)
    online_channel = client.get_channel(615522198073114625)
    total_channel = client.get_channel(615522151742701590)
    bot_channel = client.get_channel(615522220672024612)
    async def count_users_task():
        while True:
            members = [m.status for m in guild.members]
            bots = [m.status for m in guild.members if m.bot]
            await online_channel.edit(name = f'Online Users: {members.count(discord.Status.online)+members.count(discord.Status.idle)+members.count(discord.Status.do_not_disturb)}')
            await total_channel.edit(name = f'Total Users: {len(client.users)}')
            await bot_channel.edit(name = f'Bots: {bots.count(discord.Status.online)+bots.count(discord.Status.idle)+bots.count(discord.Status.do_not_disturb)}')
            await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.watching, name=f'{len(client.users)} Hydro Members'))
            await asyncio.sleep(1200)
    client.loop.create_task(count_users_task())
    print('Bot is ready.')

@client.command()
async def count(ctx):
    guild = client.get_guild(494184372258471936)
    members = [m.status for m in guild.members]
    await ctx.send(f'Online Members: {members.count(discord.Status.online)}\nIdle Members: {members.count(discord.Status.idle)}\nDo not disturb Members: {members.count(discord.Status.do_not_disturb)}\nOffline Members: {members.count(discord.Status.offline)}')

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