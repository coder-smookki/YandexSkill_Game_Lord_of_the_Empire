from utils.globalStorage import *
from utils.responseHelper import *
from utils.dbHandler import *
from gameCore.historyHandler import passEpisode

def createStartInfo(history):
    return {
        "posEpisode": [0],
        "maxPosEpisode": [len(history) - 1],
        "pastPosEpisode": None,
        "choice": "none",
        "pastHasEvent": None,
        "stats": {"church": 50, "army": 50, "nation": 50, "coffers": 50},
        "notAppliedStats": {
            "true": [0, 0, 0, 0],
            "false": [0, 0, 0, 0],
            "always": [0, 0, 0, 0],
        },
    }


# {
#     "name": "имя",
#     "message": "сообщение",
#     "buttons": ["trueBtn", "falseBtn"],
#     "card": "айди картинки",
#     "stats": {"church": 50, "army": 50, "nation": 50, "coffers": 50},
#     "changeStats": [[trueStats], [falseStats]], - в таком же порядке, что и в "stats".
#           Может иметь не 2 массива, а 4 цифры - изменения стат после хода при любом выборе.
#           Может быть None.
# }
def getConfig(event):
    history = globalStorage["history"]
    statsEnds = globalStorage["statsEnds"]

    userId = getUserId(event)
    if "game_" + userId in globalStorage:
        info = selectGameInfo(cur, userId)
    else:
        cur = globalStorage["mariaDBcur"]
        info = selectGameInfo(cur, userId)
        if not info:
            info = createStartInfo(history)
            setInGlobalStorage("game_" + userId, info)

    episode = passEpisode(info, history, statsEnds)

    config = {
        "tts": episode["name"] + ' ' + episode["message"],
        "buttons": [
            # "Повторить ещё раз", TODO: добавить повторение
            "Что ты умеешь?",
            "Помощь",
            "Назад",
            "Выход",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "1540737/f7f920f27d7c294e189b", # заменить потом на айди картинки
            "title": episode["name"],
            "description": episode["message"],
        },
    }



    if len(episode['buttons']) != 0:
        config['buttons'] = episode['buttons'] + config['buttons']

    session_state = {"branch": "game"}

    return {
        "tts": config["tts"],
        "buttons": config["buttons"],
        "card": config["card"],
        "session_state": session_state,
    }
