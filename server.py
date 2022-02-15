import settings
import discord

from bot_interface import BotInterface


class Server(BotInterface):

    async def on_message(self, message):
        return

    async def set_default_role(self, member):
        role_id = int(settings.DEFAULT_ROLE_GUILD)
        role = discord.utils.get(member.guild.roles, id=role_id)
        await member.add_roles(role)