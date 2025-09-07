import discord
from discord import Interaction

async def close_ticket(interaction: Interaction, button: discord.ui.Button):
    channel = interaction.channel 
    
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message(
            content="Você não possui as permissções necessárias para utilizar esta funcionalidade!",
            ephemeral=True 
        )
        return 
    
    if not channel.category.name.lower() == "tickets":
        return 
    
    everyone_overwrites = discord.PermissionOverwrite(view_channel=False, send_messages=False)
    
    try:        
        await interaction.response.send_message(
            content="Você tem certeza que deseja fechar este ticket?(Digite `sim` ou `s` para confirmar, ou `não/n` para cancelar.)",
            ephemeral=True 
        )
        
        response = await interaction.client.wait_for("message", check=lambda u: u.author.id == interaction.user.id, timeout=15000)
        content = response.content.lower()
        
        if content == "sim" or content == "s":
            await channel.edit(
                overwrites={
                        interaction.guild.default_role: everyone_overwrites
                    }
                )
            
            if interaction.response.is_done():
                await interaction.followup.send(
                    content="Ticket fechado com sucesso!",
                    ephemeral=True
                )
                
            else:
                await interaction.response.send_message(
                    content="Ticket fechado com sucesso!",
                    ephemeral=True
                )       
            
            close_tickets_category = discord.utils.get(interaction.guild.categories, name="FECHADOS")
            
            if not close_tickets_category:
                await interaction.guild.create_category(
                    name="FECHADOS"
                )
            
            await channel.edit(
                category=close_tickets_category
            )
            
        elif content == "não" or content == "n":
            return
        
    except Exception as err:
        print(f"Ocorreu um erro ao fechar o canal de ticket({channel.name})\n\n--- [ERROR LOG] ---\n{err}")
        
        if interaction.response.is_done():
            await interaction.followup.send(
                content="Não foi possível fechar este ticket! Tente novamente mais tarde.",
                ephemeral=True 
            )
            return 
        
        await interaction.response.send_message(
            content="Não foi possível fechar este ticket! Tente novamente mais tarde.",
            ephemeral=True    
        )