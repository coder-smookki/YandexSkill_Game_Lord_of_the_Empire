import random
import re

from dialogs.dontUnderstand.config import getConfig as dontUnderstandConfig
from utils.globalStorage import *
from utils.intents import RepeatIntents, HowToUseIntents, WhatDoYouCanIntents, HelpIntents, MenuIntents

from dialogs.howToUse.config import getConfig as howToUseGetConfig
from dialogs.whatYouCan.config import getConfig as whatYouCanGetConfig
from dialogs.help.config import getConfig as helpGetConfig
from dialogs.mainMenu.config import getConfig as mainMenuGetConfig

from utils.responseHelper import *
from utils.dbHandler import *
from utils.triggerHelper import *
from utils.intents import YesIntents, NoIntents
from gameCore.historyHandler import passEpisode
from utils.image_gen.get_id import get_id
from dialogs.mainMenu.config import getConfig as getMainMenuConfig
from utils.intents import RepeatIntents
from utils.branchHandler import getDialogResponseFromEnd

# "howToUse": howToUse,
    # "whatYouCan": whatYouCan,
    # "help": help,
    # "mainMenu": mainMenu,

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

pre_ttss = ["Я вас не понял.", "Не удалось распознать выбор.", "Мне не ясно, что вы имели в виду.", "Прошу прощения, я не смог понять ваше сообщение.",
            "Прошу прощения, но я не смог понять ваше намерение.", "Я извиняюсь, но мне нужна более точная информация. Что именно вы хотите сделать?"]


def isReplicaSimilar(replica, arr):
    for elem in arr:
        if isinstance(elem, re.Pattern):
            print('repattern')
            if re.search(elem, replica):
                return True
        elif elem in replica:
            return True
    return False

# надо ли включить какое-то меню
def isMenuChange(event, canLastChoicedArr, intents):
    # 1. проверить реилку на сходность
    # 2. проверить ответы на сходность
    # если сходство в реплике, но нет сходства в ответе: true
    # иначе: false

    isChoiceSim = False
    isCommandSim = False


    if not canLastChoicedArr is None:
        for choice in canLastChoicedArr:
            if isReplicaSimilar(choice, intents):
                isChoiceSim = True
                break
    
    if isInCommandOr(event, intents):
        isCommandSim = True
    
    if not isChoiceSim and isCommandSim:
        return True
    
    return False

    


def addStatsInInfo(info, episode):
    stats = episode['stats']

    # "notAppliedStats": {
    #   "true": [0, 0, 0, 0],
    #   "false": [0, 0, 0, 0],
    #   "always": [0, 0, 0, 0],
    # },

    for fraction in info['stats']:
        info['stats'][fraction] += stats['fraction']

    

# preTts - фраза "я вас не понял, повторяю" когда не понял ход
def compileConfigFromEpisode(
    event, episode, haveInterface, preTts="", userStateUpdate=None
):
    print('abobaEpisode',episode)
    # получить статы
    stats = episode["stats"]

    print(episode['message'])

    print("stats:", stats)

    # Local variable 'cardId' might be referenced before assignment
    cardId = None

    # если в эпизоде есть имя (выступает персонаж)
    if episode["name"]:
        # добавить sfx, имя и сообщение в tts
        tts = random.choice(sfx) + preTts + episode["name"] + ". " + episode["message"]

        if haveInterface:
            if len(episode["buttons"]) == 0:
                cardId = "1540737/c91ef7d5c3116ed113fc"
            else:
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
                    name=selectName(globalStorage["mariaDBconn"], getUserId(event)),
                )

            # # если карточка не вернулась, использовать арбуз
            # if cardId is None:
            #     cardId = "1533899/d371aab5224c91137cfc"
    else:
        # если эпизод - оповещение (нет имени), то добавить sfx и сообщение в tts
        tts = random.choice(sfx) + episode["message"]

        if haveInterface:
            if len(episode["buttons"]) == 0:
                cardId = "1540737/c91ef7d5c3116ed113fc"
            else:
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
                    name=selectName(globalStorage["mariaDBconn"], getUserId(event)),
                )

    if haveInterface:
        # создать конфиг для интерфейсных устройств
        config = {
            "tts": tts,
            "buttons": [
                "В главное меню",
                "Повторить ещё раз",
                "Помощь",
                "Что ты умеешь",
                "Выход",
            ],
            "card": {
                "type": "BigImage",
                "image_id": cardId,
                "title": episode["name"] if "name" in episode else None,
                "description": episode["message"],
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
            config["card"]["title"] = "КОНЕЦ"
            config["card"][
                "description"
            ] += (
                ' Чтобы выйти в главное меню, скажите или нажмите кнопку "Главное меню"'
            )
            config[
                "tts"
            ] += (
                ' Чтобы выйти в главное меню, скажите или нажмите кнопку "Главное меню"'
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
            buttonsStr += button + ". "

        # добавить в tts кнопки и статы
        config["tts"] = config["tts"] + ". " + "Варианты ответа: " + buttonsStr

        if len(episode["buttons"]) == 0:
            config["card"][
                "description"
            ] += ' Чтобы выйти в главное меню, скажите "Главное меню"'
            config["tts"] += ' Чтобы выйти в главное меню, скажите "Главное меню"'

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

    config['session_state']['fromGame'] = True

    # вернуть конфиг
    return config


# создать стартовое сохранение
def createStartInfo(history):
    return {
        "posEpisode": [0],
        "maxPosEpisode": [len(history) - 1],
        'playEnd': False,
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

    print("check1")
    print(firstLastChoiceCommand)
    # пройтись по всем словам команды
    # если ответы "да" или "нет", то зачекать через интенты
    isYes = isReplicaSimilar(command, YesIntents)
    isNo = isReplicaSimilar(command, NoIntents)
    if firstLastChoiceCommandArr[0] == "да":
        if (isYes and not isNo) or isReplicaSimilar(command, ['перв', 'слев', 'один', '1']):
            return "true"
    if secondLastChoiceCommandArr[0] == "нет":
        if isNo or isReplicaSimilar(command, ['второй', 'справа', 'два', '2']):
            return "false"

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


def getConfig(event, allDialogs, needCreateNewInfo=False, fromGame=True, repeat=False):
    
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


    print('repeat?', repeat)
    print('####start pos',info['posEpisode'])
    print('####start maxPos',info['maxPosEpisode'])
    

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


    print(canLastChoicedArr)

    # "howToUse": howToUse,
    # "whatYouCan": whatYouCan,
    # "help": help,
    # "mainMenu": mainMenu,
    if isMenuChange(event, canLastChoicedArr, HowToUseIntents):
        print('!!!!howToUse')
        return howToUseGetConfig(event)

    if isMenuChange(event, canLastChoicedArr, WhatDoYouCanIntents):
        print('!!!!WhatDoYouCan')
        return whatYouCanGetConfig(event)
    
    if isMenuChange(event, canLastChoicedArr, HelpIntents):
        print('!!!!Help')
        return helpGetConfig(event)

    if isMenuChange(event, canLastChoicedArr, MenuIntents):
        print('!!!!Menu')
        return mainMenuGetConfig(event)


    # вернуть прошлый эпизод, если игрок попросил повторить
    if isInCommandOr(event, RepeatIntents) and (canLastChoicedArr and len(canLastChoicedArr) != 0):
        config = compileConfigFromEpisode(event, lastEpisode, haveUserInterface)
        canLastState = {'canLastChoiced': canLastChoicedArr}
        if not "user_state_update" in config:
            config["user_state_update"] = canLastState
        else:
            config["user_state_update"] = {
                **config["user_state_update"],
                **canLastState,
            }

    if repeat and (canLastChoicedArr and len(canLastChoicedArr) != 0):
        print('nadristal')
        print(lastEpisode)
        config = compileConfigFromEpisode(event, lastEpisode, haveUserInterface)
        canLastState = {'canLastChoiced': canLastChoicedArr}
        if not "user_state_update" in config:
            config["user_state_update"] = canLastState
        else:
            config["user_state_update"] = {
                **config["user_state_update"],
                **canLastState,
            }

    # получить команду
    command = getCommand(event)

    # если нет кнопок для выбора на прошлом эпизоде (игрок умер или была показана концовка)
    if not canLastChoicedArr is None and len(canLastChoicedArr) == 0:
        # если игрок попросил повторить
        if isInCommandOr(event, RepeatIntents):
            # если это первая игра
            if not haveGlobalState(event, "playedBefore") or not getGlobalState(
                event, "playedBefore"
            ):
                config = compileConfigFromEpisode(
                    event,
                    lastEpisode,
                    haveInterface,
                    userStateUpdate={"playedBefore": True},
                )

                canLastState = {'canLastChoiced': canLastChoicedArr}
                if not "user_state_update" in config:
                    config["user_state_update"] = canLastState
                else:
                    config["user_state_update"] = {
                        **config["user_state_update"],
                        **canLastState,
                    }
                return config

            print('arbuzi')

            # вернуть последний эпизод
            config = compileConfigFromEpisode(event, lastEpisode, haveUserInterface)
            canLastState = {'canLastChoiced': canLastChoicedArr}
            if not "user_state_update" in config:
                config["user_state_update"] = canLastState
            else:
                config["user_state_update"] = {
                    **config["user_state_update"],
                    **canLastState,
                }

        # соединение с БД
        conn = globalStorage["mariaDBconn"]

        # айди юзера
        userId = getUserId(event)

        # удалить последнее сохранение
        removeSave(conn, userId)

        # добавить 1 смерть в статистику и новую концовку (если она новая)
        # increaseStat(conn, userId, deaths=1, openEnds=lastEpisode["message"])

        # получить конфиг
        config = getConfig(event, allDialogs)

        # стейт о том, что игрок сыграл впервый раз
        userState = {"playedBefore": True}

        # если это первая концовка игрока, то добавить глобальным стейтом "playedBefore"
        if (
            not haveGlobalState(event, "playedBefore")
            or getGlobalState(event, "playedBefore") == False
        ):
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
            if userChoice is None and not fromGame:
                # вернуть прошлый эпизод
                # if isInCommandOr(event, LetsPlayIntents) or isInCommandOr(
                #     event, RepeatIntents
                # ):
                    
                config = dontUnderstandConfig(
                    event, variants_of_the_choice=canLastChoicedArr, branch="game"
                )

                if not 'session_state' in config:
                    config['session_state'] = {}

                config['session_state']['fromGame'] = True
                return config
                    # if repeat:
                    #     return compileConfigFromEpisode(
                    #         event, lastEpisode, haveUserInterface
                    #     )
            
                    
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
        if 'playEnding' in info and info['playEnding'] == True:
            episode = passEpisode(info, statsEnds[info['whatPlayEnding'][0]][info['whatPlayEnding'][1]], statsEnds)
        else:
            episode = passEpisode(info, firstGameHistory, statsEnds)
        
        
    # пройти к следующему эпизоду, если юзер уже играл
    else:
    # info = createStartInfo(statsEnds[fraction]['full'])
    # info['playEnding'] = True
    # info['whatPlayEnding'] = [fraction,'full']
    # updateSave(conn,userId,info)
    # return getConfig(event, allDialogs, needCreateNewInfo=False, fromGame=False)

    
        if 'playEnding' in info and info['playEnding'] == True:
            episode = passEpisode(info, statsEnds[info['whatPlayEnding'][0]][info['whatPlayEnding'][1]], statsEnds)
        else:
            episode = passEpisode(info, history, statsEnds)

    print('####pos',info['posEpisode'])
    print('####maxPos',info['maxPosEpisode'])

    nowStats = info['stats']
    print('nowStats',nowStats)

    # если навык закончился
    if episode == 'its all':
        # удалить последнее сохранение
        removeSave(conn, userId)
        return getConfig(event, allDialogs, needCreateNewInfo=True, fromGame=fromGame, repeat=repeat)


    if not 'playEnding' in info or info['playEnding'] != True:
        for fraction in nowStats:
            if nowStats[fraction] >= 100:
                saveStats = info['stats']
                info = createStartInfo(statsEnds[fraction]['full'])
                info['stats'] = saveStats
                info['playEnding'] = True
                info['whatPlayEnding'] = [fraction,'full']
                updateSave(conn,userId,info)
                return getConfig(event, allDialogs, needCreateNewInfo=False, fromGame=False)
            elif nowStats[fraction] <= 0:
                saveStats = info['stats']
                info = createStartInfo(statsEnds[fraction]['empty'])
                info['stats'] = saveStats
                info['playEnding'] = True
                info['whatPlayEnding'] = [fraction,'empty']
                updateSave(conn,userId,info)
                return getConfig(event, allDialogs, needCreateNewInfo=False, fromGame=False)



    # если надо принудительно повторить
    if repeat and lastEpisode:
        # если это первая игра
        if not haveGlobalState(event, "playedBefore") or not getGlobalState(
            event, "playedBefore"
        ):
            return compileConfigFromEpisode(
                event,
                lastEpisode,
                haveInterface,
                userStateUpdate={"playedBefore": True},
            )

        print('pelmeny')

        # вернуть последний эпизод
        return compileConfigFromEpisode(event, lastEpisode, haveUserInterface)

    if "name" in episode and not episode["name"] is None:
        increaseStat(conn, userId, meetedCharacters=episode["name"])

    # закинуть текущий эпизод в качестве последнего для следующего вызова
    info["lastEpisode"] = json.dumps(episode, ensure_ascii=False)


    # "true": [0, 0, 0, 0],
    #   "false": [0, 0, 0, 0],
    #   "always": [0, 0, 0, 0],
    #xcv
    # info['notAppliedStats']

    

    # скомпилировать конфиг из эпизода и вернуть его
    config = compileConfigFromEpisode(event, episode, haveUserInterface)

    if len(episode["buttons"]) == 0:
        addStatsState = []
        if (
            haveGlobalState(event, "addStats")
            and type(getGlobalState(event, "addStats")) == list
        ):
            stats = getGlobalState(event, "addStats")
            stats.append([1, lastEpisode["message"]])
            addStatsState = stats
        else:
            addStatsState = [[1, lastEpisode["message"]]]

        if not "user_state_update" in config:
            config["user_state_update"] = {"addStats": addStatsState} 
        else:
            config["user_state_update"] = {
                **config["user_state_update"],
                "addStats": addStatsState,
            }

        config['user_state_update']['playedBefore'] = True

    # обновить сохранение в БД
    updateSave(conn, userId, info)

    return config