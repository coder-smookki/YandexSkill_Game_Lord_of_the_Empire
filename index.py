from dialogs.Opening.Opening import *
from dialogs.Cashed import *
from core.skillAliceEmulator import *
from core.historyHandler import *
import sys
sys.setrecursionlimit(5000)

# Формат: "text // trueBtn // falseBtn // church army nation coffers // cardId"
# Пример: "text // asd // zxc // 0 0 -10 5 // zxc123"
history = """
"text // true // false // 0 0 0 20 // card"
"text // None // None // 0 0 0 0 // card"
"""

# формат такой-же
# full - когда стата заполняется на 100+
# empty - когда стата опускается до 0-
statsEnds = {
    "church": {"full": "fullChurch", "empty": "emptyChurch"},
    "army": {"full": "fullArmy", "empty": "emptyArmy"},
    "nation": {"full": "fullNation", "empty": "emptyNation"},
    "coffers": {"full": "fullCoffers", "empty": "emptyCoffers"}
}


# skillEmulate(historyText=,statsEnds=,linkEpisodes=)

from core.yandexskillcore import startServer
from core.responseHelper import createCard
def handler(event):
    return createCard(event,'test', 'test', 'title')
startServer(handler=handler)