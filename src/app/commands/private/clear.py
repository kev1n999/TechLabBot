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
            channel = interaction.channel 
            del_messages = await channel.purge(
                limit=amount 
            )
            
            await interaction.response.send_message(
                content=f"{len(del_messages)} mensagens foram deletadas neste canal.", 
                ephemeral=True
            )
        except Exception as err:
            await interaction.response.send_message(
                content="Ocorreu um erro ao deletar as mensagens neste canal.",
                ephemeral=True 
            )