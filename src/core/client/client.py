import os 
import discord 
from discord import app_commands 
from dotenv import load_dotenv 
from .handlers.command import load_commands
from core.utils.logger import setup_logger

load_dotenv()

# Configura o logger para este módulo
logger = setup_logger(__name__)

# Classe para se conectar ao client
class DiscordClient(discord.Client): 
    """
    Cliente principal do bot que gerencia a conexão, sincronização de comandos e carregamento automático.

    Essa classe estende `discord.Client` e configura um `app_commands.CommandTree` para lidar com comandos de barra (slash commands),
    buscando automaticamente comandos em subpastas de `src/commands/`.

    Args:
        token (str): Token do bot.
        intents (discord.Intents, optional): Intenções do gateway do Discord. Padrão é `discord.Intents.all()`(Todas as intents ativadas).

    Attributes:
        token (str): Token do bot.
        client_intents (discord.Intents): Intents configuradas.
        tree (app_commands.CommandTree): Árvore de comandos usada para registrar e sincronizar os comandos de barra.
    """
    def __init__(self, token, intents=None): 
        self.token = token 
        self.client_intents = intents  
        self.welcome_channel_id = 1410430056035127383 
        
        if self.client_intents is None:
            self.client_intents = discord.Intents.all() 
            logger.debug("Usando todas as intents do Discord")
            
        super().__init__(intents=self.client_intents)
        self.tree = app_commands.CommandTree(self)
        logger.info("Cliente Discord inicializado")
        
    async def setup_hook(self):
        logger.info("Configurando hooks do bot...")
        load_commands(self.tree)
        await self.tree.sync()
        logger.info("Comandos sincronizados com sucesso")
        
    async def on_ready(self):
        from app.components.selects.ticket_options import select_menu_options
        from app.components.buttons.ticket_options import ticket_buttons
        from app.components.buttons.feedback_button import feedback_button_view
        
        self.add_view(select_menu_options)
        self.add_view(ticket_buttons)
        self.add_view(feedback_button_view)
        
        logger.info(f"Bot está online como {self.user.name} (ID: {self.user.id})")
        
        await self.change_presence(
            activity=discord.Game("Entregando soluções eficientes para seus problemas!")
        )
        
    async def on_member_join(self, member: discord.Member):
        if member.bot:
            bot_role = member.guild.get_role(1417240352250789908)
            await member.add_roles(bot_role)
        else:
            member_role = member.guild.get_role(1410430055984922777)
            await member.add_roles(member_role)
        
        channel = discord.utils.get(member.guild.text_channels, id=self.welcome_channel_id)
        
        embed = discord.Embed(
            description=f"# 👋🏻 Seja bem vindo a TechLab!\n",
            color=0x242429
        )
        
        embed.set_image(url="https://media.discordapp.net/attachments/1414050304030150828/1414064011112087624/image.png?ex=68be353c&is=68bce3bc&hm=198f1f87621d527a9a9c0611403545c2b2d3156572fe5afe61d6aa7c506a5031&=&format=webp&quality=lossless")
        embed.set_footer(text="TechLab - 2025")
        
        await channel.send(
            content=f"Seja bem vindo {member.mention}!",    
            embed=embed
        )
        
    async def on_error(self, event_method, *args, **kwargs):
        logger.error(f"Erro no evento {event_method}", exc_info=True)
        
    def run_bot(self):
        try:
            logger.info("Iniciando conexão com o Discord...")
            self.run(self.token)
        except Exception as e:
            logger.error(f"Erro ao conectar com o Discord: {str(e)}", exc_info=True)
            raise
            
# Cria a instância do bot
client = DiscordClient(token=os.getenv("BOT_TOKEN"))