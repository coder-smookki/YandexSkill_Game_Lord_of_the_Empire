from random import choice

ttss = [
    """Простите, я не понял Вас. Можете повторить, пожалуйста? Большое спасибо.""",
    """Извините, не совсем понял, что Вы имели ввиду. Можете повторить, пожалуйста? Большое спасибо.""",
    """Прошу прощения, я не уловил смысл Вашего сообщения. Не могли бы Вы повторить ещё раз? Спасибо.""",
    """Сожалею, но я не понимаю Вас. Можете повторить, пожалуйста? Благодарю вас""",
    """Извините, но я не улавливаю Вашу мысль. Прошу повторить ещё раз. Большое спасибо"""
]


def getConfig(event, variants_of_the_choice: list[str] = '', branch='mainMenu'):
    tts = choice(ttss)
    config = {
        "tts": f"""{tts}...{'...'.join(variants_of_the_choice)}""",

        "buttons": [
            "В главное меню",
            "Повторить ещё раз",
            "Что ты умеешь?",
            "Назад",
            "Выход",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "1533899/d371aab5224c91137cfc",
            "title": "НЕ СОВСЕМ ПОНЯТНО",
            "description": tts,
        },
    }

    if variants_of_the_choice:
        config["buttons"] = [*variants_of_the_choice, *config["buttons"]]

    session_state = {"branch": branch}

    return {
        'message': config["tts"],
        "tts": config["tts"],
        "buttons": config["buttons"],
        "card": config["card"],
        "session_state": session_state,
    }
