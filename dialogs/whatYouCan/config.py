def getConfig(event):
    config = {
        "tts": """что умеешь""",
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
            "title": "ЧТО Я УМЕЮ",
            "description": """
            что умеешь
            """,
        },
    }

    session_state = {"branch": "whatYouCan"}

    return {
        "tts": config["tts"],
        "buttons": config["buttons"],
        "card": config["card"],
        "session_state": session_state,
    }
