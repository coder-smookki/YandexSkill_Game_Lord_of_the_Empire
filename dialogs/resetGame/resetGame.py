from utils.triggerHelper import *
from utils.branchHandler import *
from utils.responseHelper import *
from .config import *
from utils.dbHandler import *
from utils.globalStorage import globalStorage

def getResponse(event, allDialogs=None):
    if isInContext(event, "resetGame") and (
        "да" in getCommand(event)
        or "конечно" in getCommand(event)
        or "уверен" in getCommand(event)
        or "точно" in getCommand(event)
        or "сброс" in getCommand(event)
        or "удали" in getCommand(event)
    ):
        return getDialogResponseFromEnd(event, 2, allDialogs)
    userId = getUserId(event)
    conn = globalStorage['mariaDBconn']
    removeSave(conn, userId)
    response = createResponse(event, getConfig(event))
    setGlobalStatesInResponse(response, {"lastEpisode": None})
    return response


def isTriggered(event):
    return (
        (
            isInContext(event, "resetGame")
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


resetGame = {"getResponse": getResponse, "isTriggered": isTriggered}
