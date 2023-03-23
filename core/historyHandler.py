import copy

history = []


# получить эпизод или связку по пути
def getEpisode(pos: list):
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
def passEpisode(info: dict, recursive=False):
    # FOR DEBUG
    if recursive:
        print('Recursive')
    print(info)

    # if info["choice"] == "true":
    #     info["posEpisode"].append("true")
    #     info["posEpisode"].append(0)
        
    #     episode = getEpisode(info["posEpisode"])

    #     info["maxPosEpisode"].append("true")
    #     info["maxPosEpisode"].append(len(episode) - 1)

    #     return passEpisode(info)

    # if info["choice"] == "false":
    #     info["posEpisode"].append("false")
    #     info["posEpisode"].append(0)
        
    #     episode = getEpisode(info["posEpisode"])

    #     info["maxPosEpisode"].append("false")
    #     info["maxPosEpisode"].append(len(episode) - 1)

        # return passEpisode(info)

    # цикл, занимающийся отслеживанием ситуаций,
    # когда на последнем уровне вложенности получился несуществующий индекс
    # или значение "true" или "false"
    while True:
        if (
            info["posEpisode"][-1] > info["maxPosEpisode"][-1]
            or info["posEpisode"][-1] == "true"
            or info["posEpisode"][-1] == "false"
        ):
            # обрезать на 1 элемент
            info["posEpisode"] = info["posEpisode"][:-1]
            info["maxPosEpisode"] = info["maxPosEpisode"][:-1]

            # если массив пустой => обрезалось все => пройдены все эпизоды => история закончена
            if len(info["posEpisode"]) == 0:
                return "its all"

            # добавить +1 к последнему индексу
            # if type(info["posEpisode"][-1]) == int:
            info["posEpisode"][-1] += 1
        else:
            break

    # получить эпизод
    episode = getEpisode(info["posEpisode"])

    # если эпизод - связка, то зарегестрировать его для дальнейшего вывода
    # и запустить функцию еще раз для корректного вывода
    if type(episode) == list:
        info["posEpisode"].append(0)
        info["maxPosEpisode"].append(len(episode) - 1)
        return passEpisode(info, True)

    # если все условия выше прошли стороной, то мы дошли до обычного эпизода
    # и стоит сместить позицию на 1 вправо
    info["pastPosEpisode"] = info["posEpisode"] 
    info["posEpisode"][-1] += 1
    
    return episode


history = [
    {
        "response": "1 // btn1 // btn2 // cardid",
        "onTrue": [{"response": "1.t // btn1 // btn2 // cardid"}],
    },
    {
        "response": "2 // btn1 // btn2 // cardid"
    }
]









info = {"posEpisode": [0], "maxPosEpisode": [len(history) - 1], "pastPosEpisode": None, "choice": "none"}



def skillEmulate(times):
    for i in range(times):
        episode = passEpisode(info)
        if type(episode) == str:
            return print(episode)
        episodeInfo = episode["response"].split("//")

        buttons = episodeInfo[1]
        if episodeInfo[2] != "none":
            buttons += episodeInfo[2]

        print(episodeInfo[0])
        choice = input(buttons + "\n")

        if choice == "t":
            info["choice"] = "true"
        else:
            info["choice"] = "false"


skillEmulate(2)
# skillEmulate(len(history))
