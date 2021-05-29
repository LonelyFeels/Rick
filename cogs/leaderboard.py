import discord
from discord.ext import commands
import mysql.connector
import mysqlcredentials


class Leaderboard(commands.Cog):

    def __init__(self,client):
        self.client = client


    #Commands
    @commands.command()
    @commands.has_any_role('Staff', 'GameMaster')
    async def lbregister(self, ctx, member: discord.Member):
        db = mysql.connector.connect(
            host = mysqlcredentials.host,
            port = mysqlcredentials.port,
            user = mysqlcredentials.user,
            password = mysqlcredentials.password,
            database = mysqlcredentials.database
        )
        mycursor = db.cursor()

        mycursor.execute(f"SELECT * FROM User WHERE id={str(member.id)}")
        data = mycursor.fetchall()
        if len(data)==0:
            mycursor.execute("INSERT INTO User (id, points) VALUES (%s, %s)", (f"{member.id}", 0))
            db.commit()
        else:
            await ctx.send('Member is already registered in GuildWars database!')


def setup(client):
    client.add_cog(Leaderboard(client))