from random import choice

ttss = ['Вы уверены в том, что хотите сбросить сохранение?',
        'Вы уверены, что хотите сбросить последнее приключение?',
        'Вы точно хотите сбросить игровой прогресс?',
        'Вы убедились, что хотите удалить сохранение?']

config = {
    "tts":
        """
        Вы уверены в том, что хотите сбросить сохранение?
        """,
    "buttons": [
        "Да",
        "Нет",
    ],
    "card": {
        "type": "BigImage",
        "image_id": "213044/f4706b04bb076f333b1b",
        "title": "СБРОСИТЬ СОХРАНЕНИЕ?",
        "description":
            """
            Вы уверены в том, что хотите сбросить сохранение?
            """,
    },
}

session_state = {"branch": "resetGame"}


def getConfig(event):
    tts = choice(ttss)
    card = config["card"].copy()
    card["description"] = tts
    return {
        'message': tts,
        "tts": tts,
        "buttons": config["buttons"],
        "card": card,
        "session_state": session_state,
    }
