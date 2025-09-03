import discord 
from core.builders.command_builder import SlashCommandBuilder
from ...components.buttons.ticket_buttons import open_ticket_button

class TicketSystemCommand(SlashCommandBuilder):
    def __init__(self, tree):
        super().__init__(
            tree,
            name="open-ticket",
            description="Abrir um novo sistema de tickets."
        )
        
    async def callback(self, interaction: discord.Interaction, channel: discord.TextChannel):
        embed = discord.Embed(
            title="✉️  Abra seu Ticket!",
            description="Para iniciar um atendimento, abra um ticket clicando no botão abaixo e aguarde ser atendido!",
            color=discord.Colour.blue()
        )
        
        embed.set_footer(text="Bot Lab 2025", icon_url=interaction.client.user.display_avatar)
        
        try:
            await channel.send(embed=embed, view=open_ticket_button)
            await interaction.response.send_message(
                content=f"A mensagem para abertura de tickets foi criada e enviada com sucesso em {channel.mention}!",
                ephemeral=True 
            )
        except:
            pass 