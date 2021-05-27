import discord
from discord.ext import commands
import json


class Leaderboard(commands.Cog):

    def __init__(self,client):
        self.client = client


    #Commands
    @commands.command()
    @commands.has_any_role('Staff', 'GameMaster')
    async def lbr(self, ctx, member: discord.Member):
        with open('leaderboard.json', 'r', encoding='utf8') as file:
            users = json.load(file)
            if str(member.id) in users:
                await ctx.send('Member is already registered in GuildWars database.')
            else:
                with open('leaderboard.json', 'w', encoding='utf8') as file:
                    users = {}
                    users[str(member.id)] = {}
                    users[str(member.id)]['points'] = 0
                    json.dump(users, file, sort_keys=True, indent=4, ensure_ascii=False)
                    await ctx.send(f'@{member} successfully registered into GuildWars.')

    @lbr.error
    async def lbm_error(self, member, error):
        if isinstance(error, commands.MissingRole):
            await member.send('You don\'t have the permissions to do that!')
        if isinstance(error, commands.MissingRequiredArgument):
            await member.send('You have to mention the Member you want to add to the database.')

    @commands.command()
    @commands.has_any_role('Staff', 'GameMaster')
    async def lba(self, ctx, member: discord.Member, number:int):
        with open('leaderboard.json', 'r') as file:
            users = json.load(file)

        users[str(member.id)]['points'] = users[str(member.id)]['points'] + number

        with open('leaderboard.json', 'w') as file:
            json.dump(users, file, sort_keys=True, indent=4, ensure_ascii=False)

        with open('leaderboard.json', 'r') as file:
            users = json.load

        await ctx.send(f'Successfully updated @{member}\'s points to' + {users[str(member.id)]['points']})


def setup(client):
    client.add_cog(Leaderboard(client))