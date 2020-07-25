import webbrowser
import requests
import discord
import random

n = random.randrange(0, 10)
client = discord.client

# request from api
r = requests.get('https://api.nasa.gov/planetary/apod?api_key=I8eUcrDHJ8ndjC9CBJd6w92bl63IHmw5NOCgk2h2')

# json
data = r.json()
print(['hdurl'])

# web browser
def web():
    webbrowser.open(['hdurl'])


if n == 10:
    await channel.send(discord.File(fattington.png))

else:
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content('fattington fetch me my socks'):
            web()
