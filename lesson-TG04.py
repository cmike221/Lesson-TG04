import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
import random

from gtts import gTTS
import os

from config import TOKEN
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.callback_query(F.data == 'news')
async def news(callback: CallbackQuery):
    await callback.answer("Новости подгружаются", show_alert=True)
    await callback.message.edit_text('Вот свежие новости!', reply_markup=await kb.test_keyboard())


@dp.message(F.text == "Тестовая кнопка 1")
async def test_button(message: Message):
    await message.answer('Обработка нажатия на reply кнопку 1')


@dp.message(F.text == "Тестовая кнопка 2")
async def test_button(message: Message):
    await message.answer('Обработка нажатия на reply кнопку 2')


@dp.message(F.text == "Тестовая кнопка 3")
async def test_button(message: Message):
    await message.answer('Обработка нажатия на reply кнопку 3')


@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды: \n /start \n /help \n /minitraining')


@dp.message(CommandStart())
async def start(message: Message):
    # await message.answer(f'Приветики, {message.from_user.first_name}', reply_markup=kb.main)
    await message.answer(f'Приветики, {message.from_user.first_name}', reply_markup=kb.inline_keyboard_test)
    #await message.answer(f'Приветики, {message.from_user.first_name}', reply_markup=await kb.test_keyboard())


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
