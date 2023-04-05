from utils.intents import WhatDoYouCanIntents
from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    return isInCommandOr(event, ['чё', 'что', 'че', ]) and isInCommandOr(event, WhatDoYouCanIntents)


whatYouCan = {"getResponse": getResponse, "isTriggered": isTriggered}
