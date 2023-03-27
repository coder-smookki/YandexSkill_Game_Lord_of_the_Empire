from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    if isNewSession(event) and not haveGlobalState(event, 'language'):
        return allDialogs['chooseLanguage']['getResponse'](event, allDialogs)

    if isInLastContext(event, 'chooseLanguage'):
        if 'рус' in getCommand(event) or 'рас' in getCommand(event) or 'rus' in getCommand(event):
            setGlobalStateInEvent(event, 'language', 'ru-RU')
        else:
            setGlobalStateInEvent(event, 'language', 'en-US')
    config = getConfig(event)
    return createResponse(event, config)

def isTriggered(event):
    # return isSimilarTokens(event, {'главное', 'меню'})
    return True


mainMenu = {'getResponse': getResponse, 'isTriggered': isTriggered}
