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
            await ctx.send(f'@{member} successfully registered into GuildWars.')
        else:
            await ctx.send('Member is already registered in GuildWars database!')

    @lbregister.error
    async def lbregister_error(self, member, error):
        if isinstance(error, commands.MissingRole):
            await member.send('You don\'t have the permissions to do that!')
        if isinstance(error, commands.MissingRequiredArgument):
            await member.send('You have to mention the Member you want to add to the database!')
    
    @commands.command()
    @commands.has_any_role('Staff', 'GameMaster')
    async def lbunregister(self, ctx, member: discord.Member):
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
            await ctx.send('Member hasn\'t been registered to Guild Wars database yet!')
        else:
            mycursor.execute(f"DELETE FROM User WHERE id={str(member.id)}")
            await ctx.send(f'@{member} successfully unregistered from GuildWars.')


def setup(client):
    client.add_cog(Leaderboard(client))