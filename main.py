from aiogram import Dispatcher, Bot, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from config import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb_start = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_start.add(KeyboardButton('/START'))

HELP_COMMAND = '''
<b>/start</b> - <em>Запуск бота</em>
<b>/description</b> - <em>Описание</em>
<b>/help</b> - <em>Запуск бота</em>'''

DESCRIPTION = '''
Предназначение бота'''


async def start_on(_):
    print('Бот запущен!!')



@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Добро пожаловать!')

@dp.message_handler(commands='description')
async def descript_command(message: types.Message):
    await message.answer(DESCRIPTION)
    await message.delete()

@dp.message_handler(commands='help')
async def help_command(message: types.Message):
    await message.answer(HELP_COMMAND, parse_mode='HTML')
    await message.delete()






executor.start_polling(dp, on_startup=start_on, skip_updates=True)