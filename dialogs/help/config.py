def getConfig(event):
    config = {
        "tts": """Выберите нужную категорию, которая поможет вам. Как связаться с разработчиками?. Кто разработчики навыка?. Как пользоваться навыком?""",
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
