from utils.dbHandler import *

conn = connect('root','root', 'Lord_of_the_Empire')

insertNewStat(conn, 'gggggggg')

print(type(getStat(conn,'gggggggg')))

increaseStat(conn, 'gggggggg', 100, 'aboba', 'abobik')

print(getStat(conn,'gggggggg'))
