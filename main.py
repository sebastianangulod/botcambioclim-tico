import discord  # Importa la librería principal de Discord.py
from discord.ext import commands  # Importa la extensión de comandos de Discord.py

intents = discord.Intents.default()  # Crea un objeto de intenciones por defecto
intents.message_content = True  # Habilita la intención de leer el contenido de los mensajes

bot = commands.Bot(command_prefix='$', intents=intents)  # Crea un objeto de bot con el prefijo '$' y las intenciones configuradas
ultimo_comando={}

@bot.event  # Decorador para definir un evento
async def on_ready():  # Evento que se ejecuta cuando el bot se conecta
    print(f'We have logged in as {bot.user}')  # Imprime un mensaje en la consola indicando que el bot se ha conectado


@bot.command()
async def start(ctx):
    global ultimo_comando
    ultimo_comando[ctx.author.id] = 'start'
    await ctx.send('Hola, bienvenido a Recreación Medioambiental, un juego interactivo donde tendrás que demostrar tus conocimientos sobre cuidado del medioambiente y reciclaje, aprenderás de manera interactiva y divertida, por favor elige una opción escribiendo el número en letras como se muestra:\nuno: Nuevo Juego\ndos: Reglas\ntres: Puntaje alto de esta sesión\ncuatro: Salir')

#Quiero configurar un comando que solo se pueda usar cuando se haya usado start como último comando, este que sea '1'

@bot.command()
async def uno(ctx):
    global ultimo_comando
    if ultimo_comando.get(ctx.author.id) == 'start':
        ultimo_comando[ctx.author.id] = {}
        await ctx.send('Has escogido la primera función')
    else:
        ultimo_comando[ctx.author.id] = {}
        await ctx.send('Solo puedes introducir este comando si el último que usaste fue "$start".')

@bot.command()
async def dos(ctx):
    global ultimo_comando
    if ultimo_comando.get(ctx.author.id) == 'start':
        await ctx.send('Has escogido la reglas del juego')
    else:
        await ctx.send('Solo puedes introducir este comando si el último que usaste fue "$start".')

@bot.command()
async def tres(ctx):
    global ultimo_comando
    if ultimo_comando.get(ctx.author.id) == 'start':
        await ctx.send('Has escogido la puntaje alto de esta sesión')
    else:
        await ctx.send('Solo puedes introducir este comando si el último que usaste fue "$start".')

@bot.command()
async def cuatro(ctx):
    global ultimo_comando
    if ultimo_comando.get(ctx.author.id) == 'start':
        ultimo_comando[ctx.author.id] = {}
        await ctx.send('Nos vemos en otra ocasion! Recuerda cuidar el ambiente y a los que lo rodean.')
    else:
        ultimo_comando[ctx.author.id] = {}
        await ctx.send('Solo puedes introducir este comando si el último que usaste fue "$start".')

bot.run("TOKEN")  # Ejecuta el bot con tu token