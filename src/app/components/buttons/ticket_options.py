import discord 
from core.builders.button_builder import ButtonBuilder
from core.builders.component_builder import ComponentBuilder
from ...functions.close_ticket import close_ticket
from ...functions.delete_ticket import delete_ticket

close_ticket_button = ComponentBuilder(
    [
        ButtonBuilder(
            label="Fechar",
            color="green",
            custom_id="close-ticket",
            button_listener=close_ticket
        ),
                
        ButtonBuilder(
            label="Deletar",
            color="red",
            custom_id="delete-ticket",
            button_listener=delete_ticket
        )
    ]
)