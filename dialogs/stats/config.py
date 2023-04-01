from utils.dbHandler import getStat
from utils.globalStorage import globalStorage
from utils.responseHelper import getUserId

def getConfig(event):
    config = {
        "tts": """Ваша статистика:""",
        "buttons": [
            "Повторить ещё раз",
            "Помощь",
            "Назад",
            "Выход",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "1533899/d371aab5224c91137cfc",
            "title": "СТАТИСТИКА",
            "description": """
            Ваша статистика:
            """,
        },
    }

    session_state = {"branch": "stats"}

    conn = globalStorage['mariaDBconn']
    stats = getStat(conn, getUserId(event))

    print('stats',stats)
    print('userId',getUserId(event))
    if stats is None:
        return {
            'message': 'У вас нет статистики',
            "tts": 'У вас нет статистики',
            "buttons": config["buttons"],
            "card": config["card"],
            "session_state": session_state,
        } 

    config['tts'] += '\nСмерти: ' + str(stats['deaths'])
    config['tts'] += '\nОткрыто концовок: ' + str(stats['openEnds']) + ' из X'
    config['tts'] += '\nВстречено героев: ' + str(stats['meetedCharacters']) + ' из 21'
    # deaths, openEnds, meetedCharacters

    return {
        'message': config["tts"],
        "tts": config["tts"],
        "buttons": config["buttons"],
        "card": config["card"],
        "session_state": session_state,
    }
