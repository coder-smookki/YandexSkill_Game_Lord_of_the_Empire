import textwrap
from io import BytesIO

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# Всякий бред, который нужен по дефолтку
MAX_VALUE = 100
no_color = (138, 124, 81)
ok_color = (249, 246, 195)
back_color = (192, 172, 98)
name_color = (249, 243, 190)
text_card_color = (254, 240, 193)
text_color = (60, 44, 23)

parent_path = Path(__file__).parent.absolute()
images_path = parent_path / 'images'
persons_path = images_path / 'persons'
name_font = ImageFont.truetype(str(parent_path / 'myraid.otf'), 63)  # Размер шрифта крутить тут
emoji_font = ImageFont.truetype(str(parent_path / 'emoji.ttf'), 50)  # Размер шрифта крутить тут
text_font = ImageFont.truetype(str(parent_path / 'blacker_sans_pro.woff'), 50)  # Размер шрифта крутить тут
green_arrow = Image.open(images_path / 'green_arrow.png', mode='r', formats=["PNG"])
red_arrow = Image.open(images_path / 'red_arrow.png', mode='r', formats=["PNG"])
default_image = Image.open(images_path / 'default_image.png', mode='r', formats=["PNG"])  # заглушка


persons = {
    "Кошка с вселившимся демоном": Image.open(persons_path / 'cat_demon600.png', mode='r', formats=["PNG"]),
    "Крестьянин Александр": Image.open(persons_path / "krestyanin_alexsandr600.png", mode='r', formats=["PNG"]),
    "Маг-целитель Хрисанф": Image.open(persons_path / 'mag-celitel600.png', mode='r', formats=["PNG"]),
    "Дух прошлого короля": Image.open(persons_path / "ghostking600.png", mode='r', formats=["PNG"]),
    "Крестьянин Иакинф": Image.open(persons_path / "krestyanin_iakinf600.png", mode='r', formats=["PNG"]),
    "Учёный Аквитанский": Image.open(persons_path / 'ucheniy600.png', mode='r', formats=["PNG"]),
    "Ионна Разумовская": Image.open(persons_path / 'elfie600.png', mode='r', formats=["PNG"]),
    "Разведчик Кирилл": Image.open(persons_path / "razvedchik600.png", mode='r', formats=["PNG"]),
    "Епископ Галактион": Image.open(persons_path / 'episkop600.png', mode='r', formats=["PNG"]),
    "Охотник Сильвестр": Image.open(persons_path / 'ohotnik600.png', mode='r', formats=["PNG"]),
    "Командир Родион": Image.open(persons_path / "rodion600.png", mode='r', formats=["PNG"]),
    "Господин Авдей": Image.open(persons_path / "Avdey600.png", mode='r', formats=["PNG"]),
    "Лучник Ираклий": Image.open(persons_path / 'luchnik600.png', mode='r', formats=["PNG"]),
    "Палач Никифор": Image.open(persons_path / "palach600.png", mode='r', formats=["PNG"]),
    "Советник Яков": Image.open(persons_path / "yakov600.png", mode='r', formats=["PNG"]),
    "Шут Радмир": Image.open(persons_path / "shit600.png", mode='r', formats=["PNG"]),
    "Дочь царя": Image.open(persons_path / "princess600.png", mode='r', formats=["PNG"]),
    "Кондрат": Image.open(persons_path / "desnica600.png", mode='r', formats=["PNG"]),
    "Дракон": Image.open(persons_path / "dragon600.png", mode='r', formats=["PNG"]),
    "Король": Image.open(persons_path / "king600.png", mode='r', formats=["PNG"]),
    "Демон": Image.open(persons_path / 'demon600.png', mode='r', formats=["PNG"]),
    "Кошка": Image.open(persons_path / 'cat600.png', mode='r', formats=["PNG"]),
}

backgrounds = {
    'light_background2': Image.open(images_path / f'light_background2.png', mode='r', formats=["PNG"]),
}


# Константы для второго генератора!!!
small_border = 44
big_border = 117.5
block = 600
fract_height = 220
fract_width = 300
step = 25
big_step = 35
black_line = 75


def get_image(
        *,
        person: str,
        replica: str,
        values: list[int] | tuple[int, int, int, int],
        name: str = ''
) -> bytes:
    """
    Генератор картинок три тысячи инатор (второй шаблон)

    :param person: Название файла с персонажем
    :param replica: Реплика персонажа
    :param values: Текущие значения фракции, в порядке Церковь, Народ, Армия, Казна
    :param name: Имя правителя.
    :return:
    """

    # Открытие шаблона и создание изображения (макета), на которое сначала будут накладываться картинки
    background = backgrounds['light_background2']
    layout_width, layout_height = background.size
    layout = Image.new("RGBA", (layout_width, layout_height), back_color)

    # Открытие и наложение персонажа
    person = get_person(person, replica)
    person_x, person_y = int(big_border * 2) + block, small_border
    layout.paste(person, (person_x, person_y))

    # Создание прямоугольников для фракций
    rects = [Image.new(
        "RGBA",
        (fract_width, fract_height),
        ok_color
    )
        for _ in range(4)
    ]

    # Рисование нужных цветов
    for value, rect in zip(values, rects):
        r_draw = ImageDraw.Draw(rect)
        width, height = rect.size
        r_draw.rectangle((0, 0, rect.width, int(height * (MAX_VALUE - value) / MAX_VALUE)), no_color)

    # Расположение прямоугольников сзади фракций
    r1, r2, r3, r4 = rects
    layout.paste(r1, (int(big_border), small_border + step))
    layout.paste(r2, (int(big_border) + fract_width, small_border + step))
    layout.paste(r3, (int(big_border), small_border + step + fract_height + big_step))
    layout.paste(r4, (int(big_border) + fract_width, small_border + step + fract_height + big_step))

    # Наложение шаблона на макет, в этот момент картинка уже с персонажем и фракциями.
    layout.paste(background, (0, 0), background)

    # Наложение имени
    draw = ImageDraw.Draw(layout)
    # name = 'Владыка ' + name  # Расскомент для приставки к имени
    bbox = name_font.getbbox(name)
    text_x = big_border + (block - bbox[2]) // 2
    draw.text((text_x, layout.height - big_border + 5), name, font=name_font, fill=name_color)  # игрек нарандомил

    # Наложение корон
    bbox = emoji_font.getbbox('👑')
    text_y = layout.height - small_border - black_line + (black_line - bbox[3]) // 2 - 3
    text_x = big_border + bbox[2] // 3
    draw.text((text_x, text_y), '👑', font=emoji_font, fill=name_color)
    text_x = big_border + block - bbox[2] - bbox[2] // 3
    draw.text((text_x, text_y), '👑', font=emoji_font, fill=name_color)

    # Итог
    img_byte_arr = BytesIO()
    layout.save(img_byte_arr, format='PNG')
    # layout.show()
    return img_byte_arr.getvalue()


def get_person(person: str | None, replica: str) -> Image:
    """
    Возвращает либо картинку с персонажем, либо текст на белом фоне.
    :param person: Имя персонажа, может быть None или "".
    :param replica: Текст, который будет на фоне, если персонажа нет.
    """

    if person:
        return persons.get(person, default_image)

    # Создание фона
    layout = Image.new("RGBA", (block, block), text_card_color)
    draw = ImageDraw.Draw(layout)

    # Подготовка линий текста
    lines = textwrap.wrap(replica.strip().strip('.,*'), width=20)  # Строки текста
    y_delta = max([text_font.getbbox(line)[3] for line in lines])  # Расстояние между строками
    total_height = y_delta * len(lines)  # Общая высота текста
    text_y = (block - total_height) // 2  # Стартовый игрек

    # Нанесение строк
    for line in lines:
        bbox = text_font.getbbox(line)
        draw.text(((block - bbox[2]) // 2, text_y), line, font=text_font, fill=text_color)
        text_y += y_delta

    return layout


# get_image(
#     person='',
#     replica='*Призрак тоскливо смотрит на вас и исчезает. Вы входите в тронный зал.*',
#     values=[50, 40, 30, 20],
#     name='Кириллка)'
# )
