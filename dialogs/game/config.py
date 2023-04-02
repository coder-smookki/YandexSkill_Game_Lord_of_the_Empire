import random
import re

from dialogs.dontUnderstand.config import getConfig as dontUnderstandConfig
from utils.globalStorage import *
from utils.intents import LetsPlayIntents, RepeatIntents
from utils.responseHelper import *
from utils.dbHandler import *
from utils.triggerHelper import *
from utils.intents import YesIntents,NoIntents
from gameCore.historyHandler import passEpisode
from utils.image_gen.get_id import get_id
from dialogs.mainMenu.config import getConfig as getMainMenuConfig
from utils.intents import RepeatIntents
from utils.branchHandler import getDialogResponseFromEnd

sfx = [
    '<speaker audio="dialogs-upload/4b310008-3fd4-4d8d-842c-34753abee342/f1d3a69c-3002-4cf7-9e28-e3c7b3514ac1.opus">',
    '<speaker audio="dialogs-upload/4b310008-3fd4-4d8d-842c-34753abee342/5b9bcd97-2d4a-4810-8639-28518868a548.opus">',
    '<speaker audio="dialogs-upload/4b310008-3fd4-4d8d-842c-34753abee342/af8d12e0-04f4-447e-9f6a-5418424c2daa.opus">',
    '<speaker audio="dialogs-upload/4b310008-3fd4-4d8d-842c-34753abee342/3b79ef82-e551-4e8c-a913-e953ffbfd7cd.opus">',
    '<speaker audio="dialogs-upload/4b310008-3fd4-4d8d-842c-34753abee342/506fc86d-ee86-4b65-82e5-cc6c59012ce9.opus">',
    '<speaker audio="dialogs-upload/4b310008-3fd4-4d8d-842c-34753abee342/59937e1e-576e-4e8a-84b7-7fdec826edbf.opus">',
    '<speaker audio="dialogs-upload/4b310008-3fd4-4d8d-842c-34753abee342/6232e501-5a2e-4c97-b193-f3e293a3d879.opus">',
    '<speaker audio="dialogs-upload/4b310008-3fd4-4d8d-842c-34753abee342/1cace3da-e83c-4eb5-aa63-9bd718ca01b7.opus">',
    '<speaker audio="dialogs-upload/4b310008-3fd4-4d8d-842c-34753abee342/3ee32d10-842e-4e93-86d6-da158cba6e3d.opus">',
]

names = list(
    {
        "Александр",
        "Борис",
        "Василий",
        "Григорий",
        "Дмитрий",
        "Евгений",
        "Ждан",
        "Захар",
        "Игорь",
        "Константин",
        "Леонид",
        "Михаил",
        "Павел",
        "Роман",
        "Ульян",
        "Федор",
        "Харитон",
        "Цезарь",
        "Чеслав",
        "Шамиль",
        "Эдуард",
        "Юлиан",
        "Анатолий",
        "Владимир",
        "Геннадий",
        "Демид",
        "Елисей",
        "Жорес",
        "Зиновий",
        "Ипполит",
        "Кирилл",
        "Лев",
        "Матвей",
        "Нестор",
        "Осип",
        "Петр",
        "Ростислав",
        "Станислав",
        "Тарас",
        "Устин",
        "Филипп",
        "Христофор",
        "Чеслав",
        "Юрий",
        "Альфонсо",
        "Бернард",
        "Вильгельм",
        "Генрих",
        "Давид",
        "Эдмунд",
        "Фердинанд",
        "Гарольд",
        "Исаак",
        "Карл",
        "Леопольд",
        "Матвей",
        "Николай",
        "Оскар",
        "Петр",
        "Ричард",
        "Сэмюэль",
        "Теодор",
        "Уильям",
    }
)

pre_ttss = ["Я вас не понял.", "Не удалось распознать выбор.", "Не понял, повторяю."]

def isReplicaSimilar(replica, arr):
    for elem in arr:
        if elem in replica:
            return True
    return False


# preTts - фраза "я вас не понял, повторяю" когда не понял ход
def compileConfigFromEpisode(
    event, episode, haveInterface, preTts="", userStateUpdate=None, repeat=False
):
    # получить статы
    stats = episode["stats"]

    print("stats:", stats)

    # Local variable 'cardId' might be referenced before assignment
    cardId = None

    # если в эпизоде есть имя (выступает персонаж)
    if episode["name"]:
        # добавить sfx, имя и сообщение в tts
        tts = random.choice(sfx) + preTts + episode["name"] + ". " + episode["message"]

        if haveInterface:
            # получить айди картинки
            cardId = get_id(
                person=episode["name"],
                replica=episode["message"],
                values=[
                    stats["church"],
                    stats["nation"],
                    stats["army"],
                    stats["coffers"],
                ],
                name=selectName(globalStorage["mariaDBconn"], getUserId(event))
            )

            # # если карточка не вернулась, использовать арбуз
            # if cardId is None:
            #     cardId = "1533899/d371aab5224c91137cfc"
    else:
        # если эпизод - оповещение (нет имени), то добавить sfx и сообщение в tts
        tts = random.choice(sfx) + episode["message"]

        if haveInterface:
            # ̶и̶с̶п̶о̶л̶ь̶з̶о̶в̶а̶т̶ь̶ ̶а̶р̶б̶у̶з̶
            # использовать картинку для текста
            cardId = get_id(
                person=None,
                replica=episode["message"],
                values=[
                    stats["church"],
                    stats["nation"],
                    stats["army"],
                    stats["coffers"],
                ],
                name=selectName(globalStorage["mariaDBconn"], getUserId(event))
            )

    if haveInterface:
        # создать конфиг для интерфейсных устройств
        config = {
            "tts": tts,
            "buttons": [
                "В главное меню",
                "Повторить ещё раз",
                "Выход",
            ],
            "card": {
                "type": "BigImage",
                "image_id": cardId,
                "title": episode["name"],
                "description": episode["message"] if episode["name"] else None,
            },
        }

        # если есть кнопки, то добавить кнопки и добавить кнопки в tts
        if len(episode["buttons"]) != 0:
            config["buttons"] = episode["buttons"] + config["buttons"]

            # вынести из массива кнопки в виде строки
            buttonsStr = ""
            for button in episode["buttons"]:
                buttonsStr += button + ". "

            # добавить в tts кнопки
            config["tts"] = (
                config["tts"] + ". " + "Варианты ответа, " + buttonsStr + "."
            )

    else:
        # создать конфиг для устройств без интерфейса
        config = {
            "message": "zxc",
            "tts": tts,
            "buttons": ["first button aboba", "second button aboba"],
        }

        # вынести текущие фракции в виде строки
        statsStr = f"""Репутация текущий фракций:
            Церковь: {stats["church"]} единиц.
            народ: {stats["nation"]} единиц.
            армия: {stats["army"]} единиц.
            казна: {stats["coffers"]} единиц.
        """

        # добавить фракции в tts
        config["tts"] += statsStr

        # вынести из массива кнопки в виде строки
        buttonsStr = ""
        for button in episode["buttons"]:
            buttonsStr += button + ", "

        # добавить в tts кнопки и статы
        config["tts"] = config["tts"] + ". " + "Варианты ответа: " + buttonsStr

    # добавить бренч в конфиг
    config["session_state"] = {"branch": "game"}

    if userStateUpdate:
        if not "user_state_update" in config:
            config["user_state_update"] = userStateUpdate
        else:
            config["user_state_update"] = {
                **config["user_state_update"],
                **userStateUpdate,
            }

    # вернуть конфиг
    return config


# создать стартовое сохранение
def createStartInfo(history):
    return {
        "posEpisode": [0],
        "maxPosEpisode": [len(history) - 1],
        "pastPosEpisode": None,
        "choice": "none",
        "pastHasEvent": None,
        "stats": {"church": 50, "army": 50, "nation": 50, "coffers": 50},
        "notAppliedStats": {
            "true": [0, 0, 0, 0],
            "false": [0, 0, 0, 0],
            "always": [0, 0, 0, 0],
        },
    }


def checkIfLastChoiceSimiliar(command, firstLastChoiceCommand, secondLastChoiceCommand):
    # разделить по пробелам команду
    commandArr = command.split(" ")

    # убрать все, кроме букв и пробелов в строках, потом разделить по пробелам
    firstLastChoiceCommandArr = re.sub(
        r"[^A-Za-zА-Яа-я ]", "", firstLastChoiceCommand.lower()
    ).split(" ")
    secondLastChoiceCommandArr = re.sub(
        r"[^A-Za-zА-Яа-я ]", "", secondLastChoiceCommand.lower()
    ).split(" ")

    print('check1')

    # пройтись по всем словам команды
    # если ответы "да" или "нет", то зачекать через интенты
    if firstLastChoiceCommand[0] == 'да':
        print('check2')
        if isReplicaSimilar(command, YesIntents):
            print('check3')
            return 'true'
    if firstLastChoiceCommand[0] == 'нет':
        if isReplicaSimilar(command, NoIntents):
            return 'false'
    print('check4')
    # иначе смотреть по словам
    for word in commandArr:
        # есть слово в массиве с первым выбором
        isInFirst = word in firstLastChoiceCommandArr

        # есть слово в массиве со вторым выбором
        isInSecond = word in secondLastChoiceCommandArr

        # если есть в первом, но нет во втором
        if isInFirst and not isInSecond:
            return "true"

        # если есть во втором, но нет в первом
        if isInSecond and not isInFirst:
            return "false"

    # если не нашлось единоличного совпадения
    return None


def getConfig(event, allDialogs, needCreateNewInfo=False):
    haveUserInterface = haveInterface(event)
    # haveUserInterface = False

    # концовки
    statsEnds = globalStorage["statsEnds"]

    # соединение с БД
    conn = globalStorage["mariaDBconn"]

    # вся стартовая история
    firstGameHistory = globalStorage["startHistory"]

    # вся история
    history = globalStorage["history"]

    # айди юзера
    userId = getUserId(event)

    # если нужно создать новую игру
    if needCreateNewInfo:
        # создать стартовое сохранение (создать новую игру)
        info = createStartInfo(history)

        # вставить это сохранение в БД
        insertSave(conn, userId, random.choice(names), info)

    else:
        # получить инфо по айди юзера
        info = selectGameInfo(conn, userId)

        # если сохранение в БД не нашлось
        if not info:
            # создать стартовое сохранение (создать новую игру)
            info = createStartInfo(history)

            # вставить это сохранение в БД
            insertSave(conn, userId, random.choice(names), info)

    # если в текущем сохранении есть прошлый эпизод
    if "lastEpisode" in info and not info["lastEpisode"] is None:
        # прошлый эпизод
        lastEpisode = json.loads(info["lastEpisode"])

        # выборы предыдущего эпизода
        canLastChoicedArr = lastEpisode["buttons"]

    else:
        # иначе просто обозначить переменные
        lastEpisode = None
        canLastChoicedArr = None

    # получить команду
    command = getCommand(event)

    # если нет кнопок для выбора на прошлом эпизоде (игрок умер или была показана концовка)
    if (
        not canLastChoicedArr is None
        and len(canLastChoicedArr) == 0
    ):
        # если игрок попросил повторить
        if isInCommandOr(event, RepeatIntents):
            # если это первая игра
            if not haveGlobalState(event, "playedBefore") or not getGlobalState(
                event, "playedBefore"
            ):
                return compileConfigFromEpisode(
                    event,
                    lastEpisode,
                    haveInterface,
                    userStateUpdate={"playedBefore": True}
                )

            # вернуть последний эпизод
            return compileConfigFromEpisode(
                event, lastEpisode, haveUserInterface, repeat=True
            )

        # соединение с БД
        conn = globalStorage["mariaDBconn"]

        # айди юзера
        userId = getUserId(event)

        # удалить последнее сохранение
        removeSave(conn, userId)

        # если игрок не просил повторить еще раз
        
        # добавить 1 смерть в статистику и новую концовку (если она новая)
        increaseStat(conn, userId, deaths=1, openEnds=lastEpisode["message"])

        # получить конфиг главного меню
        config = getMainMenuConfig(event)
        
        # стейт о том, что игрок сыграл впервый раз
        userState = {"playedBefore": True}

        # если это первая концовка игрока, то добавить глобальным стейтом "playedBefore"
        if not haveGlobalState(event,"playedBefore") or getGlobalState(event, "playedBefore") == False:
            if not "user_state_update" in config:
                config["user_state_update"] = userState
            else:
                config["user_state_update"] = {
                    **config["user_state_update"],
                    **userState,
                }

        # вернуть конфиг
        return config

    if canLastChoicedArr:
        # если только один
        if len(canLastChoicedArr) == 1:
            info["choice"] = "true"
        # иначе их 2
        else:
            # получить выбор пользователя
            userChoice = checkIfLastChoiceSimiliar(
                command, canLastChoicedArr[0], canLastChoicedArr[1]
            )
            print("Выбор пользователя:", userChoice)

            # если определить выбор не удалось
            if userChoice is None:
                # вернуть прошлый эпизод
                if isInCommandOr(event, LetsPlayIntents) or isInCommandOr(
                    event, RepeatIntents
                ):
                    return compileConfigFromEpisode(
                        event, lastEpisode, haveUserInterface
                    )
                return dontUnderstandConfig(
                    event, variants_of_the_choice=canLastChoicedArr, branch="game"
                )
            else:
                # иначе установить выбор в сохранении
                info["choice"] = userChoice

    # print('STATES', haveGlobalState(event, 'playedBefore'), getGlobalState(event, 'playedBefore'))
    # try:
    #     print(event['state']['user'])
    # except KeyError as e:
    #     print('KEYERROR', e)

    # пройти к следующему эпизоду, если это первая игра
    if not haveGlobalState(event, "playedBefore") or not getGlobalState(
        event, "playedBefore"
    ):
        episode = passEpisode(info, firstGameHistory, statsEnds)
    # пройти к следующему эпизоду, если юзер уже играл
    else:
        episode = passEpisode(info, history, statsEnds)

    if "name" in episode and not episode["name"] is None:
        increaseStat(conn, userId, meetedCharacters=episode["name"])

    # закинуть текущий эпизод в качестве последнего для следующего вызова
    info["lastEpisode"] = json.dumps(episode, ensure_ascii=False)

    # обновить сохранение в БД
    updateSave(conn, userId, info)

    # скомпилировать конфиг из эпизода и вернуть его
    return compileConfigFromEpisode(event, episode, haveUserInterface)
