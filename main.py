import os
import discord
import random
from keep_running import keep_alive

my_secret = os.environ['TOKEN']
client = discord.Client()

def add(msg):
    f = open("contestants.txt",'w')
    f.truncate(0)
    f.write(msg)
    arr = msg.split(',')
    counter = str(len(arr))
    random.shuffle(arr)
    separator = ','
    arr = separator.join(arr)
    f.write("\n")
    f.write(arr)
    f.write("\n")
    f.write(counter+'\n')
    f.close()

@client.event

async def on_ready():
  print('we have logged in as {0.user}'.format(client) )

@client.event

async def on_message(message):

  if message.author == client.user:
    return

  if message.content.startswith('!list'):
    await message.channel.send('**!list:** List all commands \n**!test:** Check if bot is online \n**!contestants:** Display the list of current contestants  \n**!add:** add contestants make sure separated by commas (need to use this once at the beginning of every round)...until further updates \n**!p:** pick random contestant')

  if message.content.startswith('!test'):
    await message.channel.send('Bot online')

  if message.content.startswith('!fishie'):
    if str(message.author) == 'BipolarBear#6749' or str(message.author) == 'littlefish#4767':
      await message.channel.send('@Fishie Bear sends :kissing_heart: ')

      with open('tenor.gif', 'rb') as f:
        picture = discord.File(f)
        await message.channel.send(file=picture)

  if message.content.startswith('!bear'):
    await message.channel.send('@Bear Fishie sends :kissing_heart: ')

  if message.content.startswith('!contestants'):
    f = open("contestants.txt",'r')
    msg = f.readlines()[0]
    await message.channel.send(msg)

  if message.content.startswith('!add'):
    msg = message.content[5:]
    add(msg)
    await message.channel.send('*Contestants added*')

  #if message.content.startswith('!addnew'):
  #if message.content.startswith('!remove'):

  if message.content.startswith('!p'):
    f = open("contestants.txt",'r')
    msg = f.readlines()[1]
    f = open("contestants.txt",'r')
    counter = int(f.readlines()[-1])
    counter -= 1
    f = open("contestants.txt",'a')
    f.writelines(str(counter) + '\n')
    msg = msg.split(",")
    #print(counter)
    await message.channel.send(msg[counter])
    if counter == 0:
      separator = ','
      msg = separator.join(msg)
      await message.channel.send("Round is over, Please use command **!add "+ msg + "** (just copy paste that) to start next round")

keep_alive()
client.run(my_secret)
