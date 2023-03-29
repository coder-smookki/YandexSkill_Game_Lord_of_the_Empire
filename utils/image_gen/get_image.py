import textwrap
from io import BytesIO

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# Всякий бред, который нужен по дефолтку
MAX_VALUE = 100
no_color = (255, 220, 130)  # FFDC82
ok_color = (247, 242, 181)
back_color = (192, 172, 98)
green = (0, 255, 0)

parent_path = Path(__file__).parent.absolute()
images_path = parent_path / 'images'
persons_path = images_path / 'persons'
font = ImageFont.truetype(str(parent_path / 'times.ttf'), 40)  # Размер шрифта крутить тут
green_arrow = Image.open(images_path / 'green_arrow.png', mode='r', formats=["PNG"])
red_arrow = Image.open(images_path / 'red_arrow.png', mode='r', formats=["PNG"])
default_image = Image.open(images_path / 'default_image.png', mode='r', formats=["PNG"])  # заглушка

persons = {
    "Маг-целитель Хрисанф": Image.open(persons_path / 'mag-celitel.png', mode='r', formats=["PNG"]),
    "Дух прошлого короля": Image.open(persons_path / "ghostking.png", mode='r', formats=["PNG"]),
    "Разведчик Кирилл": Image.open(persons_path / "razvedchik.png", mode='r', formats=["PNG"]),
    "Командир Родион": Image.open(persons_path / "rodion.png", mode='r', formats=["PNG"]),
    "Господин Авдей": Image.open(persons_path / "Avdey.png", mode='r', formats=["PNG"]),
    "Дочь царя": Image.open(persons_path / "princess.png", mode='r', formats=["PNG"]),
    "Кондрат": Image.open(persons_path / "desnica.png",  mode='r', formats=["PNG"]),
    "Дракон": Image.open(persons_path / "dragon.png", mode='r', formats=["PNG"]),
    "Король": Image.open(persons_path / "king.png", mode='r', formats=["PNG"]),
}


def get_image(
        *,
        background: str = 'light_background',
        person: str,
        replica: str,
        values: list[int] | tuple[int, int, int, int],
        changes: list[int] | tuple[int, int, int, int],
) -> bytes:
    """
    Генератор картинок две тысячи инатор

    :param background: Название файла с фоном
    :param person: Название файла с персонажем
    :param replica: Реплика персонажа
    :param values: Текущие значения фракции, в порядке Церковь, Народ, Армия, Казна
    :param changes: Плюс или минус куда, порядок тот же.
    :return:
    """

    # Открытие шаблона и создание изображения (макета), на которое сначала будут накладываться картинки
    background = Image.open(images_path / f'{background}.png', mode='r', formats=["PNG"])
    layout_width, layout_height = background.size
    layout = Image.new("RGBA", (layout_width, layout_height), back_color)

    # Открытие и наложение персонажа
    person = persons.get(person, default_image)
    person_width, person_height = person.size
    person_x, person_y = (layout_width - person_width) // 2, 0
    layout.paste(person, (person_x, person_y))

    # Определение области для фракций
    values_width, values_height = int(layout_width * 0.31), person_height

    # это 75 пикселей для наибольшего размера, отступ сверху для значка фракций и между ними по высоте
    step = round(round(person_height * 0.09) * 1.5)

    # Создание прямоугольников для фракций
    rects = [Image.new(
        "RGBA",
        (values_width // 2, values_height // 2 - step),
        ok_color
    )
        for _ in range(4)
    ]

    # Рисование нужных цветов
    for value, rect in zip(values, rects):
        r_draw = ImageDraw.Draw(rect)
        width, height = rect.size
        r_draw.rectangle((0, 0, rect.width, int(height * (MAX_VALUE - value) / MAX_VALUE)), no_color)

    # Цвет для того, чтобы не кринжевать с полосок при несовпадении пикселей
    draw = ImageDraw.Draw(layout)
    draw.rectangle((0, 0, values_width, values_height), no_color)

    # Наложение значений фракций на макет
    kostil = int((values_height / 100))  # Костыль, размером около 5 пикселей
    r1, r2, r3, r4 = rects
    layout.paste(r1, (0, step))
    layout.paste(r2, (values_width // 2, step))
    layout.paste(r3, (0, step + values_height // 2 - kostil))
    layout.paste(r4, (values_width // 2, step + values_height // 2 - kostil))

    # Наложение шаблона на макет, в этот момент картинка уже с персонажем и фракциями.
    layout.paste(background, (0, 0), background)

    # Наложение стрелочек на макет
    for i, change in enumerate(changes):
        if change > 0:
            arrow = green_arrow
        elif change < 0:
            arrow = red_arrow
        else:
            continue
        x = i % 2 * values_width // 2 + (values_width // 2 - arrow.width) // 2
        y = i // 2 * values_height // 2 + (step - arrow.height) // 2
        layout.paste(arrow, (x, y), arrow)

    # Наложение текста на шаблон (?)
    # replica_x, replica_y = layout_width * 0.7, layout_height * 0.05
    # for line in textwrap.wrap(replica, width=25):  # Ширину крутить тут, если текст вышел за границу, щас ~380 влезает
    #     draw.text((replica_x, replica_y), line, font=font, fill="#000000")
    #     replica_y += font.getbbox(line)[-1]

    # Итог
    img_byte_arr = BytesIO()
    layout.save(img_byte_arr, format='PNG')
    return img_byte_arr.getvalue()
