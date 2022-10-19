import commandList
import discord
commands = {


  "jimmy" : commandList.jimmyisabadword,
  "needmotivation" : commandList.needmotivation,
  "pepedrive" :commandList.pepedrive,
  "pepeclap" :commandList.pepeclap,
  "heyimsorry" :commandList.heyimsorry,
  "hehehe" :commandList.hehehe,
  "pepelaugh":commandList.pepelaugh,
  "sadge" :commandList.sadge,
  "sydney" :commandList.sydney,
  "liangzai" : commandList.liangzai,
  "adamshates" :commandList.adamshateswhat,
  "question?" :commandList.question,
  "asianbaldski" :commandList.asianbaldski,
  "summoningjutsu" :commandList.summoningjutsu,
  "wakeywakey" :commandList.wakeywakey,
  "demon" :commandList.demon,
  "dead" :commandList.dead,
  "givehimattention" :commandList.givehimattention,
  "kill" :commandList.kill,
  "youbitch" :commandList.youbitch,
  "sad" :commandList.sad,
  "gocrazy": commandList.gocrazy,
  "liangnui" :commandList.liangnui,
  "hamster": commandList.hamster,
  "dog" :commandList.dog,
  "wanka": commandList.wanka,
  "goodsoup" :commandList.goodsoup,
  "female" :commandList.female,
  "eric" :commandList.eric,
  "haomings" :commandList.haomings,
  "commands" :commandList.commands,
  "hornyjail" :commandList.hornyjail,
  "lumfao" : commandList.lumfao,
  "pepedance" : commandList.pepedance,
  "loser" : commandList.loser,
  "troll" : commandList.troll,
  "sus" : commandList.sus,
  "pepehigh" :commandList.pepehigh,
  "d:" :commandList.D,
  "kekw" :commandList.kekw,
  "evil" :commandList.evil,
  "stfu" :commandList.stfu,
  "crawling" :commandList.crawling,
  "forakiss" :commandList.all_for_a_kiss,
  "dontmakemelaugh" :commandList.dontmakemelaugh,
  "meme" :commandList.meme,
  "friendsgon" :commandList.friendsgon,
  "lockmonkeyz": commandList.lockmonkeyz,
  "pepecookie": commandList.pepecookie,
  "richestorags":commandList.richestorags
}



def fire(message):
  print(message.content in commands)
  if message.content.lower() in commands:
    return commands[message.content.lower()](message)
    