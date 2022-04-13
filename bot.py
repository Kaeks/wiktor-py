from dotenv import load_dotenv
from os import getenv
import discord

load_dotenv()

token = getenv("TOKEN")

class Client(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}'.format(self.user))
    
    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = Client()
client.run(token)
