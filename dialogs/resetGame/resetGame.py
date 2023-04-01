from utils.intents import ResetIntents
from utils.triggerHelper import *
from utils.branchHandler import *
from utils.responseHelper import *
from .config import *
from utils.dbHandler import *
from utils.globalStorage import globalStorage


def getResponse(event, allDialogs=None):
    if isInCommandOr(event, ResetIntents):
        getDialogResponseFromEnd(event, 2, allDialogs)
    userId = getUserId(event)
    conn = globalStorage['mariaDBconn']
    removeSave(conn, userId)
    response = createResponse(event, getConfig(event))
    setGlobalStatesInResponse(response, {"lastEpisode": None})
    return response


def isTriggered(event):
    return isInCommandOr(event, ResetIntents)


resetGame = {"getResponse": getResponse, "isTriggered": isTriggered}
