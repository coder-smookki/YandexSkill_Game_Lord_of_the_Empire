import os

import flask
from pathlib import Path


host = "0.0.0.0"
images_path = Path(__file__).parent.absolute() / 'temp_images'
default_image = images_path / 'error404.png'
keepcharacters = (' ','.','_', '-')


def images_endpoint(filename: str):
    """
    Возвращает картинку по файлу
    """

    filename = "".join(c for c in filename if c.isalnum() or c in keepcharacters).strip()
    return flask.send_from_directory(images_path, filename, mimetype='image/png')


def register_image_endpoint():
    local_app = flask.Flask(__name__)
    local_app.add_url_rule('/images/<filename>', view_func=images_endpoint)
    local_app.run(host=host, port=443)
