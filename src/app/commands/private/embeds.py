import discord
from core.builders.command_builder import SlashCommandBuilder
from ...components.layouts.containers import PricesLayout, TipsLayout, RulesLayout, AboutLayout, FeedbackLayout

class SendEmbeds(SlashCommandBuilder):
    def __init__(self, tree):
        super().__init__(
            app=tree,
            name="send-embed",
            description="Envia embeds estáticas para determinado canal da loja."
        )

    async def callback(self, interaction: discord.Interaction, keyword: str):
        guild = interaction.guild
        channel = interaction.channel 
        
        price_channel = guild.get_channel(1413989899027218452)
        rules_channel = guild.get_channel(1415385901944803510)
        tips_channel = guild.get_channel(1410430056479850640)
        about_channel = guild.get_channel(1416464766473474169)
        make_feedback_channel = guild.get_channel(1422341491141115925)
        
        try:
            if keyword.lower() == "prices":
                await interaction.channel.send(
                    content="Defina o preço para o serviço de bots(Em Euro e Real), ex: `10€ / R$ 10,00`"
                )
                bot_price = await interaction.client.wait_for("message", check=lambda m: m.author.id == interaction.user.id, timeout=15.0)
                
                if bot_price.content.lower() == "null" or bot_price.content.lower() == "none":
                    bot_price, site_price, automation_price = (None, None, None) 
                
                else:
                    await channel.send(
                        content="Defina o preço para o serviço de sites(Em Euro e Real)" 
                    )
                    site_price = await interaction.client.wait_for("message", check=lambda m: m.author.id == interaction.user.id, timeout=15.0)
                    
                    await channel.send(
                        content="Defina o preço para o serviço de automações(Em Euro e Real)" 
                    )
                    automation_price = await interaction.client.wait_for("message", check=lambda m: m.author.id == interaction.user.id, timeout=15.0)
                    bot_price, site_price, automation_price = (bot_price.content, site_price.content, automation_price.content)
                    
                layout = PricesLayout(bot_price, site_price, automation_price)
                
                await price_channel.send(view=layout)
                
                await interaction.response.send_message(
                    f"A mensagem foi enviada para {price_channel.mention}!"
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
            
            elif keyword.lower() == "feedback":
                layout = FeedbackLayout()
                await make_feedback_channel.send(view=layout)
                await interaction.response.send_message(
                    f"A mensagem foi enviada para {make_feedback_channel.mention}!", ephemeral=True
                )
                
        except Exception as err:
            print(err)
            await interaction.response.send_message(
                f"Ocorreu um erro ao enviar a mensagem: {err}", ephemeral=True
            )
