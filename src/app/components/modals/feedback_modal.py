import discord 
from core.builders.modal_builder import ModalBuilder, InputTextBuilder
from ...constants.constants import FEEDBACK_CHANNEL_ID, DEFAULT_EMBED_COLOR, EMOJIS

modal_fields = [
    InputTextBuilder(label="⭐ Quantas estrelas você nos dá?", placeholder="Use um número de 1 a 5!", style="short", custom_id="stars", required=True),
    InputTextBuilder(label="📜 Deixe o seu Feedback!", placeholder="O que você tem a dizer sobre a TechLab Store?", style="paragraph", custom_id="feedback", required=True),
    InputTextBuilder(label="❔ Recomenda a nossa loja?", placeholder="Você recomenda a TechLab Store?", style="short", custom_id="recomenda", required=True)
]

async def feedback_modal_listener(interaction: discord.Interaction):
    feedback_channel = interaction.guild.get_channel(FEEDBACK_CHANNEL_ID)
    user = interaction.user 
    stars = ""
    f = ""
    
    stars_field = modal_fields[0].value 
    feedback_field = modal_fields[1].value 
    recomenda_field = modal_fields[2].value 
    
    if int(stars_field) == 1:
        stars += f"{EMOJIS['starfull']} {EMOJIS['starvoid']} {EMOJIS['starvoid']} {EMOJIS['starvoid']} {EMOJIS['starvoid']}"
        f += "1/5"
    elif int(stars_field) == 2:
        stars += f"{EMOJIS['starfull']} {EMOJIS['starfull']} {EMOJIS['starvoid']} {EMOJIS['starvoid']} {EMOJIS['starvoid']}"
        f += "2/5"
        
    elif int(stars_field) == 3:
        stars += f"{EMOJIS['starfull']} {EMOJIS['starfull']} {EMOJIS['starfull']} {EMOJIS['starvoid']} {EMOJIS['starvoid']}"
        f += "3/5"
        
    elif int(stars_field) == 4:
        stars += f"{EMOJIS['starfull']} {EMOJIS['starfull']} {EMOJIS['starfull']} {EMOJIS['starfull']} {EMOJIS['starvoid']}"
        f += "4/5"
        
    elif int(stars_field) == 5:
        stars += f"{EMOJIS['starfull']} {EMOJIS['starfull']} {EMOJIS['starfull']} {EMOJIS['starfull']} {EMOJIS['starfull']}"
        f += "5/5"
        
    feedback_embed = discord.Embed(
        description=f"# {EMOJIS['user']}  {user.name}\n> {feedback_field}", 
        color=DEFAULT_EMBED_COLOR
    )
    
    feedback_embed.add_field(
        name=f"{EMOJIS['set']}  Recomenda a TechLab Store?",
        value=recomenda_field.capitalize(),
        inline=True
    )
    
    feedback_embed.add_field(
        name=f"{EMOJIS['set']}  Nota ({f})",
        value=stars,
        inline=False
    )
    
    feedback_embed.set_thumbnail(url=user.display_avatar)
    feedback_embed.set_footer(text="TechLab 2025 - Agradecemos o seu feedback!", icon_url=interaction.client.user.display_avatar)
    
    await feedback_channel.send(embed=feedback_embed)
    await interaction.response.send_message(
        content=f"Feedback enviado com sucesso para {feedback_channel.mention}, agradecmos pela sua avaliação!",
        ephemeral=True 
    )
    
feedback_modal = ModalBuilder(
    title="Avalie a TechLab Store",
    items=modal_fields,
    modal_listener=feedback_modal_listener,
    custom_id="feedback-modal" 
)