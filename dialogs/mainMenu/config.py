def getConfig(event):
    config = {
        "tts":
            """ 
            главное меню
            """,
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
            "title": "КАТАЛОГ",
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
