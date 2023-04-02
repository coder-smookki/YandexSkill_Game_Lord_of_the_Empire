from random import choice

ttss = ['Вы уверены в том, что хотите выйти?', 'Вы точно хотите выйти?', 'Вы подтверждаете свой выход?',
        'Вы намерены выйти?']
see_you_agains = ['До скорых встреч! Были рады вас видеть в нашем навыке!',
                  'До свидания! Будем ждать вас снова!',
                  'До новых встреч! Надеюсь, увидеть вас снова!',
                  'До встречи позже! Были рады вас видеть в нашем навыке!']

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
    tts = choice(ttss)
    card = config["card"].copy()
    card["description"] = tts
    return {
        'message': tts,
        "tts": tts,
        "buttons": config["buttons"],
        "card": card,
        "session_state": session_state,
    }


def getConfirmResponse(event):
    see_you_again = choice(see_you_agains)
    return {
        "response": {
            "text": see_you_again,
            "tts": see_you_again,
            "buttons": [],
            "end_session": True,
        },
        "version": event["version"],
        "dontUpdateBranches": True,
    }
