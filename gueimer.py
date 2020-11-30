import discord
from discord.ext import commands
import settings
import random


class GueimerBot(commands.Bot):
    def __init__(self, intents):
        super(GueimerBot, self).__init__(command_prefix='!', intents=intents)

    async def on_ready(self):
        print(f'{self.user} ta ONLINE poah !')
    
    async def on_message(self, message):
        if message.author == self.user:
            return

        roles = message.role_mentions

        if roles:
            for role in roles:
                if self.is_role_gamer(role):
                    await self.invite_players(role, message)

        '''if message.content.lower() == 'guei':
            trolls = ['TEU PAI', 'É TU', 'TEU TIO', 'TU Q DEIXA', 'MACHISTA', 'QUEM ?', 'O BIRO LIRO', 'O BRUNO', 'TE LASCAR']
            msg = random.choice(trolls)
            await message.channel.send(msg)
        
        if message.content.lower() in ['tu', 'é tu', 'eh tu']:
            trolls = ['TEU PAI', 'PERGUNTOU ?', 'TEU TIO', 'QUEM ?', 'TE LASCAR']
            msg = random.choice(trolls)
            await message.channel.send(msg)'''
    
    async def on_member_join(self, member):
        role_id = int(settings.DEFAULT_ROLE_GUILD)
        role = discord.utils.get(member.guild.roles, id=role_id )
        await member.add_roles(role)
    
    @commands.command(name='teste')
    async def teste(self, ctx):
        print('FKEJFIJIFE')
        await ctx.send('AKSDKASD')
        return

    async def invite_players(self, role, ctx):
        author = ctx.author
        guild = ctx.guild
        players = role.members
        players_inviteds = f"Os seguintes players foram convidados para jogar {role.name}: "
        print(role)
        print(guild)
        for member in players:
            if member == author:
                continue
            
            try:
                await member.create_dm()
                await member.dm_channel.send(
                    f'Coé {member.name}, {author.name} chamou pra jogar um {role.name} no servidor {guild.name}'
                )
                players_inviteds += f" {member.name},"
            except:
                print(f'EXCEPTION IN MEMBER: {member.name}')
                continue
        
        try:
            await author.create_dm()
            await author.dm_channel.send(
                players_inviteds[:-1]
            )
        except:
            print(f'EXCEPTION IN AUTHOR: {author.name}')

    def is_role_gamer(self, role):
        print(f'{role.id} {role.name}')
        return role.name[0] == '_' and role.name[-1] == '_'
    


intents = discord.Intents.default()
intents.members = True
client = GueimerBot(intents)
client.run(settings.TOKEN)