from utils.dbHandler import *

conn = connect('root','root', 'Lord_of_the_Empire')

insertNewStat(conn, 'ggggggg')

print(type(getStat(conn,'ggggggg')))

increaseStat(conn, 'ggggggg', 100, 'aboba', 'abobik')

print(getStat(conn,'ggggggg'))
