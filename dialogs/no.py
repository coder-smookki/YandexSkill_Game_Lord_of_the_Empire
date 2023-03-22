from core.responseHelper import createCard

def getResponse(event):
    return createCard(event, 'Ты сказал нет', None, buttons=['Вернуться'])