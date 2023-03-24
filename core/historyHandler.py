import copy
import random


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

            # если идет индекс
            lastEpisode = lastEpisode[pos[depth]]

    # если случилась ошибка, значит была попытка обратиться к несуществующему индексу/полю
    # => неправильный путь
    except:
        print(pos)
        raise IndexError("Неправильный путь")

    # вернуть эпизод
    return lastEpisode


# пройти эпизод
def passEpisode(info: dict, history: list, statsEnds: dict, recursive=False):
    # FOR DEBUG
    # if recursive:
    #     print("Recursive")
    # print(info)

    # проверка на переполненность/недостаток фракций
    for key in info["stats"]:
        if info["stats"][key] >= 100:
            return statsEnds[key]["full"]
        elif info["stats"][key] <= 0:
            return statsEnds[key]["empty"]

    # если прошлый эпизод имел ивент и выбор игрока совпадает с ивентом, то обработать ивент
    if (info["pastHasEvent"] == "true" or info["pastHasEvent"] == "both") and info[
        "choice"
    ] == "true":
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
        if info["posEpisode"][-1] > info["maxPosEpisode"][-1]:
            # обрезать на 1 элемент
            info["posEpisode"] = info["posEpisode"][:-1]
            info["maxPosEpisode"] = info["maxPosEpisode"][:-1]

            # если массив пустой => обрезалось все => пройдены все эпизоды => история закончена
            if len(info["posEpisode"]) == 0:
                return "its all"

            # если после обрезанного индекса у нас стоит "true", "false" или "chance"
            if (
                info["posEpisode"][-1] == "true"
                or info["posEpisode"][-1] == "false"
                or info["posEpisode"][-1] == "chance"
            ):
                # обрезать "true", "false" или "chance"
                info["posEpisode"] = info["posEpisode"][:-1]
                info["maxPosEpisode"] = info["maxPosEpisode"][:-1]

            # добавить +1 к последнему индексу
            info["posEpisode"][-1] += 1
        else:
            break

    # получить эпизод
    episode = getEpisode(info["posEpisode"], history)

    # если эпизод имеет шанс
    if "[chance]" in episode["response"]:
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

    # Формат: "text // trueBtn // falseBtn // church army nation coffers // cardId"
    # Пример: "text // asd // zxc // 0 0 -10 5 // zxc"
    stats = episodeInfo[3].split(" ")[1:-1]
    stats = {
        "church": int(stats[0]),
        "army": int(stats[1]),
        "nation": int(stats[2]),
        "coffers": int(stats[3]),
    }

    info["stats"]["church"] += stats["church"]
    info["stats"]["army"] += stats["army"]
    info["stats"]["nation"] += stats["nation"]
    info["stats"]["coffers"] += stats["coffers"]

    return episode
