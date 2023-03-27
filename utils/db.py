import mariadb



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
        userId VARCHAR(255),
        gameInfo JSON
    );
    """

    # создать таблицу с сохранениями, если ее не существует
    cur.execute(createTable)

    # Вернуть курсор
    return cur

def selectGameInfo(cur, userId):
    gameInfo = cur.execute("SELECT gameInfo FROM saves WHERE userId=?", (userId))
    return gameInfo 

def updateSave(cur, userId, save):
    pass


