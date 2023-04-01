import mariadb
import json
from utils.globalStorage import removeFromGlobalStorage


def connect(user, password, databaseName):
    # Подключиться к MariaDB
    try:
        conn = mariadb.connect(
            user=user,
            password=password,
            host="localhost",
            port=3306,
            database=databaseName,
        )
    except mariadb.Error as e:
        raise mariadb.Error(f"Ошибка при подключении к MariaDB: {e}")

    # Получить курсор
    cur = conn.cursor()

    createSavesTable = """
    CREATE TABLE IF NOT EXISTS saves (
        userId VARCHAR(255) PRIMARY KEY,
        gameInfo TEXT
    );
    """

    createStatsTable = """
    CREATE TABLE IF NOT EXISTS stats (
        userId VARCHAR(255) PRIMARY KEY,
        deaths INT,
        openEnds TEXT,
        meetedCharacters TEXT
    );
    """

    # создать таблицу с сохранениями, если ее не существует
    cur.execute(createSavesTable)

    # создать таблицу со статистикой, если ее не существует
    cur.execute(createStatsTable)

    # Вернуть соединение
    return conn


def selectGameInfo(conn, userId):
    cur = conn.cursor()
    cur.execute("SELECT gameInfo FROM saves WHERE userId=%s", [userId])
    # gameInfo = cur['gameInfo']
    for (gameInfo) in cur:
    # print(f"First Name: {first_name}, Last Name: {last_name}")
        print('gameInfo db',gameInfo[0])
        return json.loads(gameInfo[0])

def updateSave(conn, userId, save):
    cur = conn.cursor()
    save = json.dumps(save, ensure_ascii=False)
    sql = "UPDATE saves SET gameInfo = %s WHERE userId = %s"
    # ON DUPLICATE KEY UPDATE gameInfo = %s

    result = cur.execute(sql, [save, userId])
    conn.commit()
    print("userId db", userId)
    print("save db", save)
    print("execute db:", result)


def insertSave(conn, userId, save):
    cur = conn.cursor()
    save = json.dumps(save, ensure_ascii=False)
    sql = "INSERT INTO saves (userId, gameInfo) VALUES (%s, %s)"

    # ON DUPLICATE KEY UPDATE gameInfo = %s

    result = cur.execute(sql, [userId, save])
    conn.commit()
    print("userId db", userId)
    print("save db", save)
    print("execute db:", result)

def removeSave(conn, userId):
    cur = conn.cursor()
    sql = """
    DELETE FROM saves WHERE userId=%s;
    """
    cur.execute(sql, [userId])
    conn.commit()

def getStat(conn, userId, statName='all'):
    cur = conn.cursor()
    if statName == 'all':
        cur.execute("SELECT * FROM stats WHERE userId=%s", [userId])
        for (result) in cur:
            returnResult = {}
            returnResult['deaths'] = result[1]
            returnResult['openEnds'] = result[2]
            returnResult['meetedCharacters'] = result[3]
            return returnResult
    else:
        cur.execute("SELECT " + statName + " FROM stats WHERE userId=%s", [userId])
        # gameInfo = cur['gameInfo']
        for (result) in cur:
            return result[0]

def increaseStat(conn, userId, deaths=0, openEnds=0, meetedCharacters=0):
    cur = conn.cursor()

    sql = """
    UPDATE stats
    SET deaths = deaths + %s, openEnds = openEnds + %s, meetedCharacters = meetedCharacters + %s
    WHERE userId = %s;
    """
    cur.execute(sql, [deaths, openEnds, meetedCharacters, userId])
    conn.commit()

def reduceStat(conn, userId, deaths=0, openEnds=0, meetedCharacters=0):
    cur = conn.cursor()
    sql = """
    UPDATE stats
    SET deaths = deaths - %s, openEnds = openEnds - %s, meetedCharacters = meetedCharacters - %s
    WHERE userId = %s;
    """
    cur.execute(sql, [deaths, openEnds, meetedCharacters, userId])
    conn.commit()

def setStat(conn, userId, deaths=0, openEnds=0, meetedCharacters=0):
    cur = conn.cursor()
    sql = """ 
    UPDATE stats
    SET deaths = %s, openEnds = %s, meetedCharacters = %s
    WHERE userId = %s;
    """
    cur.execute(sql, [deaths, openEnds, meetedCharacters, userId])
    conn.commit()

# deaths int(11)
# openEnds smallint(6)
# meetedCharacters smallint(6)