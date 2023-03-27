def getConfig(event):
    config = {
        "tts": """Вы всегда можете написать на нашу почту, superscriptsdebugers@yandex.ru""",
        "buttons": [
            "Повторить ещё раз",
            "Что ты умеешь?",
            "Помощь",
            "Назад",
            "Выход",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "1540737/f7f920f27d7c294e189b",
            "title": "КАК СВЯЗАТЬСЯ С НАМИ?",
            "description": """
            Почта команды: superscriptsdebugers@yandex.ru
            """,
        },
    }

    session_state = {"branch": "howToContactDevelopers"}

    return {
        "tts": config["tts"],
        "buttons": config["buttons"],
        "card": config["card"],
        "session_state": session_state,
    }