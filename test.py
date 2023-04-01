from utils.dbHandler import *

conn = connect('root','root', 'Lord_of_the_Empire')

insertNewStat(conn, 'ggg')

print(getStat(conn,'ggg'))

increaseStat(conn, 'ggg', 100, 'aboba', 'abobik')

print(getStat(conn,'ggg'))
