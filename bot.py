from dotenv import load_dotenv
import os
import telebot
from fuzzywuzzy import process

# Import the function from the other file
from menu_handlers import menu_opcao1, menu_opcao2, main_menu
from verifiers import verify, verify_main_menu
from data_loader import load_data


# Load the data using the function from the other file
questions, answers, code_answer, codes = load_data()


load_dotenv()


bot = telebot.TeleBot(os.getenv('TELEGRAM_API_KEY'))


def handle_sub_option(message, option_code):
    response = code_answer[option_code]
    bot.reply_to(message, str(response))


@bot.message_handler(commands=codes)
def sub_menu(message):
    option_code_str = message.text.split('/')[1]
    handle_sub_option(message, option_code_str)


@bot.message_handler(commands=['01'])
def handle_menu_opcao1(message):
    menu_opcao1(bot, message)


@bot.message_handler(commands=['02'])
def handle_menu_opcao2(message):
    menu_opcao2(bot, message)


@bot.message_handler(func=lambda message: verify_main_menu(message, questions))
def handle_main_menu(message):
    main_menu(bot, message)


@bot.message_handler(func=lambda message: verify(message, questions))
def respond(message):
    question = message.text
    best_match = process.extractOne(question, questions)
    response = answers[best_match[0]]
    bot.reply_to(message, str(response))


bot.polling()
