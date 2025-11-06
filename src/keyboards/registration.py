from aiogram.types import (KeyboardButton, 
                           ReplyKeyboardMarkup, 
                           InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder

def language_choice():
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="Русский 🇷🇺", callback_data="lang_russian"),
                 InlineKeyboardButton(text="English 🇺🇸", callback_data="lang_english"))
    return keyboard.as_markup()