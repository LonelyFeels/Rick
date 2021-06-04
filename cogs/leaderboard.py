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
        if isinstance(error, commands.MissingAnyRole):
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
            db.commit()
            await ctx.send(f'@{member} successfully unregistered from GuildWars.')

    @lbunregister.error
    async def lbunregister_error(self, member, error):
        if isinstance(error, commands.MissingAnyRole):
            await member.send('You don\'t have the permissions to do that!')
        if isinstance(error, commands.MissingRequiredArgument):
            await member.send('You have to mention the Member you want to remove from the database!')

    @commands.command()
    @commands.has_any_role('Staff', 'GameMaster')
    async def lbadd(self, ctx, member: discord.Member, number:int):
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
            await ctx.send(f'@{member} is not in the GuildWars database. Let me add them for you.')
            mycursor.execute("INSERT INTO User (id, points) VALUES (%s, %s)", (f"{member.id}", number))
            db.commit()
            await ctx.send(f'@{member} successfully registered into GuildWars with starting points of {number}.')
        else:
            mycursor.execute(f"SELECT points FROM User WHERE id={str(member.id)}")
            points = mycursor.fetchall()[0][0]
            mycursor.execute(f"UPDATE User SET points={int(points)+number} WHERE id={str(member.id)}")
            db.commit()
            await ctx.send(f'Successfully updated @{member}\'s points to {int(points)+number}.')

    @lbadd.error
    async def lbadd_error(self, member, error):
        if isinstance(error, commands.MissingAnyRole):
            await member.send('You don\'t have the permissions to do that!')
        if isinstance(error, commands.MissingRequiredArgument):
            await member.send('You have to mention the Member you want to add points to and put down the number of points!')

    @commands.command()
    @commands.has_any_role('Staff', 'GameMaster')
    async def lbsubtract(self, ctx, member: discord.Member, number:int):
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
            await ctx.send(f'@{member} is not in the GuildWars database. Let me add them for you.')
            mycursor.execute("INSERT INTO User (id, points) VALUES (%s, %s)", (f"{member.id}", 0-number))
            db.commit()
            await ctx.send(f'@{member} successfully registered into GuildWars with starting points of -{number}.')
        else:
            mycursor.execute(f"SELECT points FROM User WHERE id={str(member.id)}")
            points = mycursor.fetchall()[0][0]
            mycursor.execute(f"UPDATE User SET points={int(points)-number} WHERE id={str(member.id)}")
            db.commit()
            await ctx.send(f'Successfully updated @{member}\'s points to {int(points)-number}.')

    @lbsubtract.error
    async def lbsubtract_error(self, member, error):
        if isinstance(error, commands.MissingRole):
            await member.send('You don\'t have the permissions to do that!')
        if isinstance(error, commands.MissingRequiredArgument):
            await member.send('You have to mention the Member you want to subtract points from and put down the number of points!')

    @commands.command()
    @commands.has_any_role('Staff', 'GameMaster')
    async def lbset(self, ctx, member: discord.Member, number:int):
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
            await ctx.send(f'@{member} is not in the GuildWars database. Let me add them for you.')
            mycursor.execute("INSERT INTO User (id, points) VALUES (%s, %s)", (f"{member.id}", number))
            db.commit()
            await ctx.send(f'@{member} successfully registered into GuildWars with starting points of {number}.')
        else:
            mycursor.execute(f"UPDATE User SET points={number} WHERE id={str(member.id)}")
            db.commit()
            await ctx.send(f'Successfully updated @{member}\'s points to {number}.')
    
    @lbset.error
    async def lbset_error(self, member, error):
        if isinstance(error, commands.MissingRole):
            await member.send('You don\'t have the permissions to do that!')
        if isinstance(error, commands.MissingRequiredArgument):
            await member.send('You have to mention the Member you want to set points to and put down the number!')

    @commands.command()
    @commands.has_any_role('Staff', 'GameMaster')
    async def lbreset(self, ctx, member: discord.Member):
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
            await ctx.send(f'@{member} is not in the GuildWars database. Let me add them for you.')
            mycursor.execute("INSERT INTO User (id, points) VALUES (%s, %s)", (f"{member.id}", 0))
            db.commit()
            await ctx.send(f'@{member} successfully registered into GuildWars with starting points of 0.')
        else:
            mycursor.execute(f"UPDATE User SET points=0 WHERE id={str(member.id)}")
            db.commit()
            await ctx.send(f'Successfully updated @{member}\'s points to 0.')
    
    @lbreset.error
    async def lbreset_error(self, member, error):
        if isinstance(error, commands.MissingRole):
            await member.send('You don\'t have the permissions to do that!')
        if isinstance(error, commands.MissingRequiredArgument):
            await member.send('You have to mention the Member you want to reset points to!')

    @commands.command()
    async def lbdisplay(self, ctx, member: discord.Member):
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
            await ctx.send(f'@{member} is not participating in Guild Wars!')
        else:
            mycursor.execute(f"SELECT points FROM User WHERE id={str(member.id)}")
            points = mycursor.fetchall()[0][0]

            member_icon = member.avatar_url
            embedlbdisplay = discord.Embed(
                title = 'Guild Wars Points',
                description = f'Check {member}\'s points from Guild Wars RP.',
                colour = discord.Colour.from_rgb(12,235,241)
            )

            embedlbdisplay.set_footer(text=f'@ Hydro Vanilla SMP', icon_url='https://i.imgur.com/VkgebnW.png')
            embedlbdisplay.set_thumbnail(url=f'{member_icon}')
            embedlbdisplay.set_author(name=f'{member}', icon_url=f'{member_icon}')
            embedlbdisplay.add_field(name=f'_ _', value='_ _', inline=False)
            embedlbdisplay.add_field(name=f'Points', value=f'{int(points)}', inline=False)

            await ctx.send(embed=embedlbdisplay)

    @lbdisplay.error
    async def lbdisplay_error(self, member, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await member.send('You have to mention the Member if you want to see their stats!')

    @commands.command()
    async def leaderboard(self, ctx):
        db = mysql.connector.connect(
            host = mysqlcredentials.host,
            port = mysqlcredentials.port,
            user = mysqlcredentials.user,
            password = mysqlcredentials.password,
            database = mysqlcredentials.database
        )
        mycursor = db.cursor()

        mycursor.execute("SELECT * FROM User ORDER BY points DESC")
        data = mycursor.fetchall()

        embedleaderboard = discord.Embed(
            title = 'Guild Wars Leaderboard',
            description = 'Check who\'s the best in Guild Wars RP.',
            colour = discord.Colour.from_rgb(12,235,241)
        )

        embedleaderboard.set_footer(text=f'@ Hydro Vanilla SMP', icon_url='https://i.imgur.com/VkgebnW.png')
        embedleaderboard.set_thumbnail(url='https://i.imgur.com/VkgebnW.png')
        embedleaderboard.add_field(name=f'1. {discord.Client.fetch_user((int(data[0][0])))}', value=f'{int(data[0][1])}', inline=False)
        embedleaderboard.add_field(name=f'2. {discord.guild.get_member(int(data[1][0]))}', value=f'{int(data[1][1])}', inline=False)

        await ctx.send(embed=embedleaderboard)


def setup(client):
    client.add_cog(Leaderboard(client))