import copy


# создать ответ Алисе в удобном для игры формате
def createCard(
    event: dict, # реквест Алисы
    message: str, # сообщение
    tts: str = None, # tts
    buttons: list[str] = ["Нет", "Да"], # кнопки
    # если нет "imageCode", то поля ниже не используются
    imageCode: str = None, # айди картинки
    title: str = None, # заголовок
    
):
    if tts is None:
        tts = message
    # если нет картинки, то вернуть текстовой респонс
    if imageCode is None:
        config = {
            "message": message,
            "tts": message if tts is None else tts,
            "buttons": buttons,
        }
    # если есть, то вернуть респонс с картинкой
    else:
        config = {
            "card": {
                "type": "BigImage",
                "image_id": imageCode,
                "title": "Not setted" if title is None else title,
                "description": message,
            },
            "tts": message if tts is None else tts,
            "buttons": buttons,
        }

    # создать
    return createResponse(event, config)

# функция, которая превращает конфиг с информацией о будующем респонсе в сам респонс
# сделано, чтобы не запариваться по поводу полей в респонсе (их реально много и они неудобные :c)
def createResponse(event, originalConfig):
    # скопировать конфиг, чтобы 100% избежать его изменения в другом файле (если там он создан глобально)
    config = copy.deepcopy(originalConfig)
    
    # возращаемый респонс
    returnResponse = {
        "response": {
            "text": config["message"] if "message" in config else "", # если есть сообщение (текстовой респонс)
            "tts": config["tts"], # tts
            "card": config["card"] if "card" in config else None, # если есть карточка (респонс с картинкой)
            "buttons": createButtons(config["buttons"]), # кнопки
            "end_session": config["end_session"] if "end_session" in config else False, # если нужно закончить сессию
        },
        "session": event["session"], # инфа для Алисы - сессия
        "session_state": config["session_state"] if "session_state" in config else {}, # передаваемые стейты
        "version": event["version"], # инфа для Алисы - версия
    }
    #
    if "user_state_update" in config: # если нужно обновить глобальные стейты
        # установить поле
        returnResponse["user_state_update"] = config["user_state_update"] 
    
    # вернуть получившийся респонс
    return returnResponse 

# метод, занимающийся преобразованием кнопок из строк в формат кнопки
# если кнопка не является строкой, то просто переносит ее как она есть
def createButtons(buttons:list):
    # сюда будут складываться кнопки
    result = []
    # пройтись по кнопкам
    for button in buttons:
        if isinstance(button, str):
            result.append({"title": button, "hide": True})
            continue
        result.append(button)

    return result


# получить ID сессии
def getSessionId(event):
    return event["session"]["session_id"]


# получить ID пользователя
def getUserId(event):
    return event["session"]["user"]["user_id"]


# получить State
def getState(event, state):
    return event["state"]["session"][state]


# получить оригинальную команду пользователя
def getOriginalUtterance(event):
    return event["request"]["original_utterance"]


# получить отформатированную команду пользователя
def getCommand(event):
    return event["request"]["command"]


# получить глобальный State
def getGlobalState(event, state):
    return event["state"]["user"][state]


# установить State в респонсе
def setStatesInResponse(response, states:dict):
    response['session_state'] = states


# установить глобальный State в респонсе
def setGlobalStatesInResponse(response, globalStates:dict):
    response["user_state_update"] = globalStates


# добавить State в респонс
def addStateInResponse(response, stateName, stateValue):
    response['session_state'][stateName] = stateValue


# добавить глобальный State в респонс
def addGlobalStateInResponse(response, stateName, stateValue):
    if not ("user_state_update" in response):
        response["user_state_update"] = {}
    response["user_state_update"][stateName] = stateValue


# установить State в Event
def setStateInEvent(event, stateName, stateValue):
    event["state"]["session"][stateName] = stateValue
    return event


# установить глобальный State в Event
def setGlobalStateInEvent(event, stateName, stateValue):
    event["state"]["user"][stateName] = stateValue
    return event


# установить отформатированную команду пользователя в Event
def setCommandInEvent(event, command:str):
    event["request"]["command"] = command
    return event 