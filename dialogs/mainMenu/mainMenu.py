from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *
from utils.intents import MenuIntents
from utils.dbHandler import *
from utils.globalStorage import globalStorage

def getResponse(event, allDialogs=None):
    config = getConfig(event)

    conn = globalStorage["mariaDBconn"]

    if haveGlobalState(event, 'addStats') and type(getGlobalState(event, 'addStats')) == list:
        stats = getGlobalState(event, 'addStats')
        for stat in stats:
            print('mainMenuStat')
            increaseStat(conn, getUserId(event), deaths=stat[0], openEnds=stat[1])
        if not 'user_state_update' in config:
            config['user_state_update'] = {}
        config['user_state_update']['addStats'] = []
    
    return createResponse(event, config)


def isTriggered(event):
    return isInCommandOr(event, MenuIntents) or isNewSession(event)


mainMenu = {'getResponse': getResponse, 'isTriggered': isTriggered}
