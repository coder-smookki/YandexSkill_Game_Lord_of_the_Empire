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
            "image_id": "imageid",
            "title": "КАТАЛОГ",
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
