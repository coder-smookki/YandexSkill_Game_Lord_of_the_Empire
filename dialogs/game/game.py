from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)

def isTriggered(event):
    return (isInCommandOr(event, ['играть']) or isInLastContext(event, 'game')) and not isInCommandAnd(event, ['меню', 'главное'])

game = {'getResponse': getResponse, 'isTriggered': isTriggered}
