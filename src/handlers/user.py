from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State

from database.queries.user import UserQueries
from src.handlers import registration

user_router = Router()

@user_router.message(Command('start'))
async def start(msg: Message):
    user = await UserQueries.is_exitsts(msg.from_user.id)
    if not user:
        await registration.start_register(msg)
    elif user:
        ...