import discord
from core.builders.command_builder import SlashCommandBuilder
from ...constants.constants import TICKET_CHANNEL_ID
from ...components.layouts.containers import PricesLayout, TipsLayout, RulesLayout

class SendEmbeds(SlashCommandBuilder):
    def __init__(self, tree):
        super().__init__(
            app=tree,
            name="send-embed",
            description="Envia embeds estáticas para determinado canal da loja."
        )

    async def callback(self, interaction: discord.Interaction, keyword: str):
        guild = interaction.guild

        channels = {
            "price_channel": discord.utils.get(guild.text_channels, id=1413989899027218452),
            "rules_channel": discord.utils.get(guild.text_channels, id=1410430056479850639),
            "tips_channel": discord.utils.get(guild.text_channels, id=1410430056479850640)
        }
        ticket_channel = discord.utils.get(guild.text_channels, id=TICKET_CHANNEL_ID)

        try:
            if keyword.lower() == "prices":
                layout = PricesLayout(ticket_channel)
                await channels["price_channel"].send(view=layout)
                await interaction.response.send_message(f"A mensagem foi enviada para {channels['price_channel'].mention}!", ephemeral=True)

            elif keyword.lower() == "rules":
                layout = RulesLayout()
                await channels["rules_channel"].send(view=layout)
                await interaction.response.send_message(f"A mensagem foi enviada para {channels['rules_channel'].mention}!", ephemeral=True)

            elif keyword.lower() == "tips":
                layout = TipsLayout(ticket_channel, channels["price_channel"])
                await channels["tips_channel"].send(view=layout)
                await interaction.response.send_message(f"A mensagem foi enviada para {channels['tips_channel'].mention}!", ephemeral=True)

        except Exception as err:
            print(err)
            await interaction.response.send_message(f"Ocorreu um erro ao enviar a mensagem: {err}", ephemeral=True)
