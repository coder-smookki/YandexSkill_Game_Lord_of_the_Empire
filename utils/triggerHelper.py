# есть стейт или нет
def haveState(event, state):
    return 'state' in event and state in event['state']['session']


# есть глобальный стейт или нет
def haveGlobalState(event, state):
    return 'state' in event and 'user' in event['state'] and state in event['state']['user']


# является ли сессия новой
def isNewSession(event):
    return event['session']['new'] is True


# является ли хоть один элемент массива подстрокой пришедшей команды
def isInCommandOr(event, arr):
    command = event["request"]['command']
    for elem in arr:
        if elem in command:
            return True
    return False


# являются ли все элементы массива подстроками пришедшей команды
def isInCommandAnd(event, arr):
    command = event["request"]['command']
    for elem in arr:
        if not (elem in command):
            return False
    return True

# есть ли в бренчах контекст "context" 
def isInContext(event, context):
    if not 'branch' in event['state']['session']:
        return False

    if isinstance(context, list):
        for elem in context:
            if elem in event['state']['session']["branch"]:
                return True
        return False
    return context in event['state']['session']["branch"]

# является ли последний контекст "context" 
def isInLastContext(event, context):
    if not 'branch' in event['state']['session']:
        return False

    if isinstance(context, list):
        for elem in context:
            if elem == event['state']['session']["branch"][-1]:
                return True
        return False
    return context == event['state']['session']["branch"][-1]