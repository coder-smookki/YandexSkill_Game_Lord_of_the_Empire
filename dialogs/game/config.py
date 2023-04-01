from utils.globalStorage import *
from utils.responseHelper import *
from utils.dbHandler import *
from utils.triggerHelper import *
from gameCore.historyHandler import passEpisode
import random
from utils.image_gen.get_id import get_id
import re

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


def getRandomSfx(sfx):
    return sfx[random.randint(0, len(sfx) - 1)]


def compileConfigFromEpisode(event,episode, haveInterface):
    # получить статы
    stats = episode["stats"]

    print('stats:',stats)

    # если в эпизоде есть имя (выступает персонаж)
    if episode["name"]:
        # добавить sfx, имя и сообщение в tts
        tts = getRandomSfx(sfx) + episode["name"] + ". " + episode["message"]

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
                changes=[0, 0, 0, 0],
            )

            # если карточка не вернулась, использовать арбуз
            if cardId is None:
                cardId = "1533899/d371aab5224c91137cfc"
    else:
        # если эпизод - оповещение (нет имени), то добавить sfx и сообщение в tts
        tts = getRandomSfx(sfx) + episode["message"]

        if haveInterface:
            # использовать арбуз
            cardId = "1533899/d371aab5224c91137cfc"

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
            config["tts"] = config["tts"] + ". " + "Варианты ответа, " + buttonsStr + "."

    else:
        # создать конфиг для устройств без интерфейса
        config = {
            'message': 'zxc',
            "tts": tts,
            'buttons': ['first button aboba','second button aboba']
        }
        
        # вынести текущие фракции в виде строки
        statsStr = f"""Репутация текущий фракций:
            Церковь: {stats["church"]} единиц.
            народ: {stats["nation"]} единиц.
            армия: {stats["army"]} единиц.
            казна: {stats["coffers"]} единиц.
        """
        
        # добавить фракции в tts
        config['tts'] += statsStr

        # вынести из массива кнопки в виде строки
        buttonsStr = ""
        for button in episode["buttons"]:
            buttonsStr += button + ', '

        # добавить в tts кнопки и статы
        config["tts"] = config["tts"] + ". " + "Варианты ответа: " + buttonsStr

    # добавить бренч в конфиг
    config["session_state"] = {"branch": "game"}

    # если нет кнопок для выбора (игрок умер)
    if episode["buttons"] is None or len(episode["buttons"]) == 0:
        # соединение с БД
        conn = globalStorage["mariaDBconn"]

        # айди юзера
        userId = getUserId(event)

        # удалить последнее сохранение
        removeSave(conn, userId)

        # добавить 1 смерть в статистику и новую концовку (если она новая)
        increaseStat(conn, userId, deaths=1, openEnds=episode["message"])

        # если это первая игра
        if not haveGlobalState(event,'playedBefore') or not getGlobalState(event,'playedBefore'):
            print('first game')
            if not 'user_state_update' in config:
                config['user_state_update'] = {}
            config['user_state_update']["playedBefore"] = True 
            config['user_state_update']["abobaAboba"] = 'hehehe' 

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
    commandArr = command.split(' ')

    # убрать все, кроме букв и пробелов в строках, потом разделить по пробелам
    firstLastChoiceCommandArr = re.sub(r'[^A-Za-zА-Яа-я ]', '', firstLastChoiceCommand.lower()).split(' ')
    secondLastChoiceCommandArr = re.sub(r'[^A-Za-zА-Яа-я ]', '', secondLastChoiceCommand.lower()).split(' ')

    # пройтись по всем словам команды
    for word in commandArr:
        # есть слово в массиве с первым выбором
        isInFirst = word in firstLastChoiceCommandArr
        
        # есть слово в массиве со вторым выбором
        isInSecond = word in secondLastChoiceCommandArr

        # если есть в первом, но нет во втором 
        if isInFirst and not isInSecond:
            return 'true'

        # если есть во втором, но нет в первом
        if isInSecond and not isInFirst:
            return 'false'

    # если не нашлось единоличного совпадения
    return None

def getConfig(event, needCreateNewInfo=False):
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
        insertSave(conn, userId, info)

    else:
        # получить инфо по айди юзера
        info = selectGameInfo(conn, userId)

        # если сохранение в БД не нашлось
        if not info:
            # создать стартовое сохранение (создать новую игру)
            info = createStartInfo(history)

            # вставить это сохранение в БД
            insertSave(conn, userId, info)

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

    # если в прошлом эпизоде были выборы
    if canLastChoicedArr:
        # если только один (обычно 2)
        if len(canLastChoicedArr) == 1:
            info["choice"] = "true"

        else:
            # получить выбор пользователя
            userChoice = checkIfLastChoiceSimiliar(command, canLastChoicedArr[0], canLastChoicedArr[1])
            print('Выбор пользователя:',userChoice)
            
            # если определить выбор не удалось
            if userChoice is None:
                # вернуть прошлый эпизод
                return compileConfigFromEpisode(event,lastEpisode,haveUserInterface)
            else:
                # иначе установить выбор в сохранении
                info["choice"] = userChoice



    # пройти к следующему эпизоду, если это первая игра
    if not haveGlobalState(event,'playedBefore') or not getGlobalState(event,'playedBefore'):
        episode = passEpisode(info, firstGameHistory, statsEnds)
    # пройти к следующему эпизоду, если юзер уже играл
    else:
        episode = passEpisode(info, history, statsEnds) 
        
    # если история закончилась
    if episode == "its all":
        # удалить последнее сохранение
        removeSave(conn, userId)

        # пройтись еще раз по функции с нулевым сохранением (начать игру заново)
        return getConfig(event, True)

    if 'name' in episode and not episode['name'] is None:
        increaseStat(conn,userId,meetedCharacters=episode['name'])

    # закинуть текущий эпизод в качестве последнего для следующего вызова
    info["lastEpisode"] = json.dumps(episode, ensure_ascii=False)

    # обновить сохранение в БД
    updateSave(conn, userId, info)

    # скомпилировать конфиг из эпизода и вернуть его
    return compileConfigFromEpisode(event,episode,haveUserInterface)
