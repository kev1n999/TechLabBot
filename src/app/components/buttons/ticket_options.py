import discord 
from core.builders.button_builder import ButtonBuilder
from core.builders.component_builder import ComponentBuilder


async def close_ticket(interaction: discord.Interaction, button: discord.Button):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message(
            content="Você não possui as permissões necessárias para fechar este ticket!",
            ephemeral=True 
        )
        return
    
    await interaction.response.send_message(
        content="Você tem certeza que deseja fechar este ticket?(Digite `sim` ou `s` para confirmar, ou `não/n` para cancelar.)",
        ephemeral=True 
    )
    
    response = await interaction.client.wait_for("message", check=lambda u: u.author.id == interaction.user.id, timeout=15000)
    content = response.content.lower()
    
    if content == "sim" or content == "s":
        await interaction.channel.delete()
    elif content == "não" or content == "n":
        return
        
close_ticket_button = ComponentBuilder(ButtonBuilder(
    label="Fechar",
    color="red",
    custom_id="close-ticket",
    button_listener=close_ticket
))