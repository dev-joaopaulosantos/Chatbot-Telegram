# menu_handlers.py

from helpers import get_salutation


def main_menu(bot, message):
    salutation = get_salutation()
    text = f"""
{salutation}, {message.from_user.first_name}! *Escolha uma opção para continuar* (Clique no item):

- /01 Como solicitar declaração
- /02 Informações sobre bolsas

Ou digite sobre o que você deseja se informar!
"""
    bot.reply_to(message, "teste")
    bot.reply_to(message, text, parse_mode='Markdown')


def menu_opcao1(bot, message):
    text = """
    Você escolheu a opção 1. Aqui estão algumas subopções:
    /OP01 Subopção 1
    /OP02 Subopção 2"""
    bot.reply_to(message, text)


def menu_opcao2(bot, message):
    text = """
    Você escolheu a opção 2. Aqui estão algumas subopções:
    /OP03 Subopção 3
    /OP04 Subopção 4"""
    bot.reply_to(message, text)
