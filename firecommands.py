import commandList
import discord
commands = {


  "needmotivation" : commandList.needmotivation,
  "pepedrive" :commandList.pepedrive,
  "pepeclap" :commandList.pepeclap,
  "heyimsorry" :commandList.heyimsorry,
  "hehehe" :commandList.hehehe,
  "pepelaugh":commandList.pepelaugh,
  "sadge" :commandList.sadge,
  "asianbaldski" :commandList.asianbaldski,
  "summoningjutsu" :commandList.summoningjutsu,
  "demon" :commandList.demon,
  "hamster": commandList.hamster,
  "dog" :commandList.dog,
  "goodsoup" :commandList.goodsoup,
  "eric" :commandList.eric,
  "lumfao" : commandList.lumfao,
  "pepedance" : commandList.pepedance,
  "loser" : commandList.loser,
  "troll" : commandList.troll,
  "sus" : commandList.sus,
  "pepehigh" :commandList.pepehigh,
  "kekw" :commandList.kekw,
  "evil" :commandList.evil,

}



def fire(message):
  print(message.content in commands)
  if message.content.lower() in commands:
    return commands[message.content.lower()](message)
    