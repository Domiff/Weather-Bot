from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from keyboards.units_keyboard import units_keyboard
from routers.weather.states import Weather

router = Router(name=__name__)


@router.message(Weather.city, F.text)
async def handle_city(message: Message, state: FSMContext):
    await state.update_data(city=message.text)
    await state.set_state(Weather.units)
    text = (
        "Прежде чем показать прогноз 🌦, уточни несколько настроек:\n"
        "🌡 Единицы измерения:\n"
        "- °C (метрика)\n"
        "- °F (имперская)\n"
        "Напиши «C» или «F»"
    )
    await message.answer(text=text, reply_markup=units_keyboard())


@router.message(Weather.city)
async def handle_wrong_city(message: Message):
    text = "Введите город текстом"
    await message.answer(text=text)
