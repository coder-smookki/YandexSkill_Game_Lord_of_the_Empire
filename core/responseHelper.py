import copy


def createCard(
        event: dict,
        message: str,
        tts: str = None,
        title: str = None,
        imageCode: str = None,
        buttons: list[str] = ["Нет", "Да"],
):
    if imageCode is None:
        config = {
            "message": message,
            "tts": message if tts is None else tts,
            "buttons": buttons,
        }
    else:
        config = {
            "card": {
                "type": "BigImage",
                "image_id": imageCode,
                "title": 'Not setted' if title is None else title,
                "description": message,
            },
            "tts": message if tts is None else tts,
            "buttons": buttons
        }
    return createResponse(event, config)


def createResponse(event, originalConfig):
    config = copy.deepcopy(originalConfig)
    returnResponse = {
        "response": {
            "text": config["message"] if "message" in config else "",
            "tts": config["tts"],
            "card": config["card"] if "card" in config else None,
            "buttons": createButtons(config["buttons"]),
            "end_session": config["end_session"] if "end_session" in config else False,
        },
        "session": event["session"],
        "session_state": config["session_state"]
        if "session_state" in config
        else {"branch": ""},
        "version": event["version"],
    }
    if "user_state_update" in config:
        returnResponse["user_state_update"] = config["user_state_update"]
    return returnResponse


def createButtons(buttons):
    result = []
    for button in buttons:
        if isinstance(button, str):
            result.append({"title": button, "hide": True})
            continue
        result.append(button)

    return result


def getSessionId(event):
    return event["session"]["session_id"]


def getUserId(event):
    return event["session"]["user"]["user_id"]


def getState(event, state):
    return event["state"]["session"][state]


def getOriginalUtterance(event):
    return event["request"]["original_utterance"]


def getCommand(event):
    return event["request"]["command"]


def getGlobalState(event, state):
    return event["state"]["user"][state]
