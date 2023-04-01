from threading import Timer

from .image_to_id import image_to_id, delete_id_from_yandex
from .get_image import get_image, get_image_2


def get_id(
        person: str,
        replica: str,
        values: list[int] | tuple[int, int, int, int],
        changes: list[int] | tuple[int, int, int, int],
        name: str
) -> str | None:
    image = get_image_2(
        person=person,  # имя
        replica=replica,  # его речь
        values=values,  # значение сейчас
        changes=changes,  # изменения по выбору
        name=name,  # имя правителя
    )
    # print(image)
    image_id = image_to_id(image)

    del_thread = Timer(5, delete_id_from_yandex, args=(image_id,))
    del_thread.start()

    return image_id
