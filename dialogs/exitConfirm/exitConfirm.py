from utils.intents import ExitIntens
from .config import *
from utils.triggerHelper import *
from utils.responseHelper import *
from utils.branchHandler import getDialogResponseFromEnd


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    if isInContext(event, "exitConfirm") and isInCommandOr(event, ExitIntens):
        return getConfirmResponse(event)
    elif isInContext(event, "exitConfirm"):
        return getDialogResponseFromEnd(event, 2, allDialogs)
    return createResponse(event, config)


def isTriggered(event):
    return isInContext(event, "exitConfirm") and isInCommandOr(event, ExitIntens)


exitConfirm = {"getResponse": getResponse, "isTriggered": isTriggered}
