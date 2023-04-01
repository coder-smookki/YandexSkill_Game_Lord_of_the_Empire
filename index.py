from utils.globalStorage import globalStorage

from gameCore.episodes.Opening.Opening import *
from gameCore.episodes.ShuffledScenario import ShuffledScenario
from gameCore.episodes.Cashed import *
from gameCore.episodes.StatsEnds import StatsEnds

from skillAliceEmulator import *
from gameCore.historyHandler import *
from yandexskillcore import startServer
from utils.responseHelper import createCard
from handler import handler
import sys
from dotenv import load_dotenv
import os

load_dotenv()

sys.setrecursionlimit(5000)

host = os.environ.get('HOST')
emulator = os.environ.get('EMULATOR')

if emulator == 'true':
    skillEmulate(Opening, StatsEnds, Cashed)
else:
    if host:
        print(colored("+", "green"), 'HOST найден:', host)
        startServer(Opening, ShuffledScenario, StatsEnds, Cashed, host=host, handler=handler)
    else:
        print(colored("-", "red"), 'HOST не найден! Запускаю сервер на 127.0.0.1')
        startServer(Opening, ShuffledScenario, StatsEnds, Cashed, handler=handler)
