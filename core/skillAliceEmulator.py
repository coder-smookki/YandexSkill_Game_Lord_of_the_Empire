from .builder import builder
from datetime import datetime
from .historyHandler import passEpisode
from termcolor import colored

# эмулятор навыка в консоли, чтобы удобно было тестировать
def skillEmulate(historyText, statsEnds, linkEpisodes=None):
    # билдинг истории в словарное-представление
    print(colored("+", "green"), "Старт синтезирования")
    startTime = datetime.now()
    history = builder(historyText, linkEpisodes, printAboutStart=True)
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
    }

    # старт истории
    print(colored("=>", "blue"), "История началась", colored("<=", "blue"))
    while True:
        # пройти и получить эпизод
        episode = passEpisode(info, statsEnds, history)
        if type(episode) == str:
            break

        # получить массив информации из "response" эпизода
        episodeInfo = episode["response"].split("//")

        # если массив состоит из <5 элементов - значит его труктура не соответствует 
        # правильному формату
        if len(episodeInfo) < 5:
            raise ValueError(colored("=>", "darkred"), "Неправильный формат текста: " + episode["response"])

        # Формат: "text // trueBtn // falseBtn // church army nation coffers // cardId"
        # Пример: "text // asd // zxc // 0 0 -10 5 // cardId123"
        text = episodeInfo[0] # сообщение
        btns = [episodeInfo[1], episodeInfo[2]] # две кнопки
        # получить, какие статы надо изменить, и поместить эту инфу в словарь
        stats = episodeInfo[3].split(" ") 
        stats = {
            "church": stats[0],
            "army": stats[1],
            "nation": stats[2],
            "coffers": stats[3],
        }
        cardId = episodeInfo[4] # айди картинки, загруженной на яндекс

        # показать сообщение
        print(text)

        # если первая кнопка == "None", значит вторая тоже => кнопки отображать не надо => конец игры
        # если только вторая кнопка == "None", значит нужно вывести одну и внезависимости от ответа
        # игрока, выдать событие "true"
        # иначе кнопки 2. первая выдает событие "true", вторая - "false" 
        countBtns = 2
        if btns[0].strip() == "None":
            countBtns = 0
        elif btns[1].strip() == "None":
            countBtns = 1

        # получить ответ пользователя
        while True:
            # выдать столько кнопок, сколько указано в "countBtns"
            choice = input(" ".join(btns[:countBtns]) + "\n")

            # если у нас есть только 1 кнопка
            if countBtns == 1:
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
