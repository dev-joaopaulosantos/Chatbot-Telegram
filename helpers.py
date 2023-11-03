# helpers.py

import datetime

def get_salutation():
    current_hour = datetime.datetime.now().hour

    if current_hour < 12:
        return 'Bom dia'
    elif 12 <= current_hour < 18:
        return 'Boa tarde'
    else:
        return 'Boa noite'