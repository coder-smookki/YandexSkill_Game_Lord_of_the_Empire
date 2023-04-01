from utils.dbHandler import *

conn = connect('root','root', 'Lord_of_the_Empire')

print(getStat(conn, 'someUserId', 'deaths'))
increaseStat(conn,'someUserId', deaths=1)
print(getStat(conn, 'someUserId', 'deaths'))