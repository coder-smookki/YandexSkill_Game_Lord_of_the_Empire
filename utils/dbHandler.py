import mariadb
import json
from utils.globalStorage import removeFromGlobalStorage

def connect(user,password, databaseName):
    # Подключиться к MariaDB
    try:
        conn = mariadb.connect(
            user=user,
            password=password,
            host="localhost",
            port=3306,
            database=databaseName

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

    # Вернуть курсор
    return cur

def selectGameInfo(cur, userId):
    gameInfo = cur.execute("SELECT gameInfo FROM saves WHERE userId=%s", [userId])
    return gameInfo 

def updateSave(cur, userId, save):
    sql = """
    INSERT INTO saves (userId, gameInfo)
    VALUES (%s, %s)
    """
    #ON DUPLICATE KEY UPDATE gameInfo = %s
    save = json.dumps(save, ensure_ascii=False)

    result = cur.execute(sql, [userId, save])
    print('userId db',userId)
    print('save db',save)
    print('execute db:',result)

def removeSave(cur, userId):
    sql = """
    DELETE FROM saves WHERE userId=%s;
    """
    cur.execute(sql, [userId])

def saveGamesFromGlobalStorage(globalStorage):
    count = 0
    cur = globalStorage['mariaDBcur']
    for key in globalStorage:
        if key[:5] == 'game_':
            updateSave(cur, key[5:], globalStorage[key])
            removeFromGlobalStorage(key)
            count += 1
    
    return count
    