import discord
from discord import client
from discord.ext import commands
import mysql.connector
import mysqlshopcredentials as credentials


class Shops(commands.Cog):

    def __init__(self,client):
        self.client = client


    #Commands
    @commands.command()
    async def storeregister(self, ctx, username, storename, location=None):
        db = mysql.connector.connect(
            host = credentials.host,
            port = credentials.port,
            user = credentials.user,
            password = credentials.password,
            database = credentials.database
        )
        mycursor = db.cursor()

        owner = ctx.message.author

        mycursor.execute(f"SELECT * FROM Store_Directory WHERE UserID={str(owner.id)}")
        data = mycursor.fetchall()
        if len(data)==0:
            mycursor.execute("INSERT INTO Store_Directory (UserID, Username, StoreName, Location) VALUES (%s, %s, %s, %s)", (f"{owner.id}", username, storename, location))
            db.commit()
            await ctx.send(f'{storename} successfully registered into Stores database.')
        else:
            await ctx.send('Store is already registered in Stores database!')

    @storeregister.error
    async def storeregister_error(self, member, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await member.send('You have state your Username, Storename (and Location)!')

    @commands.command()
    async def storeedit(self, ctx, item, price:int, description=None):
        db = mysql.connector.connect(
            host = credentials.host,
            port = credentials.port,
            user = credentials.user,
            password = credentials.password,
            database = credentials.database
        )
        mycursor = db.cursor()

        owner = ctx.message.author

        mycursor.execute(f"SELECT * FROM Store_Directory WHERE UserID={str(owner.id)}")
        data = mycursor.fetchall()
        store = data[0][2]

        mycursor.execute(f"SELECT * FROM Item_Listings WHERE Item={str(item)} AND StoreName={str(store)}")
        if len(data)==0:
            mycursor.execute("INSERT INTO Item_Listings (Item, StoreName, Price, Description) VALUES (%s, %s, %s, %s)", (f"{item}", f"{store}", f"{price}", f"{description}"))
            db.commit()
            await ctx.send(f'{item} successfully added to {price} Diamonds in {store} store.')
        else:
            mycursor.execute(f"UPDATE Item_Listings SET Price={int(price)} WHERE Item={str(item)} AND StoreName={str(store)}")
            db.commit()
            await ctx.send(f'{item} successfully updated to {price} Diamonds in {store} store.')


def setup(client):
    client.add_cog(Shops(client))