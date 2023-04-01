from utils.intents import HelpIntents
from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    return isInCommandOr(event, HelpIntents)


help = {'getResponse': getResponse, 'isTriggered': isTriggered}
