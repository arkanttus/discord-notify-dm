import discord
import settings


class GueimerClient(discord.Client):
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

        if message.content == 'GUEI':
            await message.channel.send('É TU')
    
    async def on_member_join(self, member):
        role_id = int(settings.CIRCO_DEFAULT_ROLE)
        role = discord.utils.get(member.guild.roles, id=role_id )
        await member.add_roles(role)
    
    async def invite_players(self, role, ctx):
        author = ctx.author
        guild = ctx.guild
        players = role.members
        players_inviteds = f"Os seguintes players foram convidados para jogar {role.name}: "
        
        for member in players:
            if member == author:
                continue
            
            await member.create_dm()
            await member.dm_channel.send(
                f'Coé {member.name}, {author.name} chamou pra jogar um {role.name} no servidor {guild.name}'
            )
            players_inviteds += f" {member.name},"
        
        await author.create_dm()
        await author.dm_channel.send(
            players_inviteds[:-1]
        )
        

    def is_role_gamer(self, role):
        print(f'{role.id} {role.name}')
        return role.name[0] == '_' and role.name[-1] == '_'
    
client = GueimerClient()
client.run(settings.TOKEN)