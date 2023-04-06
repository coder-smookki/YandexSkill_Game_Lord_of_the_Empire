import time

from dotenv import load_dotenv
load_dotenv()

# from utils.triggerHelper import isInCommandOr
from utils.image_gen.get_id import get_id
# import re



# a = ['zxc', 'vbn', re.compile('[A-Za-zа-яА-Я]')]

event = {
    'request': {
        'command': 'а'
    }
}

# print(
#     isInCommandOr(event, a)
# )

# times = []
# for i in range(100):
#     start = time.time()
#     print(get_id("Дракон", "123123", [0, 0, 0, 0], "Киря ку)"))
#     end = time.time()
#     times.append(end - start)
# print(sum(times) / len(times))
