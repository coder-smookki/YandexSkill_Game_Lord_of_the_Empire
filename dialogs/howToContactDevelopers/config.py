from random import choice

ttss = ['Вы всегда можете написать на нашу почту',
        'Вы всегда можете написать нам на почту',
        'Если у вас есть вопросы, не стесняйтесь обращаться к нам по электронной почте',
        'Наша электронная почта всегда открыта для ваших просьб и предложений']


def getConfig(event):
    tts = choice(ttss)
    config = {
        "tts": f"""{tts}. super. scripts. debugers. @ yandex. точка. ru.
        Варианты ответов которые доступны вам сейчас:
        Играть. Повторить ещё раз. Что ты умеешь?. Назад. Выход.""",
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
            Почта команды: SuperScriptsDebugers@yandex.ru
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