# menu_handlers.py

from helpers import get_salutation


# def welcome(bot, message):
#     text = f"""
# Olá, {message.from_user.first_name}! Seja bem vindo(a) a *Assistente do IFPI Pedro II*
# Irei tirar suas dúvidas em relação aos processos da instituição
# de forma intuitiva e explicativa.

# Clique /aqui para começar ou digite a sua pergunta.
# """
#     bot.reply_to(message, text, parse_mode='Markdown')


def menu(bot, message):
    salutation = get_salutation()
    text = f"""
{salutation}, {message.from_user.first_name}! *Escolha uma opção para continuar* (Clique no item):

- /01 Como solicitar declaração
- /02 Informações sobre bolsas

Ou digite sobre o que você deseja se informar!
"""
    bot.send_message(message.chat.id, text, parse_mode='Markdown')


def submenu_01(bot, message):
    text = """
    Você escolheu a opção 1. Aqui estão algumas subopções:
    /OP01 Subopção 1
    /OP02 Subopção 2"""
    bot.send_message(message.chat.id, text)


def submenu_02(bot, message):
    text = """
    Você escolheu a opção 2. Aqui estão algumas subopções:
    /OP03 Subopção 3
    /OP04 Subopção 4"""
    bot.send_message(message.chat.id, text)
