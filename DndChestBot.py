#for Dnd ChestBot
import discord
import random
import time
from discord.ext import commands, tasks
 
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True
                          , presences = True)
client = commands.Bot(command_prefix = '_', intents = intents) 

#include your bot token here
botToken = 


@client.event
async def on_ready():
  activity = discord.Activity(name='your inventory fill', type=discord.ActivityType.watching)
  await client.change_presence(activity=activity)  
  print("Chest is up and running")
  load_inventory()
  activity = discord.Activity(name='your inventory', type=discord.ActivityType.watching)
  await client.change_presence(activity=activity)   
  
@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send("Sorry, I don't understand what you're asking. Please try again")
   
@client.command(help = "Checks latency")
async def ping(ctx):
  await ctx.send(f'Pong! {round(client.latency * 1000)} ms') 
  
@client.command(help = "Empty all items out of wallet or inventory. Example use: _empty inventory or _empty wallet")
async def empty(ctx, *, item):
  if item == 'inventory':
    open('inventory.txt', 'w').close()
    global inventory
    inventory = []
    await ctx.send("Your inventory has been emptied")
    print("inventory")
  elif item == 'wallet':
    open('wallet.txt', 'w').close()
    global balance
    balance = ['0','0','0','0','0']
    await ctx.send("Your wallet has been emptied")
  else:
    print("test")
    await ctx.send("Please specify if you'd like to empty your wallet or your inventory")

@client.command()
async def add(ctx, *, item):
  #adding item to the inventory, append it to the end
  await ctx.send(f"{item} is being added")
  load_inventory()
  
  if item[len(item)-2] == "c" and item[len(item)-1] == "p":
    print("its probably copper")
    if item[len(item)-3] == " ":
      value = item.replace(" cp","")
    else:
      value = item.replace("cp","")
    try:
      value = int(value)
    except:
      print("not money")
      await ctx.send(f"{item} was added to your inventory")
      addItem(item)
    else:
      addMoney(value, 0)
      await ctx.send(f"{item} was added to your wallet")
  
  elif item[len(item)-2] == "s" and item[len(item)-1] == "p":
    print("its probably silver")
    if item[len(item)-3] == " ":
      value = item.replace(" sp","")
    else:
      value = item.replace("sp","")
    try:
      value = int(value)
    except:
      print("not money")
      await ctx.send(f"{item} was added to your inventory")
      addItem(item)
    else:
      addMoney(value, 1)
      await ctx.send(f"{item} was added to your wallet")
      
  elif item[len(item)-2] == "e" and item[len(item)-1] == "p":
    print("its probably electrum")
    if item[len(item)-3] == " ":
      value = item.replace(" ep","")
    else:
      value = item.replace("ep","")
    try:
      value = int(value)
    except:
      print("not money")
      await ctx.send(f"{item} was added to your inventory")
      addItem(item)
    else:
      addMoney(value, 2)
      await ctx.send(f"{item} was added to your wallet")
      
  elif item[len(item)-2] == "g" and item[len(item)-1] == "p":
    print("its probably gold")
    if item[len(item)-3] == " ":
      value = item.replace(" gp","")
    else:
      value = item.replace("gp","")
    try:
      value = int(value)
    except:
      print("not money")
      await ctx.send(f"{item} was added to your inventory")
      addItem(item)
    else:
      addMoney(value, 3)
      await ctx.send(f"{item} was added to your wallet")
      
  elif item[len(item)-2] == "p" and item[len(item)-1] == "p":
    print("its probably plat")
    
    if item[len(item)-3] == " ":
      value = item.replace(" pp","")
    else:
      value = item.replace("pp","")
      
    try:
      int(value)
    except:
      print("not money")
      await ctx.send(f"{item} was added to your inventory")
      addItem(item)
    else:
      addMoney(int(value), 4)
      await ctx.send(f"{item} was added to your wallet")
  else:
    await ctx.send(f"{item} was added to your inventory")
    addItem(item)    


@client.command()
async def grab(ctx, *, item):
  #adding item to the inventory, append it to the end
  await ctx.send(f"{item} is being removed")
  load_inventory()
  
  if item[len(item)-2] == "c" and item[len(item)-1] == "p":
    print("its probably copper")
    if item[len(item)-3] == " ":
      value = item.replace(" cp","")
    else:
      value = item.replace("cp","")
    try:
      value = int(value)
    except:
      print("not money")
      await ctx.send(f"{item} was removed from your inventory")
      subItem(item)
    else:
      if value > int(balance[0]):
        await ctx.send("You don't have that much Copper")
      else:
        addMoney(value*-1, 0)
        await ctx.send(f"{item} was taken from your wallet")
      
  elif item[len(item)-2] == "s" and item[len(item)-1] == "p":
    print("its probably silver")
    if item[len(item)-3] == " ":
      value = item.replace(" sp","")
    else:
      value = item.replace("sp","")
    try:
      value = int(value)
    except:
      print("not money")
      await ctx.send(f"{item} was removed from your inventory")
      subItem(item)
    else:
      if value > int(balance[1]):
        await ctx.send("You don't have that much silver")
      else:
        addMoney(value*-1, 1)
        await ctx.send(f"{item} was taken from your wallet")
      
  elif item[len(item)-2] == "e" and item[len(item)-1] == "p":
    print("its probably electrum")
    if item[len(item)-3] == " ":
      value = item.replace(" ep","")
    else:
      value = item.replace("ep","")
    try:
      value = int(value)
    except:
      print("not money")
      await ctx.send(f"{item} was removed from your inventory")
      subItem(item)
    else:
      if value > int(balance[2]):
        await ctx.send("You don't have that much electrum")
      else:
        addMoney(value*-1, 2)
        await ctx.send(f"{item} was taken from your wallet")
      
  elif item[len(item)-2] == "g" and item[len(item)-1] == "p":
    print("its probably gold")
    if item[len(item)-3] == " ":
      value = item.replace(" gp","")
    else:
      value = item.replace("gp","")
    try:
      value = int(value)
    except:
      print("not money")
      await ctx.send(f"{item} was removed from your inventory")
      subItem(item)
    else:
      if value > int(balance[3]):
        await ctx.send("You don't have that much gold")
      else:
        addMoney(value*-1, 3)
        await ctx.send(f"{item} was taken from your wallet")
      
  elif item[len(item)-2] == "p" and item[len(item)-1] == "p":
    print("its probably plat")
    if item[len(item)-3] == " ":
      value = item.replace(" pp","")
    else:
      value = item.replace("pp","")
    try:
      value = int(value)
    except:
      print("not money")
      await ctx.send(f"{item} was removed from your inventory")
      test = subItem(item)
    else:
      if value > int(balance[4]):
        await ctx.send("You don't have that much platinum")
      else:
        addMoney(value*-1, 4)
        await ctx.send(f"{item} was taken from your wallet")
  
  
  else:
    if subItem(item): 
      await ctx.send(f"{item} was removed from your inventory")
    else:
      await ctx.send(f"{item} was not in your inventory")

      

    
  #appending to the file for inventory
def addItem(item):
  inventory.append(item)
  inventory.sort()
  open('inventory.txt', 'w').close()
  inventoryFile = open ("inventory.txt", "a")
  for x in inventory:
    inventoryFile.write(x + "\n")
  inventoryFile.close()
  
def subItem(item):
  try:
    inventory.remove(item)
    open('inventory.txt', 'w').close()
    inventoryFile = open ("inventory.txt", "a")
    for x in inventory:
      inventoryFile.write(x + "\n")
    inventoryFile.close()
    return True
  except:
    return False
  print("I'll get to this")
  
  #adding money to global balance as well as updating file
def addMoney(amount, currency):
  balance[currency]= str(int(balance[currency]) + amount)
  print(balance[currency])
  text = str(balance[0] + ":" + balance[1] + ":" + balance[2] +":" + balance[3] + ":" + balance[4])
  print(text)
  wr = open("wallet.txt", 'w')
  wr.write(text)
  wr.close()
  
  #save to file
  
@client.command()
async def inventory(ctx):
  #see whats in your inventory
  inventoryFile = open ("inventory.txt", "r")
  await ctx.send(f"**Current inventory:**\n{inventoryFile.read()}")
  


@client.command()
async def wallet(ctx):
  #see the balance of the wallet
  await ctx.send(f"**Current balance:**\nCopper: {balance[0]}\nSilver: {str(balance[1])}\nElectrum: {str(balance[2])}\nGold: {str(balance[3])}\nPlatinum: {str(balance[4])}")
  
@client.command()
async def update(ctx):
  await ctx.send("Updating to match files")
  load_inventory()
  await ctx.send("Inventory Updated")


#Appends items to the "inventory" and "balance" lists from their respective saved files
#Make sure there is an inventory.txt and balance.txt file in the same folder as this file.
def load_inventory():  
  inventoryFile = open("inventory.txt", "r")
  global inventory
  inventory = []
  for line in inventoryFile:
    inventory.append(line.strip())
  print(inventory)
  
  walletFile = open("wallet.txt", "r")
  walletBalance = walletFile.read()
  global balance
  balance = walletBalance.split(":")   #they are saved as STRINGS, please remember this!!!
  print(balance)
  if balance == ['']:
    balance = ['0','0','0','0','0']
  walletFile.close()
  inventoryFile.close()
  
   
client.run(botToken)
