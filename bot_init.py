from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config import settings

def bot_with_default() -> Bot:
    bot = Bot(token=settings.TOKEN_bot,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    return bot