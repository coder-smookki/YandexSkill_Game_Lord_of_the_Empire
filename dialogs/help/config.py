def getConfig(event):
    config = {
        "tts": """Выберите нужную категорию, которая поможет вам. Как связаться с разработчиками?. Кто разработчики навыка?. Как пользоваться навыком?
        На данный момент вам доступны такие варианты ответов:
        Играть. Как связаться с разработчиками?. Кто разработчики навыка?. Как пользоваться навыком?. Повторить ещё раз. Что ты умеешь?. Назад. Выход.""",
        "buttons": [
            "Повторить ещё раз",
            "Что ты умеешь?",
            "Назад",
            "Выход",
            {"title": "Как связаться с разработчиками?",
             "hide": False
             },
            {"title": "Кто разработчики навыка?",
             "hide": False
             },
            {"title": "Как пользоваться навыком?",
             "hide": False
             },

        ],
        "card": {
            "type": "BigImage",
            "image_id": "1533899/d371aab5224c91137cfc",
            "title": "ПОМОЩЬ",
            "description": """
            Выберите нужную категорию, которая поможет вам.
                """,
        },
    }

    session_state = {"branch": "help"}

    return {
        'message': config["tts"],
        "tts": config["tts"],
        "buttons": config["buttons"],
        "card": config["card"],
        "session_state": session_state,
    }
