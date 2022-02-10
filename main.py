# bot.py
import os
import random
import discord

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user.name} has connected to: \n'
        f'{guild.name}(id: {guild.id})'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user: 
     # ensures no recursive loop where bot reacts to its own message 
        return
    
    #TODO: add more dune quotes lol
    dune_quotes = [
    "I must not fear. Fear is the mind-killer.",
    "He who controls the spice controls the universe.",
    "The people who can destroy a thing, they control it."
    ]   

    if (message.content).lower() == "dune":
        response = random.choice(dune_quotes)
        await message.channel.send(response)
    if (message.content).lower() == "tatakae":
        await message.channel.send("tatakae")
    elif message.content == 'raise-exception':
        raise discord.DiscordException   

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise   

client.run(TOKEN)