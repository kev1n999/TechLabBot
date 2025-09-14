import discord 
from discord import Interaction 
from ..components.buttons.ticket_options import ticket_buttons
from ..constants.constants import DEFAULT_EMBED_COLOR

async def create_ticket(interaction: Interaction, member: discord.Member, choice: str):
    guild = interaction.guild 
            
    try:    
        ticket_category = discord.utils.get(guild.categories, id=1410706150910984212)
            
        if not ticket_category:
            await guild.create_category(name="tickets")
            
        if choice == "pedido":
            choice = "Fazer um pedido"
            
        elif choice == "ajuda":
            choice = "Tirar uma dúvida"
            
        elif choice == "orcamento":
            choice = "Fazer um orçamento"
            
        everyone_overwrites = discord.PermissionOverwrite(view_channel=False, send_messages=False)
        author_overwrites = discord.PermissionOverwrite(view_channel=True, send_messages=True)
            
        ticket_channel = await ticket_category.create_text_channel(name=f"📂》{interaction.user.name}", overwrites={
            guild.default_role: everyone_overwrites,
            interaction.user: author_overwrites
        })
            
        embed = discord.Embed(
            title="📩  Ticket Aberto",
            color=DEFAULT_EMBED_COLOR
        )
        
        embed.add_field(
            name="Usuário",
            value=member.name,
            inline=True 
        )
        
        embed.add_field(
            name="Opção Escolhida",
            value=f"`{choice}`",
            inline=False
        )
        
        embed.set_footer(
            text="TechLab - 2025",
            icon_url=interaction.client.user.display_avatar
        )
        
        embed.set_thumbnail(url=member.display_avatar)
        
        await interaction.response.send_message(
            content=f"Seu ticket foi aberto com sucesso em {ticket_channel.mention}!",
            ephemeral=True 
        )
            
        await ticket_channel.send("Olá {}, Seja bem vindo ao seu ticket!".format(member.mention), embed=embed, view=ticket_buttons)
    except:
        pass 