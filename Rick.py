import discord
import os
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '.', intents=intents, help_command=None)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb,
    activity=discord.Activity(type=discord.ActivityType.listening, name="to Hydro Applications"))
    print('Bot is ready.')

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

@client.command()
async def iam(ctx, *, role):
    user = ctx.message.author
    role = discord.utils.get(ctx.guild.roles, name=f'{role}')
    if role in user.roles:
        await ctx.send(f"You already have {role} role.")
    else:
        await user.add_roles(role)
        await ctx.send(f"You've been given {role} role.")

for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


if __name__ == '__main__':
    import config
    client.run(config.token)