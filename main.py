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


@dp.callback_query(F.data == 'more')
async def more(callback: CallbackQuery):
    await callback.message.edit_text('Выберите опцию:', reply_markup=await kb.send_option())


@dp.callback_query(F.data == 'option1')
async def option1(callback: CallbackQuery):
    await callback.message.answer('Текст для Опции 1')


@dp.callback_query(F.data == 'option2')
async def option2(callback: CallbackQuery):
    await callback.message.answer('Сообщение для Опции 2')


@dp.message(F.text == "Привет!")
async def test_button(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}!')


@dp.message(F.text == "Пока!")
async def test_button(message: Message):
    await message.answer(f'До свидания, {message.from_user.first_name}!')


@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды: \n /start \n /help \n /links \n /dynamic')


@dp.message(Command('links'))
async def links(message: Message):
    await message.answer(f'Ссылки', reply_markup=await kb.test_keyboard())


@dp.message(Command('dynamic'))
async def dynamic(message: Message):
    await message.answer('Изменить клавиатуру', reply_markup=kb.inline_keyboard_links)


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}', reply_markup=kb.main)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
