from dialogs.Opening.Opening import *
from dialogs.Cashed import *
from skillAliceEmulator import *
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
    "church": {"full": "\"fullChurch // None // None // // card\"",
               "empty": "\"emptyChurch // None // None // // card\""},
    "army": {"full": "\"fullArmy // None // None // // card\"", "empty": "\"emptyArmy // None // None // // card\""},
    "nation": {"full": "\"fullNation // None // None // // card\"",
               "empty": "\"emptyNation // None // None // // card\""},
    "coffers": {"full": "\"fullCoffers // None // None // // card\"",
                "empty": "\"emptyCoffers // None // None // // card\""},
}



# Opening = """
# "[bundle]"
# bundle:
#     'hehe // true // false // // card'
#     true:
#         '{link3}'
#     false:
#         'ok // None // None // // asd'
# """

# Cashed = {

#     "link1" : """
#     "[bundle]"
#     bundle:
#         "[bundle]"
#         bundle:
#             "bundlzxc1 // true // false // // card"
#         "[bundle]"
#         bundle:
#             "zbundlzxc1 // true // false // // card"
    
#     """,
#     "link2": """
#     "{link1}"
#     """,

#     "link3": """
#     "{link2}"

    
#     """,    
# }



host = os.environ.get('HOST')
emulator = os.environ.get('EMULATOR')
if emulator == 'true':
    skillEmulate(Opening, statsEnds, Cashed)
else:
    if host:
        print(colored("+", "green"), 'HOST найден:', host)
        startServer(Opening, statsEnds, Cashed, host=host, handler=handler)
    else:
        print(colored("-", "red"), 'HOST не найден! Запускаю сервер на 127.0.0.1')
        startServer(Opening, statsEnds, Cashed, handler=handler)
