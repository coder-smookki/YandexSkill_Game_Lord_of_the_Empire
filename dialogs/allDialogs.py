from dialogs.mainMenu.mainMenu import mainMenu
from dialogs.exitConfirm.exitConfirm import exitConfirm
from dialogs.whatYouCan.whatYouCan import whatYouCan
from dialogs.help.help import help
from dialogs.backDialog.backDialog import backDialog
from dialogs.repeat.repeat import repeat
from dialogs.game.game import game
from dialogs.whoAreCreators.whoAreCreators import whoAreCreators
from dialogs.howToUse.howToUse import howToUse
from dialogs.howToContactDevelopers import howToContactDevelopers
allDialogs = {
    "exitConfirm": exitConfirm,
    'game': game,
    "whoAreCreators": whoAreCreators,
    "howToUse": howToUse,
    "howToContactDevelopers": howToContactDevelopers,
    "repeat": repeat,
    "whatYouCan": whatYouCan,
    "help": help,
    "backDialog": backDialog,
    "mainMenu": mainMenu,
}