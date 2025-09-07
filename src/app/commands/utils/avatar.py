import discord 
from core.builders.command_builder import SlashCommandBuilder
from ...components.selects.selected_user_avatar import selected_user
from ...constants.constants import DEFAULT_EMBED_COLOR

class UserAvatarCommand(SlashCommandBuilder):
    def __init__(self, tree):
        super().__init__(
            tree,
            name="avatar",
            description="Retorna o avatar do usuário mencionado"
        )
        
    async def callback(self, interaction: discord.Interaction, user: discord.User=None):
        if user is None:
            user = interaction.user 
        
        avatar_url = user.display_avatar 
        
        embed = discord.Embed(
            title=f"🖼 Avatar de {user.name}",
            color=DEFAULT_EMBED_COLOR
            
        )
        
        embed.set_image(url=avatar_url)
        
        await interaction.response.send_message(
            embed=embed,
            ephemeral=True,
            view=selected_user 
        )
    