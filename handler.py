from utils.triggerHelper import *
from utils.responseHelper import *
from utils.branchHandler import *

from middlewares.allMiddlewares import allMiddlewares
from dialogs.allDialogs import allDialogs


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

import os


def handler(event):
    if (
        "session" in event
        and "skill_id" in event["session"]
        and event["session"]["skill_id"] != os.environ["SKILL_ID"]
    ):
        return "привет =)"
    # ['state']['session']
    if not "state" in event:
        event["state"] = {"session": {'branch': []}}
    elif not 'session' in event['state']:
        event["state"]['session'] = {'branch': []}

    if not isNewSession(event):
        for key in allMiddlewares:
            if not allMiddlewares[key]["isTriggered"](event):
                continue
            return allMiddlewares[key]["getResponse"](event, allDialogs)

    # искать диалог, подходящий под запрос
    for key in allDialogs:
        # если диалог не затриггерился
        if not allDialogs[key]["isTriggered"](event):
            continue

        # если диалог затриггерился, получить его респонс
        response = allDialogs[key]["getResponse"](event, allDialogs)

        # обработать брэнчи
        branchedResponse = updateBranchToResponse(event, response, "mainMenu")

        # FOR DEBUG
        if branchedResponse and "session_state" in branchedResponse:
            print("Брэнчи: " + str(branchedResponse["session_state"]["branch"]))
        else:
            print("Брэнчей нет")
        print("---------------------------")
        
        return branchedResponse

    return response
