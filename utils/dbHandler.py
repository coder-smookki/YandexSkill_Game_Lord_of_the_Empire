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

    createTable = """
    CREATE TABLE IF NOT EXISTS saves (
        userId VARCHAR(255) PRIMARY KEY,
        gameInfo TEXT
    );
    """

    # создать таблицу с сохранениями, если ее не существует
    cur.execute(createTable)

    # Вернуть соединение
    return conn


def selectGameInfo(conn, userId):
    cur = conn.cursor()
    cur.execute("SELECT gameInfo FROM saves WHERE userId=%s", [userId])
    gameInfo = cur['gameInfo']
    for (gameInfo) in cur:
    # print(f"First Name: {first_name}, Last Name: {last_name}")
        return gameInfo

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
