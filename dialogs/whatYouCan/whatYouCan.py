from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    return "что" in getCommand(event) and (
        "умеешь" in getCommand(event)
        or "можешь" in getCommand(event)
        or "способен" in getCommand(event)
    )


whatYouCan = {"getResponse": getResponse, "isTriggered": isTriggered}
