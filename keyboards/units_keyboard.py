from aiogram.utils.keyboard import ReplyKeyboardBuilder


def units_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="C")
    builder.button(text="F")
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)
