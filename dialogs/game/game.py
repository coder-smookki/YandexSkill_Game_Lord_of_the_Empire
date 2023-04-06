from utils.intents import LetsPlayIntents, YesIntents
from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    if not haveState(event, 'fromGame') or getState(event, 'fromGame') == False:
        print('not fromGame')
        config = getConfig(event, allDialogs, repeat=True)
    else:
        print('fromGame')
        config = getConfig(event, allDialogs)

    return createResponse(event, config)


def isTriggered(event):
    return isInCommandOr(event, LetsPlayIntents) or isInLastContext(event, "game")


game = {"getResponse": getResponse, "isTriggered": isTriggered}
