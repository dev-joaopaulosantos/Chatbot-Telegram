from dotenv import load_dotenv
import os

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import telebot
from general_training import general_training

load_dotenv()

chatbot = ChatBot('FAQbot')
trainer = ListTrainer(chatbot)

# comando para limpar o banco de dados de treinamento
# chatbot.storage.drop()

trainer.train(general_training)

# Chave de API do Telegram
TELEGRAM_API_KEY = os.environ['TELEGRAM_API_KEY']

bot = telebot.TeleBot(TELEGRAM_API_KEY)


# @bot.message_handler(commands=["opcao1"])
# def option1(message):
#     bot.send_message(
#         message.chat.id, "Para mais informações sobre curriculos, procurar o controle academico!")


# @bot.message_handler(commands=["opcao2"])
# def option2(message):
#     bot.send_message(
#         message.chat.id, "Para informações sobre como trancar o curso, procurar o controle academico!")


# @bot.message_handler(commands=["opcao3"])
# def option3(message):
#     bot.send_message(
#         message.chat.id, "Para mais informações sobre dispensa de matérias, procurar o controle academico!")


# Função para verificar se a mensagem deve ser respondida pelo bot
def verify(message):
    return True


@bot.message_handler(func=verify)
def respond(message):
    question = message.text
    response = chatbot.get_response(question)

    if float(response.confidence) >= 0.6:
        bot.reply_to(message, str(response))
    else:
        bot.send_message(
            message.chat.id, "Peço desculpas, no momento não tenho a resposta para sua pergunta.")


# Iniciando a escuta de novas mensagens pelo bot
bot.polling()
