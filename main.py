from charaiPY.AsyncPyCAI2 import PyAsyncCAI2
import discord 
import discord.ext


token_discord = "<token discord>"
owner_id = '<CAI TOKEN>'
char = "<CHHAR ID"
chat_id = "<CHAT ID>"

aut_set ={
    "author_id": "<AUTHOR ID>",
    "is_human": True,
    "name": "<CAI USER NAME>"
}


client = PyAsyncCAI2(owner_id)
intents = discord.Intents.default()
bot = discord.Client(intents=intents)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    response = await pycai(message.content)


    await message.channel.send(response)

async def pycai(message):

    print("[PyCAI2] STARTING TO PROCESS MESSAGE")
    transin = await PyAsyncCAI2.chat2.transl(message, 'en', 'id')
    print("[PyCAI2] Translate Message: ", transin)

    async with client.connect(owner_id) as chat2:
        r = await chat2.send_message(char, chat_id, transin, aut_set)
    
    transout = await PyAsyncCAI2.chat2.transl(r, 'id', 'en')    
    print("[PyCAI2] Translate Message: ", transout)
    return transout


bot.run(token_discord)
