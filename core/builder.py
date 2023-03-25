# Нами был создан специальный формат записи эпизодов. Он называться ssd-format
# Для превращения ssd-format в python-словарь, промежуточно ssd-format превращается в формат yaml,
# из которого уже и происходит трансформация в словарь при помощи библиотеки pyyaml
import yaml


# заменить ссылки в "response"ах в виде строк "{link}" на ссылочные эпизоды в словарном представлении
def replaceLinkEpisodes(history, linkEpisodes):
    # если попалась связка, то выполнить замену для всего внутри
    if type(history) == list:
        for episode in history:
            replaceLinkEpisodes(episode, linkEpisodes)

    # если есть ссылка вида "{link}"
    elif "{" in history["response"]:
        # получить адрес ссылки
        key = history["response"][1:-1]

        # если адрес существует, то заменить, иначе выдать ошибку
        if key in linkEpisodes:
            # перенести респонс
            history["response"] = linkEpisodes[key][0]["response"]
            # перенести true-ивент
            if "onTrue" in linkEpisodes[key][0]:
                history["onTrue"] = linkEpisodes[key][0]["onTrue"]
            # перенести false-ивент
            if "onFalse" in linkEpisodes[key][0]:
                history["onFalse"] = linkEpisodes[key][0]["onFalse"]
            # перенести эпизоды, если респонс случайного эпизода
            if "[chance]" in linkEpisodes[key][0]:
                history["chance"] = linkEpisodes[key][0]["chance"]
        else:
            # если такой ссылки нет 
            raise IndexError("Попытка обратиться к несуществующей ссылке:",history["response"])


    # выполнить внутреннюю замену
    # - случайного эпизода
    elif "chance" in history:
        replaceLinkEpisodes(history["chance"], linkEpisodes)

    # - эпизода с ивентом
    elif "onTrue" in history or "onFalse" in history:
        if "onTrue" in history:
            replaceLinkEpisodes(history["onTrue"], linkEpisodes)
        if "onFalse" in history:
            replaceLinkEpisodes(history["onFalse"], linkEpisodes)

    # вернуть историю
    return history


# трансформировать ssd-format в словарное представление
def builder(
    history: str, # основная история 
    linkEpisodes: dict = None, # ссылочные эпизоды
    transformLinkEpisodes: bool = True, # нужно ли трансформировать ссылочные эпизоды
    printText: str = None, # вывести о начале работы билдера (чтоб красиво было :c)
):
    if printText:
        print("Синтезирование " + printText + '...')

    # заменить одинарные кавычки на двойные
    history = history.replace("'", '"')

    # поделить на строки для дальнейшей обработки
    arr = history.split("\n")

    # форматирование ssd-format => yaml
    resultArr = []  # список, куда будут записываться уже отформатированные строки
    for i in range(len(arr)):
        n = arr[i]

        # если строка пустая, то она нам не нужна
        if n == "":
            continue

        # если строка с условием "true", то заменить само условие на "onTrue" (нужно для обработчика)
        if "true:" in n:
            n = n.replace("true", "  onTrue")
            resultArr.append(n)
            continue

        # если строка с условием "false", то заменить само условие на "onFalse" (нужно для обработчика)
        if "false:" in n:
            n = n.replace("false", "  onFalse")
            resultArr.append(n)
            continue

        # добавить пробел для "chance" (для обработчика)
        if "chance" in n and not ("[chance]" in n):
            n = n.replace("chance", "  chance")
            resultArr.append(n)
            continue

        # если строка содержит в себе response, то добавить ключ "response" и обернуть блок в массив
        if '"' in n:
            n = n.replace('"', '- response: "', 1)
            resultArr.append(n)
            continue

    # соединить все строки в одно целое. в итоге у нас получится yaml
    yamlResult = "\n".join(resultArr)

    # форматирование yaml => словарное-представление
    result = yaml.load(yamlResult, Loader=yaml.Loader)

    # форматирование ssd-format => словарное-представление для ссылочных эпизодов
    if transformLinkEpisodes and not (linkEpisodes is None):
        print("Синтезирование ссылочных эпизодов...")
        for key in linkEpisodes:
            linkEpisodes[key] = builder(linkEpisodes[key], linkEpisodes)

    # заменить ссылки в "response"ах в виде строк "{link}" на словари
    replaceLinkEpisodes(result, linkEpisodes)

    # вернуть результат
    return result
