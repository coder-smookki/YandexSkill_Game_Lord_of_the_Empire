import os

import requests


oauth_key = os.environ.get('OAUTH_IMAGE_KEY')
skill_id = os.environ.get("SKILL_ID")
url = f'https://dialogs.yandex.net/api/v1/skills/{skill_id}/images/'


def image_to_id(image: bytes) -> str | None:
    headers = {
        "Authorization": f'OAuth {oauth_key}',
    }
    yandex_response = requests.post(
        url,
        headers=headers,
        files={'file': image}
    )

    if yandex_response.status_code == 429:  # Обработка момента, когда занята вся память навыка (около 2к картинок)
        raise RuntimeError("Киря, бачок потик, места нема!!! КАРТИНОК БОЛЬШЕ СТА МЕГАБАЙТ")

    if not yandex_response:
        print(f'Возникла ошибка {yandex_response.status_code} "{yandex_response.text}"')
        return None

    image_id = yandex_response.json()["image"]["id"]

    return image_id


def delete_id_from_yandex(image_id: str):
    headers = {
        "Authorization": f'OAuth {oauth_key}',
    }
    yandex_response = requests.delete(url + image_id, headers=headers)
    if not yandex_response:
        print(f'Не удалось удалить image {image_id}\n{yandex_response.text}')
