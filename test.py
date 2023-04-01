from utils.dbHandler import *

conn = connect('root','root', 'Lord_of_the_Empire')

print(getStat(conn, 'someUserId', 'deaths'))
setStat(conn,'someUserId', deaths=15)
print(getStat(conn, 'someUserId', 'deaths'))