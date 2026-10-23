import discord
import random
import os
import requests
from settings import settings
from discord.ext import commands
from bot_logic import gen_password

intents = discord.Intents.default()
intents.message_content = True
 
bot = commands.Bot(command_prefix="!", intents=intents)
lista_emoji = [
    "🐍", "🚀", "🤖", "🔥", "🌍",
    "🍕", "🎮", "💎", "🦊", "🌈",
    "⚡", "🎯", "🐉", "🌙", "🎉"
]

mems_images = ["bot/images/mem1.webp","bot/images/mem10.webp","bot/images/mem5.webp","bot/images/mem3.webp"]
 
@bot.event
async def on_ready():
    print(f"Abbiamo fatto l'accesso come {bot.user}")
    
@bot.command()
async def ciao(ctx):
    await ctx.send("Ciao!")
    
@bot.command()
async def arrivederci(ctx):
    await ctx.send("🙂")
    
    
@bot.command()
async def moltiplica_parola(ctx, parola:str, numero:int):
    risultato = str(parola + " ") * numero 
    await ctx.send(risultato)

@bot.command()
async def somma(ctx, numero1:int, numero2:int):
    risultato = numero1 + numero2
    await ctx.send(f"La somma di {numero1} e {numero2} è: {risultato}")
    
@bot.command()
async def genera_password(ctx, lunghezza:int):
    password = str(gen_password(lunghezza))
    await ctx.send("La password generata è: " + password)
    
@bot.command()
async def emoji(ctx):
    await ctx.send(random.choice(lista_emoji))
    
@bot.command()
async def testa_o_croce(ctx):
    possibilità = ["testa", "croce"]
    await ctx.send(random.choice(possibilità))
    
@bot.command()
async def info(ctx):
    await ctx.send("Ciao! Questo è un server creato appositamente per testare il mio bot, scrivi !help per vedere tutti i comandi di cui è dotato!")
    
@bot.command()
async def aiuto(ctx):
    await ctx.send("!ciao: stampa ciao")
    await ctx.send("!arrivederci: stampa arrivederci")
    await ctx.send("!moltiplica_parola str int: moltiplica una parola per un tot di volte")
    await ctx.send("!somma int int: esegue la somma tra due interi")
    await ctx.send("!genera_password int: stampa una password con un tot di caratteri")
    await ctx.send("!emoji: stampa un emoji casuale")
    await ctx.send("!testa_o_croce: scrive o testa o croce")
    await ctx.send("!info: stampa le informazioni del server")
    await ctx.send("!aiuto: scrive tutti i comandi che può eseguire il bot")
    

@bot.command()
async def meme(ctx):
    image_random = random.choice(os.listdir(r"bot\images"))
    print(image_random)
    with open(f"bot\images\{image_random}", 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    
def get_meme_image_url():    
    url = 'https://meme-api.com/gimme'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command()
async def meme_api(ctx):
    image_url = get_meme_image_url()
    await ctx.send(image_url)
    
bot.run(settings["TOKEN"])
