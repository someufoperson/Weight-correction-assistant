from aiogram import Dispatcher

from src.handlers.user import user_router
from src.handlers.registration import register_router
from database.database import async_main
from log_config import logger
from bot_init import bot_with_default

import asyncio

bot = bot_with_default()

async def main():
    """
    async_main() it's create table from Base.metadata
    """
    await async_main()
    dp = Dispatcher()
    dp.include_routers(user_router, register_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        logger.info(msg="Try start bot")
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.warning(msg="The script was stopped by pressing ctrl+c")
    except Exception as e:
        logger.error(msg=e)