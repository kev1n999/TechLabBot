import discord 
from core.builders.command_builder import SlashCommandBuilder

class BanCommand(SlashCommandBuilder):
    def __init__(self, tree):
        super().__init__(
            tree,
            name="ban",
            description="Bane um membro do servidor"
        )
        
    async def callback(self, interaction: discord.Interaction, member: discord.Member):
        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message(
                content="Você não possui as permissções necessárias para a execução deste comando!",
                ephemeral=True 
            )
            return 
        
        