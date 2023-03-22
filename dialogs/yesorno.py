from core.responseHelper import createCard

def getResponse(event):
    return createCard(event, 'Да или нет?', None)