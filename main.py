import asyncio
import logging

from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.utils import markdown

from core.config import config
from weather import router as weather_router

bot = Bot(token=config["bot_token"], default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

base_router = Router()


@base_router.message(CommandStart())
async def handle_start(message: Message):
    text = markdown.text(
        f"Привет {message.from_user.full_name}!\nЯ — {markdown.hitalic('WeatherBot')} 🌤.\n"
        "Я умею показывать текущую погоду для любого города.\n"
        f"Начнём? Просто введи {markdown.hcode('/weather')}, "
        f"или набери {markdown.hcode('/help')}, если что-то непонятно."
    )
    await message.answer(text=text)


@base_router.message(Command("help"))
async def handle_help(message: Message):
    text = markdown.text(
        "🆘 Помощь — вот что я могу:\n"
        f"• {markdown.hcode('/start')} — начни диалог со мной и узнай, как я работаю\n"
        f"• {markdown.hcode('/weather')} — узнать текущую погоду и я попрошу название города\n"
        f"• {markdown.hcode('/cancel')} — отменить текущий ввод или запрос\n"
    )
    await message.answer(text=text)


dp.include_routers(base_router, weather_router)


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
