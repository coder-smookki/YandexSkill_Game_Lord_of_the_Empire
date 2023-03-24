# Нами был создан специальный формат записи эпизодов. Он называться ssd-format
# Для превращения ssd-format в python-словарь, промежуточно ssd-format превращается в формат yaml,
# из которого уже и происходит трансформация в словарь при помощи библиотеки pyyaml
import yaml

# заменить все ссылочные эпизоды
def replaceLinkEpisodes(history, linkEpisodes):
    if type(history) == list:
        for episode in history:
            replaceLinkEpisodes(episode,linkEpisodes)
    
    elif '{' in history['response']:
        key = history['response'][1:-1]
        if key in linkEpisodes:
            history['response'] = linkEpisodes[key]
        else: 
            raise IndexError('Попытка обратиться к несуществующей ссылке')
    elif 'onTrue' in history:
        replaceLinkEpisodes(history['onTrue'],linkEpisodes)
    if 'onFalse' in history:
        replaceLinkEpisodes(history['onFalse'],linkEpisodes)

    return history


# трансформировать ssd-format в словарное представление 
def builder(q: str, linkEpisodes:dict = None):
    # заменить одинарные кавычки на двойные
    q = q.replace("'", '"')

    # поделить на строки для дальнейшей обработки
    arr = q.split("\n")
    
    # форматирование ssd-format => yaml
    resultArr = [] # список, куда будут записываться уже отформатированные строки
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

        # если строка содержит в себе response, то добавить ключ "response" и обернуть блок в массив
        if '"' in n:
            n = n.replace('"', '- response: "', 1)
            resultArr.append(n)
            continue

    # соединить все строки в одно целое. в итоге у нас получился yaml
    yamlResult = "\n".join(resultArr)

    # трансформировать yaml в словарное представление
    result = yaml.load(yamlResult, Loader=yaml.Loader)

    if not (linkEpisodes is None):
        # трансформировать ssd-format в словарное представление в ссылочных эпизодах
        for key in linkEpisodes:
            linkEpisodes[key] = builder(linkEpisodes[key])
        result = replaceLinkEpisodes(result, linkEpisodes)
    return result
