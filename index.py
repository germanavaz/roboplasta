from http import client
import discord, random, datetime, decouple
from decouple import config
from discord.ext import commands, tasks

bot = commands.Bot("!")

@bot.event
async def on_ready():
    print(f"Estou pronto! Estou conectado como {bot.user}")
    current_time.start()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if "faro" in message.content:
        response = ['cavaaaaalo', 'ratinhoooo', 'ele gostaaaa', 
        'só veio arrumar o cabelo', 'tome', 'aiiii', 'uuuui', 
        'não', 'demais', 'cheeeega', 'que papelão ein', 'aaai mamããããe',
        'aaaaai, meu deus', 'tomi', 'tapa', 'ai', 'que isso meu filho, calma',
        'uéépaaa', 'atumalaca', 'PARE', 'dança gatinho, dança', 'é brincadeira hein', 
        'okay okay', 'calma la'] 
        await message.channel.send(f"{random.choice(response)}")

    await bot.process_commands(message)


@tasks.loop(hours=1)
async def current_time():
    now =  datetime.datetime.now( )
    channel= bot.get_channel(889272147472678913)
    response = ['cavaaaaalo', 'ratinhoooo', 'ele gostaaaa', 
        'só veio arrumar o cabelo', 'tome', 'aiiii', 'uuuui', 
        'não', 'demais', 'cheeeega', 'que papelão ein', 'aaai mamããããe',
        'aaaaai, meu deus', 'tomi', 'tapa', 'ai', 'que isso meu filho, calma',
        'uéépaaa', 'atumalaca', 'PARE', 'dança gatinho, dança', 'é brincadeira hein', 
        'okay okay', 'calma la']  
    await channel.send(f"{random.choice(response)}")


TOKEN = config("TOKEN")
bot.run(TOKEN)       
