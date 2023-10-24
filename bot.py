from dotenv import load_dotenv
import os
import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import telebot
# from general_training import conversation

load_dotenv()

data = json.loads(open('training.json', 'r', encoding='utf-8').read())
conv = []

for row in data:
    for question in row['questions']:
        conv.append(question)
        conv.append(row['answer'])


chatbot = ChatBot('FAQbot')
trainer = ListTrainer(chatbot)

# Limpa o banco de dados de treinamento
# chatbot.storage.drop()

trainer.train(conv)

# Chave de API do Telegram
TELEGRAM_API_KEY = os.environ['TELEGRAM_API_KEY']

bot = telebot.TeleBot(TELEGRAM_API_KEY)

# Função para verificar se a mensagem deve ser respondida pelo bot


def verify(message):
    return True


@bot.message_handler(func=verify)
def respond(message):
    question = message.text
    response = chatbot.get_response(question)

    if float(response.confidence) >= 0.4:
        bot.reply_to(message, str(response))
    else:
        bot.send_message(
            message.chat.id, "Peço desculpas, no momento não tenho a resposta para sua pergunta.")


# Iniciando a escuta de novas mensagens pelo bot
bot.polling()