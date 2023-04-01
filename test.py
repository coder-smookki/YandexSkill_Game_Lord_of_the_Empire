from utils.dbHandler import *

conn = connect('root','root', 'Lord_of_the_Empire')

insertNewStat(conn, 'gggggg')

print(type(getStat(conn,'gggggg')))

increaseStat(conn, 'gggggg', 100, 'aboba', 'abobik')

print(getStat(conn,'gggggg'))
