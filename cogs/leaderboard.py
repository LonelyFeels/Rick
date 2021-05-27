import discord
from discord.ext import commands
import json


class Leaderboard(commands.Cog):

    def __init__(self,client):
        self.client = client


    #Commands
    @commands.command()
    @commands.has_any_role('Staff', 'GameMaster')
    async def lbm(self, ctx, member: discord.Member):
        with open('leaderboard.json', 'w', encoding='utf8') as file:
            user = {}
            user[str(member.id)] = {}
            user[str(member.id)]['points'] = 0
            json.dump(user, file, sort_keys=True, indent=4, ensure_ascii=False)

    @lbm.error
    async def lbm_error(self, member, error):
        if isinstance(error, commands.MissingRole):
            await member.send('You don\'t have the permissions to do that!')
        if isinstance(error, commands.MissingRequiredArgument):
            await member.send('You have to mention the Member you want to add to the database.')

    @commands.command()
    @commands.has_any_role('Staff', 'GameMaster')
    async def lba(self, number, member: discord.Member):
        try:
            with open('leaderboard.json', 'r', encoding='utf8') as file:
                user = json.load(file)
            with open('leaderboard.json', 'w', encoding='utf8') as file:
                user[str(member.id)]['points'] = user[str(member.id)]['points'] + number
                json.dump(user, file, sort_keys=True, indent=4, ensure_ascii=False)
        except:
            await member.send(f'{member} is not in the database. Let me add them for you.')
            with open('leaderboard.json', 'r', encoding='utf8') as file:
                user = json.load(file)
            with open('leaderboard.json', 'w', encoding='utf8') as file:
                user = {}
                user[str(member.id)] = {}
                user[str(member.id)]['points'] = 0
                json.dump(user, file, sort_keys=True, indent=4, ensure_ascii=False)
            with open('leaderboard.json', 'w', encoding='utf8') as file:    
                user[str(member.id)]['points'] = user[str(member.id)]['points'] + number
                json.dump(user, file, sort_keys=True, indent=4, ensure_ascii=False)
    
    @lba.error
    async def lba_error(self, member, error):
        if isinstance(error, commands.MissingRole):
            await member.send('You don\'t have the permissions to do that!')
        if isinstance(error, commands.MissingRequiredArgument):
            await member.send('You have to put down points and mention Member you want to add points.')

    @commands.command()
    @commands.has_any_role('Staff', 'GameMaster')
    async def lbs(self, number, member: discord.Member):
        try:
            with open('leaderboard.json', 'r', encoding='utf8') as file:
                user = json.load(file)
            with open('leaderboard.json', 'w', encoding='utf8') as file:
                user[str(member.id)]['points'] = user[str(member.id)]['points'] - number
        except:
            await member.send(f'{member} is not in the database. Let me add them for you.')
            with open('leaderboard.json', 'w', encoding='utf8') as file:
                user = {}
                user[str(member.id)] = {}
                user[str(member.id)]['points'] = 0
                json.dump(user, file, sort_keys=True, indent=4, ensure_ascii=False)

    @lbs.error
    async def lbs_error(self, member, error):
        if isinstance(error, commands.MissingRole):
            await member.send('You don\'t have the permissions to do that!')
        if isinstance(error, commands.MissingRequiredArgument):
            await member.send('You have to put down points and mention Member you want to subtract points.')


def setup(client):
    client.add_cog(Leaderboard(client))