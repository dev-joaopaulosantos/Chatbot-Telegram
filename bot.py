from dotenv import load_dotenv
import os
import json
import telebot
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

load_dotenv()

data = json.loads(open('training.json', 'r', encoding='utf-8').read())
questions = []
answers = {}
id_to_answer = {}
codes = []

for row in data:
    for question in row['questions']:
        questions.append(question)
        answers[question] = row['answer']
    id_to_answer[row['id']] = row['answer']
    codes.append(row['code'])

# print(questions)
# print("= = = = = = = = = = = = = = = = = = =")
# print(codes)

bot = telebot.TeleBot(os.getenv('TELEGRAM_API_KEY'))


def verify(message):
    question = message.text
    best_match = process.extractOne(question, questions)
    if best_match[1] > 80:
        return True


def verify_main_menu(message):
    question = message.text
    best_match = process.extractOne(question, questions)
    if best_match[1] <= 80:
        return True


def handle_sub_option(message, option_id):
    response = id_to_answer[option_id]
    bot.reply_to(message, str(response))


@bot.message_handler(commands=codes)
def sub_menu(message):
    option_id_str = message.text.split('OP')[-1]
    option_id_int = int(option_id_str)
    handle_sub_option(message, option_id_int)


@bot.message_handler(commands=['01'])
def menu_opcao1(message):
    text = """
    Você escolheu a opção 1. Aqui estão algumas subopções:
    /OP01 Subopção 1
    /OP02 Subopção 2"""
    bot.reply_to(message, text)


@bot.message_handler(commands=['02'])
def menu_opcao2(message):
    text = """
    Você escolheu a opção 2. Aqui estão algumas subopções:
    /OP03 Subopção 3
    /OP04 Subopção 4"""
    bot.reply_to(message, text)


@bot.message_handler(func=verify_main_menu)
def main_menu(message):
    text = """
*Escolha uma opção para continuar* (Clique no item):

- /01 Como solicitar declaração
- /02 Informações sobre bolsas

Ou digite sobre o que você deseja se informar!
"""
    bot.reply_to(message, text, parse_mode='Markdown')


@bot.message_handler(func=verify)
def respond(message):
    question = message.text
    best_match = process.extractOne(question, questions)
    response = answers[best_match[0]]
    bot.reply_to(message, str(response))


bot.polling()
