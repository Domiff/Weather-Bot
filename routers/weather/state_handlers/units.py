from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from routers.weather.states import Weather
from script import get_result

router = Router(name=__name__)


async def send_weather(message: Message, data: dict):
    text = get_result(city=data["city"], units=data["units"])
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())


@router.message(Weather.units, F.text)
async def handle_metrics(message: Message, state: FSMContext):
    data = await state.update_data(units=message.text)
    await state.clear()
    await send_weather(message, data)


@router.message(Weather.units)
async def handle_wrong_metrics(message: Message):
    text = "Выберите из предложенных вариантов и напишите текстом"
    await message.answer(text=text)
