import discord 
from discord import Interaction 
from ..components.buttons.ticket_options import close_ticket_button

async def create_ticket(interaction: Interaction, member: discord.Member, choice: str):
    guild = interaction.guild 

    try:    
        ticket_category = discord.utils.get(guild.categories, id=1410706150910984212)
            
        if not ticket_category:
            await guild.create_category(name="tickets")
            
        everyone_overwrites = discord.PermissionOverwrite(view_channel=False, send_messages=False)
        author_overwrites = discord.PermissionOverwrite(view_channel=True, send_messages=True)
            
        ticket_channel = await ticket_category.create_text_channel(name=f"{interaction.user.name}", overwrites={
            guild.default_role: everyone_overwrites,
            interaction.user: author_overwrites
        })
            
        embed = discord.Embed(
            title="📩  Ticket Aberto",
            color=discord.Colour.blue()
        )
        
        embed.add_field(
            name="Usuário",
            value=member.name,
            inline=True 
        )
        
        embed.add_field(
            name="Opção Escolhida",
            value="`Fazer um pedido`" if choice == "pedido" else "`Tirar uma dúvida`",
            inline=True 
        )
        
        embed.set_footer(
            text="Bot Lab - 2025",
            icon_url=interaction.client.user.display_avatar
        )
        
        await interaction.response.send_message(
            content=f"Seu ticket foi aberto com sucesso em {ticket_channel.mention}!",
            ephemeral=True 
        )
        
        await ticket_channel.send("Olá {}, Seja bem vindo ao seu ticket!".format(member.mention), embed=embed, view=close_ticket_button)
    except:
        pass 