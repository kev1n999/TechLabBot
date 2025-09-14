import discord
from core.builders.command_builder import SlashCommandBuilder
from ...constants.constants import TICKET_CHANNEL_ID
from ...components.layouts.containers import PricesLayout, TipsLayout, RulesLayout, AboutLayout

class SendEmbeds(SlashCommandBuilder):
    def __init__(self, tree):
        super().__init__(
            app=tree,
            name="send-embed",
            description="Envia embeds estáticas para determinado canal da loja."
        )

    async def callback(self, interaction: discord.Interaction, keyword: str):
        guild = interaction.guild

        price_channel = guild.get_channel(1413989899027218452)
        rules_channel = guild.get_channel(1415385901944803510)
        tips_channel = guild.get_channel(1410430056479850640)
        ticket_channel = guild.get_channel(TICKET_CHANNEL_ID)
        about_channel = guild.get_channel(1416464766473474169)
        
        try:
            if keyword.lower() == "prices":
                layout = PricesLayout()
                await price_channel.send(view=layout)
                await interaction.response.send_message(
                    f"A mensagem foi enviada para {price_channel.mention}!", ephemeral=True
                )

            elif keyword.lower() == "rules":
                layout = RulesLayout()
                await rules_channel.send(view=layout)
                await interaction.response.send_message(
                    f"A mensagem foi enviada para {rules_channel.mention}!", ephemeral=True
                )

            elif keyword.lower() == "tips":
                layout = TipsLayout()
                await tips_channel.send(view=layout)
                await interaction.response.send_message(
                    f"A mensagem foi enviada para {tips_channel.mention}!", ephemeral=True
                )
                
            elif keyword.lower() == "about":
                layout = AboutLayout()
                await about_channel.send(view=layout)
                await interaction.response.send_message(
                    f"A mensagem foi enviada para {about_channel.mention}!", ephemeral=True
                )
        except Exception as err:
            print(err)
            await interaction.response.send_message(
                f"Ocorreu um erro ao enviar a mensagem: {err}", ephemeral=True
            )
