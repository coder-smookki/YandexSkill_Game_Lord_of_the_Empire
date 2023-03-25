from core.triggerHelper import *
from core.responseHelper import *
from dialogs.Opening import Opening

def handler(event):
    
    if isInCommandOr(event, ['сброс']):
        response = createCard(event, 'Вы очистили сохранение.', 'Вы очистили сохранение.', ['Новая игра'])
        setGlobalStatesInResponse(response, {})
        return response
        
    # если человек не имеет сохранения, то предложить начать новую игру
    if not haveGlobalState(event, 'info'):
        card = createCard(event, 'Здравствуйте, у вас нет сохранения.', 'Здравствуйте, у вас нет сохранения.', ['Новая игра'])
        return card

    # если человек имеет сохранение, то предложить продолжить игру или начать новую
    if haveGlobalState(event, 'info'):
        card = createCard(event, 'Здравствуйте, вас есть сохранение.', 'Здравствуйте, вас есть сохранение.', ['Продолжить','Новая игра'])
        return card

    # info = {
    #     "posEpisode": [0],
    #     "maxPosEpisode": [len(Opening) - 1],
    #     "pastPosEpisode": None,
    #     "choice": "none",
    #     "pastHasEvent": None,
    #     "stats": {"church": 50, "army": 50, "nation": 50, "coffers": 50},
    # }

    # return createCard(event, "test", "test", "title")

