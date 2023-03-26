# Нами был создан специальный формат записи эпизодов. Он называться ssd-format
# Для превращения ssd-format в python-словарь, промежуточно ssd-format превращается в формат yaml,
# из которого уже и происходит трансформация в словарь при помощи библиотеки pyyaml
import yaml
from termcolor import colored

temp = None

# заменить ссылки в "response"ах в виде строк "{link}" на ссылочные эпизоды в словарном представлении
def replaceLinkEpisodes(history, linkEpisodes):
    global temp
    # если попалась связка, то выполнить замену для всего внутри
    if type(history) == list:
        for episode in history:
            replaceLinkEpisodes(episode, linkEpisodes)

    elif type(history) == str:
        # print(temp)
        raise ValueError('di4\' proizoshla')

    elif not ("response" in history):
        raise ValueError(history)

    # если есть ссылка вида "{link}"
    elif "{" in history["response"]:
        # получить адрес ссылки
        key = history["response"][1:-1]
        print('KEY',key)
        # если адрес существует, то заменить, иначе выдать ошибку
        if key in linkEpisodes:
            # print(linkEpisodes[key][0])
            # перенести респонс
            history["response"] = linkEpisodes[key][0]["response"]
            # перенести true-ивент
            if "onTrue" in linkEpisodes[key][0]:
                history["onTrue"] = linkEpisodes[key][0]["onTrue"]
            # перенести false-ивент
            if "onFalse" in linkEpisodes[key][0]:
                history["onFalse"] = linkEpisodes[key][0]["onFalse"]
            # перенести эпизоды, если респонс случайного эпизода
            if "chance" in linkEpisodes[key][0]:
                history["chance"] = linkEpisodes[key][0]["chance"]
            # перенести эпизоды, если респонс бандла
            if "bundle]" in linkEpisodes[key][0]:
                # print('gahsdjhkdas')
                history["bundle"] = linkEpisodes[key][0]["bundle"]
            # перенести эпизоды, если респонс шафла
            if "shuffle" in linkEpisodes[key][0]:
                history["shuffle"] = linkEpisodes[key][0]["shuffle"]
        else:
            # если такой ссылки нет 
            raise IndexError("Попытка обратиться к несуществующей ссылке:",history["response"])

    # выполнить внутреннюю замену
    # - случайного эпизода
    if "chance" in history:
        replaceLinkEpisodes(history["chance"], linkEpisodes)

    # - шафла
    if 'shuffle' in history:
        replaceLinkEpisodes(history['shuffle'], linkEpisodes)

    # - теговой связки
    if 'bundle' in history:
        replaceLinkEpisodes(history['bundle'], linkEpisodes)

    # - эпизода с ивентом
    if "onTrue" in history or "onFalse" in history:
        if "onTrue" in history:
            replaceLinkEpisodes(history["onTrue"], linkEpisodes)
        if "onFalse" in history:
            replaceLinkEpisodes(history["onFalse"], linkEpisodes)


    temp = history
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
        print(colored("=", "yellow"),"Синтезирование " + printText + '...')

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
        if "chance" in n and not ("[chance" in n):
            n = n.replace("chance", "  chance")
            resultArr.append(n)
            continue

        # добавить пробел для "bundle" (для обработчика)
        if "bundle" in n and not ("[bundle" in n):
            n = n.replace("bundle", "  bundle")
            resultArr.append(n)
            continue

        # добавить пробел для "shuffle" (для обработчика)
        if "shuffle" in n and not ("[shuffle" in n):
            n = n.replace("shuffle", "  shuffle")
            resultArr.append(n)
            continue

        # если строка содержит в себе response, то добавить ключ "response" и обернуть блок в массив
        if '"' in n:
            n = n.replace('"', '- response: "', 1)
            resultArr.append(n)
            continue

    # соединить все строки в одно целое. в итоге у нас получится yaml
    yamlResult = "\n".join(resultArr)
    # print(yamlResult)

    # форматирование yaml => словарное-представление
    result = yaml.load(yamlResult, Loader=yaml.Loader)

    # форматирование ssd-format => словарное-представление для ссылочных эпизодов
    if transformLinkEpisodes and not (linkEpisodes is None):
        print(colored("=", "yellow"),"Синтезирование ссылочных эпизодов...")
        for key in linkEpisodes:
            linkEpisodes[key] = builder(linkEpisodes[key], linkEpisodes, False)

    # заменить ссылки в "response"ах в виде строк "{link}" на словари
    replaceLinkEpisodes(result, linkEpisodes)

    # print(result)

    # вернуть результат
    return result
