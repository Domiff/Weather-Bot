from aiogram.utils.keyboard import ReplyKeyboardBuilder


def city_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Москва")
    builder.button(text="Воронеж")
    builder.button(text="Санкт Петербург")
    builder.button(text="Казань")
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


def units_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="C")
    builder.button(text="F")
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)
