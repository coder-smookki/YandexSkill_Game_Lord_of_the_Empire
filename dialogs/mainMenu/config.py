def getConfig(event):
    config = {
        "tts":
            """ 
            ГЛАВНОЕ МЕНЮ, НАЖМИТЕ ИЛИ СКАЖИТЕ ИГРАТЬ, ЧТОБ НАЧАТЬ ИГРУ, ПОМОЩЬ - ДЛЯ ДОПОЛНИТЕЛЬНОЙ ИНФОРМАЦИИ
            """,
        "buttons": [
            'Играть',
            "Повторить ещё раз",
            "Что ты умеешь?",
            "Помощь",
            "Назад",
            "Выход",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "1540737/f7f920f27d7c294e189b",
            "title": "ГЛАВНОЕ МЕНЮ",
            "description":
                """
Выберите нужную категорию, которая поможет вам.
                """,
        },
}

    session_state = {"branch": "mainMenu"}

    return {
        "tts": config["tts"],
        "buttons": config["buttons"],
        "card": config["card"],
        "session_state": session_state,
    }
