from .builder import builder
from datetime import datetime
from .historyHandler import passEpisode
from termcolor import colored


def skillEmulate(historyText, statsEnds, linkEpisodes=None):
    print(colored("+", "green"), "Старт синтезирования")
    startTime = datetime.now()
    history = builder(historyText, linkEpisodes, printAboutStart=True)
    endTime = datetime.now()
    print(
        colored("+", "green"),
        "Синтезирование завершено с кайфом за: " + str(endTime - startTime),
    )

    info = {
        "posEpisode": [0],
        "maxPosEpisode": [len(history) - 1],
        "pastPosEpisode": None,
        "choice": "none",
        "pastHasEvent": None,
        "stats": {"church": 50, "army": 50, "nation": 50, "coffers": 50},
    }

    print("=> История началась <=")
    while True:
        episode = passEpisode(info, statsEnds, history)
        if type(episode) == str:
            break

        episodeInfo = episode["response"].split("//")

        if len(episodeInfo) < 5:
            raise ValueError("Неправильный формат текста: " + episode["response"])

        # text // trueBtn // falseBtn // church army nation coffers // cardId
        # "text // asd // zxc // 0 0 -10 5 // zxc"
        text = episodeInfo[0]
        btns = [episodeInfo[1], episodeInfo[2]]
        stats = episodeInfo[3].split(" ")
        stats = {
            "church": stats[0],
            "army": stats[1],
            "nation": stats[2],
            "coffers": stats[3],
        }
        cardId = episodeInfo[4]

        print(text)

        countBtns = 2
        if btns[0].strip() == "None":
            countBtns = 0
        elif btns[1].strip() == "None":
            countBtns = 1

        while True:
            choice = input(" ".join(btns[:countBtns]) + "\n")

            if choice == "t" or choice == "y":
                info["choice"] = "true"
                break

            elif choice == "f" or choice == "n":
                info["choice"] = "false"
                break

    print("=> История закончилась <=")
