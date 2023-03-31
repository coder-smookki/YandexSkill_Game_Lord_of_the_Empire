from utils.triggerHelper import *
from utils.responseHelper import *
from utils.branchHandler import *

from middlewares.allMiddlewares import allMiddlewares
from dialogs.allDialogs import allDialogs
import os


def handler(event):
    # if (
    #     "session" in event
    #     and "skill_id" in event["session"]
    #     and event["session"]["skill_id"] != os.environ["SKILL_ID"]
    # ):
    #     return "привет =)"
    
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
