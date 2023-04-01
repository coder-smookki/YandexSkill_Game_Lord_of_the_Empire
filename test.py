from utils.dbHandler import *

conn = connect('root','root', 'Lord_of_the_Empire')

getStat(conn, 'someUserId', 'deaths') 