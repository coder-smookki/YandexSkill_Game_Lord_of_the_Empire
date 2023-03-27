from utils.triggerHelper import *
from utils.responseHelper import *

def getResponse(event, allDialogs=None):
    return allDialogs[getState(event, "branch")[-1]]["getResponse"](event, allDialogs)


def isTriggered(event):
    return (
        "повтори" in getCommand(event)
        or "еще раз" in getCommand(event)
        or "ещё раз" in getCommand(event)
    )


repeat = {"getResponse": getResponse, "isTriggered": isTriggered}
