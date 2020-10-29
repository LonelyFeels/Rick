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
            title = 'Upvode | Downvote',
            description = 'Suggest features to Hydro with `-suggest <suggestion>`',
            colour = discord.Colour.from_rgb(12,235,241)
        )

        embedsuggest.set_footer(text=f'@ Hydro Vanilla SMP', icon_url='https://hydrovanillasmp.com/wp-content/uploads/2019/06/HydroSMP_BaseLogo.png')
        embedsuggest.set_thumbnail(url=f'{author_icon}')
        embedsuggest.set_author(name=f'{author}', icon_url=f'{author_icon}')
        embedsuggest.set_image(url='https://i.imgur.com/kSWpxnG.gif')
        embedsuggest.add_field(name=f'Suggestion', value=f'{suggestion}', inline=False)

        suggestion_message = await channel.send(embedsuggest)
        await self.client.add_reaction(suggestion_message, emoji='👍')
        await self.client.add_reaction(suggestion_message, emoji='👎')

def setup(client):
    client.add_cog(Suggestions(client))