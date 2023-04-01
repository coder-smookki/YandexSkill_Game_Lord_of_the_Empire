from utils.intents import ResetIntents,YesIntents
from utils.triggerHelper import *
from utils.branchHandler import *
from utils.responseHelper import *
from .config import *
from utils.dbHandler import *
from utils.globalStorage import globalStorage


def getResponse(event, allDialogs=None):
    if isInCommandOr(event, YesIntents) and isInLastContext(event, 'resetGame'):
        userId = getUserId(event)
        conn = globalStorage['mariaDBconn']
        removeSave(conn, userId)
        response = getDialogResponseFromEnd(event, 2, allDialogs)
        addGlobalStateInResponse(response,'playedBefore', False)

    return createResponse(event, getConfig(event))
    


def isTriggered(event):
    return isInCommandOr(event, ResetIntents) or isInLastContext(event, 'resetGame')


resetGame = {"getResponse": getResponse, "isTriggered": isTriggered}
