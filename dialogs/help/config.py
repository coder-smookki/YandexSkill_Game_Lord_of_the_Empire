from random import choice

ttss = ["Выберите нужную категорию, которая поможет вам",
        'Выберите категорию, которая подходит для вас',
        'Определитесь с категорией, которая будет полезна для вас',
        'Найдите категорию, которая поможет вам решить вашу проблему',
        'Какой вопрос вас интересует?',
        'Что вы хотите узнать?',
        ]


def getConfig(event):
    tts = choice(ttss)
    config = {
        "tts": f"""{tts}. Как связаться с разработчиками?. Кто разработчики навыка?. Как играть?""",
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
            {"title": "Как играть?",
             "hide": False
             },

        ],
        "card": {
            "type": "BigImage",
            "image_id": "1521359/3349afd66fa90845fd03",
            "title": "ПОМОЩЬ",
            "description": tts,
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
