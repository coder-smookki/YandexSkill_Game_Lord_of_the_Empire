def getConfig(event):
    config = {
        "tts": """Вы всегда можете написать на нашу почту, super, scripts, debugers, @ yandex.ru""",
        "buttons": [
            "Повторить ещё раз",
            "Что ты умеешь?",
            "Назад",
            "Выход",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "1533899/d371aab5224c91137cfc",
            "title": "КАК СВЯЗАТЬСЯ С НАМИ?",
            "description": """
            Почта команды: superscriptsdebugers@yandex.ru
            """,
        },
    }

    session_state = {"branch": "howToContactDevelopers"}

    return {
        'message': config["tts"],
        "tts": config["tts"],
        "buttons": config["buttons"],
        "card": config["card"],
        "session_state": session_state,
    }