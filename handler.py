from core.triggerHelper import *
from core.responseHelper import *
from dialogs.Opening import Opening

def tipaIgraesh(event):
    card = createCard(event, 'Типа играешь...', '', ['Новая игра'])
    addStateInResponse(card, 'playing', True)
    return card

def handler(event):
    if isInCommandOr(event, ['меню', 'выйди', 'выход']):
        setCommandInEvent(event, '')

    if haveState(event, 'playing') and getState(event, 'playing') == True:
        return tipaIgraesh(event)

    # если человек хочет начать новую игру
    if isInCommandAnd(event, ['новая', 'игра']):
        return tipaIgraesh(event)

    # если человек хочет продолжить с последнего места
    if isInCommandAnd(event, ['продолжить']):
        return tipaIgraesh(event)

    # если человек не имеет сохранения, то предложить начать новую игру
    if not haveGlobalState(event, 'info'):
        card = createCard(event, 'У вас нет сохранения. Хотите начать новую игру?', 'У вас нет сохранения. Хотите начать новую игру?', ['Новая игра'])
        return card

    # если человек имеет сохранение, то предложить продолжить игру или начать новую
    if haveGlobalState(event, 'info'):
        card = createCard(event, 'У вас есть сохранение. Хотите продолжить с последнего момента или начать новую игру?', 'У вас есть сохранение. Хотите продолжить с последнего момента или начать новую игру?', ['Продолжить','Новая игра'])
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

