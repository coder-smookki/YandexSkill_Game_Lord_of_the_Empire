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
from dialogs.dontUnderstand.dontUnderstand import dontUnderstandDangerous

allDialogs = {
    'dontUnderstandDangerous': dontUnderstandDangerous,
    "exitConfirm": exitConfirm,

    'game': game,

    "howToUse": howToUse,
    "howToContactDevelopers": howToContactDeveloveps,
    "whatYouCan": whatYouCan,
    "help": help,
    "mainMenu": mainMenu,

    'resetGame': resetGame,
    'stats': stats,
    "whoAreCreators": whoAreCreators,
    "backDialog": backDialog,
    "repeat": repeat,
    "dontUnderstand": dontUnderstand
}

# помощь, как пользоваться
