from utils.dbHandler import *

conn = connect('root','root', 'Lord_of_the_Empire')

insertNewStat(conn, 'someUserId')

print(getStat(conn,'someUserId'))

increaseStat(conn, 'someUserId', 100, 'aboba', 'abobik')

print(getStat(conn,'someUserId'))