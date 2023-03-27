def getConfig(event):
    config = {
        "tts": """Вы всегда можете написать на нашу почту, superscriptsdebugers@yandex.ru""",
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
            "title": "КАК СВЯЗАТЬСЯ С НАМИ?",
            "description": """
            Ильин Кирилл (ТимЛидер): tg - https://t.me/ShVePs86, email - medved3loy@yandex.ru, discord - Shveps#9488
            Плюснин Александр (Разработчик): tg - https://t.me/elogrus, email - null, discord - elogrus#7802
            Кунакбаев Радмир (Сценарист): tg - https://t.me/sq1li, email - null , discord - oryh qdvwbd#2390
            Лесовой Кирилл (Тестировщик): tg - https://t.me/K1rLes, email - null, discord - K1rLes#3663
            Кутников Родион (Дизайнер): tg - https://t.me/Zl0yKobra, email - null, discord - IT_Технократ#7295
            """,
        },
    }

    session_state = {"branch": "howToContactDevelopers"}

    return {
        "tts": config["tts"],
        "buttons": config["buttons"],
        "card": config["card"],
        "session_state": session_state,
    }