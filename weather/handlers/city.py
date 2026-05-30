from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from weather.keyboards import units_keyboard
from weather.states import Weather


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
    await message.answer("Введите город текстом")
