def getConfig(event):
    config = {
        "tts": """Ильин Кирилл, Плюснин Александр, Кунакбаев Радмир, Лесовой Кирилл, Кутников Родион""",
        "buttons": [
            "Повторить ещё раз",
            "Что ты умеешь?",
            "Помощь",
            "Назад",
            "Выход"
            ,
        ],
        "card": {
            "type": "BigImage",
            "image_id": "1540737/f7f920f27d7c294e189b",
            "title": "СОЗДАТЕЛИ НАВЫКА",
            "description": """
            Ильин Кирилл - ТимЛидер команды SSD - Super Scripts Debugers, 
            Плюснин Александр - Главный Разработчик (отвечающий за всю оболочку навыка), 
            Кунакбаев Радмир - Разработчик и Сценарист (дополняет функционал игры и придумывает весь сценарий игры), 
            Лесовой Кирилл - Разработчик и Тестировщик (обеспечивает навык полным функционалом игры и фиксирует ошибки), 
            Кутников Родион - Дизайнер (рисует АРТ картинки для навыка и придумывает дизайн навыка)
            """,
        },
    }

    session_state = {"branch": "whoAreCreators"}

    return {
        "tts": config["tts"],
        "buttons": config["buttons"],
        "card": config["card"],
        "session_state": session_state,
    }