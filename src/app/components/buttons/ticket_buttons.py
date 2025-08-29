import discord 
from core.builders.button_builder import ButtonBuilder
from core.builders.component_builder import ComponentBuilder

async def open_ticket_listener(interaction: discord.Interaction, button: discord.ui.Button):
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
        
        await ticket_channel.send("Olá {}".format(interaction.user.mention))
    except:
        pass     
    
open_ticket_button = ComponentBuilder(ButtonBuilder(
    label="Abrir Ticket",
    color="green",
    custom_id="open-ticket",
    button_listener=open_ticket_listener
))