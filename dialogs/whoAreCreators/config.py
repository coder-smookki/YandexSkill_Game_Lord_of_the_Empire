
def getConfig(event):
    config = {
        "tts": """как дела
            
норм

нормально""",
        "buttons": [
            "Повторить ещё раз",
            "Что ты умеешь?",
            "Назад",
            "Выход"
            ,
        ],
        "card": {
            "type": "BigImage",
            "image_id": "1521359/3349afd66fa90845fd03",
            "title": "СОЗДАТЕЛИ НАВЫКА",
            "description": """как дела
            
норм

нормально""",
        },
    }

    session_state = {"branch": "whoAreCreators"}

    return {
        'message': config["tts"],
        "tts": config["tts"],
        "buttons": config["buttons"],
        "card": config["card"],
        "session_state": session_state,
    }
