import random
import discord
import asyncio

file = open('123.txt', 'r')
lines = file.readlines()
file.close()
dialogs = set()
class Trollingbot(discord.Client):
    async def on_ready(self):
        print('ready')

    async def on_message(self,message):
        if message.author == self.user or not isinstance(message.channel, discord.DMChannel):
            return
        if message.author.id in dialogs:
            return
        dialogs.add(message.author.id)
        print('сообщение ', message.content)
        msg = lines[random.randint(0,len(lines)-1)]
        channel = message.channel
        with channel.typing():
            await asyncio.sleep(len(msg)*0.2)
            await channel.send(content = msg)
            dialogs.remove(message.author.id)

A = Trollingbot()
#A.run(токен,bot=False)