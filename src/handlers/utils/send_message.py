from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup
from bot_init import bot_with_default

bot = bot_with_default()

async def from_call(text: str, 
                    call: CallbackQuery,
                    reply_markup: InlineKeyboardMarkup = None):
    """Send message with trying edit callbackquery message"""
    try:
        await bot.edit_message_text(text=text, 
                                    chat_id=call.from_user.id, 
                                    message_id=call.message.message_id,
                                    reply_markup=reply_markup)
    except Exception as e:
        print(e)
        await bot.send_message(chat_id=call.from_user.id, 
                               text=text,
                               reply_markup=reply_markup)

async def from_msg(text: str, 
                    msg: Message, 
                    reply_markup: InlineKeyboardMarkup = None):
    """Send message with trying delete messages from bot and user"""
    try:
        await bot.delete_messages(chat_id=msg.from_user.id,
                                  message_ids=[msg.message_id, msg.message_id-1])
    except Exception as e:
        print(e)
    await bot.send_message(chat_id=msg.from_user.id, 
                           text=text,
                           reply_markup=reply_markup)