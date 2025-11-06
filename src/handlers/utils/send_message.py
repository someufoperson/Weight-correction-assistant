from aiogram import Bot
from aiogram.types import Message
from config import settings

bot = Bot(token=settings.TOKEN_bot)

#Need moooooore tests
async def send_message(text: str, chat_id: int, message_id: int):
    print(message_id)
    try:
        await bot.edit_message_text(text=text, chat_id=chat_id, message_id=message_id+1)
    except Exception as e:
        print(e)