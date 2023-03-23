info = {"posEpisode": [0], "choice": "true", "pastEpisode": {}}
history = []

# на момент запуска этой функции должна быть 100% гарантия правильности пути. путь также может быть неполным (вести на связку)
def passEpisode(info: dict):
    if "onTrue" in info["pastEpisode"] and info["choice"] == "true":
        info["posEpisode"][-1] -= 1
        info["posEpisode"].append("true")
        info["pastEpisode"] = {}
        return passEpisode(info)
    if "onFalse" in info["pastEpisode"] and info["choice"] == "false":
        info["posEpisode"][-1] -= 1
        info["posEpisode"].append("false")
        info["pastEpisode"] = {}
        return passEpisode(info)

    # если история закончилась
    if len(info["posEpisode"]) == 1 and info["posEpisode"][-1] >= len(history):
        return "The end"

    # получить эпизод по пути
    episode = getEpisode(info["posEpisode"])

    # если к нам пришла связка
    if type(episode) == list:
        info["posEpisode"].append(0)
        episode = getEpisode(info["posEpisode"])

    # перейти к следующему диалогу на следующем запуске функции
    info["posEpisode"][-1] += 1

    # если текущая связка закончилась, то перейти к следующей на следующем запуске функции
    if (
        info["posEpisode"][-1] >= len(getEpisode(info["posEpisode"][:-1]))
        and len(info["posEpisode"]) > 1
    ):
        info["posEpisode"] = info["posEpisode"][:-1]
        if info["posEpisode"][-1] == "true" or info["posEpisode"][-1] == "false":
            info["posEpisode"] = info["posEpisode"][:-1]
        info["posEpisode"][-1] += 1
    info["pastEpisode"] = episode

    # вернуть эпизод
    return episode


q = """

"1"
true:
    '2'
    true:
        '3'
false:
    '4'

"""

result = [
    {
        "response": "1",
        "onTrue": {"response": "2", "onTrue": [{"response": "3"}]},
        "onFalse": {"response": "4"},
    }
]


# # print(getEpisode(info["posEpisode"]))
# print(passEpisode(info))
# # print(info)
# print(passEpisode(info))
# # print(info)
# print(passEpisode(info))
# # print(info)
# print(passEpisode(info))
# # print(info)
# print(passEpisode(info))
# # print(info)
# print(passEpisode(info))
# print(passEpisode(info))
# print(passEpisode(info))
# print(info)
# print(passEpisode(info))
# print(passEpisode(info))
# print(passEpisode(info))
# #print(info)
# print(passEpisode(info))
# print(passEpisode(info))
# print(passEpisode(info))
# print(passEpisode(info))
# print(info)
# print(passEpisode(info))
# print(passEpisode(info))


# print(info)
# print(passEpisode(info))

# print(passEpisode(info))

# print(passEpisode(info))
# print(getEpisode(info, True))
# print(passEpisode(info))
# print(passEpisode(info))
