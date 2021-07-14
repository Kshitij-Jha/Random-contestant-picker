import os
import discord
import random
from keep_running import keep_alive

my_secret = os.environ['TOKEN']
client = discord.Client()

def add(msg):
  arr = msg.split(',')
  counter = str(len(arr))
  random.shuffle(arr)
  separator = ','
  arr = separator.join(arr)
  f = open("contestants.txt",'w')
  f.truncate(0)
  f.write(msg.strip())
  f.write("\n")
  f.write(arr.strip())
  f.write("\n")
  f.write(counter+"\n")
  f.close()

'''def replace(msg):
  arr = msg.split(',')
  counter = str(len(arr))
  random.shuffle(arr)
  separator = ','
  arr = separator.join(arr)
  f = open('contestants.txt', 'w')
  f[1].write(arr)'''

@client.event

async def on_ready():
  print('we have logged in as {0.user}'.format(client) )

@client.event

async def on_message(message):

  if message.author == client.user:
    return

  if message.content.startswith('!list'):
    await message.channel.send('**!list:** List all commands \n**!test:** Check if bot is online \n**!contestants:** Display the list of current contestants  \n**!add:** add contestants make sure separated by commas (need to use this once at the beginning of every round)...until further updates \n**!new:** add a new contestant  \n**!p:** pick random contestant')

  if message.content.startswith('!test'):
    await message.channel.send('Bot online')

  if message.content.startswith('!fishie'):
    if str(message.author) == 'BipolarBear#6749' or str(message.author) == 'littlefish#4767':
      with open('tenor.gif', 'rb') as f:
        picture = discord.File(f)
      f.close()
      await message.channel.send('<@!809248682838982687> Bear sends :kissing_heart:', file=picture)

  if message.content.startswith('!bear'):
    if str(message.author) == 'BipolarBear#6749' or str(message.author) == 'littlefish#4767':   
      with open('milk-and-mocha-kiss.gif', 'rb') as f:
        picture = discord.File(f)
      f.close()
      await message.channel.send('<@!432162806691921921> Fishie sends :kissing_heart:', file=picture)

  if message.content.startswith('!contestants'):
    f = open("contestants.txt",'r')
    msg = f.readlines()[0]
    f.close()
    await message.channel.send(msg)

  if message.content.startswith('!add'):
    msg = message.content[5:]
    add(msg)
    await message.channel.send('*Contestants added*')

  if message.content.startswith('!new'):
    new = message.content[5:]
    f = open("contestants.txt",'r')
    msg = f.readlines()[0].strip()
    f.close()
    msg = msg.split(",")
    if new not in msg:
      msg.append(new)
    else:
      await message.channel.send("*Player already in list*")
      return
    separator = ','
    msg = separator.join(msg)
    add(msg)
    await message.channel.send("**"+new+"** " + '*has been added to list*')

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
    f.close()
    await message.channel.send(msg[counter])
    if counter == 0:
      f = open('contestants.txt', 'r+')
      msg = f.readlines()[0].strip()
      f.truncate(0)
      f.close()
      add(msg)

keep_alive()
client.run(my_secret)