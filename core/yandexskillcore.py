from flask import Flask, request
from .notused.dialogsHandler import *
from termcolor import colored
from core.builder import builder
from datetime import datetime


# функция для удобного запуска фласка
def startServer(
    historyText: str,
    statsEnds: dict,
    linkEpisodes: dict,
    route: str = "/",
    methods: list[str] = ["POST"],
    host: str = "localhost",
    port: int = 8443,
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

    # создать приложение фласка
    app = Flask(__name__)

    # установить кодировку
    app.config["JSON_AS_ASCII"] = False
    app.config["JSONIFY_MIMETYPE"] = "application/json;charset=utf-8"

    # получить дату из полученного реквеста, прогнать ее через "handler" и вернуть запрос
    @app.route(route, methods=methods)
    def content():
        data = request.get_json()
        print(data)
        response = handler(data, history, statsEnds)
        return response

    # метод запуска сервера
    def start():
        print(colored("+", "green"), "Сервер запускается...")
        app.run(host=host, port=port)
        print(colored("-", "red"), "Остановка!")

    # запуск
    start()
