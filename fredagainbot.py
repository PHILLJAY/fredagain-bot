import random
import discord
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'fred' in message.content.lower():  
        await message.channel.send('hey its me fred again')
        return
    
    if random.random() < 0.02:
        embed = discord.Embed()
        embed.set_image(url='https://i.postimg.cc/h4ZvQmzJ/Fred-Again.jpg')
        await message.channel.send(embed=embed)

client.run(token)