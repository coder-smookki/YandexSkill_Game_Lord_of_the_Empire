from core.responseHelper import createCard

def getResponse(event):
    return createCard(event, 'Ты - истинный владыка?', 'Ты - истинный владыка?', None, None, buttons=['Да', 'Нет', 'Повторить ещё раз', 'Что ты умеешь?', 'Помощь', 'Выйти'])