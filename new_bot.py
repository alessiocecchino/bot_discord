import discord
import random
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
    

    


bot.run(settings["TOKEN"])