from flask import Flask, request
from termcolor import colored
from gameCore.builder import builder
from datetime import datetime
from utils.globalStorage import *
from utils.dbHandler import *
from utils.asyncHalper import *
import os

from utils.image_gen.images_endpoint import register_image_endpoint


# функция для удобного запуска фласка
def startServer(
        startHistoryText: str,
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
    startHistory = builder(startHistoryText, linkEpisodes, "стартовой истории")
    history = builder(historyText, linkEpisodes, "истории", False)

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

    # записать стартовую историю
    setInGlobalStorage('startHistory', startHistory, saveLinks=True)
    # записать историю
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
    conn = connect(dbUser, dbPassword, dbName)

    # записать подключение
    setInGlobalStorage('mariaDBconn', conn, saveLinks=True)

    # установить кодировку
    app.config["JSON_AS_ASCII"] = False
    app.config["JSONIFY_MIMETYPE"] = "application/json;charset=utf-8"

    # получить дату из полученного реквеста, прогнать ее через "handler" и вернуть запрос
    @app.route(route, methods=methods)
    def content():
        data = request.get_json()
        response = handler(data)
        return response

    # метод запуска сервера
    def start():
        print(colored("+", "green"), "Сервер запускается...")
        register_image_endpoint(app)
        app.run(host=host, port=port)
        print(colored("-", "red"), "Остановка!")

    # запуск
    start()
