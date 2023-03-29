from utils.triggerHelper import *
from utils.branchHandler import *

def getResponse(event, allDialogs=None):
    response = getDialogResponseFromEnd(event, 2, allDialogs)
    response["user_state_update"] = {'lastEpisode': None}
    return response


def isTriggered(event):
    return not isInLastContext(event, 'game') and isInCommandOr(event, ["сброс"])


backDialog = {"getResponse": getResponse, "isTriggered": isTriggered}
