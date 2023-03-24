# >>> moduleNames = ['sys', 'os', 're', 'unittest']
# >>> moduleNames
# ['sys', 'os', 're', 'unittest']
# >>> modules = map(__import__, moduleNames)
from flask import Flask, request
from .dialogsHandler import *


def startServer(
    route: str = "/",
    methods: list[str] = ["POST"],
    host: str = "localhost",
    port: int = 8443,
    handler: callable = lambda data: print("handler works!"),
):
    app = Flask(__name__)

    @app.route(route, methods=methods)
    def content():
        data = request.get_json()
        response = handler(data)
        return response

    def start():
        print("Server starting...")
        app.run(host=host, port=port)
        print("Shutdown!")

    start()
