from utils.intents import RepeatIntents
from utils.triggerHelper import *
from utils.responseHelper import *


def getResponse(event, allDialogs=None):
    return allDialogs[getState(event, "branch")[-1]]["getResponse"](event, allDialogs)


def isTriggered(event):
    return isInCommandOr(event, RepeatIntents)


repeat = {"getResponse": getResponse, "isTriggered": isTriggered}
