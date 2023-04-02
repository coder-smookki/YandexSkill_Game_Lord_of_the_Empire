from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *
from utils.intents import MenuIntents
from utils.dbHandler import *

def getResponse(event, allDialogs=None):
    config = getConfig(event)

    if not haveGlobalState(event, 'endGame') or getGlobalState(event, 'endGame') == False:
        # добавить 1 смерть в статистику и новую концовку (если она новая)
        increaseStat(conn, getUserId(event), deaths=1, openEnds=lastEpisode["message"])

    return createResponse(event, config)


def isTriggered(event):
    return isInCommandOr(event, MenuIntents) or isNewSession(event)


mainMenu = {'getResponse': getResponse, 'isTriggered': isTriggered}
