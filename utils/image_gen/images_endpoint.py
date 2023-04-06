import flask
from pathlib import Path


images_path = Path(__file__).parent.absolute() / 'temp_images'
default_image = images_path / 'error404.png'
keepcharacters = (' ','.','_', '-')


def images_endpoint(filename: str):
    """
    Возвращает картинку по файлу
    """

    filename = "".join(c for c in filename if c.isalnum() or c in keepcharacters).strip()
    print(images_path, filename)
    return flask.send_from_directory(images_path, filename, mimetype='image/png')


def register_image_endpoint(app: flask.Flask):
    app.add_url_rule('/images/<filename>', view_func=images_endpoint)
