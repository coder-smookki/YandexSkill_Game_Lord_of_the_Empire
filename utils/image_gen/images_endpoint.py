import os.path

import flask
from pathlib import Path


images_path = Path(__file__).parent.absolute() / 'temp_images'
default_image = images_path / 'error404.jpeg'
keepcharacters = (' ','.','_', '-')


def images_endpoint(filename: str):
    """
    Возвращает картинку по файлу
    """
    print('!' * 50)

    filename = "".join(c for c in filename if c.isalnum() or c in keepcharacters).strip()
    if os.path.exists(images_path / filename):
        return flask.send_from_directory(images_path, filename, mimetype='image/jpeg')
    return flask.send_from_directory(images_path, 'error404.jpeg', mimetype='image/jpeg')


def register_image_endpoint(app: flask.Flask):
    app.add_url_rule('/images/<filename>', view_func=images_endpoint, methods=['GET', 'POST'])
