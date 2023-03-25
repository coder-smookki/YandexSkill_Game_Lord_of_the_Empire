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

    episode = passEpisode(info, history, statsEnds)
    response = 1

    

    # addGlobalStateInResponse(response, "save", info)


    return episode

    # return createCard(event, "test", "test", "title")
