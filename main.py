from aiogram import Dispatcher, Bot, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards import kb_oficial_page, kb_main_menu
from config import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


HELP_COMMAND = '''
<b>/start</b> - <em>Запуск бота</em>
<b>/description</b> - <em>Описание</em>
<b>/help</b> - <em>Запуск бота</em>'''

DESCRIPTION = '''
Предназначение бота'''


async def start_on(_):
    print('Бот запущен!!')



# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    
    # Отправляем сообщение с клавиатурой
    await bot.send_message(message.chat.id, "Выберите раздел:", reply_markup=kb_oficial_page)

# Обработчик кнопок
@dp.callback_query_handler(lambda c: True)
async def process_callback_button(callback_query: types.CallbackQuery):
    # Отправляем сообщение с текстом, соответствующим нажатой кнопке
    if callback_query.data == 'catalog':
        await bot.send_message(callback_query.from_user.id, "Вы выбрали раздел 'Каталог'")
    elif callback_query.data == 'our_works':
        await bot.send_message(callback_query.from_user.id, "Вы выбрали раздел 'Наши работы'")
    elif callback_query.data == 'where_to_buy':
        await bot.send_message(callback_query.from_user.id, "Вы выбрали раздел 'Где купить'")
    elif callback_query.data == 'company':
        await bot.send_message(callback_query.from_user.id, "Вы выбрали раздел 'Компания'")
    elif callback_query.data == 'contacts':
        await bot.send_message(callback_query.from_user.id, "Вы выбрали раздел 'Контакты'")
    else:
        pass

@dp.message_handler(commands='description')
async def descript_command(message: types.Message):
    await message.answer(DESCRIPTION)
    await message.delete()

@dp.message_handler(commands='help')
async def help_command(message: types.Message):
    await message.answer(HELP_COMMAND, parse_mode='HTML')
    await message.delete()






executor.start_polling(dp, on_startup=start_on, skip_updates=True)