import settings
from gamer import Gamer
from server import Server

import discord
from discord.ext import commands


class GueimerBot(commands.Bot):
    def __init__(self, intents, gamer: Gamer, server: Server):
        super(GueimerBot, self).__init__(command_prefix='!', intents=intents)
        self._gamer = gamer
        self._server = server
        self.listeners = [gamer, server]

    async def on_ready(self):
        print(f'{self.user} ta ONLINE poah !')
    
    async def on_message(self, message):
        if message.author == self.user:
            return

        for listener in self.listeners:
            await listener.on_message(message)
    
    async def on_member_join(self, member):
        await self._server.set_default_role(member)
    


gamer = Gamer()
server = Server()

intents = discord.Intents.default()
intents.members = True

client = GueimerBot(intents, gamer=gamer, server=server)
client.run(settings.TOKEN)