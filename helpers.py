# helpers.py

import datetime
import pytz

def get_salutation():
    # Configurar o fuso horário desejado
    tz = pytz.timezone('America/Sao_Paulo')  # Substitua pelo seu fuso horário

    # Obter a hora atual no fuso horário especificado
    current_time = datetime.datetime.now(tz)

    # Extrair a hora do objeto de data e hora
    current_hour = current_time.hour

    if current_hour < 12:
        return 'Bom dia'
    elif 12 <= current_hour < 18:
        return 'Boa tarde'
    else:
        return 'Boa noite'
