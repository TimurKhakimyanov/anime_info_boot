from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import CallbackQuery

from aiogram.dispatcher.filters import Command
import dock
from aiogram import Bot, Dispatcher, executor, types
from parse_by_kh import get_pic, get_url
import os

bot = Bot (token=dock.token)
dp = Dispatcher(bot)

async def on_startup(_):
    print("on start")

bt1 = KeyboardButton("Музыка из аниме")
bt2 = KeyboardButton("Информация об аниме")

keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(bt1, bt2)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Привет, чем займемся?", reply_markup=keyboard)

# Обработчик нажатия кнопок
@dp.message_handler(lambda message: message.text in ["Музыка из аниме", "Информация об аниме"])
async def process_button_click(message: types.Message):
    a = types.ReplyKeyboardRemove()
    global butt
    match message.text:
        case "Музыка из аниме":
            await bot.send_message(message.chat.id, text="Введи название для получение музыки из аниме", reply_markup=a)
            butt = "music"
        case "Информация об аниме":
            await bot.send_message(message.chat.id, text="Введи название для получения информации об аниме", reply_markup=a)
            butt = "info"
    

@dp.message_handler(content_types=types.ContentType.TEXT)
async def handle_text_message(message: types.Message):
    global butt
    txt = message.text
    bb = "Описание" 
    try:
        match butt:
            case "music":
                await bot.send_message(message.chat.id, text= butt)
            case "info":
                urll = get_url(txt)
                url2 = urll["url"]
                get_pic(url2)
                stt = urll["stat"]
                dcc = urll["desc"]
                with open("123.jpg", 'rb') as photo:
                    await bot.send_photo(message.chat.id, photo=photo, caption=f"Ссылка: {url2}")
                    photo.close()
                # await bot.send_message(message.chat.id, text= urll["desc"])
                # await bot.send_message(message.chat.id, text= urll["tags"])
                # await bot.send_message(message.chat.id, text= f"Статус: {stt}")
                os.remove("123.jpg")
            
    except NameError:
        await bot.send_message(message.chat.id, text= "Выберите действие")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
