# import json

# a = {
#     "posEpisode": [0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0],  "maxPosEpisode": [1],
#     "pastPosEpisode": None,
#     "choice": "none",
#     "pastHasEvent": None,
#     "stats": {"church": 50, "army": 50, "nation": 50, "coffers": 50},
#     "notAppliedStats": {
#         "true": [0, 0, 0, 0],
#         "false": [0, 0, 0, 0],
#         "always": [0, 0, 0, 0],
#     },
# }


# js = json.dumps(a, separators=(',', ':'))
# import sys
# import json_minify

# compressed_data = json_minify.json_minify(js)
# print(compressed_data)
# print(sys.getsizeof(compressed_data) / 1024)

# import re 

# a = '[shuffle 2]'

# b = re.findall(r'\d+', a)[0]
# print(b)

import random

def getShuffleIndex(total:int, used:list):
    values = [x for x in range(1, total+1) if x not in used]

    for i in range(len(values)-1, 0, -1):
        j = random.randint(0, i)
        values[i], values[j] = values[j], values[i]

    result = values.pop()

    return result

print(getShuffleIndex(10, [1,3,5]))