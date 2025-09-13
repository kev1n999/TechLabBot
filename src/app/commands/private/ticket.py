import discord 
from core.builders.command_builder import SlashCommandBuilder
from ...components.selects.ticket_options import select_menu_options
from ...constants.constants import DEFAULT_EMBED_COLOR

class TicketSystemCommand(SlashCommandBuilder):
    def __init__(self, tree):
        super().__init__(
            tree,
            name="open-ticket",
            description="Abrir um novo sistema de tickets."
        )
        
    async def callback(self, interaction: discord.Interaction, channel: discord.TextChannel):
        embed = discord.Embed(
            description="# Abra seu Ticket\nPara iniciar um atendimento, abra um ticket clicando no botão abaixo e aguarde ser atendido!",
            color=DEFAULT_EMBED_COLOR
        )
        
        embed.set_image(url="https://media.discordapp.net/attachments/1414050304030150828/1414051013538877593/image.png?ex=68be2921&is=68bcd7a1&hm=b9b9813dc84024b08432115b1994cfcbd2b7ee0ee788578111d5ac69d3d61c61&=&format=webp&quality=lossless")
        embed.set_footer(text="TechLab - 2025")
        
        try:
            await channel.send(embed=embed, view=select_menu_options)
            await interaction.response.send_message(
                content=f"A mensagem para abertura de tickets foi criada e enviada com sucesso em {channel.mention}!",
                ephemeral=True 
            )
        except:
            await interaction.response.send_message(
                content="Ocorreu um erro ao tentar enviar a mensagem para abertura de tickes.",
                ephemeral=True
            )
        