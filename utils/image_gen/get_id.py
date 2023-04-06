import time
from threading import Timer

from .image_to_id import image_to_id, delete_image_anywhere
from .get_image import save_image


def get_id(
        person: str,
        replica: str,
        values: list[int] | tuple[int, int, int, int],
        name: str
) -> str | None:
    start = time.time()

    filename = save_image(
        person=person,  # имя
        replica=replica,  # его речь
        values=values,  # значение сейчас
        name=name,  # имя правителя
    )

    image_id = image_to_id(filename)

    Timer(5, delete_image_anywhere, args=(filename, image_id)).start()

    print(time.time() - start)

    return image_id
