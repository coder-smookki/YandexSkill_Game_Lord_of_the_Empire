from .builder import builder
from datetime import datetime
from .historyHandler import passEpisode

def skillEmulate(historyText, linkEpisodes=None):
    print('Синтезирование истории...')
    startTime = datetime.now()
    history = builder(historyText, linkEpisodes)
    endTime = datetime.now()
    print('Синтезирование завершено с кайфом за: ' + str(endTime - startTime))

    info = {
        "posEpisode": [0],
        "maxPosEpisode": [len(history) - 1],
        "pastPosEpisode": None,
        "choice": "none",
        "pastHasEvent": None,
    }

    print("=> История началась <=")
    while True:
        episode = passEpisode(info, history)
        if type(episode) == str:
            break

        episodeInfo = episode["response"].split("//")
        if len(episodeInfo) < 4:
            raise ValueError('Неправильный формат текста: ' + episode["response"])

        buttons = episodeInfo[1]
        if episodeInfo[2] != "none":
            buttons += episodeInfo[2]

        print(episodeInfo[0])

        while True:
            choice = input(buttons + "\n")
            if choice == "t" or choice == "y":
                info["choice"] = "true"
                break
            elif choice == "f" or choice == "n":
                info["choice"] = "false"
                break
    print("=> История закончилась <=")





































