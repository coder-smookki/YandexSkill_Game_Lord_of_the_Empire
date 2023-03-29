from utils.globalStorage import *
from utils.responseHelper import *
from utils.dbHandler import *
from utils.triggerHelper import *
from gameCore.historyHandler import passEpisode
import random
from utils.image_gen.get_id import get_id

sfx = [
    '<speaker audio="dialogs-upload/4b310008-3fd4-4d8d-842c-34753abee342/f1d3a69c-3002-4cf7-9e28-e3c7b3514ac1.opus">',
    '<speaker audio="dialogs-upload/4b310008-3fd4-4d8d-842c-34753abee342/5b9bcd97-2d4a-4810-8639-28518868a548.opus">',
    '<speaker audio="dialogs-upload/4b310008-3fd4-4d8d-842c-34753abee342/af8d12e0-04f4-447e-9f6a-5418424c2daa.opus">',
    '<speaker audio="dialogs-upload/4b310008-3fd4-4d8d-842c-34753abee342/3b79ef82-e551-4e8c-a913-e953ffbfd7cd.opus">',
    '<speaker audio="dialogs-upload/4b310008-3fd4-4d8d-842c-34753abee342/506fc86d-ee86-4b65-82e5-cc6c59012ce9.opus">',
    '<speaker audio="dialogs-upload/4b310008-3fd4-4d8d-842c-34753abee342/59937e1e-576e-4e8a-84b7-7fdec826edbf.opus">',
    '<speaker audio="dialogs-upload/4b310008-3fd4-4d8d-842c-34753abee342/6232e501-5a2e-4c97-b193-f3e293a3d879.opus">',
    '<speaker audio="dialogs-upload/4b310008-3fd4-4d8d-842c-34753abee342/1cace3da-e83c-4eb5-aa63-9bd718ca01b7.opus">',
    '<speaker audio="dialogs-upload/4b310008-3fd4-4d8d-842c-34753abee342/3ee32d10-842e-4e93-86d6-da158cba6e3d.opus">'
]

def getRandomSfx(sfx):
    return sfx[random.randint(0, len(sfx) - 1)]

def compileResultFromEpisode(episode):
    print('EPISODE', episode)

    if episode == "its all":
        print('getted its all episode')
        return "its all"

    if episode["name"] and not ('Крестьянин' in episode["name"]):
        tts = getRandomSfx(sfx) + episode["name"] + '. ' + episode["message"]
        # print('VALUES',episode['stats'])
        stats = episode['stats']
        cardId = get_id(
            person=episode["name"],
            replica=episode["message"],
            values=[stats['church'],stats['nation'],stats['army'],stats['coffers']],
            changes=[0,0,0,0]
        )
        if cardId is None:
            cardId = "1533899/d371aab5224c91137cfc"
    else:
        tts = getRandomSfx(sfx) + episode["message"]
        cardId = "1533899/d371aab5224c91137cfc"



    config = {
        "tts": tts,
        "buttons": [
            # "Повторить ещё раз", TODO: добавить повторение
            "В главное меню",
            "Выход",
        ],
        "card": {
            "type": "BigImage",
            "image_id": cardId,
            "title": episode["name"],
            "description": episode["message"],
        },
    }

    if len(episode['buttons']) != 0:
        config['buttons'] = episode['buttons'] + config['buttons']
        user_state_update = {'lastEpisode': json.dumps(episode, ensure_ascii=False)}

    session_state = {"branch": "game"}
    
    result = {
        "tts": config["tts"],
        "buttons": config["buttons"],
        "card": config["card"],
        "session_state": session_state,
    }
    if user_state_update:
        result['user_state_update'] = user_state_update
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
        # cur = globalStorage["mariaDBcur"]
        # info = selectGameInfo(cur, userId)
        info = False
        if not info:
            info = createStartInfo(history)

    if haveGlobalState(event, 'lastEpisode'):
        lastEpisode = json.loads(getGlobalState(event, 'lastEpisode'))
        canLastChoicedArr = lastEpisode['buttons']
    else:
        canLastChoicedArr = None

    if not canLastChoicedArr and len(canLastChoicedArr) == 0:
        removeFromGlobalStorage("game_" + userId)
        return getConfig(event)

        # ''.join(filter(str.isalnum, s))
    command = getOriginalUtterance(event)

    # print('canLastChoicedArr:', canLastChoicedArr)

    if canLastChoicedArr:
        if len(canLastChoicedArr) == 1:
            # print('one button')
            # print('canLastChoicedArr:',canLastChoicedArr[0])
            info["choice"] = 'true'
        elif canLastChoicedArr[0] == command:
            # print('true')
            # print('command:',command)
            # print('canLastChoicedArr:',canLastChoicedArr[0])
            info["choice"] = 'true'
        elif canLastChoicedArr[1] == command:
            # print('false')
            # print('command:',command)
            # print('canLastChoicedArr:',canLastChoicedArr[1])
            info["choice"] = 'false'
        else:
            # print('none')
            # print('command:', command)
            # print('canLastChoicedArr:',canLastChoicedArr)
            return compileResultFromEpisode(lastEpisode)

    episode = passEpisode(info, history, statsEnds)

    # print('info before', info)
    setInGlobalStorage("game_" + userId, info, True)
    # print('info after', info)

    
    return compileResultFromEpisode(episode)
