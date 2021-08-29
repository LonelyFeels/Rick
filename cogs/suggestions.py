import discord
from discord.ext import commands


class Suggestions(commands.Cog):

    def __init__(self,client):
        self.client = client


    #Commands
    @commands.command()
    async def suggest(self, ctx, *, suggestion):
        channel = self.client.get_channel(651831753258041365)
        author = ctx.message.author
        author_icon = author.avatar_url
        embedsuggest = discord.Embed(
            title = '👍 Upvote | 👎 Downvote',
            description = 'Suggest features to Hydro with `!suggest <suggestion>`',
            colour = discord.Colour.from_rgb(12,235,241)
        )

        embedsuggest.set_footer(text=f'@ Hydro Vanilla SMP', icon_url='https://i.imgur.com/VkgebnW.png')
        embedsuggest.set_thumbnail(url=f'{author_icon}')
        embedsuggest.set_author(name=f'{author}', icon_url=f'{author_icon}')
        embedsuggest.add_field(name=f'_ _', value='_ _', inline=False)
        embedsuggest.add_field(name=f'Suggestion', value=f'{suggestion}', inline=False)

        suggestion_message = await channel.send(embed=embedsuggest)
        await suggestion_message.add_reaction(emoji='\N{THUMBS UP SIGN}')
        await suggestion_message.add_reaction(emoji='\N{THUMBS DOWN SIGN}')

    @suggest.error
    async def suggest_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You have to suggest something in order to use this command.')
        else:
            raise error

def setup(client):
    client.add_cog(Suggestions(client))