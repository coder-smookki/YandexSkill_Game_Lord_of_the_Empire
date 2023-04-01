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
    for gameInfo in cur:
        # print(f"First Name: {first_name}, Last Name: {last_name}")
        print("gameInfo db", gameInfo[0])
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


def getStat(conn, userId, statName="all"):
    print("getStat: " + statName)
    cur = conn.cursor()
    if statName == "all":
        cur.execute("SELECT * FROM stats WHERE userId=%s", [userId])
        for (result) in cur:
            # print(result)
            returnResult = {}
            returnResult["deaths"] = result[1]
            returnResult["openEnds"] = json.loads(result[2])
            returnResult["meetedCharacters"] = json.loads(result[3])
            # print(result)
            print('returnResult',returnResult)
            return returnResult
    else:
        cur.execute("SELECT " + statName + " FROM stats WHERE userId=%s", [userId])
        # gameInfo = cur['gameInfo']
        for (result) in cur:
            if statName != "deaths":
                return json.loads(result[0])
            return result[0]


def insertNewStat(conn, userId):
    print("insert new stat")
    cur = conn.cursor()
    sql = "INSERT INTO stats (userId,deaths,openEnds, meetedCharacters) VALUES (%s, %s,%s,%s)"

    deaths = 0
    openEnds = json.dumps([], ensure_ascii=False)
    meetedCharacters = json.dumps([], ensure_ascii=False)

    cur.execute(sql, [userId, deaths, openEnds, meetedCharacters])

    conn.commit()


def removeRepeatsFromList(l):
    print('removeRepeats',l)
    result = [*set(l)]
    print('removeRepeatsResult',result)
    return result


def setStat(conn, userId, deaths=0, openEnds=[], meetedCharacters=[]):
    cur = conn.cursor()
    sql = """ 
    UPDATE stats
    SET deaths = %s, openEnds = %s, meetedCharacters = %s
    WHERE userId = %s;
    """
    cur.execute(sql, [deaths, openEnds, meetedCharacters, userId])
    conn.commit()

def increaseStat(conn, userId, deaths=0, openEnds=None, meetedCharacters=None):
    getted = getStat(conn, userId)
    
    nowDeaths = getted["deaths"] + deaths
    nowOpenEnds = getted["openEnds"]
    nowMeetedCharacters = getted["meetedCharacters"]

    print('getted',type(nowOpenEnds))

    if not openEnds is None:
        nowOpenEnds.append(openEnds)
        nowOpenEnds = removeRepeatsFromList(nowOpenEnds)
    
    if not meetedCharacters is None:
        nowMeetedCharacters.append(meetedCharacters)
        nowMeetedCharacters = removeRepeatsFromList(nowMeetedCharacters)
    
    setStat(conn, userId, nowDeaths, nowOpenEnds, nowMeetedCharacters)

def reduceStat(conn, userId, deaths=0, openEnds=None, meetedCharacters=None):
    getted = getStat(conn, userId)
    
    nowDeaths = getted["deaths"] - deaths
    nowOpenEnds = getted["openEnds"]
    nowMeetedCharacters = getted["meetedCharacters"]

    if not openEnds is None:
        nowOpenEnds.remove(openEnds)
    
    if not meetedCharacters is None:
        nowMeetedCharacters.remove(openEnds)
    
    setStat(conn, userId, nowDeaths, nowOpenEnds, nowMeetedCharacters)



# deaths int(11)
# openEnds smallint(6)
# meetedCharacters smallint(6)
