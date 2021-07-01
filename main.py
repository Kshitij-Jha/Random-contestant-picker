import os
import discord
import random
from keep_running import keep_alive

my_secret = os.environ['TOKEN']
client = discord.Client()

@client.event

async def on_ready():
  print('we have logged in as {0.user}'.format(client) )

@client.event

async def on_message(message):

  if message.author == client.user:
    return

  if message.content.startswith('!list'):
    await message.channel.send('**!list:** List all commands, **!test:** Check if bot is online, **!add:** add contestants make sure separated by commas, **!p:** pick random contestant')

  if message.content.startswith('!test'):
    await message.channel.send('Bot online')

  if message.content.startswith('!fishie'):
    await message.channel.send('@Fishie Bear sends :kissing_heart: ')

  if message.content.startswith('!bear'):
    await message.channel.send('@Bear Fishie sends :kissing_heart: ')
    #await channel.send(file=discord.File('tenor.gif')

  if message.content.startswith('!contestants'):
    f = open("contestants.txt",'r')
    msg = f.read()
    await message.channel.send(msg)

  if message.content.startswith('!add'):
    msg = message.content[4:]
    f = open("contestants.txt",'w')
    f.truncate(0)
    f.write(msg)
    f.close()
    await message.channel.send('*Contestants added*')

  #if message.content.startswith('!addnew'):
  #if message.content.startswith('!remove'):

  if message.content.startswith('!p'):
    f = open("contestants.txt",'r')
    msg = f.read()
    msg = msg.split(",")
    choice = random.choice(msg)
    await message.channel.send(choice)

keep_alive()
client.run(my_secret)
