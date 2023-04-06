import os

import requests
from pathlib import Path

webhook_url = os.environ.get('URL')
port = os.environ.get('PORT')
oauth_key = os.environ.get('OAUTH_IMAGE_KEY')
skill_id = os.environ.get("SKILL_ID")
temp_images = Path(__file__).parent.absolute() / 'temp_images'


def image_to_id(filename: str) -> str:
    url = f'https://dialogs.yandex.net/api/v1/skills/{skill_id}/images/'
    image_url = f'https://{webhook_url}:{port}/images/{filename}'

    headers = {
        "Authorization": f'OAuth {oauth_key}',
        "Content-Type": "application/json"
    }
    data = {
        "url": image_url
    }
    yandex_response = requests.post(url, headers=headers, json=data)

    if not yandex_response:
        print(f'Возникла ошибка {yandex_response.status_code} "{yandex_response.text}"')
        return "997614/ca506e7918d405f24764"  # какая-то затычка

    image_id = yandex_response.json()["image"]["id"]

    return image_id


def delete_image_anywhere(filename: str, image_id: str):
    url = f'https://dialogs.yandex.net/api/v1/skills/{skill_id}/images/'

    headers = {
        "Authorization": f'OAuth {oauth_key}',
    }
    yandex_response = requests.delete(url + image_id, headers=headers)
    if not yandex_response:
        print(f'Не удалось удалить image {image_id}\n{yandex_response.text}')

    os.remove(temp_images / filename)
