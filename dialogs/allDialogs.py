from dialogs.mainMenu.mainMenu import mainMenu
from dialogs.exitConfirm.exitConfirm import exitConfirm
from dialogs.whatYouCan.whatYouCan import whatYouCan
from dialogs.help.help import help
from dialogs.backDialog.backDialog import backDialog
from dialogs.repeat.repeat import repeat

allDialogs = {
    "exitConfirm": exitConfirm,
    "repeat": repeat,
    "whatYouCan": whatYouCan,
    "help": help,
    "backDialog": backDialog,
    "mainMenu": mainMenu,
}