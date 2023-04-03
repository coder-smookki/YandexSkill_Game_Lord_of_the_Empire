from random import choice

ttss = ["Вы уверены в том, что хотите выйти?", "Вы точно хотите выйти?", "Вы подтверждаете свой выход?",
        "Вы намерены выйти?", "Подтверждаете ли вы свое решение о выходе из нашего навыка?", ]
see_you_agains = ["До скорых встреч! Были рады вас видеть в нашем навыке!",
                  "До свидания! Будем ждать вас снова!",
                  "До новых встреч! Надеюсь, увидеть вас снова!",
                  "До встречи позже! Были рады вас видеть в нашем навыке!",
                  "Спасибо за использование нашего навыка! Ждем вас снова!",
                  "Надеемся, что наш навык был интересен для вас. До скорой встречи!",
                  "Было приятно видеть вас в нашем навыке.До новых встреч!",
                  "Надеемся, что вы остались довольны нашим навыком. До скорой встречи!",
                  "Желаем вам успехов и удачи в использовании нашего навыка. До встречи позже!",
                  "Спасибо, что воспользовались нашим навыком. Будем ждать вас снова!"]

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
        "image_id": "213044/f4706b04bb076f333b1b",
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
