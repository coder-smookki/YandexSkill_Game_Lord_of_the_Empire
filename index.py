from core.builder import builder
from dialogs.Opening.Opening import *
from dialogs.Cashed import *
from core.skillAliceEmulator import *
from dialogs.SecondExtension.SecondExtension import *
from core.historyHandler import passEpisode

from core.historyHandler import *

import sys
sys.setrecursionlimit(5000)


skillEmulate(Opening, Cashed)