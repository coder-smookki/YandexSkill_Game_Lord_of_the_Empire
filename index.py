from core.yandexskillcore import *
from core.responseHelper import *

dialogs = subscribeDialogs('./dialogs')

def handler(event):
    if getCommand(event) == 'Да':
        return dialogs['yes'](event)
    if getCommand(event) == 'Нет':
        return dialogs['no'](event)
    return dialogs['yesorno'](event)

startServer(handler=handler)
