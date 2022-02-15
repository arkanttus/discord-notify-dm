import random
import settings

from bot_interface import BotInterface


class Meme(BotInterface):
    async def on_message(self, message):
        if message.content.lower() in settings.MEMES_PHRASES[0]:
            msg = random.choice(settings.MEMES_PHRASES[1])
            await message.channel.send(msg)
        
        if message.content.lower() in settings.ANWSER_MEMES[0]:
            msg = random.choice(settings.ANWSER_MEMES[1])
            await message.channel.send(msg)