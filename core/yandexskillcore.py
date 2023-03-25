from flask import Flask, request
from .notused.dialogsHandler import *
from termcolor import colored


# функция для удобного запуска фласка
def startServer(
    route: str = "/",  # роут, по которому будет приходить реквесты
    methods: list[str] = ["POST"],  # методы, принимаемые фласком
    host: str = "localhost",  # хост
    port: int = 8443,  # порт
    handler: callable = lambda data: print(
        "handler works!"
    ),  # хандлер, через который будут прогоняться запросы и который будет отдавать респонс
):

    # создать приложение фласка
    app = Flask(__name__)

    # установить кодировку
    app.config['JSON_AS_ASCII'] = False
    app.config['JSONIFY_MIMETYPE'] = 'application/json;charset=utf-8'

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
