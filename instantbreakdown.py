# Couch Bot by yarforceone
# ID: 639461334169157653
# Invite link: https://discordapp.com/api/oauth2/authorize?client_id=639461334169157653scope=bot&permissions=1a

import discord
import asyncio
import random
from random import randint
import os
from discord.utils import get

TOKEN = 'token'

client = discord.Client()
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('$help'):
        await message.channel.send('List of couchmands: \n $help --List of commands \n +couch --Random couchie response \n !couch [phrase] --I tried to [phrase] once. I spent random time on the couch.')
    elif message.content.startswith('+couch'):
        flip = random.choice([
            'FUCK WITH THIS NEW BEAT!  \n    --------  \n    Pierce the Veil',
            'DISRESPECT YOUR SURROUNDINGS!  \n    --------  \n    A Day to Remember'
            'As low as I can get.  Burn the bridge.  Rip the stitch out.  PICK IT UP!  \n    --------  \n    Wage War'
           ])
        await message.channel.send(flip)
 

    if 'couch' in message.content:
        if message.author == client.user:
            #return if the bot is the author
            return
        else:
            emoji = '🛋'
            #emoji converter: https://www.fileformat.info/info/unicode/char/search.htm
            return await client.add_reaction(message, emoji)

client.run(TOKEN)
