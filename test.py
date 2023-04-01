from utils.dbHandler import *

conn = connect('root','root', 'Lord_of_the_Empire')

insertNewStat(conn, 'asd')

print(getStat(conn,'asd'))

increaseStat(conn, 'zxc', 100, 'aboba', 'abobik')

# print(getStat(conn,'zxc'))
