from utils.dbHandler import *

conn = connect('root','root', 'Lord_of_the_Empire')

insertNewStat(conn, 'gggg')

print(type(getStat(conn,'gggg')))

increaseStat(conn, 'gggg', 100, 'aboba', 'abobik')

print(getStat(conn,'gggg'))
