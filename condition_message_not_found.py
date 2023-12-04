from verifiers import verify_menu, verify_first_message
from data_loader import load_data

questions, answers, code_answer, codes = load_data()

first_messages = ["Olá", "Oi", "Bom dia", "Boa tarde", "Boa noite", "Oi, tudo bem?", "start", "/start", "/menu"]


def check_conditions(message):
    return verify_menu(message, questions) and not verify_first_message(message, first_messages)