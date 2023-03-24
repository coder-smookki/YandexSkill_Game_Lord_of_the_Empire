import copy

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
def passEpisode(info: dict, history:list, recursive=False):
    # FOR DEBUG
    # if recursive:
    #     print("Recursive")
    # print(info)

    # если прошлый эпизод имел ивент и выбор игрока совпадает с ивентом, то обработать ивент
    if (info["pastHasEvent"] == "true" or info["pastHasEvent"] == "both") and info["choice"] == "true":
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
        return passEpisode(info, history, True)

    # аналогично для "false"
    elif (info["pastHasEvent"] == "false" or info["pastHasEvent"] == "both") and info["choice"] == "false":
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
        return passEpisode(info, history, True)

    # если какой-то ивент был, но пользователь ответил иначе
    elif not (info["pastHasEvent"] is None):
        # очистить детектор ивента
        info["pastHasEvent"] = None

        # перейти на шаг вправо, т.к. мы это не сделали раньше (на 131 строке)
        info["posEpisode"][-1] += 1

    # цикл, занимающийся отслеживанием ситуаций,
    # когда на последнем уровне вложенности получился несуществующий индекс
    while True:
        if info["posEpisode"][-1] > info["maxPosEpisode"][-1]:
            # обрезать на 1 элемент
            info["posEpisode"] = info["posEpisode"][:-1]
            info["maxPosEpisode"] = info["maxPosEpisode"][:-1]

            # если массив пустой => обрезалось все => пройдены все эпизоды => история закончена
            if len(info["posEpisode"]) == 0:
                return "its all"

            # если после обрезанного индекса у нас стоит "true" или "false"
            if info["posEpisode"][-1] == "true" or info["posEpisode"][-1] == "false":
                # обрезать "true" или "false"
                info["posEpisode"] = info["posEpisode"][:-1]
                info["maxPosEpisode"] = info["maxPosEpisode"][:-1]

            # добавить +1 к последнему индексу
            # if type(info["posEpisode"][-1]) == int:
            info["posEpisode"][-1] += 1
        else:
            break

    # получить эпизод
    episode = getEpisode(info["posEpisode"], history)

    # если эпизод - связка, то зарегистрировать его для дальнейшего вывода
    # и запустить функцию еще раз для вывода эпизода
    if type(episode) == list:
        info["posEpisode"].append(0)
        info["maxPosEpisode"].append(len(episode) - 1)
        return passEpisode(info, history, True)

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
    
    return episode
