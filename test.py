from utils.dbHandler import *

conn = connect('root','root', 'Lord_of_the_Empire')

insertNewStat(conn, 'zxc')

print(getStat(conn,'zxc'))

increaseStat(conn, 'zxc', 100, 'aboba', 'abobik')

print(getStat(conn,'zxc'))