from utils.dbHandler import *

conn = connect('root','root', 'Lord_of_the_Empire')

# insertNewStat(conn, 'ggggggggg')

print(type(getStat(conn,'ggggggggg')))

increaseStat(conn, 'ggggggggg', 100, 'aboba', 'abobik')

print(getStat(conn,'ggggggggg'))
