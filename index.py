from dialogs.Opening.Opening import *
from dialogs.Cashed import *
from core.skillAliceEmulator import *
from core.historyHandler import *
from core.yandexskillcore import startServer
from core.responseHelper import createCard
from handler import handler
import sys
from dotenv import load_dotenv
import os
load_dotenv()

sys.setrecursionlimit(5000)


# концовки при переполнении/недостатка какой-то статы
# формат такой-же
# full - когда стата заполняется на 100+
# empty - когда стата опускается до 0-
statsEnds = {
    "church": {"full": "\"fullChurch // None // None // // card\"", "empty": "\"emptyChurch // None // None // // card\""},
    "army": {"full": "\"fullArmy // None // None // // card\"", "empty": "\"emptyArmy // None // None // // card\""},
    "nation": {"full": "\"fullNation // None // None // // card\"", "empty": "\"emptyNation // None // None // // card\""},
    "coffers": {"full": "\"fullCoffers // None // None // // card\"", "empty": "\"emptyCoffers // None // None // // card\""},
}

history = """
"1 // true // false // 10 10 10 10 $ -10 -10 -10 -10 // card"
true:
    "empty? // true // None // -100 -100 -100 -100 // card"
false:
    "full? // true // None // 100 100 100 100 // card"
"""


# skillEmulate(history,statsEnds)


host = os.environ.get('HOST')
if host:
    print(colored("+", "green"),'HOST найден:', host)
    startServer(host=host, handler=handler)
else:
    print(colored("-", "red"), 'HOST не найден! Запускаю сервер на 127.0.0.1')
    startServer(handler=handler)



