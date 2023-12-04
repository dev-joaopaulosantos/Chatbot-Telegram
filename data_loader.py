# data_loader.py

import json

def load_data():
    with open('data_base.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    questions = []
    answers = {}
    code_answer = {}
    codes = []

    for row in data:
        for question in row['questions']:
            questions.append(question)
            answers[question] = row['answer']
        code_answer[row['code']] = row['answer']
        codes.append(row['code'])

    return questions, answers, code_answer, codes
