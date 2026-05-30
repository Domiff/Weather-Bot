from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from core.client import weather_client
from weather.states import Weather

router = Router(name=__name__)


@router.message(Weather.units, F.text)
async def handle_metrics(message: Message, state: FSMContext):
    data = await state.update_data(units=message.text)
    await state.clear()
    try:
        raw = await weather_client.fetch(city=data["city"], units=data["units"])
        text = weather_client.format(raw)
    except Exception:
        text = "Не удалось получить погоду. Проверьте название города."
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())


@router.message(Weather.units)
async def handle_wrong_metrics(message: Message):
    await message.answer("Выберите из предложенных вариантов или напишите текстом")
