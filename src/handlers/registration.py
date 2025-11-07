from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery

from database.queries.user import UserQueries
from src.keyboards import registration as keyboard_reg
from src.handlers.utils import send_message as send_msg
from src.handlers.utils.language import get_language

register_router = Router()

class Registration_state(StatesGroup):
    name = State()
    age = State()
    weight = State()
    desired_weight = State()
    height = State()
    undesirable_products = State()
    preferred_products = State()

async def test(msg: Message):
    await UserQueries.new_user_id(user_id=msg.from_user.id)
    msg_text = "🇷🇺\n"
    msg_text += "Ого! Кажется, мы с тобой ещё не знакомы... Исправим это?😉\n"
    msg_text += "Меня зовут Бодя-лис и я профессиональный помощник в коррекции"
    msg_text += " веса 🦊 Подскажи, на каком языке я могу с тобой общаться?"
    msg_text += "\n\n🇺🇸\n"
    msg_text += "Wow! It seems we haven't met yet... Shall we fix that?😉\n"
    msg_text += "My name is Bodya-fox and I am a professional weight loss "
    msg_text += "coach 🦊 Please tell me which language I can use to "
    msg_text += "communicate with you"
    await send_msg.from_msg(text=msg_text, 
                            msg=msg, 
                            reply_markup=keyboard_reg.language_choice())

@register_router.callback_query(F.data.startswith("lang_"))
async def language_add(call: CallbackQuery, state: FSMContext):
    language = call.data.split("_")[1]
    await state.update_data(language = language)
    await UserQueries.edit_lang(user_id=call.from_user.id, language=language)
    await call.answer()
    if language == "russian":
        msg_text = "Отлично! Как я могу к тебе обращаться? 😊"

    elif language == "english":
        msg_text = "Great! How can I address you? 😊"

    await send_msg.from_call(text=msg_text, call=call)
    await state.set_state(Registration_state.name)

@register_router.message(Registration_state.name)
async def name_add(msg: Message, state: FSMContext):
    #FUNCTION NEED EDIT, msg_text with date of birth
    await UserQueries.edit_name(user_id=msg.from_user.id, name=msg.text)
    language = await get_language(state=state)
    if language == "russian":
        msg_text = f"Приятно познакомиться, {msg.text}!\nУкажите Вашу дату рождения. "
        msg_text += "Данная информация нужна для более корректного составления "
        msg_text += "программы питания, достаточно указать возраст без даты рождения😊"
    elif language == "english":
        msg_text = f"Nice to meet you, {msg.text}!\nPlease indicate your date of birth. "
        msg_text += "This information is needed to create a more accurate "
        msg_text += "nutrition plan. Please indicate your age without your date of birth😊"
    await send_msg.from_msg(msg_text, msg=msg)
    await state.set_state(Registration_state.age)