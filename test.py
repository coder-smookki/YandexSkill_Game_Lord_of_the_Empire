from utils.dbHandler import *


cur = connect('root', 'root', 'Lord_of_the_Empire')

print(selectGameInfo(cur, '12345'))