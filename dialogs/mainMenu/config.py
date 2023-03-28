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
            "image_id": "1533899/d371aab5224c91137cfc",
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
