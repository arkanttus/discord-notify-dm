import logging
import random
from bot_interface import BotInterface

GREETINGS = ["Eae", "Coé", "Fala", "Hii"]

class Gamer(BotInterface):
    
    async def on_message(self, message):
        roles = message.role_mentions

        if roles:
            for role in roles:
                if self.is_role_gamer(role):
                    await self.invite_players(role, message)

    def is_role_gamer(self, role):
        print(f'{role.id} {role.name}')
        return role.name[0] == '_' and role.name[-1] == '_'

    async def invite_players(self, role, ctx):
        game_name = role.name
        guild_name = ctx.guild.name
        
        logging.info(f"Inviting players for play {game_name} in {guild_name}")

        author = ctx.author
        players = role.members
        players_inviteds = []

        for member in players:
            if (member == author) or self._in_same_channel(author, member):
                continue
            
            invite_message = self._make_invite_message(author, member, game_name, guild_name)
        
            try:
                await member.create_dm()
                await member.dm_channel.send(invite_message)

                players_inviteds.append(member.name)
            except:
                logging.warning(f'Exception in member: {member.name}')
                continue
        
        author_message = self._make_message_to_author(game_name, players_inviteds)

        try:
            await author.create_dm()
            await author.dm_channel.send(author_message)
        except:
            logging.warning(f'Exception in author: {author.name}')
    
    def _in_same_channel(self, member1, member2):
        return (
            member1.voice is not None and 
            member2.voice is not None and 
            member1.voice.channel == member2.voice.channel
        )
    
    def _make_invite_message(self, author, member, game, guild_name):
        greeting = random.choice(GREETINGS)
        return f'{greeting} {member.name}, {author.name} chamou pra jogar um {game} no servidor {guild_name}'

    def _make_message_to_author(self, game, inviteds):
        # Separate inviteds name by comma and space
        parsed_inviteds = ', '.join(inviteds)
        return f"Os seguintes players foram convidados para jogar {game}: {parsed_inviteds}"