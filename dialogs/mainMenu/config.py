def getConfig(event):
    config = {
        "tts":
            """ 
Вы в главном меню. Скажите или нажмите кнопку Играть. Чтобы начать игру. Скажите или нажмите кнопку Помощь - для дополнительной информации по навыку.
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
            "image_id": "1533899/3d5238fe1ebfc6d7a360",
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
