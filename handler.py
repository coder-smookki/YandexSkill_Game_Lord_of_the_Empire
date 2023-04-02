from utils.triggerHelper import *
from utils.responseHelper import *
from utils.branchHandler import *
from utils.dbHandler import insertNewStat, getStat
from middlewares.allMiddlewares import allMiddlewares
from dialogs.allDialogs import allDialogs
from utils.globalStorage import globalStorage
import os


def handler(event):
    if (
        "session" in event
        and "skill_id" in event["session"]
        and event["session"]["skill_id"] != os.environ["SKILL_ID"]
    ):
        return "привет =)"
    
    # если человек раньше не заходил, то создать для него отдельную строку со статистикой
    # Я сделал через запрос в бд, потому что мы не первый раз, а в бд нас нет
    # if not haveGlobalState(event, 'wasBefore') or getGlobalState(event, 'wasBefore') == False:
    if getStat(globalStorage["mariaDBconn"], getUserId(event)) is None:
        print('isWasBefore:', haveGlobalState(event, 'wasBefore'))
        insertNewStat(globalStorage['mariaDBconn'], getUserId(event))

    # глобальные стейты
    print(event["state"]["user"])

    # пройтись через мидлвейры
    for key in allMiddlewares:
        if not allMiddlewares[key]["isTriggered"](event):
            continue
        return allMiddlewares[key]["getResponse"](event, allDialogs)

    response = None  # на строке `return response` красным горело, поэтому так
    # искать диалог, подходящий под запрос
    for key in allDialogs:
        # если диалог не затриггерился
        if not allDialogs[key]["isTriggered"](event):
            continue

        if haveGlobalState(event, 'addStats'):
            print("Статы: ",getGlobalState(event, 'addStats'))
        else:
            print("Статов нет")

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
