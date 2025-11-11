from datetime import date
from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery

from locales.locale_read import locale_read
from database.queries.user import UserQueries
from src.keyboards import registration as keyboard_reg
from src.handlers.utils import send_message as send_msg
from src.handlers.utils.language import get_language

register_router = Router()

class Registration_state(StatesGroup):
    name = State()
    date_of_birth = State()
    weight = State()
    desired_weight = State()
    height = State()
    undesirable_products = State()
    preferred_products = State()

async def start_register(msg: Message):
    await UserQueries.new_user_id(user_id=msg.from_user.id)
    msg_text = locale_read(language="", func_name="start_register")
    await send_msg.from_msg(text=msg_text, 
                            msg=msg, 
                            reply_markup=keyboard_reg.language_choice())

@register_router.callback_query(F.data.startswith("lang_"))
async def language_add(call: CallbackQuery, state: FSMContext):
    language = call.data.split("_")[1]
    await state.update_data(language = language)
    await UserQueries.edit_lang(user_id=call.from_user.id, language=language)
    await call.answer()
    msg_text = locale_read(language=language, func_name=language_add.__name__)
    await send_msg.from_call(text=msg_text, call=call)
    await state.set_state(Registration_state.name)

@register_router.message(Registration_state.name)
async def name_add(msg: Message, state: FSMContext):
    await UserQueries.edit_name(user_id=msg.from_user.id, name=msg.text)
    language = await get_language(state=state)
    context = {"name": msg.text}
    msg_text = locale_read(language=language, 
                           func_name=name_add.__name__).format(**context)
    await send_msg.from_msg(msg_text, msg=msg)
    await state.set_state(Registration_state.date_of_birth)

@register_router.message(Registration_state.date_of_birth)
async def dob_add(msg: Message, state: FSMContext):
    """The function checks whether the user's text matches the date 
    in the required format dd.mm.yyyy. If it matches, it checks the user's 
    current age. If the user is under 18, it notifies them that the 
    functionality will be partially available. If the user is over 18 but 
    under 60, it simply greets them. If the user is over 60, it asks them to 
    consult their doctor about all the options offered by the bot"""
    try:
        day, mounth, year = msg.text.split(".")
    except Exception as e:
        print(e)
    d = date(int(year), int(mounth), int(day))
    print(d)