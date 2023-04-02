from utils.intents import ExitIntents, YesIntents
from .config import *
from utils.triggerHelper import *
from utils.responseHelper import *
from utils.branchHandler import getDialogResponseFromEnd


def getResponse(event, allDialogs=None):
    isYes = isInCommandOr(event, YesIntents)
    isExit = isInCommandOr(event, ExitIntents)

    print(isYes)
    print(isExit)
    if isInLastContext(event, 'exitConfirm'):
        if isExit or isYes:
            return getConfirmResponse(event)
        return getDialogResponseFromEnd(event, 2, allDialogs)

    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    return isInCommandOr(event, ExitIntents) or isInLastContext(event, 'exitConfirm')

exitConfirm = {"getResponse": getResponse, "isTriggered": isTriggered}
