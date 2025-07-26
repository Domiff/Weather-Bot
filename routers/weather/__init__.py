__all__ = "router",

from aiogram import Router

from .commands_handlers import router as handlers_router


router = Router(name=__name__)
router.include_router(handlers_router)
