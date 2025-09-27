import discord 
from core.builders.command_builder import SlashCommandBuilder
from ...components.modals.feedback_modal import feedback_modal

class FeedbackCommand(SlashCommandBuilder):
    def __init__(self, tree):
        super().__init__(
            app=tree, 
            name="feedback",
            description="Avalie a nossa loja e dê o seu feedback!"
        )
        
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_modal(feedback_modal)