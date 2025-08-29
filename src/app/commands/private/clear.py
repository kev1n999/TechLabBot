import discord 
from core.builders.command_builder import SlashCommandBuilder

class ClearCommand(SlashCommandBuilder):
    def __init__(self, tree):
        super().__init__(
            tree, 
            name="clear",
            description="Limpa mensagens em massa neste canal."
        )
        
    async def callback(self, interaction: discord.Interaction, amount: int):
        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message(
                content="Você não possui as permissões necessárias para utilizar este comando!",
                ephemeral=True 
            )
            return
        
        try:
            del_messages = await interaction.channel.purge(amount)
            
            await interaction.response.send_message(
                content=f"{len(del_messages)} mensagens foram deletadas neste canal.", 
                ephemeral=True
            )
        except:
            await interaction.response.send_message(
                content="Ocorreu um erro ao deletar as mensagens neste canal.",
                ephemeral=True 
            )