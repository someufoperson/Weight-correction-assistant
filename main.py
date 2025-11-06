from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from src.handlers.user import user_router
from database.database import async_main
from log_config import logger

import asyncio

from config import settings


async def main():
    """
    async_main() it's create table from Base.metadata
    """
    await async_main()
    bot = Bot(token=settings.TOKEN_bot, 
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(router=user_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        logger.info(msg="Try start bot")
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.warning(msg="The script was stopped by pressing ctrl+c")
    except Exception as e:
        logger.error(msg=e)