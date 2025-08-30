import discord 
from core.builders.command_builder import SlashCommandBuilder

class BanCommand(SlashCommandBuilder):
    def __init__(self, tree):
        super().__init__(
            tree,
            name="ban",
            description="Bane um membro do servidor"
        )
        
    async def callback(self, interaction: discord.Interaction, member: discord.Member, reason: str=None):
        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message(
                content="Você não possui as permissções necessárias para a execução deste comando!",
                ephemeral=True 
            )
            return 
        
        if member.guild_permissions.value >= interaction.user.guild_permissions.value:
            await interaction.response.send_message(
                content="Você não pode banir um membro que tenha permissões superiores ou iguais as suas!",
                ephemeral=True 
            )
            return 
        
        try:
            await member.ban(
                reason=reason 
            )
            
            if reason is None:
                reason = "Sem motivo"
            
            try:
                await member.send(
                    content=f"Você foi banido do servidor **{interaction.guild.name}** por **{interaction.user.name}**\nMotivo: `{reason}`"
                )    
            except:
                print(f"Não foi possível enviar uma mensagem ao membro banido: {member.name}")
                
            await interaction.response.send_message(
                content=f"{member.mention} foi banido com sucesso do servidor.\nMotivo: **{reason}**",
                ephemeral=True 
            )
            
        except:
            await interaction.response.send_message(
                content="Ocorreu um erro ao banir este usuário.",
                ephemeral=True 
            )