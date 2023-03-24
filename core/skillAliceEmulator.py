from .builder import builder
from datetime import datetime
from .historyHandler import passEpisode

history = [
    {
        "response": "1 // true // false // chatid",
        "onTrue": [
            {"response": "1t // true // false // chatid", "onTrue": [{"response": "1.1tt // true // false // chatid"}, {"response": "1.2tt // true // false // chatid"}]}
        ],
    },
    {"response": "2 // true // false // chatid"},
]

def skillEmulate(historyText):
    info = {
        "posEpisode": [0],
        "maxPosEpisode": [len(history) - 1],
        "pastPosEpisode": None,
        "choice": "none",
        "pastHasEvent": None,
    }
    
    print('Синтезирование истории...')
    startTime = datetime.now()
    history = builder(historyText)
    endTime = datetime.now()
    print('Синтезирование завершено с кайфом за: ' + str(endTime - startTime))

    print("=> История началась <=")
    while True:
        episode = passEpisode(info)
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
            elif choice == "t" or choice == "n":
                info["choice"] = "false"
                break
    print("=> История закончилась <=")