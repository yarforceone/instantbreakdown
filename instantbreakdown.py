# Couch Bot by yarforceone
# ID: 639461334169157653
# Invite link: https://discordapp.com/api/oauth2/authorize?client_id=452124773699551254&scope=bot&permissions=1a

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
        await client.send_message(message.channel, 'List of couchmands: \n $help --List of commands \n +couch --Random couchie response \n !couch [phrase] --I tried to [phrase] once. I spent random time on the couch.')
    elif message.content.startswith('!breakdown'):
        flip = random.choice([
            "Some sweet couch time happening tonight!", 
            "That will land you on the couch for sure.", 
            "Yeah, I tried that once too and it earned me a full week of pillowy, fluffy couch time. :)", 
            "STANDBY FOR COUCHFALL!", 
            "Awe, no couch for you this time.", 
            "Hot tits! You earned the couch for the night!", 
            "Good news! Couch time is immanent!", 
            "Ready the loveseat. Couch time is coming!", 
            "Some call it a couch, my grandmother calls it a davenport, but regardless, you'll surely be sleeping on one tonight.",                 "Fvck yo couch. Sleep on mine instead!", 
            "Much couch. So fa.", 
            "Disregard females. Acquire chesterfields.", 
            "Ohhh, you gonna be chaising longue tonight!", 
            "Annnnd boom goes the dynamite. Couch tonight!", 
            "Sheeeeeeit, you gettin the couch!", 
            "All the couch are belong to you.", 
            "https://media.giphy.com/media/12oCddjphC1do4/giphy.gif"])
        await client.send_message(message.channel, flip)
    

    if 'breakdown' in message.content:
        if message.author == client.user:
            #return if the bot is the author
            return
        else:
            emoji = '🛋'
            #emoji converter: https://www.fileformat.info/info/unicode/char/search.htm
            return await client.add_reaction(message, emoji)

client.run(TOKEN)
