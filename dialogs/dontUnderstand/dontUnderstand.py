from dialogs.dontUnderstand.config import getConfig
from utils.intents import RepeatIntents
from utils.triggerHelper import *
from utils.responseHelper import *


def getResponse(event, allDialogs=None):\
    print('dontUnderst Dialog')
    config = getConfig(event)
    return createResponse(event, config)

def isTriggered(event):
    return True

def isTriggeredDangerous(event):
    return isDangerousContext(event)


dontUnderstand = {"getResponse": getResponse, "isTriggered": isTriggered}
dontUnderstandDangerous = {"getResponse": getResponse, "isTriggered": isTriggeredDangerous}