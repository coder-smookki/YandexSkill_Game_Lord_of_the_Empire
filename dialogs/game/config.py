from utils.globalStorage import *
from utils.responseHelper import *
from utils.dbHandler import *
from utils.triggerHelper import *
from gameCore.historyHandler import passEpisode

def compileResultFromEpisode(episode):
    print('EPISODE', episode)
    config = {
        "tts": episode["name"] + ': ' + episode["message"],
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
    
    result = {
        "tts": config["tts"],
        "buttons": config["buttons"],
        "card": config["card"],
        "session_state": session_state,
    }

    result['user_state_update'] = {'lastEpisode': json.dumps(episode, ensure_ascii=False)}
    return result

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


def getConfig(event):
    history = globalStorage["history"]
    statsEnds = globalStorage["statsEnds"]

    userId = getUserId(event)
    if "game_" + userId in globalStorage:
        info = globalStorage["game_" + userId]
        # result['user_state_update']['lastEpisode']
    else:
        cur = globalStorage["mariaDBcur"]
        info = selectGameInfo(cur, userId)
        if not info:
            info = createStartInfo(history)

    if haveGlobalState(event, 'lastEpisode'):
        lastEpisode = json.loads(getGlobalState(event, 'lastEpisode'))
        canLastChoicedArr = lastEpisode['buttons']
    else:
        canLastChoicedArr = None
    command = getOriginalUtterance(event)

    # print('canLastChoicedArr:', canLastChoicedArr)

    if not (canLastChoicedArr is None):
        if len(canLastChoicedArr) == 1:
            print('one button')
            print('canLastChoicedArr:',canLastChoicedArr[0])
            info["choice"] = 'true'
        elif canLastChoicedArr[0] == command:
            print('true')
            print('command:',command)
            print('canLastChoicedArr:',canLastChoicedArr[0])
            info["choice"] = 'true'
        elif canLastChoicedArr[1] == command:
            print('false')
            print('command:',command)
            print('canLastChoicedArr:',canLastChoicedArr[1])
            info["choice"] = 'false'
        else:
            print('none')
            print('command:', command)
            print('canLastChoicedArr:',canLastChoicedArr)
            return compileResultFromEpisode(lastEpisode)

    episode = passEpisode(info, history, statsEnds)
    
    print('info before', info)
    setInGlobalStorage("game_" + userId, info, True)
    print('info after', info)

    
    return compileResultFromEpisode(episode)