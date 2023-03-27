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
            "image_id": "1540737/f7f920f27d7c294e189b",
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