from aiogram import Dispatcher, Bot, types, executor
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
from keyboards import kb_main_menu, ikb_faq, ikb_main_menu, ikb_ready_to_buy
from config import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

# images = ['https://i.pinimg.com/originals/8a/de/fe/8adefe5af862b4f9cec286c6ee4722cb.jpg', 'https://img3.akspic.ru/previews/7/4/2/8/6/168247/168247-kosti_3d-igra_v_kosti_3d-azartnaya_igra-pitevaya_igra-kazino-500x.jpg', 'https://img1.akspic.ru/previews/7/4/7/9/6/169747/169747-ikanvas-art-pechat_na_holste-poster-oblako-500x.jpg' , 'https://mobimg.b-cdn.net/v3/fetch/94/94c56e15f13f1de4740a76742b0b594f.jpeg']

last_message_id = None
last_photo_id = None

HELP_COMMAND = '''
<b>/start</b> - <em>Запуск бота</em>
<b>/description</b> - <em>Описание</em>
<b>/help</b> - <em>Запуск бота</em>'''

DESCRIPTION = '''
Информация о комании SanFlow, продуктах что продаём и производителей продуктов'''






async def start_on(_):
    print('Бот запущен!!')



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    # Отправляем сообщение с клавиатурой
    global last_message_id, last_photo_id
    with open('media\photo_2023-03-09_22-37-54.jpg', 'rb') as photo_logo:
        await bot.send_photo(message.chat.id, photo=photo_logo, reply_markup=kb_main_menu)
    last_message_id = (await bot.send_message(message.chat.id, "Вас приветствует компания SanFlow выберите продукт который вас интересует", reply_markup=ikb_main_menu)).message_id
    

@dp.message_handler(Text(equals='Запросить звонок'))
async def send_mess_help(message: types.Message):
    await message.answer("Пожалуйста, поделитесь своим контактом")
    await message.delete()

@dp.message_handler(Text(equals='📞 О нас'))
async def send_mess_help(message: types.Message):
    await message.answer(text=DESCRIPTION, parse_mode='HTML')
    await message.delete()

@dp.message_handler(Text(equals='Вопрос/Ответ'))
async def send_mess_help(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=last_message_id)
    await message.answer(text='Меню FAQ:', reply_markup=ikb_faq)
    await message.delete()


    
@dp.message_handler(content_types=types.ContentType.TEXT, regexp='сантехника')
async def handle_santekhnika(message: types.Message):
    # отправляем ответное сообщение
    await message.reply(text='Могу предложить простое и эффективное решение для обслуживания коммуникаций, канализации и трубопроводов в доме или на улице, хотите ознакомиться?')

@dp.message_handler(lambda message: message.text.lower() == 'да')
async def get_private_chat(message: types.Message):
    await bot.send_message(message.from_user.id, 'Описание/ Реклама.  ФОРМАТ еще обдумывается')

@dp.callback_query_handler()
async def process_callback_button(callback_query: types.CallbackQuery):
    global last_message_id, last_photo_id
    # Удаляем предыдущие фото и клавиатуры перед отправкой нового сообщения
    await bot.delete_message(callback_query.from_user.id, last_message_id)
    if last_photo_id is not None:
        await bot.delete_message(callback_query.from_user.id, last_photo_id)
#     # Отправляем сообщение с текстом, соответствующим нажатой кнопке
    if callback_query.data == 'rev_luk':
        last_message = await bot.send_photo(callback_query.from_user.id, photo='https://shag-ma.ru/upload/medialibrary/111/c9l9ag1tnp5cpqwu2xk3fwdmh4epgdwa.jpg', reply_markup=ikb_rev_luk)
        last_message_id = last_message.message_id
#     elif callback_query.data == 'odnost':
#         last_message = await bot.send_photo(callback_query.from_user.id, photo='https://shag-ma.ru/upload/medialibrary/424/p0qvzyetlcrim1x5vxywlvqnlapjrzyn.jpg', reply_markup=ikb_view_buy)
#         last_message_id = last_message.message_id
#     elif callback_query.data == 'odn_v1':
#         last_message = await bot.send_photo(callback_query.from_user.id, photo='https://lh3.googleusercontent.com/unz6g-pk_83GHr4Z85m6CCe2vtlH7mLM_bZZKzfVfLksQ4O9FroZm0TtDnP5UMHM8vxW_7fu_PObd6QsIpTXzVRIXJHU37YkdFZFN6hkua6HUv0nBpQTFl4DGIGFvb-RYPBmQzwfdqMiRIh2pkCj7y-TSuuOlueezfFh5xe2I2yqiWLxE6DWqr1m9WsERmzGctRQdiju0WqOlT2hpULBc9MyH4Ay1uEVc8WE4L14LxgPRZzDAnKoAGG9lvR9W7mt9D1GfnEGhuJo82uRby1s3d2cA1eQKHCzQyZpcAolJB9n9taqr4lPGClOT8FIcsxEXEvCBzc9ITCXiyugcct5qrqf8dfW1ZzIxvUwWQ_ZtzYl92jjQIRcPf7iYoq1ka7ShcQ3BxZT6RsNg81T4Ot2ZITgy1UBONYmFPsiQR9unJXBDQPDvzdpiaPYSHLRkZwmMujGr2TStZYo_CRI-jTaS2n05VqCeHCeqSM5PrjZjFMdqpOd84U0ZJRTdvSGNVqvdP5QgwV1Ka4DSzQd0PoTPWBu4UEpNxYhqcmgVWgoQ-JTDPoMxVtyDrp-9MlJZK-1_OvdpMj6RLNsht8Np6jG78PrKvxs_vkA7FdS14cDJHMrciBn5tgELOt_TzD2quCKFeTtoHhM_Asen6jGuU91NEaeiGBNnyVL4NokzASAuBU5Z1kE_3ub9zQGt5TE3vF-EiXeLwZGq1KCGc5gcC8ITLCxiEwNNhYQmSlNTZLJSUkuFm4GhfWo580lEe7fodUMmYDczhOP2l2aenvYlsKC804GysK4BCqAP9-hMzBjB6BqgTqlEG8pmSH0TC5skfBPfzytBzfP0-4NSpeijKYh9Q1HYWDNIEAKduk2HVMDNPg8T6iDkfOem4suvPDsjaMRsRXtN2JjQE5DVxWe6PjYSSYAtnE4Ai6DDWQIbOqain2i=w597-h624-no?authuser=0', caption='Вы выбрали Вариант №1', reply_markup=ikb_odnost_v1)
#         last_message_id = last_message.message_id
#     elif callback_query.data == 'odn_v1_photos':
#         last_message = await bot.send_photo(callback_query.from_user.id, photo='https://downloader.disk.yandex.ru/preview/f04629fdf8ed2f03a3efffc91a09e829cccee32edf7718b3c51138873bf160e0/63fecb37/KYY58Jh4gtgzz5899_Rgtlc4B7G3mQW9exTtvI-Xj3H3UhaSiYVLRYL9uIab7T5YViMFP1WtEAnm_tbWxJjOLw%3D%3D?uid=0&filename=2022-05-11%2021-19-14.JPG&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=997x882', caption='Вы выбрали Вариант №1', reply_markup=ikb_odnost_v1)
#         last_message_id = last_message.message_id
    elif callback_query.data == 'faq':
        last_message = await bot.send_message(callback_query.from_user.id, "Вы перешли в меню 'FAQ'", reply_markup=ikb_faq)
        last_message_id = last_message.message_id
#     elif callback_query.data == 'back_to_rev_luk':
#         last_message = await bot.send_message(callback_query.from_user.id, "Вы перешли в меню 'Ревизионный люк'", reply_markup=ikb_rev_luk)
#         last_message_id = last_message.message_id
#     elif callback_query.data == 'back_to_view_buy':
#         last_message = await bot.send_message(callback_query.from_user.id, "Вы перешли в меню 'Ревизионный люк'", reply_markup=ikb_view_buy)
#         last_message_id = last_message.message_id
#     elif callback_query.data == 'mm':
#         last_message = await bot.send_message(callback_query.from_user.id, "Вы перешли в Главное меню", reply_markup=ikb_oficial_page)
#         last_message_id = last_message.message_id
#     elif callback_query.data == 'odn_v1_buy':
#         last_message = await bot.send_message(callback_query.from_user.id, "Здесь будет опросник (Формат ещё обдумывается)", reply_markup=ikb_next_buy)
#         last_message_id = last_message.message_id
#     elif callback_query.data == 'next_buy':
#         last_message = await bot.send_message(callback_query.from_user.id, "Вы перешли в меню 'Каталог'", reply_markup=ikb_catalog)
#         last_message_id = last_message.message_id
    else:
        pass



executor.start_polling(dp, on_startup=start_on, skip_updates=True)