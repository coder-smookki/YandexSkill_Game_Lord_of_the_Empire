from utils.triggerHelper import isInCommandOr
import re

a = ['zxc', 'vbn', re.compile('[A-Za-zа-яА-Я]')]

event = {
    'request': {
        'command': 'а'
    }
}

print(
    isInCommandOr(event, a)
)