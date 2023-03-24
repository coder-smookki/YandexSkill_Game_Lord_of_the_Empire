# Нами был создан специальный формат записи эпизодов. Он называться ssd-format
# Для превращения ssd-format в python-словарь, промежуточно ssd-format превращается в формат yaml,
# из которого уже и происходит трансформация в словарь при помощи библиотеки pyyaml
import yaml


# заменить все ссылочные эпизоды
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
            history["response"] = linkEpisodes[key][0]["response"]
            if "onTrue" in linkEpisodes[key][0]:
                history["onTrue"] = linkEpisodes[key][0]["onTrue"]
            if "onFalse" in linkEpisodes[key][0]:
                history["onFalse"] = linkEpisodes[key][0]["onFalse"]
            if "[chance]" in linkEpisodes[key][0]:
                history["chance"] = linkEpisodes[key][0]["chance"]
        else:
            raise IndexError("Попытка обратиться к несуществующей ссылке")

    # выполнить внутреннюю замену
    # случайного эпизода
    elif "chance" in history:
        replaceLinkEpisodes(history["chance"], linkEpisodes)

    # эпизода с ивентом
    elif "onTrue" in history or "onFalse" in history:
        if "onTrue" in history:
            replaceLinkEpisodes(history["onTrue"], linkEpisodes)
        if "onFalse" in history:
            replaceLinkEpisodes(history["onFalse"], linkEpisodes)

    return history


# трансформировать ssd-format в словарное представление
def builder(
    q: str,
    linkEpisodes: dict = None,
    transformLinkEpisodes: bool = True,
    printAboutStart: bool = False,
):
    if printAboutStart:
        print("Синтезирование истории...")
    # заменить одинарные кавычки на двойные
    q = q.replace("'", '"')

    # поделить на строки для дальнейшей обработки
    arr = q.split("\n")

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

        # аналогично для "false"
        if "false:" in n:
            n = n.replace("false", "  onFalse")
            resultArr.append(n)
            continue

        # добавить пробел для "chance"
        if "chance" in n and not ("[chance]" in n):
            n = n.replace("chance", "  chance")
            resultArr.append(n)
            continue

        # если строка содержит в себе response, то добавить ключ "response" и обернуть блок в массив
        if '"' in n:
            n = n.replace('"', '- response: "', 1)
            resultArr.append(n)
            continue

    # соединить все строки в одно целое. в итоге у нас получился yaml
    yamlResult = "\n".join(resultArr)

    # трансформировать yaml в словарное представление
    result = yaml.load(yamlResult, Loader=yaml.Loader)

    # трансформировать ssd-format в словарное представление в ссылочных эпизодах
    if transformLinkEpisodes and not (linkEpisodes is None):
        print("Синтезирование ссылочных эпизодов...")
        for key in linkEpisodes:
            linkEpisodes[key] = builder(linkEpisodes[key], linkEpisodes, False)

    replaceLinkEpisodes(result, linkEpisodes)

    return result
