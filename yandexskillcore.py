from flask import Flask, request
from termcolor import colored
from gameCore.builder import builder
from datetime import datetime
from utils.globalStorage import *
from utils.dbHandler import *
from utils.asyncHalper import *
import os
import threading
import time

# функция для удобного запуска фласка
def startServer(
    historyText: str,
    statsEnds: dict,
    linkEpisodes: dict,
    route: str = "/",
    methods: list[str] = ["POST"],
    host: str = "localhost",
    port: int = 2083,
    handler: callable = lambda data: print("handler works!"),
):

    # билдинг истории в словарное-представление
    print(colored("+", "green"), "Старт синтезирования")
    startTime = datetime.now()
    history = builder(historyText, linkEpisodes, "истории")

    # билдинг концовок
    for key in statsEnds:
        for kkey in statsEnds[key]:
            statsEnds[key][kkey] = builder(
                statsEnds[key][kkey],
                transformLinkEpisodes=False,
                printText="концовки: " + key + "-" + kkey,
            )

    endTime = datetime.now()

    print(
        colored("+", "green"),
        "Синтезирование завершено с кайфом за: " + str(endTime - startTime),
    )

    # записал историю
    setInGlobalStorage('history', history, saveLinks=True)
    # записать концовки
    setInGlobalStorage('statsEnds', statsEnds, saveLinks=True)

    # создать приложение фласка
    app = Flask(__name__)

    # записать приложение в глобальное хранилище
    setInGlobalStorage('app', app, saveLinks=True)

    # создать подключение к mariadb
    dbUser = os.environ.get('DB_USER')
    dbPassword = os.environ.get('DB_PASSWORD')
    dbName = os.environ.get('DB_NAME')
    cur = connect(dbUser, dbPassword, dbName)

    # записать курсор
    setInGlobalStorage('mariaDBconn', cur, saveLinks=True)

    # установить кодировку
    app.config["JSON_AS_ASCII"] = False
    app.config["JSONIFY_MIMETYPE"] = "application/json;charset=utf-8"

    # # запуск цикла для сохранений игр в БД
    # def saveGamesCycle(globalStorage):
    #     while True:
    #         globalStorage = copy.deepcopy(globalStorage)
    #         print('Сохранение игр...')
    #         count = saveGamesFromGlobalStorage(globalStorage) 
    #         print('Количество записанных игр:', count)
    #         # 600 секунд = 10 минут
    #         time.sleep(5)

    # doFuncAsAsync(saveGamesCycle, [globalStorage])

    # получить дату из полученного реквеста, прогнать ее через "handler" и вернуть запрос
    @app.route(route, methods=methods)
    def content():
        data = request.get_json()
        response = handler(data)
        return response

    # метод запуска сервера
    def start():
        print(colored("+", "green"), "Сервер запускается...")
        app.run(host=host, port=port)
        print(colored("-", "red"), "Остановка!")

    # запуск
    start()
