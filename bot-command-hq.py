import nextcord
from nextcord.ext import commands
from keys import *


TESTING_GUILD_ID = 743467696179380376  # Replace with your guild ID

bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(description="bing", guild_ids=[TESTING_GUILD_ID])
async def bing(interaction: nextcord.Interaction):
    await interaction.send("bong !")

bot.run(gfm_token)
