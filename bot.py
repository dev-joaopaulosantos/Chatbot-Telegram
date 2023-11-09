from dotenv import load_dotenv
import os
import telebot
from thefuzz import fuzz
from thefuzz import process

# Import the function from the other file
from menu_handlers import submenu_01, submenu_02,submenu_03,submenu_04, menu
from verifiers import verify, verify_menu
from data_loader import load_data


# Load the data using the function from the other file
questions, answers, code_answer, codes = load_data()


load_dotenv()
bot = telebot.TeleBot(os.getenv('TELEGRAM_API_KEY'))


def handle_sub_option(message, option_code):
    response = code_answer[option_code]
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


@bot.message_handler(func=lambda message: verify_menu(message, questions))
def handle_menu(message):
    menu(bot, message)


@bot.message_handler(func=lambda message: verify(message, questions))
def respond(message):
    question = message.text
    best_match = process.extractOne(question, questions)
    response = answers[best_match[0]]
    bot.reply_to(message, str(response))


bot.polling() 
