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
        await message.channel.send('List of couchmands: \n $help --List of commands \n +breakdown--Random breakdown to get your head spinning')
    elif message.content.startswith('+breakdown'):
        flip = random.choice([
            	'FUCK WITH THIS NEW BEAT!  \n    --------  \n    Pierce the Veil',
            	'DISRESPECT YOUR SURROUNDINGS!  \n    --------  \n    A Day to Remember',
            	'As low as I can get.  Burn the bridge.  Rip the stitch out.  PICK IT UP!  \n    --------  \n    Wage War',
		'LET THIS DESTROY ME!  \n    --------  \n    Fit for a King',
	 	'I THINK THE SILENCE SPEAKS VOLUMMMMMES    \n   --------  \n    While She Sleeps',
	 	'Say its a waste of time.  Say Ill never get a real shot.  ILL BE BANGING MY HEAD TIL MY BRAIN ROTS!    \n   --------  \n    Beartooth',
		'THIS.  IS.  SEMPITERNAL!!!!    \n   --------  \n    Bring Me the Horizon',
		'This is getting out of hand.  This is getting out of hand.  THIS IS GETTING OUT OF HAND.  ITS GETTING OUT OF HAND.  FUCK!!!    \n   --------  \n    Fever 333',
		'I always knew you were a coward, I knew you were a fake, a fraud.  I knew youd RUN LIKE A BIIITTCCCH.    \n   --------  \n    Devour the Day',
		'With the setting sun put the gun in my hand....DONT FAIL ME NOW    \n   --------  \n    blessthefall',
		'Just know if I could go back, this would all be different.  THIS WOULD ALL BE DIFFERENT.    \n   --------  \n    Memphis May Fire',
		'I THINK IM GONNA DIE HEEEEERRREEEE.    \n   --------  \n    Chelsea Grin'
           ])
        await message.channel.send(flip)
 


    if 'breakdown' in message.content:
        if message.author == client.user:
            #return if the bot is the author
            return
        else:
            emoji = '🛋'
            #emoji converter: https://www.fileformat.info/info/unicode/char/search.htm
            return await client.add_reaction(message, emoji)

client.run(TOKEN)
