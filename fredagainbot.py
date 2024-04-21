import random
import discord
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('FRED_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

fredResponses = ('can you not ping me im djing', 'look im busy right now can we talk later', 'check this video out: https://www.youtube.com/watch?v=6b7C79Vxk6Q',
 'mfmmmfmm')


def fredOutput():
    if random.randint(0,len(fredResponses))==0:
        return f'check out this cool number: {random.randint(1,100)}'
    return random.choice(fredResponses) 
    

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'fred' in message.content.lower():  
        await message.channel.send(fredOutput())
        return
    
    if client.application_id in map(lambda x: x.id, message.mentions):
        await message.chanel.send('what do you want')

    if random.random() < 0.02:
        embed = discord.Embed()
        embed.set_image(url='https://i.postimg.cc/h4ZvQmzJ/Fred-Again.jpg')
        await message.channel.send(embed=embed)

    

client.run(token)