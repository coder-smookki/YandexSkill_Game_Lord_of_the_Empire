def getConfig(event):
    config = {
        "tts": """помощь""",
        "buttons": [
            "Повторить ещё раз",
            "Что ты умеешь?",
            "Помощь",
            "Назад",
            "Выход",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "imageid",
            "title": "КАТАЛОГ",
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
