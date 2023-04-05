from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *
from utils.intents import MenuIntents
from utils.dbHandler import *
from utils.globalStorage import globalStorage


def getResponse(event, allDialogs=None):
    config = getConfig(event)

    return createResponse(event, config)


def isTriggered(event):
    return isInCommandOr(event, MenuIntents) or isNewSession(event)


mainMenu = {'getResponse': getResponse, 'isTriggered': isTriggered}
