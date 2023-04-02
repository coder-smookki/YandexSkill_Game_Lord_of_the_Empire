from dialogs.mainMenu.mainMenu import mainMenu
from dialogs.exitConfirm.exitConfirm import exitConfirm
from dialogs.whatYouCan.whatYouCan import whatYouCan
from dialogs.help.help import help
from dialogs.backDialog.backDialog import backDialog
from dialogs.repeat.repeat import repeat
from dialogs.game.game import game
from dialogs.whoAreCreators.whoAreCreators import whoAreCreators
from dialogs.howToUse.howToUse import howToUse
from dialogs.howToContactDevelopers.howToContactDevelopers import howToContactDeveloveps
from dialogs.resetGame.resetGame import resetGame
from dialogs.stats.stats import stats
from dialogs.dontUnderstand.dontUnderstand import dontUnderstand

allDialogs = {
    "exitConfirm": exitConfirm,
    'game': game,
    'resetGame': resetGame,
    'stats': stats,
    "whoAreCreators": whoAreCreators,
    "howToUse": howToUse,
    "howToContactDevelopers": howToContactDeveloveps,
    "whatYouCan": whatYouCan,
    "help": help,
    "backDialog": backDialog,
    "repeat": repeat,
    "mainMenu": mainMenu,
    "dontUnderstand": dontUnderstand
}
