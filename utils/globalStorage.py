import copy

globalStorage = {}


def setInGlobalStorage(key, data, overwrite=False, saveLinks=False):
    if key in globalStorage and not overwrite:
        raise ValueError(
            'Global storage already have field with key ' + key + '.\nUse overwrite=True to allow overwrite')
    if saveLinks:
        globalStorage[key] = data
    else:
        newData = copy.deepcopy(data)
        globalStorage[key] = newData


def removeFromGlobalStorage(key):
    del globalStorage[key]
