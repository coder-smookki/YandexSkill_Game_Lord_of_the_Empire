from .config import *
from utils.triggerHelper import *
from utils.responseHelper import *
from utils.branchHandler import getDialogResponseFromEnd


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    if isInContext(event, "exitConfirm") and (
        "да" in getCommand(event)
        or "конечно" in getCommand(event)
        or "уверен" in getCommand(event)
        or "точно" in getCommand(event)
        or "выйти" in getCommand(event)
        or "выход" in getCommand(event)
        or "выйди" in getCommand(event)
    ):
        return getConfirmResponse(event)
    elif isInContext(event, "exitConfirm"):
        return getDialogResponseFromEnd(event, 2, allDialogs)
    return createResponse(event, config)


def isTriggered(event):
    return (
        (
            isInContext(event, "exitConfirm")
            and (
                "да" in getCommand(event)
                or "конечно" in getCommand(event)
                or "уверен" in getCommand(event)
                or "точно" in getCommand(event)
                or "выйти" in getCommand(event)
                or "выход" in getCommand(event)
                or "выйди" in getCommand(event)
            )
        )
        or "выйти" in getCommand(event)
        or "выход" in getCommand(event)
        or "выйди" in getCommand(event)
    )


exitConfirm = {"getResponse": getResponse, "isTriggered": isTriggered}
