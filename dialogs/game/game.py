from utils.intents import LetsPlayIntents, YesIntents
from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event, allDialogs)
    return createResponse(event, config)


def isTriggered(event):
    return (
        isInCommandOr(event, LetsPlayIntents)
        or (
            isInLastContext(event, "game")
            and not haveState(event, "endGame")
        )
        or (
            isInLastContext(event, "game")
            and haveState(event, "endGame")
            and isInCommandOr(event, YesIntents)
        )
        
    )


game = {"getResponse": getResponse, "isTriggered": isTriggered}
