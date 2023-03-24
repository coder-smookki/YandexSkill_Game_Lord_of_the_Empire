from core.builder import builder
from dialogs.Opening.Opening import *
from dialogs.Cashed import *
from core.skillAliceEmulator import *
from dialogs.SecondExtension.SecondExtension import *
from core.historyHandler import passEpisode

skillEmulate(Opening, Cashed)
# print(builder(history, cached))