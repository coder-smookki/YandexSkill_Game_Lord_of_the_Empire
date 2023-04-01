from utils.dbHandler import *

conn = connect('root','root', 'Lord_of_the_Empire')

insertNewStat(conn, 'ggggg')

print(type(getStat(conn,'ggggg')))

increaseStat(conn, 'ggggg', 100, 'aboba', 'abobik')

print(getStat(conn,'ggggg'))
