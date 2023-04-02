from utils.intents import ResetIntents, YesIntents, NoIntents
from utils.triggerHelper import *
from utils.branchHandler import *
from utils.responseHelper import *
from .config import *
from utils.dbHandler import *
from utils.globalStorage import globalStorage


def getResponse(event, allDialogs=None):
    isYes = isInCommandOr(event, YesIntents)
    isReset = isInCommandOr(event, ResetIntents)
    if isInLastContext(event, 'resetGame'):
        if isReset or isYes:
            userId = getUserId(event)
            conn = globalStorage['mariaDBconn']
            removeSave(conn, userId)
        response = getDialogResponseFromEnd(event, 2, allDialogs)
        # addGlobalStateInResponse(response,'playedBefore', False)
        return response

    return createResponse(event, getConfig(event))


def isTriggered(event):
    return (isInCommandOr(event, ResetIntents) and isInLastContext(event, 'mainMenu')) or isInLastContext(event, 'resetGame')
        


resetGame = {"getResponse": getResponse, "isTriggered": isTriggered}
