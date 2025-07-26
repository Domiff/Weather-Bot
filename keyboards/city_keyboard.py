from aiogram.utils.keyboard import ReplyKeyboardBuilder


def city_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Москва")
    builder.button(text="Ломоносов")
    builder.button(text="Санкт Петербург")
    builder.button(text="Воронеж")
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)
