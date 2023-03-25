from core.triggerHelper import *
from core.responseHelper import *
from core.historyHandler import passEpisode


def tipaIgraesh(event):
    card = createCard(event, "Типа играешь...", "", ["Новая игра"])
    addStateInResponse(card, "playing", True)
    return card


def createStartInfo(history):
    return {
        "posEpisode": [0],
        "maxPosEpisode": [len(history) - 1],
        "pastPosEpisode": None,
        "choice": "none",
        "pastHasEvent": None,
        "stats": {"church": 50, "army": 50, "nation": 50, "coffers": 50},
        "notAppliedStats": {
            "true": [0, 0, 0, 0],
            "false": [0, 0, 0, 0],
            "always": [0, 0, 0, 0],
        },
    }

def handler(event, history, statsEnds):
    if not haveGlobalState(event, "save"):
        info = createStartInfo(history)
    else:
        info = getGlobalState(event, "save")
        command = getOriginalUtterance(event)

    episode = passEpisode(info, history, statsEnds)
    response = createCard(event, episode['text'], None, episode['buttons'])
    
    if 'lastFalseButton' in info and not (info['lastFalseButton'] is None) and info['lastFalseButton'] == command:
        info['choice'] =  'false'
    else: 
        info['choice'] =  'true'

    info['lastTrueButton'] = None
    info['lastFalseButton'] = None

    if len(episode['buttons']) == 0:
        addGlobalStateInResponse(response, "save", createStartInfo(history))
        return response
    
    elif len(episode['buttons']) == 1:
        info['lastTrueButton'] = episode['buttons'][0]

    elif len(episode['buttons']) == 2:        
        info['lastTrueButton'] = episode['buttons'][0]
        info['lastFalseButton'] = episode['buttons'][1]

    addGlobalStateInResponse(response, "save", info)

    return response

    # return createCard(event, "test", "test", "title")