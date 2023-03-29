from utils.triggerHelper import *
from utils.branchHandler import *
from utils.responseHelper import *
from .config import *
from utils.globalStorage import *

def getResponse(event, allDialogs=None):
    if isInContext(event, "resetGame") and (
        "да" in getCommand(event)
        or "конечно" in getCommand(event)
        or "уверен" in getCommand(event)
        or "точно" in getCommand(event)
        or "выйти" in getCommand(event)
        or "выход" in getCommand(event)
        or "выйди" in getCommand(event)
    ):
        userId = getUserId(event)
        removeFromGlobalStorage("game_" + userId)
        response = createResponse(event, getConfig(event))
        setGlobalStatesInResponse(response, {'lastEpisode': None})
        return response

    return getDialogResponseFromEnd(event, 2, allDialogs)


def isTriggered(event):
    return (
        (
            isInContext(event, "exitConfirm")
            and (
                "да" in getCommand(event)
                or "конечно" in getCommand(event)
                or "уверен" in getCommand(event)
                or "точно" in getCommand(event)
                or "сброс" in getCommand(event)
                or "удали" in getCommand(event)
            )
        )
        or "сброс" in getCommand(event)
        or "сброс" in getCommand(event)
        or "сброс" in getCommand(event)
    )

backDialog = {"getResponse": getResponse, "isTriggered": isTriggered}
