from dialogs.dontUnderstand.config import getConfig
from utils.intents import RepeatIntents
from utils.triggerHelper import *
from utils.responseHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    return True


dontUnderstand = {"getResponse": getResponse, "isTriggered": isTriggered}