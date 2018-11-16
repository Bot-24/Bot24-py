import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import requests
import os


type = 1
client = discord.Client()

BOT_TOKEN = 'NDk3NDE1NzQ1NTg4OTUzMDg4.DtDL9g.2pTzRkQ06TcSxjwbA0S5WGgmPWQ'

players = {}

lennexid = "297452622489845760"

minutes = 0
hour = 0

@client.event
async def on_ready():
    print("Eingeloggt als SteamarinoBot V0.1")
    print(client.user.name)
    print(client.user.id)
    print("------------")
    await client.change_presence(game=discord.Game(name="discord.me/steamarino | &help"))


@client.event
async def on_message(message):
    if message.content.startswith("&test"):
        await client.send_message(message.channel, "Test erfolgreich")


    if message.content.startswith("&ping"):
        await client.send_message (message.channel, "PONG!")


    if message.content.startswith("&supreme"):
        await client.send_message (message.channel, "http://www.supremenewyork.com")


    if message.content.startswith("&steam"):
        await client.send_message (message.channel, "http://steamcommunity.com/id/steamarino/")


    if message.content.startswith("&botowner"):
        await client.send_message(message.channel, "Dieser Bot wurde von **Hendrik** erstellt und von **Steamarino** Modifiziert. Bin stolz drauf.")


    if message.content.startswith("&memes"):
        await client.send_message(message.channel, "Memes an die Macht!")


    if message.content.lower().startswith("&info"):
        info = discord.Embed(
            title="Hey, Ich bin der SteamarinoBot :)",
            color=0xe74c3c,
            description="Hey, hier siehst Du die aktuellen Commands:\n"
                        "Beta 0.1"

        )

        await client.send_message(message.channel, embed=info)



    if message.content.startswith("&russia"):
        response = requests.get("https://i.ytimg.com/vi/d0z_uXA_pdI/maxresdefault.jpg", stream=True)
        await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename="Bild.png", content="For Mother Russia")


    if message.content.lower().startswith("&help"):
        help = discord.Embed(
            title="**Hey, Ich bin der SteamarinoBot** :)",
            color=0xe74c3c,
            description="hier kannst du alle derzeit möglichen Commands sehen: \n"
                        "https://pastebin.com/GKcrpTun"



        )
        help.set_author(
            name="*klick hier*",
            url="https://www.youtube.com/watch?v=MG9e6m_4yVY"

         )
        help.add_field(
            name="**Neuerungen bei der V0.2**",
            value="1. Custom Command bei PN\n" 
                  "2. Es wurde die Musik Funktion hinzugefügt\n",
        )




        await client.send_message(message.channel, embed=help)

    if message.content.startswith('&game') and message.author.id == steamarinoid:
        game = message.content[6:]
        await client.change_presence(game=discord.Game(name=game))
        await client.send_message(message.channel, "Status zu " + game + " geändert")

    if message.content.startswith("&hardbass"):
        await client.send_message(message.channel,"Ich heiße Niklas, und das ist mein Hardbass!")



    if message.content.startswith("&asmr"):
        await client.send_message(message.channel, "`Autonomous Sensory Meridian Response (oft als ASMR abgekürzt) bezeichnet die Erfahrung eines statisch-ähnlichen oder kribbelnden Gefühls auf der Haut, das typischerweise auf der Kopfhaut beginnt und sich am Nacken und der oberen Wirbelsäule entlang bewegt (sogenannte Tingles)`")


    if message.content.startswith("&gif"):
        gif_tag = message.content[5:]
        rgif = g.random(tag=str(gif_tag))
        response = requests.get(
            str(rgif.get("data", {}).get('image_original_url')), stream=True
        )
        await  client.send_file(message.channel, io.BytesIO(response.raw.read()), filename="video.gif")
        
        
    if message.content.startswith('&uptime'):
        await client.send_message(message.channel, "Ich bin **{0}** Stunde/n und **{1}** Minuten auf **{2}** online!. **".format(hour, minutes, message.server))
        
        
        
    if message.content.lower().startswith('&flip'): #Coinflip 50/50% chance kopf oder zahl
        choice = random.randint(1,2)
        if choice == 1:
            await client.add_reaction(message, '🌑')
        if choice == 2:
            await client.add_reaction(message, '🌕')
        

async def total_uptime():
    await client.wait_until_ready()
    global minutes
    minutes = 0
    global hour
    hour = 0
    while not client.is_closed:
        await asyncio.sleep(60)
        minutes += 1
        if minutes == 60:
            minutes = 0
            hour += 1

client.loop.create_task(total_uptime())    

   






client.run(str(os.environ.get('BOT_TOKEN')))
