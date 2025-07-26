from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.utils import markdown

from keyboards.city_keyboard import city_keyboard
from routers.weather.states import Weather
from .state_handlers import router as state_router


router = Router(name=__name__)
router.include_router(state_router)


@router.message(Command("weather"), default_state)
async def handle_weather(message: Message, state: FSMContext):
    await state.set_state(Weather.city)
    await message.answer("Выберите город или введите, если город не указан в списке", reply_markup=city_keyboard())


@router.message(Command("cancel"), Weather())
async def handle_cancel(message: Message, state: FSMContext):
    current_state = await state.get_state()
    await state.clear()
    text = f"Вы закончили {current_state}, что начать сначала нажмите {markdown.hcode("/weather")}"
    await message.answer(text=text)
