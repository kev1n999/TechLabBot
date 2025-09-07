import discord 
from core.builders.select_builder import SelectOptionBuilder, SelectMenuBuilder
from core.builders.component_builder import ComponentBuilder
from ...functions.create_ticket import create_ticket

options = [
    SelectOptionBuilder(label="🤖 Fazer um pedido", description="Clique para iniciar um pedido", value="pedido"),
    SelectOptionBuilder(label="❓ Pedir Ajuda", description="Clique para pedir ajuda ou tirar uma dúvida", value="ajuda")
]

async def select_options_listener(interaction: discord.Interaction, select: discord.ui.Select):
    choice = select.values[0]
    
    if choice == "pedido":
        await create_ticket(interaction, interaction.user, choice)        
    
    elif choice == "ajuda":
        await create_ticket(interaction, interaction.user, choice)   
        
    select.values.clear()
    
    await interaction.message.edit(view=ComponentBuilder(SelectMenuBuilder(
        placeholder="Selecione uma opção...",
        options=options, 
        select_listener=select_options_listener
    )))
    
select_menu_options = ComponentBuilder(SelectMenuBuilder(
    placeholder="Selecione uma opção...",
    options=options, 
    select_listener=select_options_listener
), persistent=True)