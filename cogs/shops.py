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

    @storeedit.error
    async def storeedit_error(self, username, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await username.send('You have to provide the Item Name, Quantity, and Price (in Diamonds)!')

    @commands.command(aliases=['itemlookup'])
    async def storeitemlookup(self, ctx, item):
        db = mysql.connector.connect(
            host = credentials.host,
            port = credentials.port,
            user = credentials.user,
            password = credentials.password,
            database = credentials.database
        )
        mycursor = db.cursor()

        # Checks if Item is in Library of Minecraft Items
        mycursor.execute(f"SELECT EXISTS (SELECT Item FROM Item_List WHERE Item='{str(item)}')")
        data = mycursor.fetchall()

        if not data[0][0]:
            # Assume the user did a misspell, and suggests an item from the list
            mycursor.execute(f"SELECT Item FROM Item_List WHERE Item SOUNDS LIKE '{str(item)}' LIMIT 1")
            data = mycursor.fetchall()
            if len(data) != 0:
                await ctx.send(f"Did you mean to look up \"{str(data[0][0])}\"? Try running this command: `!storeitemlookup \"{str(data[0][0])}\"`")
            else:
                await ctx.send("I\'m not sure what you're trying to lookup. Try another search term.")
        else:
            # Item exists in Library, display all listings for said item lookup
            mycursor.execute(f"SELECT EXISTS (SELECT StoreName, Quantity, Price, Description FROM Item_Listings WHERE Item='{str(item)}')")
            data = mycursor.fetchall()

            if data[0][0]:
                mycursor.execute(f"SELECT StoreName, Quantity, Price, Description FROM Item_Listings WHERE Item='{str(item)}'")
                data = mycursor.fetchall()
                embeditemlookup = discord.Embed(
                    title = 'Store Item Lookup',
                    description = f'Showing all store listings for {item}.',
                    colour = discord.Colour.from_rgb(12,235,241)
                )
                for row in data:
                    embeditemlookup.add_field(name=row[0], value=f"Quantity: {str(row[1])} \n Price: {str(row[2])} \n Description: {str(row[3])}", inline=False)
                await ctx.send(embed=embeditemlookup)
            else:
                await ctx.send(f"No one is currently selling any {str(item)}s.")

    @storeitemlookup.error
    async def storeitemlookup_error(self, username, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await username.send('Make sure to either have either a one word search term, or enclose your search term in quotations, like this:\n`!itemlookup "search term"`')

    @commands.command(aliases=['storeremoveitem'])
    async def storeremove(self, ctx, item):
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
            storename = data[0][2]
            # Checks if Item is in Library of Minecraft Items
            mycursor.execute(f"SELECT EXISTS (SELECT Item FROM Item_List WHERE Item='{str(item)}')")
            data = mycursor.fetchall()

            if not data[0][0]:
                # Assume the user did a misspell, and suggests an item from the list
                mycursor.execute(f"SELECT Item FROM Item_List WHERE Item SOUNDS LIKE '{str(item)}' LIMIT 1")
                data = mycursor.fetchall()
                if len(data) != 0:
                    await ctx.send(f"Did you mean to remove \"{str(data[0][0])}\" from your store? Try running this command: `!storeremove \"{str(data[0][0])}\"`")
                else:
                    await ctx.send("I\'m not sure what you're trying to remove. Try another search term.")
            else:
                # Try to remove item from store
                mycursor.execute(f"SELECT EXISTS (SELECT * FROM Item_Listings WHERE Item='{str(item)}' AND StoreName='{str(storename)}')")
                data = mycursor.fetchall()
                if not data[0][0]:
                    await ctx.send(f"You do not have any {str(item)}s in your store.")
                else:
                    mycursor.execute(f"DELETE FROM Item_Listings WHERE Item='{str(item)}' AND StoreName='{str(storename)}'")
                    db.commit()
                    deleteresult = mycursor.fetchall()
                    print(deleteresult)
                    if deleteresult: 
                        await ctx.send(f"Successfully removed {str(item)} from your store.")
                    else:
                        await ctx.send("Something happened when trying to remove an item from your store. Contact an Admin for help.")

    @storeedit.error
    async def storeremove_error(self, username, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await username.send('Make sure to either have either a one word search term, or enclose your search term in quotations, like this:\n`!storeremove "search term"`')

def setup(client):
    client.add_cog(Shops(client))