#potato_bot.py
import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    send_msgs.start()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


@tasks.loop(seconds=1)
async def send_msgs():
    print("Entered loop")
    message_channel = client.get_channel(710331553401798689)
    print(message_channel)
    await message_channel.send("Hello")



client.run(os.getenv('TOKEN'))

