from discord import ButtonStyle, Interaction, ui
from core.builders.button_builder import ButtonBuilder
from core.builders.component_builder import ComponentBuilder
from ...components.modals.feedback_modal import feedback_modal
from ...constants.constants import CLIENT_ROLE_ID

async def feedback_button_listener(interaction: Interaction, button: ui.Button):
    client_role = interaction.guild.get_role(CLIENT_ROLE_ID)
    
    if not client_role in interaction.user.roles:
        await interaction.response.send_message(
            content="Vocẽ ainda não é um cliente da TechLab para nos avaliar!",
            ephemeral=True
        )
        return 
    
    await interaction.response.send_modal(feedback_modal)
    
feedback_button = ui.ActionRow(ButtonBuilder(
    label="Avalie a TechLab",
    color=ButtonStyle.secondary,
    custom_id="feedback-button",
    button_listener=feedback_button_listener
))

feedback_button_view = ComponentBuilder(
    ButtonBuilder(
        label="Avalie a TechLab",
        color=ButtonStyle.secondary,
        custom_id="feedback-button",
        button_listener=feedback_button_listener
    ),
    persistent=True
)