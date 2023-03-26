import copy
import random
import re


def formateEpisodeInfo(episodeInfo):
    trueButton = episodeInfo[1][1:-1]
    falseButton = episodeInfo[2][1:-1]
    buttons = []
    if trueButton != "None":
        buttons.append(trueButton)
        if falseButton != "None":
            buttons.append(falseButton)
    return {"text": episodeInfo[0][:-1], "buttons": buttons, "card": episodeInfo[4][1:]}


# отформатировать статы
# если стат нет => вернется None
# если стата одна => вернется массив вида [0,0,0,0]
# если статы две => вернется массив с двумя массивами вида [0,0,0,0]
def formatStats(statsString):
    try:
        arr = statsString[1:-1].split(" $ ")
        if arr[0] == "":
            return None

        if len(arr) == 1:
            stats = list(map(int, arr[0].split(" ")))
            if len(stats) != 4:
                raise ValueError("Неправильная структура стат:", statsString)
            return stats

        trueStats = list(map(int, arr[0].split(" ")))
        falseStats = list(map(int, arr[1].split(" ")))
        if len(trueStats) != 4 or len(falseStats) != 4:
            raise ValueError("Неправильная структура стат:", statsString)

        return [trueStats, falseStats]
    except:
        raise ValueError("Неправильная структура стат:", statsString)


# получить следующий рандомный неиспользуемый индекс шафла
# total - максимальный индекс
# used - список уже используемых значений
def getShuffleIndex(total: int, used: list):
    values = [x for x in range(0, total) if x not in used]

    for i in range(len(values) - 1, 0, -1):
        j = random.randint(0, i)
        values[i], values[j] = values[j], values[i]

    if len(values) == 0:
        raise ValueError('Не получилось взять новый индекс:', total, used)

    return values[-1]


# выбрать сценарий в случайном эпизоде
def getChanceIndex(response):
    # поделить строку вида "[chance] 1 2 3" на числа и убрать "[chance]"
    chances = response.split(" ")[1:]

    # суммировать все числа
    chancesSum = 0
    for chance in chances:
        chancesSum += int(chance)

    # получить случайное число от 1 до суммы всех чисел
    randomNum = random.randint(1, chancesSum)

    # выявить удачное число и вернуть его индекс в массиве,
    # который равен индексу в массиве случайных эпизодов
    lastSum = 0
    for i in range(len(chances)):
        lastSum += int(chances[i])
        if randomNum <= lastSum:
            return i

    raise ValueError(
        "По какой-то причине не получилось выбрать случайный сценарий:",
        response,
        " ",
        randomNum,
    )


# получить эпизод или связку по пути
def getEpisode(pos: list, history: list):
    # самый последний эпизод на текущий момент
    lastEpisode = history
    # перебирание пути, запись конечной точки
    try:
        for depth in range(len(pos)):
            # если путь идет по ветке onTrue
            if pos[depth] == "true":
                lastEpisode = lastEpisode["onTrue"]
                continue

            # если путь идет по ветке onFalse
            if pos[depth] == "false":
                lastEpisode = lastEpisode["onFalse"]
                continue

            # если путь идет по случайному сценарию
            if pos[depth] == "chance":
                lastEpisode = lastEpisode["chance"]
                continue

            # если путь идет по теговой связке
            if pos[depth] == "bundle":
                lastEpisode = lastEpisode["bundle"]
                continue

            # если путь идет по шафлу
            if type(pos[depth]) == str and "shuffle" in pos[depth]:
                lastEpisode = lastEpisode["shuffle"]
                continue

            # если идет индекс
            lastEpisode = lastEpisode[pos[depth]]

    # # если случилась ошибка, значит была попытка обратиться к несуществующему индексу/полю
    # # => неправильный путь
    except:
        raise IndexError("Неправильный путь:", pos)

    # вернуть эпизод
    return lastEpisode


# пройти эпизод
def passEpisode(info: dict, history: list, statsEnds: dict, recursive=False):
    # FOR DEBUG
    # if recursive:
    #     print("Recursive")
    # print(info)

    # если прошлый эпизод имел ивент "true" и выбор игрока совпадает с ивентом, то обработать ивент
    if (info["pastHasEvent"] == "true" or info["pastHasEvent"] == "both") and info[
        "choice"
    ] == "true":
        # применить статы
        info["stats"]["church"] += info["notAppliedStats"]["true"][0]
        info["stats"]["army"] += info["notAppliedStats"]["true"][1]
        info["stats"]["nation"] += info["notAppliedStats"]["true"][2]
        info["stats"]["coffers"] += info["notAppliedStats"]["true"][3]

        # очистить статы
        info["notAppliedStats"]["true"] = [0, 0, 0, 0]
        info["notAppliedStats"]["false"] = [0, 0, 0, 0]

        # очистить детектор ивента
        info["pastHasEvent"] = None

        # изменить путь
        info["posEpisode"].append("true")

        # получить эпизод по ветке ивента
        episode = getEpisode(info["posEpisode"], history)

        # добавляю 0 в путь после получения эпизода,
        # т.к. мне нужно получить именно массив "onTrue" в качестве эпизода
        info["posEpisode"].append(0)

        # изменить ограничитель
        info["maxPosEpisode"].append("true")
        info["maxPosEpisode"].append(len(episode) - 1)

        # пройтись по новой ветке
        return passEpisode(info, history, statsEnds, True)

    # аналогично для "false"
    elif (info["pastHasEvent"] == "false" or info["pastHasEvent"] == "both") and info[
        "choice"
    ] == "false":
        # применить статы
        info["stats"]["church"] += info["notAppliedStats"]["false"][0]
        info["stats"]["army"] += info["notAppliedStats"]["false"][1]
        info["stats"]["nation"] += info["notAppliedStats"]["false"][2]
        info["stats"]["coffers"] += info["notAppliedStats"]["false"][3]

        # очистить статы
        info["notAppliedStats"]["true"] = [0, 0, 0, 0]
        info["notAppliedStats"]["false"] = [0, 0, 0, 0]

        # очистить детектор ивента
        info["pastHasEvent"] = None

        # изменить путь
        info["posEpisode"].append("false")

        # получить эпизод по ветке ивента
        episode = getEpisode(info["posEpisode"], history)

        # добавляю 0 в путь только после получения эпизода,
        # т.к. далее для изменения ограничителя нужно получить
        # длину массива "onFalse"
        info["posEpisode"].append(0)

        # изменить ограничитель
        info["maxPosEpisode"].append("false")
        info["maxPosEpisode"].append(len(episode) - 1)

        # пройтись по новой ветке
        return passEpisode(info, history, statsEnds, True)

    # если какой-то ивент был, но пользователь ответил иначе
    elif not (info["pastHasEvent"] is None):
        # очистить детектор ивента
        info["pastHasEvent"] = None

        # перейти на шаг вправо, т.к. мы это не сделали раньше (на 131 строке)
        info["posEpisode"][-1] += 1

    # цикл, занимающийся отслеживанием ситуаций,
    # когда на последнем уровне вложенности получился несуществующий индекс
    # из-за сдвигов
    while True:
        # условие для шафла
        if len(info["posEpisode"]) >= 2 and type(info["posEpisode"][-2]) == str and 'shuffle' in info["posEpisode"][-2]:
            info["posEpisode"] = info["posEpisode"][:-1]
            info["maxPosEpisode"] = info["maxPosEpisode"][:-1]

            # на этом моменте последняя позиция 100% - "shuffle-n,n,n..."

            # Формат posEpisode: "shuffle-usedIndex,usedIndex,usedIndex..."
            # Формат maxPosEpisode: "shuffle-totalShows"

            # получить сколько всего нужно показать эпизодов
            shuffleTotalShows = int(re.findall(r"\d+", info["maxPosEpisode"][-1])[0])

            # получить уже использованные эпизоды
            shuffleUsedIndexes = list(map(int, re.findall(r"\d+", info["posEpisode"][-1])))

            # если было показано столько эпизодов, сколько нужно
            if len(shuffleUsedIndexes) >= shuffleTotalShows:
                # обрезать на 1 элемент
                info["posEpisode"] = info["posEpisode"][:-1]
                info["maxPosEpisode"] = info["maxPosEpisode"][:-1]

                # перейти на следующий эпизод после шафла
                info["posEpisode"][-1] += 1

            # иначе показать еще эпизод
            else:
                # получить новый индекс
                newShuffleIndex = getShuffleIndex(shuffleTotalShows, shuffleUsedIndexes)

                # вставить эпизод как использованный
                if len(shuffleUsedIndexes) == 0:  # если первый элемент
                    info["posEpisode"][-1] += str(newShuffleIndex)
                else:
                    info["posEpisode"][-1] += ',' + str(newShuffleIndex)

                # вставить индексы
                info["posEpisode"].append(newShuffleIndex)
                info["maxPosEpisode"].append(newShuffleIndex)

        # для всего остального
        if (info["posEpisode"][-1] > info["maxPosEpisode"][-1]):
            # обрезать на 1 элемент
            info["posEpisode"] = info["posEpisode"][:-1]
            info["maxPosEpisode"] = info["maxPosEpisode"][:-1]

            # если массив пустой => обрезалось все => пройдены все эпизоды => история закончена
            if len(info["posEpisode"]) == 0:
                return "its all"

            # если после обрезанного индекса у нас стоит "true", "false", "chance" или "bundle"
            if (
                    info["posEpisode"][-1] == "true"
                    or info["posEpisode"][-1] == "false"
                    or info["posEpisode"][-1] == "chance"
                    or info["posEpisode"][-1] == "bundle"
            ):
                # обрезать "true", "false", "chance" или "bundle"
                info["posEpisode"] = info["posEpisode"][:-1]
                info["maxPosEpisode"] = info["maxPosEpisode"][:-1]

            # добавить +1 к последнему индексу
            info["posEpisode"][-1] += 1
        else:
            break

    # получить эпизод
    episode = getEpisode(info["posEpisode"], history)

    # если эпизод - теговая связка
    if "[bundle]" in episode["response"]:
        info["posEpisode"].append("bundle")
        info["maxPosEpisode"].append("bundle")

        maxIndex = len(episode["bundle"]) - 1

        info["posEpisode"].append(0)
        info["maxPosEpisode"].append(maxIndex)

        return passEpisode(info, history, statsEnds, True)

    # если эпизод - шафл
    if "[shuffle" in episode["response"]:
        totalShows = re.findall(r"\d+", episode["response"])
        shuffleIndex = getShuffleIndex(len(episode["shuffle"]), [])

        if len(totalShows) == 0:
            totalShows = len(episode["shuffle"])
        else:
            totalShows = int(totalShows[0])

        # print('ASDASDASD',totalShows)

        # shuffle-usedIndexes
        info["posEpisode"].append("shuffle-")
        # shuffle-totalShows
        info["maxPosEpisode"].append("shuffle-" + str(totalShows))

        info["posEpisode"].append(shuffleIndex)
        info["maxPosEpisode"].append(shuffleIndex)

        return passEpisode(info, history, statsEnds, True)

    # если эпизод имеет шанс
    if "[chance" in episode["response"]:
        info["posEpisode"].append("chance")
        info["maxPosEpisode"].append("chance")

        chanceIndex = getChanceIndex(episode["response"])

        info["posEpisode"].append(chanceIndex)
        info["maxPosEpisode"].append(chanceIndex)

        return passEpisode(info, history, statsEnds, True)

    # если эпизод - связка, то зарегистрировать его для дальнейшего вывода
    # и запустить функцию еще раз для вывода эпизода
    if type(episode) == list:
        info["posEpisode"].append(0)
        info["maxPosEpisode"].append(len(episode) - 1)
        return passEpisode(info, history, statsEnds, True)

    # если эпизод имеет ивент, то записать его, чтобы на следующем запуске функции он отработался
    if "onTrue" in episode and "onFalse" in episode:
        info["pastHasEvent"] = "both"
    elif "onTrue" in episode:
        info["pastHasEvent"] = "true"
    elif "onFalse" in episode:
        info["pastHasEvent"] = "false"
    else:
        # если все условия выше прошли стороной, то мы дошли до обычного эпизода
        # и стоит сместить позицию на 1 вправо
        info["pastPosEpisode"] = info["posEpisode"]
        info["posEpisode"][-1] += 1

    episodeInfo = episode["response"].split("//")
    if len(episodeInfo) < 5:
        raise ValueError("Неправильный формат текста: " + episode["response"])

    # применить статы независимые от ответа
    info["stats"]["church"] += info["notAppliedStats"]["always"][0]
    info["stats"]["army"] += info["notAppliedStats"]["always"][1]
    info["stats"]["nation"] += info["notAppliedStats"]["always"][2]
    info["stats"]["coffers"] += info["notAppliedStats"]["always"][3]

    # очистить статы
    info["notAppliedStats"]["always"] = [0, 0, 0, 0]

    # Формат: "text // trueBtn // falseBtn // church army nation coffers $ church army nation coffers // cardId"
    # Пример: "text // asd // zxc // 0 0 -10 5 $ 10 0 0 -20 // zxc"
    stats = formatStats(episodeInfo[3])
    if stats is None:
        trueStats = [0, 0, 0, 0]
        falseStats = [0, 0, 0, 0]
        alwaysStats = [0, 0, 0, 0]
    elif len(stats) == 4:  # если указаны статы внезависимости от выбора
        trueStats = [0, 0, 0, 0]
        falseStats = [0, 0, 0, 0]
        alwaysStats = stats
    # если статы на true или false
    elif len(stats) == 2:
        trueStats = stats[0]
        falseStats = stats[1]
        alwaysStats = [0, 0, 0, 0]

    info["notAppliedStats"]["true"] = trueStats
    info["notAppliedStats"]["false"] = falseStats
    info["notAppliedStats"]["always"] = alwaysStats

    trueButton = episodeInfo[1][1:-1]
    falseButton = episodeInfo[2][1:-1]
    buttons = []
    if trueButton != "None":
        buttons.append(trueButton)
        if falseButton != "None":
            buttons.append(falseButton)

    result = formateEpisodeInfo(episodeInfo)  # отформатировать инфу с респонса эпизода
    result["stats"] = info["stats"]  # добавить в результат еще текущую статистику
    result["changeStats"] = stats  # и возможные изменения на каждый выбор
    return result
