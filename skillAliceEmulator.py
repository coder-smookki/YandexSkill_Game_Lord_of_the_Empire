from gameCore.builder import builder
from datetime import datetime
from gameCore.historyHandler import passEpisode
from termcolor import colored
 

# эмулятор навыка в консоли, чтобы удобно было тестировать
def skillEmulate(historyText, statsEnds, linkEpisodes=None):
    # билдинг истории в словарное-представление
    print(colored("+", "green"), "Старт синтезирования")
    startTime = datetime.now()
    history = builder(historyText, linkEpisodes, "истории")

    # билдинг концовок
    for key in statsEnds:
        for kkey in statsEnds[key]:
            statsEnds[key][kkey] = builder(
                statsEnds[key][kkey],
                transformLinkEpisodes=False,
                printText="концовки: " + key + "-" + kkey,
            )

    endTime = datetime.now()
    print(
        colored("+", "green"),
        "Синтезирование завершено с кайфом за: " + str(endTime - startTime),
    )

    # создание начальной информации об игре
    info = {
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

    # старт истории
    print(colored("=>", "blue"), "История началась", colored("<=", "blue"))
    while True:
        # пройти и получить эпизод
        episode = passEpisode(info, history, statsEnds)

        # print(info["posEpisode"])
        # print(episode)

        if episode == "its all":
            break

        # показать статы
        print(episode["stats"])

        # показать имя (если оно есть)
        if 'name' in episode and not (episode['name'] is None):
            print('' + episode["name"] + ':')

        # показать сообщение
        print(episode["message"])

        # получить ответ пользователя
        while True:
            # если конец игры, то
            if len(episode["buttons"]) == 0:
                break

            # выдать кнопоки
            choice = input(" ".join(episode["buttons"]) + "\n")

            # если у нас есть только 1 кнопка
            if len(episode["buttons"]) == 1:
                info["choice"] = "true"
                break

            # если пользователь выбрал "t"
            if choice == "t" or choice == "y":
                info["choice"] = "true"
                break

            # если пользователь выбрал "f"
            elif choice == "f" or choice == "n":
                info["choice"] = "false"
                break
    # конец =)
    print("=> История закончилась <=")
