from aiogram import Router

from weather.handlers import city, commands, units

router = Router(name=__name__)
router.include_routers(commands.router, city.router, units.router)
