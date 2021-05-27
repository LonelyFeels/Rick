import discord
from discord.ext import commands
import mysql.connector
import mysqlcredentials as msc


class Leaderboard(commands.Cog):

    def __init__(self,client):
        self.client = client


    #Commands
    @commands.command()
    @commands.has_any_role('Staff', 'GameMaster')
    async def lbregister(self, ctx, member: discord.Member):
        msc.connectdb()
        mycursor = msc.connectdb().db
        mycursor.execute("INSERT INTO User (id, points) VALUES (%s, %s)", (f"{member.id}", 0))
        mycursor.execute("SELECT * FROM User")
        for x in mycursor:
            print(x)


def setup(client):
    client.add_cog(Leaderboard(client))