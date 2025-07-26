from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.utils import markdown


router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: Message):
    text = markdown.text(
        f"Привет {message.from_user.full_name}!\nЯ — {markdown.hitalic("WeatherBot")} 🌤.\n"
        "Я умею показывать текущую погоду для любого города.\n"
        f"Начнём? Просто введи {markdown.hcode("/weather")}, "
        f"или набери {markdown.hcode("/help")}, если что-то непонятно."
    )
    await message.answer(text=text)


@router.message(Command("help"))
async def handle_help(message: Message):
    text = markdown.text(
        "🆘 Помощь — вот что я могу:\n"
        f"• {markdown.hcode("/start")} — начни диалог со мной и узнай, как я работаю\n"
        f"• {markdown.hcode("/weather")} — узнать текущую погоду и я попрошу название города\n"
        # f"• {markdown.hcode("/settings")} — настроить язык, единицы измерения и формат времени\n"
        f"• {markdown.hcode("/cancel")} — отменить текущий ввод или запрос\n"
        # f"• {markdown.hcode("/info")} — узнать информацию обо мне"
    )
    await message.answer(text=text)
