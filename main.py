from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters import Command
import dock
from aiogram import Bot, Dispatcher, executor, types


bot = Bot (token=dock.bott)
dp = Dispatcher(bot)

async def on_startup(_):
    print("on start")

kb0 = InlineKeyboardMarkup(row_width=1)
kb1 = InlineKeyboardButton(text="Музыка из аниме", callback_data="kb1")
kb2 = InlineKeyboardButton(text="Информация об аниме", callback_data="kb2")
kb3 = InlineKeyboardButton(text="", callback_data="kb3")

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):


