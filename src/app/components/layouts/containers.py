from ...constants.constants import EMOJIS
from discord import ui, SeparatorSpacing

class PricesLayout(ui.LayoutView):
    def __init__(self, ticket_channel):
        super().__init__()

        container = ui.Container(ui.TextDisplay('# Serviços e Preços'))
        container.add_item(ui.Separator(spacing=SeparatorSpacing.large))

        container.add_item(ui.TextDisplay('### Como fazer um pedido?'))
        container.add_item(
            ui.TextDisplay(f'{EMOJIS["set"]} Para fazer um pedido na TechLab, abra um ticket em: {ticket_channel.mention}')
        )
        container.add_item(ui.Separator(spacing=SeparatorSpacing.small))

        container.add_item(ui.TextDisplay('### Valores mínimos'))
        container.add_item(ui.TextDisplay(f'{EMOJIS["set"]} Bots: 80€ / R$ 150,00'))
        container.add_item(ui.TextDisplay(f'{EMOJIS["set"]} Automações: 150€ / R$ 250,00'))
        container.add_item(ui.TextDisplay(f'{EMOJIS["set"]} Sites: 150€ / R$ 350,00'))
        container.add_item(ui.Separator(spacing=SeparatorSpacing.small))

        container.add_item(ui.TextDisplay('### Métodos de pagamento'))
        container.add_item(ui.TextDisplay(f'{EMOJIS["set"]} PIX & PayPal'))

        self.add_item(container)


class RulesLayout(ui.LayoutView):
    def __init__(self):
        super().__init__()

        container = ui.Container(ui.TextDisplay('# Regras da TechLab'))
        container.add_item(ui.Separator(spacing=SeparatorSpacing.large))

        rules = [
            ("Respeito acima de tudo", "Trate todos os membros com educação e respeito. Ofensas, discriminação ou ataques não serão tolerados."),
            ("Sem spam ou publicidade", "Não envie links ou promoções de outros serviços sem permissão da equipe."),
            ("Pedidos e vendas", "Negociações devem ocorrer nos canais corretos. Fornecedores devem mostrar portfólio ou exemplos."),
            ("Conteúdo permitido", "Somente conteúdos relacionados a tecnologia, bots, automações e desenvolvimento web. Conteúdos NSFW, pirataria ou ilegais são proibidos."),
            ("Canais de suporte", "Use os canais de suporte para dúvidas, feedback ou problemas com serviços contratados."),
            ("Canais de voz", "Seja educado e evite ruídos ou interrupções."),
            ("Penalidades", "Quebra de regras pode resultar em advertência, mute, kick ou banimento, dependendo da gravidade.")
        ]

        for title, desc in rules:
            container.add_item(ui.Separator(spacing=SeparatorSpacing.small))
            container.add_item(ui.TextDisplay(f'### {EMOJIS["set"]} {title}'))
            container.add_item(ui.TextDisplay(desc))

        self.add_item(container)


class TipsLayout(ui.LayoutView):
    def __init__(self, ticket_channel, price_channel):
        super().__init__()

        container = ui.Container(ui.TextDisplay('# Dicas e Informações'))
        container.add_item(ui.Separator(spacing=SeparatorSpacing.large))

        tips = [
            (f'{EMOJIS["set"]} Como fazer um pedido?', f'Abra um ticket em: {ticket_channel.mention}'),
            (f'{EMOJIS["set"]} Como fazer um orçamento?', f'Abra um ticket em: {ticket_channel.mention} e selecione "Solicitar Orçamento"'),
            (f'{EMOJIS["set"]} Pagamento', f'Informações de valores e métodos estão em {price_channel.mention}'),
            (f'{EMOJIS["exclamacao"]} Atenção', 'Será cobrado 40% do valor total adiantado em todos os pedidos.')
        ]

        for title, desc in tips:
            container.add_item(ui.Separator(spacing=SeparatorSpacing.small))
            container.add_item(ui.TextDisplay(f'### {title}'))
            container.add_item(ui.TextDisplay(desc))

        self.add_item(container)