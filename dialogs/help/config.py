def getConfig(event):
    config = {
        "tts": """Раздел помощи""",
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
            "title": "ПОМОЩЬ",
            "description": """
Выберите нужную категорию, которая поможет вам.
                """,
        },
    }

    session_state = {"branch": "help"}

    return {
        "tts": config["tts"],
        "buttons": config["buttons"],
        "card": config["card"],
        "session_state": session_state,
    }
