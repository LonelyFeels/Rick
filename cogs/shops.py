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
    async def storeregister_error(self, username, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await username.send('You have state your Username, Storename (and Location)!')

    @commands.command()
    async def storeedit(self, ctx, item, quantity:int, price:int, description=None):
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
            await ctx.send('Your store does not exist in Stores database!')
        else:
            store = data[0][2]

            mycursor.execute(f"SELECT EXISTS (SELECT * FROM Item_Listings WHERE Item='{str(item)}' AND StoreName='{str(store)}')")
            itemexists = mycursor.fetchall()
            if itemexists[0][0]:
                mycursor.execute(f"UPDATE Item_Listings SET Quantity={int(quantity)}, Price={int(price)} WHERE Item='{str(item)}' AND StoreName='{str(store)}'")
                db.commit()
                await ctx.send(f'{quantity}x{item}\'s price successfully updated to {price} Diamonds in {store} Store.')
            else:
                mycursor.execute("INSERT INTO Item_Listings (Item, StoreName, Quantity, Price, Description) VALUES (%s, %s, %s, %s, %s)", (item, store, quantity, price, description))
                db.commit()
                await ctx.send(f'{quantity}x{item}\'s successfully added with price at {price} Diamonds in {store} Store.')


def setup(client):
    client.add_cog(Shops(client))