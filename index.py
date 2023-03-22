from core.yandexskillcore import *
from core.responseHelper import *

def handler(event):
    return createCard(event, 'hello', None, 'TITLE SKADHKJADSHKJDSA', 'ashdasd')

startServer(handler=handler)
dialogs = subscribeDialogs('./dialogs')