config = {
        "tts":
            """
            Вы уверены в том, что хотите выйти?
            """,
        "buttons": [
            "Да",
            "Нет",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "1533899/d371aab5224c91137cfc",
            "title": "ВЫЙТИ ИЗ НАВЫКА?",
            "description":
                """
                Вы уверены в том, что хотите выйти?
                """,
        },
}

session_state = {"branch": "exitConfirm"}


def getConfig(event):
    return {
        "tts": config["tts"],
        "buttons": config["buttons"],
        "card": config["card"],
        "session_state": session_state,
    }


def getConfirmResponse(event):
        return {
            "response": {
                "text": "До скорых встреч! Были рады вас видеть в нашем навыке!",
                "tts": "До скорых встреч! Были рады вас видеть в нашем навыке!",
                "buttons": [],
                "end_session": True,
            },
            "version": event["version"],
            "dontUpdateBranches": True,
        }