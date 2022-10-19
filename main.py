import os
import discord
import re
import firecommands

debtCommands = ["!add", "!remove",]


#debt class
from debtCollector import debt

#keep_alive
from run import *


#database
from database import *
import firebase_admin 
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate(database)
data = firebase_admin.initialize_app(cred, {'databaseURL' : url})




my_secret = os.environ['tk']

keep_alive()
client = discord.Client()

#finding chars index
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    
    if message.content =="!debt":
        await message.channel.send("Creating New Debts Table")
        if (str(message.author.id) not in db.reference("/UserList").get()):
          db.reference("/UserList").update({
            message.author.id : {
              "DebtHolders" : {
                "USERS" : "OWE"
              }
            }


          })
    elif message.content.startswith("!debt add"):
      
      




      listofMentions = find(message.content, "<")
     
      listofFloats = result = re.findall(r"[-+]?\d*\.\d+|\d+", message.content)
      
      await message.channel.send("How much: do !add [amount]")


      #makes sure the person is using add command
      def check(mes):
        return mes.content.startswith("!add")

      response = await client.wait_for("message",check = check, timeout = 50.0)
      listofFloats = result = re.findall(r"[-+]?\d*\.\d+|\d+", response.content)
      
      
          

      index = 0
  
      for i in listofMentions:
        mentionId = message.content[i + 3: i + 21]
        #if their data is not in the database then create new
        if (message.content[i + 3: i + 21]) not in db.reference("/UserList/" + str(message.author.id) + "/DebtHolders").get():
          #creating new data
          db.reference("/UserList/" + str(message.author.id) + "/DebtHolders").update(
            {
              mentionId : listofFloats[index]
            }
          )

          db.reference("/UserList/" + str(message.author.id) + "/DebtHolders").child(mentionId)
          index += 1

        #if data is found in data base we add on
        elif (mentionId) in db.reference("/UserList/" + str(message.author.id) + "/DebtHolders").get():
          
          dataReference = db.reference("/UserList/" + str(message.author.id) + "/DebtHolders/" + mentionId)

          dataReference.set(str(float(dataReference.get()) + float(listofFloats[index])))
          index +=1
    elif message.content.startswith("!debt remove"):
      listofMentions = find(message.content, "<")
     
      listofFloats = result = re.findall(r"[-+]?\d*\.\d+|\d+", message.content)

      await message.channel.send("How much: do !remove [amount]")


      #makes sure the person is using add command
      def check(mes):
        return mes.content.startswith("!remove")

      response = await client.wait_for("message",check = check, timeout = 50.0)
      listofFloats = result = re.findall(r"[-+]?\d*\.\d+|\d+", response.content)
      
      
          

      index = 0
  
      for i in listofMentions:
        mentionId = message.content[i + 3: i + 21]
        #if their data is not in the database then create new
        if (message.content[i + 3: i + 21]) not in db.reference("/UserList/" + str(message.author.id) + "/DebtHolders").get():
          #creating new data
          await message.channel.send("He has nothing to pay you")
          index += 1

        #if data is found in data base we add on
        elif (mentionId) in db.reference("/UserList/" + str(message.author.id) + "/DebtHolders").get():
          
          dataReference = db.reference("/UserList/" + str(message.author.id) + "/DebtHolders/" + mentionId)

          dataReference.set(str(float(dataReference.get()) - float(listofFloats[index])))
          index +=1
    elif message.content == "!check":
      id = message.author.id
      
      if str(id) not in db.reference("/UserList").get():
        await message.channel.send("Need to do !debt to create a new profile")
        return
      
      
      dataReference = db.reference("/UserList/" + str(message.author.id) + "/DebtHolders")
      string = ""

      numberOfPeople = 0

      for i in dataReference.get():
        if i != "USERS":
          numberOfPeople+=1
          string += "<@" + str(i) + "> owes you " + dataReference.get()[i] +"\n"

      if numberOfPeople == 0:
        string = "Nobody Owes You Shit"

      await message.channel.send(string)
    elif message.content.startswith("HOLY SHIT"):
      await message.channel.send("https://tenor.com/view/anime-goku-dbz-dragon-ball-super-saiyan-gif-8246706")

    elif message.content.startswith("!ericremove"):
      print("x")
    elif message.content.startswith("!ericadd"):
      pass
    else:
      table = message.content.lower().split()
      print(table)
      
      for i in table:
        
        if i in firecommands.commands:
          x = firecommands.fire(message)
          await message.channel.send(x)
        else:
          print("NO word")

    

      


        
       
          


  
        
          

@client.event
async def on_message_delete(message):
    print(message.content)
    print(message.author.id)

    




client.run(my_secret)

