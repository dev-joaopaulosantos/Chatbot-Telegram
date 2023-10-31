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

for row in data:
    for question in row['questions']:
        questions.append(question)
        answers[question] = row['answer']

print(questions)
print("= = = = = = = = = = = = = = = = = = = = = = = = = =")
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

@bot.message_handler(func=verify_main_menu)
def main_menu(message):
    text = """
    Escolha uma opção para continuar (Clique no item):

    /opcao1 Como solicitar declaração
    /opcao2 Informações sobre bolsas
    /opcao3 Informações sobre estágios

Ou digite sobre o que você deseja se informar!"""
    bot.reply_to(message, text)

@bot.message_handler(func=verify)
def respond(message):
    question = message.text
    best_match = process.extractOne(question, questions)
    response = answers[best_match[0]]
    bot.reply_to(message, str(response))

bot.polling()
