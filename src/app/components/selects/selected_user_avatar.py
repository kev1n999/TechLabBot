import discord 
from core.builders.select_builder import SelectUserBuilder
from core.builders.component_builder import ComponentBuilder

async def returns_user_avatar(interaction: discord.Interaction, select: discord.ui.Select) -> None:
    user = select.values[0]
    avatar = user.display_avatar 
    embed = discord.Embed(
        title=f"🖼 Avatar de {user.name}",
        color=discord.Colour.blue() 
    )
    embed.set_image(url=avatar.url)

    await interaction.response.edit_message(
        embed=embed
    )

selected_user = ComponentBuilder(SelectUserBuilder(
    placeholder="Selecione um usuário...",
    custom_id="sel-user",
    select_listener=returns_user_avatar
))