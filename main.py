from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

import asyncio

bot = Bot(token="", default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

async def main():
    dp.include_router(router="")
    await dp.start_polling(bot)

if __name__ == "__name__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Script exit...")