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
from dialogs.StatsEnds import StatsEnds

load_dotenv()

sys.setrecursionlimit(5000)

host = os.environ.get('HOST')
emulator = os.environ.get('EMULATOR')
if emulator == 'true':
    skillEmulate(Opening, StatsEnds, Cashed)
else:
    if host:
        print(colored("+", "green"), 'HOST найден:', host)
        startServer(Opening, StatsEnds, Cashed, host=host, handler=handler)
    else:
        print(colored("-", "red"), 'HOST не найден! Запускаю сервер на 127.0.0.1')
        startServer(Opening, StatsEnds, Cashed, handler=handler)
