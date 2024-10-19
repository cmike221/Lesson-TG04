from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Привет!"), KeyboardButton(text="Пока!")],
], resize_keyboard=True)

inline_keyboard_links = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Показать больше", callback_data='more')],
])

test = ["Новости", "Музыка", "Видео"]


async def test_keyboard():
    keyboard = InlineKeyboardBuilder()
    for key in test:
        if key == "Новости":
            keyboard.add(InlineKeyboardButton(text=key, url='https://ria.ru/'))
        elif key == "Музыка":
            keyboard.add(InlineKeyboardButton(text=key, url='https://music.yandex.ru/home'))
        else:
            keyboard.add(InlineKeyboardButton(text=key, url='https://rutube.ru/'))

    return keyboard.adjust(3).as_markup()

options = ["Опция 1", "Опция 2"]


async def send_option():
    keyboard = InlineKeyboardBuilder()
    for option in options:
        if option == "Опция 1":
            keyboard.add(InlineKeyboardButton(text=option, callback_data='option1'))
        else:
            keyboard.add(InlineKeyboardButton(text=option, callback_data='option2'))

    return keyboard.adjust(2).as_markup()
