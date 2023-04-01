from utils.triggerHelper import *
from utils.branchHandler import *
from utils.intents import BackIntents


def getResponse(event, allDialogs=None):
    return getDialogResponseFromEnd(event, 2, allDialogs)


def isTriggered(event):
    return not isInLastContext(event, 'game') and isInCommandOr(event, BackIntents)


backDialog = {"getResponse": getResponse, "isTriggered": isTriggered}
