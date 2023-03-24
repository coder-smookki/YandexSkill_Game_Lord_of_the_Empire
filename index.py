from core.skillAliceEmulator import skillEmulate
from dialogs.Opening.Opening import Opening
import sys
print('Is 64?:', sys.maxsize > 2**32)
skillEmulate(Opening)

