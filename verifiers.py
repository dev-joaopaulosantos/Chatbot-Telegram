# verifiers.py

from thefuzz import fuzz
from thefuzz import process

def verify(message, questions):
    question = message.text
    best_match = process.extractOne(question, questions)
    if best_match[1] > 90:
        print(question, best_match)
        return True
    return False

def verify_menu(message, questions):
    question = message.text
    best_match = process.extractOne(question, questions)
    if best_match[1] <= 90:
        print(best_match)
        return True
    return False


def verify_first_message(message, first_messages):
    user_message = message.text.lower().strip()
    first_messages = [msg.lower().strip() for msg in first_messages]
    if user_message in first_messages:
        return True
    return False