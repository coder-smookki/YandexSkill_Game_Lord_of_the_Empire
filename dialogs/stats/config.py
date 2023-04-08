from utils.dbHandler import getStat
from utils.globalStorage import globalStorage
from utils.responseHelper import getUserId


def getConfig(event):
    config = {
        "tts": """Ваша статистика:""",
        "buttons": [
            "Повторить ещё раз",
            "Помощь",
            "Что ты умеешь?",
            "Назад",
            "Выход",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "213044/429b006958760896984b",
            "title": "СТАТИСТИКА",
            "description": """
            Ваша статистика:
            """,
        },
    }

    session_state = {"branch": "stats"}

    conn = globalStorage['mariaDBconn']
    stats = getStat(conn, getUserId(event))

    if stats is None:
        return {
            'message': 'У вас нет статистики.',
            "tts": 'У вас нет статистики.',
            "buttons": config["buttons"],
            "card": config["card"],
            "session_state": session_state,
        }

    config['tts'] += '\nСмерти: ' + str(stats['deaths']) + '.'
    config['tts'] += '\nОткрыто концовок: ' + str(len(stats['openEnds'])) + ' из 23.'
    config['tts'] += '\nВстречено героев: ' + str(len(stats['meetedCharacters'])) + ' из 21.'
    config['tts'] += '\nВарианты ответа для продолжения использования навыка. Повторить ещё раз, Помощь, Что ты умеешь?, Назад, Выход.'

    config['card']['description'] += '\nСмерти: ' + str(stats['deaths']) + '.'
    config['card']['description'] += '\nОткрыто концовок: ' + str(len(stats['openEnds'])) + ' из 23.'
    config['card']['description'] += '\nВстречено героев: ' + str(len(stats['meetedCharacters'])) + ' из 21.'

    # deaths, openEnds, meetedCharacters

    return {
        'message': config["tts"],
        "tts": config["tts"],
        "buttons": config["buttons"],
        "card": config["card"],
        "session_state": session_state,
    }
