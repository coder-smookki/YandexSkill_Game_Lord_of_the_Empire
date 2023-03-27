from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)

def isTriggered(event):
    return "связаться" in getCommand(event) or "обратиться" in getCommand(event)

howToContactDeveloveps = {'getResponse': getResponse, 'isTriggered': isTriggered}