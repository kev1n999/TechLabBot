import discord 
from core.builders.command_builder import SlashCommandBuilder
from ...constants.constants import DEFAULT_EMBED_COLOR, TICKET_CHANNEL_ID, EMOJIS

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
                price_embed = discord.Embed(
                    description="# **Serviços e Preços**\nConfira abaixo como funcionam nossos serviços e a precificação para cada tipo de projeto:",
                    color=DEFAULT_EMBED_COLOR  
                )
                
                price_embed.add_field(
                    name="<:set:1414719063846031462> Como Funciona",
                    value=f"• Os preços variam de acordo com a complexidade do projeto e o prazo de entrega.\n• Garantimos suporte e qualidade em todos os projetos.\nSolicite um orçamento em: {ticket_channel.mention}",
                    inline=True 
                )
                
                price_embed.add_field(
                    name="<:set:1414719063846031462> Valores Mínimos",
                    value="• **Bots:** 80€ / R$ 150,00\n• **Automações:** 150€ / R$ 250,00\n• **Sites:** 150€ / R$ 350,00",
                    inline=False 
                )
                
                price_embed.add_field(
                    name="<:set:1414719063846031462> Métodos de Pagamento",
                    value="• <:paypal:1414721354795843605> PayPal\n• <:pix:1414721358096764959> PIX",
                    inline=True 
                )

                price_embed.set_footer(text="Techlab - 2025")
                
                await channels["price_channel"].send(
                    embed=price_embed 
                )
                
                await interaction.response.send_message(
                    content=f"A embed foi enviada com sucesso para o canal {channels["price_channel"].mention}!",
                    ephemeral=True 
                )
                
            elif keyword.lower() == "rules":
                rules_embed = discord.Embed(
                    description='# Regras da TechLab\nSiga as regras abaixo para manter a comunidade saudável e produtiva.',
                    color=DEFAULT_EMBED_COLOR
                    )
                
                rules_embed.add_field(
                    name=f'{EMOJIS["set"]} Respeito acima de tudo',
                    value='Trate todos os membros com educação e respeito. Ofensas, discriminação ou ataques não serão tolerados.',
                    inline=False
                )


                rules_embed.add_field(
                    name=f'{EMOJIS["set"]} Sem spam ou publicidade',
                    value='Não envie links ou promoções de outros serviços sem permissão da equipe. O foco é bots, automações e sites.',
                    inline=False
                )


                rules_embed.add_field(
                    name=f'{EMOJIS["set"]} Pedidos e vendas',
                    value=('Negociações devem ocorrer nos canais corretos.\n'
                    'Fornecedores devem mostrar portfólio ou exemplos.\n'
                    'Compradores: verifiquem os serviços antes de pagar.\n'
                    'A equipe pode mediar disputas, mas não se responsabiliza por golpes.'),
                    inline=False
                )


                rules_embed.add_field(
                    name=f'{EMOJIS["set"]} Conteúdo permitido',
                    value='Somente conteúdos relacionados a tecnologia, bots, automações e desenvolvimento web. Conteúdos NSFW, pirataria ou ilegais são proibidos.',
                    inline=False
                )


                rules_embed.add_field(
                    name=f'{EMOJIS["set"]} Canais de suporte',
                    value='Use os canais de suporte para dúvidas, feedback ou problemas com serviços contratados. Evite marcar membros ou a equipe sem necessidade.',
                    inline=False
                )


                rules_embed.add_field(
                    name=f'{EMOJIS["set"]} Canais de voz',
                    value='Seja educado e evite ruídos ou interrupções. Conversas fora do tema podem ser redirecionadas para canais de bate-papo.',
                    inline=False
                )


                rules_embed.add_field(
                    name=f'{EMOJIS["set"]} Penalidades',
                    value='Quebra de regras pode resultar em advertência, mute, kick ou banimento, dependendo da gravidade.',
                    inline=False
                )

                rules_embed.set_footer(text='TechLab - 2025')
                
                await channels["rules_channel"].send(
                    embed=rules_embed
                ) 
                
                await interaction.response.send_message(
                    content=f"A embed foi enviada com sucesso para o canal {channels["price_channel"].mention}!",
                    ephemeral=True 
                )    
            
            elif keyword.lower() == "tips":
                embed = discord.Embed(
                    description=f"# Como funciona?",
                    color=DEFAULT_EMBED_COLOR 
                )
                
                embed.add_field(
                    name=f"{EMOJIS['set']} Como fazer um pedido?",
                    value=f"Para fazer um pedido na TechLab, você deverá abrir um ticket de atendimento em: {ticket_channel.mention}",
                    inline=True 
                )
                
                embed.add_field(
                    name=f"{EMOJIS['set']} Como fazer um orçamento personalizado?",
                    value=f"Para fazer um orçamento personalizado, abra um ticket de atendimento selecionando a opção `Solicitar um Orçamento` em: {ticket_channel.mention}",
                    inline=False 
                )
                
                embed.add_field(
                    name=f"{EMOJIS['set']} Como funciona o pagamento?",
                    value=f"Para acessar informações como valores e métodos de pagamento, vá para: {channels['price_channel'].mention}",
                    inline=True
                )
                
                embed.add_field(
                    name=f"{EMOJIS['exclamacao']} Atenção",
                    value="Em todo pedido e negociação de projetos, será cobrado um valor fixo de 40% do valor total adiantado.",
                    inline=False
                )
                
                embed.set_footer(text="TechLab - 2025")
                
                await channels["tips_channel"].send(
                    embed=embed 
                )
                
                await interaction.response.send_message(
                    content=f"Mensagem de dicas enviada com sucesso para o canal {channels['tips_channel'].mention}",
                    ephemeral=True
                )
        except Exception as err:
            await interaction.response.send_message(
                content=f"Ocorreu um erro ao tentar enviar a embed com a keyword `{keyword}`.", 
                ephemeral=True 
            )