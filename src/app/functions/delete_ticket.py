import discord
from discord import Interaction

async def delete_ticket(interaction: Interaction, button: discord.ui.Button):
    channel = interaction.channel 
    
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message(
            content="Você não possui as permissões necessárias para utilizar esta funcionalidade!",
            ephemeral=True 
        )
        return 
    
    try:
        if channel.category.name.lower() == "tickets" or channel.category.name.lower() == "fechados":
            await channel.delete()
            
    except:
        await interaction.response.send_message(
            content="Ocorreu um erro ao tentar deletar este ticket! Tente novamente mais tarde.",
            ephemeral=True 
        )