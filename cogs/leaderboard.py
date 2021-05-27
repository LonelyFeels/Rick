import discord
from discord.ext import commands
import json


class Leaderboard(commands.Cog):

    def __init__(self,client):
        self.client = client


    #Commands
    @commands.command()
    @commands.has_any_role('Staff', 'GameMaster')
    async def lbregister(self, ctx, member: discord.Member):
        with open('leaderboard.json', 'r', encoding='utf8') as file:
            users = json.load(file)
            if str(member.id) in users:
                await ctx.send('Member is already registered in GuildWars database!')
            else:
                with open('leaderboard.json', 'w', encoding='utf8') as file:
                    users = {}
                    users[str(member.id)] = {}
                    users[str(member.id)]['points'] = 0
                    json.dump(users, file, sort_keys=True, indent=4, ensure_ascii=False)
                    await ctx.send(f'@{member} successfully registered into GuildWars.')

    @lbregister.error
    async def lbregister_error(self, member, error):
        if isinstance(error, commands.MissingRole):
            await member.send('You don\'t have the permissions to do that!')
        if isinstance(error, commands.MissingRequiredArgument):
            await member.send('You have to mention the Member you want to add to the database!')

    @commands.command()
    @commands.has_any_role('Staff', 'GameMaster')
    async def lbunregister(self, ctx, member: discord.Member):
        with open('leaderboard.json', 'r', encoding='utf8') as file:
            users = json.load(file)
            if not str(member.id) in users:
                await ctx.send('Member hasn\'t been registered to Guild Wars database yet!')
            else:
                users.pop(str(member.id))
                with open('leaderboard.json', 'w', encoding='utf8') as file:
                    json.dump(users, file, indent=4)
                    await ctx.send(f'@{member} successfully unregistered from GuildWars.')

    @commands.command()
    @commands.has_any_role('Staff', 'GameMaster')
    async def lbadd(self, ctx, member: discord.Member, number:int):
        with open('leaderboard.json', 'r') as file:
            users = json.load(file)
            if str(member.id) in users:
                users[str(member.id)]['points'] = users[str(member.id)]['points'] + number
                upoints = users[str(member.id)]['points']
                with open('leaderboard.json', 'w') as file:
                    json.dump(users, file, sort_keys=True, indent=4, ensure_ascii=False)
                await ctx.send(f'Successfully updated @{member}\'s points to {upoints}.')
            else:
                await ctx.send(f'@{member} is not in the GuildWars database. Let me add them for you.')
                with open('leaderboard.json', 'w', encoding='utf8') as file:
                    users = {}
                    users[str(member.id)] = {}
                    users[str(member.id)]['points'] = number
                    json.dump(users, file, sort_keys=True, indent=4, ensure_ascii=False)
                    await ctx.send(f'@{member} successfully registered into GuildWars with starting points of {number}.')
    
    @lbadd.error
    async def lbadd_error(self, member, error):
        if isinstance(error, commands.MissingRole):
            await member.send('You don\'t have the permissions to do that!')
        if isinstance(error, commands.MissingRequiredArgument):
            await member.send('You have to mention the Member you want to add points to and put down the number of points!')

    @commands.command()
    @commands.has_any_role('Staff', 'GameMaster')
    async def lbsubtract(self, ctx, member: discord.Member, number:int):
        with open('leaderboard.json', 'r') as file:
            users = json.load(file)
            if str(member.id) in users:
                users[str(member.id)]['points'] = users[str(member.id)]['points'] - number
                upoints = users[str(member.id)]['points']
                with open('leaderboard.json', 'w') as file:
                    json.dump(users, file, sort_keys=True, indent=4, ensure_ascii=False)
                await ctx.send(f'Successfully updated @{member}\'s points to {upoints}.')
            else:
                await ctx.send(f'@{member} is not in the GuildWars database. Let me add them for you.')
                with open('leaderboard.json', 'w', encoding='utf8') as file:
                    users = {}
                    users[str(member.id)] = {}
                    users[str(member.id)]['points'] = number
                    json.dump(users, file, sort_keys=True, indent=4, ensure_ascii=False)
                    await ctx.send(f'@{member} successfully registered into GuildWars with starting points of -{number}.')

    @lbsubtract.error
    async def lbsubtract_error(self, member, error):
        if isinstance(error, commands.MissingRole):
            await member.send('You don\'t have the permissions to do that!')
        if isinstance(error, commands.MissingRequiredArgument):
            await member.send('You have to mention the Member you want to subtract points from and put down the number of points!')

    @commands.command()
    @commands.has_any_role('Staff', 'GameMaster')
    async def lbreset(self, ctx, member: discord.Member):
        with open('leaderboard.json', 'r') as file:
            users = json.load(file)
            if str(member.id) in users:
                users[str(member.id)]['points'] = 0
                with open('leaderboard.json', 'w') as file:
                    json.dump(users, file, sort_keys=True, indent=4, ensure_ascii=False)
                await ctx.send(f'Successfully updated @{member}\'s points to 0.')
            else:
                await ctx.send(f'@{member} is not in the GuildWars database. Let me add them for you.')
                with open('leaderboard.json', 'w', encoding='utf8') as file:
                    users = {}
                    users[str(member.id)] = {}
                    users[str(member.id)]['points'] = 0
                    json.dump(users, file, sort_keys=True, indent=4, ensure_ascii=False)
                    await ctx.send(f'@{member} successfully registered into GuildWars with starting points of 0.')

    @lbreset.error
    async def lbreset_error(self, member, error):
        if isinstance(error, commands.MissingRole):
            await member.send('You don\'t have the permissions to do that!')
        if isinstance(error, commands.MissingRequiredArgument):
            await member.send('You have to mention the Member you want to reset points to!')



def setup(client):
    client.add_cog(Leaderboard(client))