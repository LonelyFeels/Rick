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

        # Rejection reasons: Store already exists under another owner OR the user is making another new store and they're already the owner of one

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

    # !storeedit [storename] [item] [quantity] [price] [description] or !sedit [storename] [item] [quantity] [price] [description]
    @commands.command(aliases=['sedit'])
    async def storeedit(self, ctx, storename, item, quantity:int, price:int, description=None):
        db = mysql.connector.connect(
            host = credentials.host,
            port = credentials.port,
            user = credentials.user,
            password = credentials.password,
            database = credentials.database
        )
        mycursor = db.cursor()
        owner = ctx.message.author
        print(owner)

        print(f"Start command: storeedit({str(storename)}, {str(item)}, {str(quantity)}, {str(price)}, {str(description)})")

        mycursor.execute(f"SELECT * FROM Store_Directory WHERE UserID={str(owner.id)} AND StoreName='{str(storename)}'")
        data = mycursor.fetchall()
        dataempty = [] == data
        print("test")
        print(data)
        if len(data) == 0:
            print("ID Failed.")
            await ctx.send('Either I could not find a store with that name or you are not a member of that store.')
        else:
            print("ID Succeeded.")
            storename = data[0][2]
            # Checks if Item is in Library of Minecraft Items
            mycursor.execute(f"SELECT EXISTS (SELECT Item FROM Item_List WHERE Item='{str(item)}')")
            data = mycursor.fetchall()

            if not data[0][0]:
                print("Misspell.")
                # Assume the user did a misspell, and suggests an item from the list
                mycursor.execute(f"SELECT Item FROM Item_List WHERE Item SOUNDS LIKE '{str(item)}' LIMIT 1")
                data = mycursor.fetchall()
                if len(data) != 0:
                    await ctx.send(f"Did you mean to update or add \"{str(data[0][0])}\" to your store? Try running this command: `!storeedit \"{str(data[0][0])}\" <quantity> <price>`")
                else:
                    await ctx.send("I\'m not sure what you're trying to update or add. Try another search term.")
            else:
                print("update or add")
                #try to update or add item to store
                mycursor.execute(f"SELECT EXISTS (SELECT * FROM Item_Listings WHERE Item='{str(item)}' AND StoreName='{str(storename)}')")
                itemexists = mycursor.fetchall()
                if itemexists[0][0]:
                    mycursor.execute(f"UPDATE Item_Listings SET Quantity={int(quantity)}, Price={int(price)}, Description='{str(description)}' WHERE Item='{str(item)}' AND StoreName='{str(storename)}'")
                    db.commit()
                    updateresult = mycursor.rowcount
                    if updateresult > 0:
                        await ctx.send(f'The listing for {quantity}x {item}\'s price was successfully updated to {price} Diamonds for the {storename} Store.')
                    else:
                        await ctx.send("Something happened when trying to add an item from your store. Contact an Admin for help.")
                else:
                    mycursor.execute("INSERT INTO Item_Listings (Item, StoreName, Quantity, Price, Description) VALUES (%s, %s, %s, %s, %s)", (item, storename, quantity, price, description))
                    db.commit()
                    addresult = mycursor.rowcount
                    if addresult > 0:
                        await ctx.send(f'A listing for {quantity}x {item} was successfully added at a price of {price} Diamonds for the {storename} Store.')
                    else:
                        await ctx.send("Something happened when trying to add an item from your store. Contact an Admin for help.")

    @storeedit.error
    async def storeedit_error(self, username, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await username.send('You have to provide the Store Name, Item Name, Quantity, and Price (in Diamonds)!')

    # !storeitemlookup [item] or !itemlookup [item] or !slookup [item]
    @commands.command(aliases=['itemlookup','slookup'])
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
                    embeditemlookup.set_footer(text=f'@ Hydro Vanilla SMP', icon_url='https://i.imgur.com/VkgebnW.png')
                    embeditemlookup.set_thumbnail(url='https://i.imgur.com/VkgebnW.png')
                    embeditemlookup.add_field(name=row[0], value=f"Quantity: {str(row[1])} \n Price: {str(row[2])} \n Description: {str(row[3])}", inline=False)
                await ctx.send(embed=embeditemlookup)
            else:
                await ctx.send(f"No one is currently selling any {str(item)}s.")

    @storeitemlookup.error
    async def storeitemlookup_error(self, username, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await username.send('Make sure to either have either a one word search term, or enclose your search term in quotations, like this:\n`!itemlookup "search term"`')

    # !storeremove [item] or !sr [item]
    @commands.command(aliases=['sr'])
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
                    deleteresult = mycursor.rowcount
                    if deleteresult > 0: 
                        await ctx.send(f"Successfully removed {str(item)} from your store.")
                    else:
                        await ctx.send("Something happened when trying to remove an item from your store. Contact an Admin for help.")

    @storeremove.error
    async def storeremove_error(self, username, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await username.send('Make sure to either have either a one word search term, or enclose your search term in quotations, like this:\n`!storeremove "search term"`')

    # !storecategories or !categories or !cat
    @commands.command(aliases=['categories', 'cat'])
    async def storecategories(self, ctx):
        db = mysql.connector.connect(
            host = credentials.host,
            port = credentials.port,
            user = credentials.user,
            password = credentials.password,
            database = credentials.database
        )
        mycursor = db.cursor()

        mycursor.execute(f"SELECT DISTINCT Category FROM Item_List")
        data = mycursor.fetchall()
        embedcategories = discord.Embed(
            title = 'Item Categories',
            colour = discord.Colour.from_rgb(12,235,241)
        )

        categorylist = ""
        for row in data:
            categorylist = categorylist + str(row[0]) + "\n"

        embedcategories.set_footer(text=f'@ Hydro Vanilla SMP', icon_url='https://i.imgur.com/VkgebnW.png')
        embedcategories.set_thumbnail(url='https://i.imgur.com/VkgebnW.png')
        embedcategories.add_field(name="Showing all item categories for the Store Listings", value=categorylist, inline=False)
        
        await ctx.send(embed=embedcategories)

    # !categoriesitems [category] or !cati [category]
    @commands.command(aliases=['cati'])
    async def categoriesitems(self, ctx, category):
        db = mysql.connector.connect(
            host = credentials.host,
            port = credentials.port,
            user = credentials.user,
            password = credentials.password,
            database = credentials.database
        )
        mycursor = db.cursor()

        # Checks if Item is in Library of Minecraft Items
        mycursor.execute(f"SELECT EXISTS (SELECT Category FROM Item_List WHERE Category='{str(category)}')")
        data = mycursor.fetchall()

        if not data[0][0]:
            # Assume the user did a misspell, and suggests an Category from the list
            mycursor.execute(f"SELECT Category FROM Item_List WHERE Category SOUNDS LIKE '{str(category)}' LIMIT 1")
            data = mycursor.fetchall()
            if len(data) != 0:
                await ctx.send(f"Did you mean to look up \"{str(data[0][0])}\"? Try running this command: `!cati \"{str(data[0][0])}\"`")
            else:
                await ctx.send("I\'m not sure what you're trying to lookup. Try another search term.")
        else:
            mycursor.execute(f"SELECT Item FROM Item_List WHERE Category='{str(category)}'")
            data = mycursor.fetchall()

            embedcitems = discord.Embed(
                title = f'Items in the {str(category)} Category',
                colour = discord.Colour.from_rgb(12,235,241)
            )
            embedcitems.set_footer(text=f'@ Hydro Vanilla SMP', icon_url='https://i.imgur.com/VkgebnW.png')
            embedcitems.set_thumbnail(url='https://i.imgur.com/VkgebnW.png')

            i = 1
            section = 1
            nextstring = data[0][0] + "\n"

            while i <= len(data):
                currentstring = ""
                while len(currentstring) + len(nextstring) < 1024 and i<= len(data):
                    currentstring = currentstring + nextstring
                    if i < len(data):
                        nextstring = str(data[i][0]) + "\n"
                    i += 1
                    # print(len(currentstring))
                    embedcitems.add_field(name=f"{str(category)} {str(section)}", value=currentstring, inline=False)
                    section += 1
            
            print(len(embedcitems))

            await ctx.send(embed=embedcitems)

    # !storeunregister or !sunreg
    @commands.command(aliases=['sunreg'])
    async def storeunregister(self, ctx):
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
            mycursor.execute(f"SELECT * FROM Item_Listings WHERE StoreName='{str(storename)}'")
            itemcount = mycursor.fetchall()
            if len(itemcount)==0:
                mycursor.execute(f"DELETE FROM Store_Directory WHERE UserID={str(owner.id)}")
                db.commit()
                deleteshop = mycursor.rowcount
                if deleteshop >0:
                    await ctx.send(f'Successfully unregistered store {storename}.')
                else:
                    await ctx.send('Something happened when trying to unregister your shop. Contact an Admin for help.')
            else:
                mycursor.execute(f"DELETE FROM Item_Listings WHERE StoreName='{str(storename)}'")
                db.commit()
                deleteresult = mycursor.rowcount
                if deleteresult > 0: 
                    await ctx.send(f"Successfully removed all items from your store.")
                    mycursor.execute(f"DELETE FROM Store_Directory WHERE UserID={str(owner.id)}")
                    db.commit()
                    deleteshop = mycursor.rowcount
                    if deleteshop >0:
                        await ctx.send(f'Successfully unregistered store {storename}.')
                    else:
                        await ctx.send('Something happened when trying to unregister your shop. Contact an Admin for help.')
                else:
                    await ctx.send("Something happened when trying to remove items from your store. Contact an Admin for help.")

    # !store
    @commands.command()
    async def store(self, ctx, storereference):
        db = mysql.connector.connect(
            host = credentials.host,
            port = credentials.port,
            user = credentials.user,
            password = credentials.password,
            database = credentials.database
        )
        mycursor = db.cursor()

        # To check if the user entered a user's tag, or a store name, we check size of string and beginning characters
        # 22 is the standard length of a member reference
        if len(storereference) == 22 and storereference[0:3] == "<@!":
            ownerid = storereference[3:21]
            mycursor.execute(f"SELECT EXISTS (SELECT * FROM Store_Directory WHERE UserID='{str(ownerid)}' AND IsOwner=1)")
            data = mycursor.fetchall()
            if not data[0][0]:
                await ctx.send("I could not find a store that is owned by that player.")
            else:
                mycursor.execute(f"SELECT StoreName FROM Store_Directory WHERE UserID='{str(ownerid)}' AND IsOwner=1 LIMIT 1")
                data = mycursor.fetchall()
                storename = data[0][0]

                # Store exists, display all listings for said item lookup
                mycursor.execute(f"SELECT EXISTS (SELECT Item, Quantity, Price, Description FROM Item_Listings WHERE StoreName='{str(storename)}')")
                data = mycursor.fetchall()

                if data[0][0]:
                    mycursor.execute(f"SELECT Item, Quantity, Price, Description FROM Item_Listings WHERE StoreName='{str(storename)}'")
                    data = mycursor.fetchall()
                    embedstoreup = discord.Embed(
                        title = 'Store Lookup',
                        description = f'Showing all listings for the {storename} store.',
                        colour = discord.Colour.from_rgb(12,235,241)
                    )
                    for row in data:
                        embedstoreup.set_footer(text=f'@ Hydro Vanilla SMP', icon_url='https://i.imgur.com/VkgebnW.png')
                        embedstoreup.set_thumbnail(url='https://i.imgur.com/VkgebnW.png')
                        embedstoreup.add_field(name=f"{str(row[0])}", value=f"Quantity: {str(row[1])} \n Price: {str(row[2])} \n Description: {str(row[3])}", inline=False)
                    await ctx.send(embed=embedstoreup)
                else:
                    await ctx.send(f"The {storename} store currently does not have any items for sale.")
        else:
            storename = storereference
            mycursor.execute(f"SELECT StoreName FROM Store_Directory WHERE StoreName='{str(storename)}' LIMIT 1")
            data = mycursor.fetchall()
            storename = data[0][0]

            if data[0][0]:
                # Store exists, display all listings for said item lookup
                mycursor.execute(f"SELECT EXISTS (SELECT Item, Quantity, Price, Description FROM Item_Listings WHERE StoreName='{str(storename)}')")
                data = mycursor.fetchall()

                if data[0][0]:
                    mycursor.execute(f"SELECT Item, Quantity, Price, Description FROM Item_Listings WHERE StoreName='{str(storename)}'")
                    data = mycursor.fetchall()
                    embedstoreup = discord.Embed(
                        title = 'Store Lookup',
                        description = f'Showing all listings for the {storename} store.',
                        colour = discord.Colour.from_rgb(12,235,241)
                    )
                    for row in data:
                        embedstoreup.set_footer(text=f'@ Hydro Vanilla SMP', icon_url='https://i.imgur.com/VkgebnW.png')
                        embedstoreup.set_thumbnail(url='https://i.imgur.com/VkgebnW.png')
                        embedstoreup.add_field(name=f"{str(row[0])}", value=f"Quantity: {str(row[1])} \n Price: {str(row[2])} \n Description: {str(row[3])}", inline=False)
                    await ctx.send(embed=embedstoreup)
                else:
                    await ctx.send(f"The {storename} store currently does not have any items for sale.")
            else:
                await ctx.send("There is no store under that name. Try again.")

def setup(client):
    client.add_cog(Shops(client))