from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    response = {
        "response": {
            "text": """Вы не авторизованы и, к сожалению, пока что не можете использовать навык. 
        Мы добавим поддержку навыка для неавторизованных игроков как можно скорее.
        Если вы хотите поиграть, то авторизируйтесь в Яндекс ID. """,
            "tts": """Вы не авторизованы и, к сожалению, пока что не можете использовать навык. 
        Мы добавим поддержку навыка для неавторизованных игроков как можно скорее.
        Если вы хотите поиграть, то авторизируйтесь в Яндекс ID. """,
            "end_session": True,
        },
        "session": event["session"],  # инфа для Алисы - сессия
        "version": event["version"],  # инфа для Алисы - версия
    }

    return response


def isTriggered(event):
    return not isAuthorized(event)


checkAuth = {"getResponse": getResponse, "isTriggered": isTriggered}
