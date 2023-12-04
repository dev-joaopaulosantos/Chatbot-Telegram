# menu_handlers.py

from helpers import get_salutation
from condition_message_not_found import check_conditions

first_time_users = set()

def menu(bot, message):
    global first_time_users

    salutation = get_salutation()
    first_name = message.from_user.first_name or ""
    last_name = message.from_user.last_name or ""

    wellcome_text = f"{salutation}, {first_name} {last_name} \nBem-vindo ao Chatbot Acadêmico do IFPI Campus Pedro II! 🎓🤖\n\nEstou aqui para te auxiliar com informações acadêmicas. Sinta-se à vontade para explorar e esclarecer suas dúvidas."

    if check_conditions(message) and message.from_user.id in first_time_users:
        bot.reply_to(message, "Desculpe, não encontrei a informação solicitada.\n\nVamos tentar novamente. Por favor, selecione uma opção do menu para continuar.")


    if message.from_user.id not in first_time_users:
        bot.reply_to(message, wellcome_text)
        first_time_users.add(message.from_user.id)



    text = f"""
{salutation}, {first_name}! *Escolha um tópico para continuar* (Clique no item):

/01 Setor de Saúde.
/02 Programas Estudantis.
/03 Processos Acadêmicos.
/04 Sistema Unificado de Administração Pública (SUAP).
/05 Atividades Complementares.
/06 Contatos da Administração.

Ou digite sobre o que você deseja se informar!
"""
    bot.send_message(message.chat.id, text, parse_mode='Markdown')




def submenu_01(bot, message):
    text = """
Você escolheu o tópico *Setor de Saúde*. selecione a opção desejada. (Clique no Item):

/A01 Sobre o setor de saúde.
/A02 Como marcar uma consulta ou solicitar atendimento.
    
Para voltar clique em -> /menu
    """
    bot.send_message(message.chat.id, text, parse_mode='Markdown')


def submenu_02(bot, message):
    text = """
Você escolheu o tópico *Programas Estudantis*. selecione a opção desejada. (Clique no Item):

/B01 PIBIC - Programa Institucional de Bolsas de Iniciação Científica.
/B02 Monitoria.
/B03 Tipos Monitoria.
    
Para voltar clique em -> /menu
    """
    bot.send_message(message.chat.id, text, parse_mode='Markdown')



def submenu_03(bot, message):
    text = """
Você escolheu o tópico *Processos Acadêmicos*. selecione a opção desejada. (Clique no Item):

/C01 Solicitação de prova de segunda chamada.
/C02 Solicitação de trancamento de curso.
/C03 Solicitação de Diploma de nível superior.
/C04 Baixar requerimento.
    
Para voltar clique em -> /menu
    """
    bot.send_message(message.chat.id, text, parse_mode='Markdown')


def submenu_04(bot, message):
    text = """
Você escolheu o tópico *SUAP*. selecione a opção desejada. (Clique no Item):

/D01 Declaração de vínculo.
/D02 Histórico.
/D03 Declaração de carga horária integralizada.
/D04 Declaração de matrícula.
/D05 Comprovante de dados acadêmicos.
    
Para voltar clique em -> /menu
    """
    bot.send_message(message.chat.id, text, parse_mode='Markdown')



def submenu_05(bot, message):
    text = """
Você escolheu o tópico *Atividades Complementares*. selecione a opção desejada. (Clique no Item):

/E01 Sobre as atividades complementares.
/E02 Validação das cargas horárias.
/E03 O que são consideradas atividades complementares.
    
Para voltar clique em -> /menu
    """
    bot.send_message(message.chat.id, text, parse_mode='Markdown')


def submenu_06(bot, message):
    text = """
Você escolheu o tópico *Contatos da Administração*. selecione a opção desejada. (Clique no Item):

/F01 Diretoria Geral.
/F02 Diretoria de Ensino.
/F03 Coordenação Pedagógica.
/F04 Coordenação de Saúde.
/F05 Coordenação de Disciplina.
/F06 Coordenação de Tecnologia da Informação.
/F07 Coordenação do Curso de Administração.
/F08 Coordenação do Curso de Ciências Biológicas.
/F09 Coordenação do Curso de ADS.
/F10 Coordenação do NAPNE.
    
Para voltar clique em -> /menu
    """
    bot.send_message(message.chat.id, text, parse_mode='Markdown')
