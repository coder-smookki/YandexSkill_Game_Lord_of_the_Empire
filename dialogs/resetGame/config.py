config = {
        "tts":
            """
            Вы уверены в том, что хотите сбросить сохранение?
            """,
        "buttons": [
            "Да",
            "Нет",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "1533899/d371aab5224c91137cfc",
            "title": "СБРОСИТЬ СОХРАНЕНИЕ?",
            "description":
                """
                Вы уверены в том, что хотите сбросить сохранение?
                """,
        },
}

session_state = {"branch": "resetGame"}


def getConfig(event):
    return {
        'message': config["tts"],
        "tts": config["tts"],
        "buttons": config["buttons"],
        "card": config["card"],
        "session_state": session_state,
    }
