from aiogram import F, Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery

from config import settings
from database.queries.user import UserQueries
from src.keyboards import registration as keyboard_reg
from src.handlers.utils.send_message import send_message as send_msg

register_router = Router()
bot = Bot(token=settings.TOKEN_bot)

class Registration_state(StatesGroup):
    name = State()
    age = State()
    weight = State()
    desired_weight = State()
    height = State()
    undesirable_products = State()
    preferred_products = State()

#ToDo: Add state machine to handler and determine the order of questions

@register_router.message()
async def test(msg: Message):
    await bot.delete_message(chat_id=msg.from_user.id, message_id=msg.message_id)
    msg_text = "🇷🇺\n"
    msg_text += "Ого! Кажется, мы с тобой ещё не знакомы... Исправим это?😉\n"
    msg_text += "Меня зовут Бодя-лис и я профессиональный помощник в коррекции"
    msg_text += " веса 🦊 Подскажи, на каком языке я могу с тобой общаться?"
    msg_text += "\n\n🇺🇸\n"
    msg_text += "Wow! It seems we haven't met yet... Shall we fix that?😉\n"
    msg_text += "My name is Bodya-fox and I am a professional weight loss "
    msg_text += "coach 🦊 Please tell me which language I can use to "
    msg_text += "communicate with you"
    await msg.answer(text=msg_text, reply_markup=keyboard_reg.language_choice())

@register_router.callback_query(F.data.startswith("lang_"))
async def edit_message(call: CallbackQuery):
    await call.answer()
    if call.data == "lang_russian":
        msg_text = "Отлично! Как я могу к тебе обращаться? 😊"

    elif call.data == "lang_english":
        msg_text = "Great! How can I address you? 😊"

    await call.message.answer(text=msg_text)