# data_loader.py

import json

def load_data():
    data = json.loads(open('training.json', 'r', encoding='utf-8').read())
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