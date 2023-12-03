from dotenv import load_dotenv
import os
import telebot
from thefuzz import fuzz
from thefuzz import process

# Importa funções de outros arquivos
# from menu_handlers import submenu_01, submenu_02,submenu_03,submenu_04, submenu_05, submenu_06, menu
# from verifiers import verify, verify_menu
# from data_loader import load_data


# Carrega dados da função load_data localizada em outro arquivo
questions, answers, code_answer, codes = load_data()


load_dotenv()
bot = telebot.TeleBot(os.getenv('TELEGRAM_API_KEY'))


@bot.message_handler(commands=['requerimento'])
def send_document(message):
    doc = open('RequerimentoNivelSuperiorPos.docx', 'rb')
    bot.send_document(message.chat.id, doc)
    doc.close()


def handle_sub_option(message, option_code):
    response = code_answer[option_code]
    response += "\n\nPara voltar clique em -> /menu."
    bot.send_message(message.chat.id, str(response))


@bot.message_handler(commands=codes)
def submenu(message):
    option_code_str = message.text.split('/')[1]
    handle_sub_option(message, option_code_str)


@bot.message_handler(commands=['01'])
def handle_submenu01(message):
    submenu_01(bot, message)


@bot.message_handler(commands=['02'])
def handle_submenu02(message):
    submenu_02(bot, message)


@bot.message_handler(commands=['03'])
def handle_submenu03(message):
    submenu_03(bot, message)


@bot.message_handler(commands=['04'])
def handle_submenu04(message):
    submenu_04(bot, message)


@bot.message_handler(commands=['05'])
def handle_submenu05(message):
    submenu_05(bot, message)

@bot.message_handler(commands=['06'])
def handle_submenu06(message):
    submenu_06(bot, message)


@bot.message_handler(func=lambda message: verify_menu(message, questions))
def handle_menu(message):
    menu(bot, message)


@bot.message_handler(func=lambda message: verify(message, questions))
def respond(message):
    question = message.text
    best_match = process.extractOne(question, questions)
    response = answers[best_match[0]]
    response += "\n\nPara voltar clique em -> /menu."  # Adicionando texto padrão ao final da resposta
    bot.reply_to(message, response)


bot.polling() 
