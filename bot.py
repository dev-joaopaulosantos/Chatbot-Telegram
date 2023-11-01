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


for row in data:
    for question in row['questions']:
        questions.append(question)
        answers[question] = row['answer']
    id_to_answer[row['id']] = row['answer']


print(questions)
print("= = = = = = = = = = = = = = = = = = = = = = =")
print(answers)

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


@bot.message_handler(commands=['subopcao1'])
def sub_menu_opcao1(message):
    response = id_to_answer[1]
    bot.reply_to(message, str(response))

@bot.message_handler(commands=['subopcao2'])
def sub_menu_opcao1(message):
    response = id_to_answer[2]
    bot.reply_to(message, str(response))

@bot.message_handler(commands=['subopcao3'])
def sub_menu_opcao1(message):
    response = id_to_answer[3]
    bot.reply_to(message, str(response))

@bot.message_handler(commands=['subopcao4'])
def sub_menu_opcao1(message):
    response = id_to_answer[4]
    bot.reply_to(message, str(response))



@bot.message_handler(commands=['opcao1'])
def menu_opcao1(message):
    text = """
    Você escolheu a opção 1. Aqui estão algumas subopções:
    /subopcao1 Subopção 1
    /subopcao2 Subopção 2"""
    bot.reply_to(message, text)



@bot.message_handler(commands=['opcao2'])
def menu_opcao2(message):
    text = """
    Você escolheu a opção 2. Aqui estão algumas subopções:
    /subopcao3 Subopção 3
    /subopcao4 Subopção 4"""
    bot.reply_to(message, text)



@bot.message_handler(func=verify_main_menu)
def main_menu(message):
    text = """
    Escolha uma opção para continuar (Clique no item):

    /opcao1 Como solicitar declaração
    /opcao2 Informações sobre bolsas

Ou digite sobre o que você deseja se informar!"""
    bot.reply_to(message, text)



@bot.message_handler(func=verify)
def respond(message):
    question = message.text
    best_match = process.extractOne(question, questions)
    response = answers[best_match[0]]
    bot.reply_to(message, str(response))

bot.polling()
