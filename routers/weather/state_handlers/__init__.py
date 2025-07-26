__all__ = "router",

from aiogram import Router

from .city import router as city_router
from .units import router as metrics_router


router = Router(name=__name__)
router.include_routers(city_router, metrics_router)
