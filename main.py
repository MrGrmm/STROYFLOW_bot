
import random
from aiogram.utils.exceptions import MessageToDeleteNotFound, MessageToEditNotFound
from aiogram import Dispatcher, Bot, types, executor
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, InputMedia, InputMediaAnimation, InputMediaPhoto, InputMediaVideo, InlineKeyboardMarkup, InlineKeyboardButton, LabeledPrice, Message, PreCheckoutQuery
from keyboards import kb_main_menu, ikb_faq, ikb_main_menu, ikb_ready_to_buy, ikb_rev_luke, ikb_buy, ikb_small_luke, ikb_midle_luke, ikb_big_luke, ikb_recomanded_rl, ikb_vibrati_var, ikb_recomanded_buy, ikb_san_uzel, ikb_oformiti_zakaz, ikb_chertej, ikb_oplata

from config import TOKEN_API
from All_products import rev_luks


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

# images = ['https://i.pinimg.com/originals/8a/de/fe/8adefe5af862b4f9cec286c6ee4722cb.jpg', 'https://img3.akspic.ru/previews/7/4/2/8/6/168247/168247-kosti_3d-igra_v_kosti_3d-azartnaya_igra-pitevaya_igra-kazino-500x.jpg', 'https://img1.akspic.ru/previews/7/4/7/9/6/169747/169747-ikanvas-art-pechat_na_holste-poster-oblako-500x.jpg' , 'https://mobimg.b-cdn.net/v3/fetch/94/94c56e15f13f1de4740a76742b0b594f.jpeg']

last_message_id = None
last_photo_id = None



vibrannii_tovar = None


HELP_COMMAND = '''
<b>/start</b> - <em>Запуск бота</em>
<b>/description</b> - <em>Описание</em>
<b>/help</b> - <em>Запуск бота</em>'''

DESCRIPTION = '''
Информация о комании SanFlow, продуктах что продаём и производителей продуктов'''


korzina = []


arr_photos_razmeri = ['media\\Small_luke.mp4',
                    'media\\midle_luke.mp4',
                    'media\\big_luke.mp4']

captions_photos_razmeri = ['Люки небольшого размера\n200x200 - 500x400','Люки среднего размера\n400x600 - 600x700','Люки большого размера\n400x900 - 600x1200']
current_photo_index = 0


photo_shema = ['https://shag-ma.ru/upload/resize_cache/iblock/fc4/1500_1500_0/bruyzuwd05sw2e6acys8t587v05ivnqy.jpg', 
               'https://shag-ma.ru/upload/iblock/e80/34kqycldpbwzm1dgpgasoj1s44n5urj3.jpg', 
               'https://shag-ma.ru/upload/iblock/fda/ckpn4rq9nz1y5mmdlh3sgx1hkou7iq09.jpg']
curr_photo_shema_index = 0


photo_recomanded = ['https://shag-ma.ru/upload/iblock/ed7/zms8qt3kmh4pczm9b5ldoj2ivusmgnif.jpg', 
               'https://shag-ma.ru/upload/iblock/b3f/rn6fu5vqpgr3s956ni6lnxv922an5bs4.jpg', 
               'https://shag-ma.ru/upload/resize_cache/iblock/0e8/1500_1500_0/cxnjayzxo8cq94p8q25r92inqmdaeww2.jpg']
curr_photo_recomanded_index = 0

async def start_on(_):
    print('Бот запущен!!')


def get_products_from_cart(user_id):
    global korzina
    if len(korzina) != 0:
        return korzina
    else:
        return []


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.chat.id, "Вас приветствует компания SanFlow выберите продукт который вас интересует", reply_markup=kb_main_menu)
    with open('media/photo_2023-03-09_22-37-54.jpg', 'rb') as photo_logo:
        await bot.send_photo(message.chat.id, photo=photo_logo, reply_markup=ikb_main_menu)
    await message.delete()



@dp.message_handler(Text(equals='🪪 О нас'))
async def send_mess_help(message: types.Message):
    await message.answer(text=DESCRIPTION, parse_mode='HTML')
    await message.delete()


@dp.message_handler(Text(equals='📞Позвоните мне'))
async def send_mess_help(message: types.Message):
    await message.answer("Пожалуйста, поделитесь своим контактом")
    await message.delete()


@dp.message_handler(Text(equals='🛒Корзина'))
async def oformiti_zakaz(message: types.Message):
    user_id = message.from_user.id
    global vibrannii_tovar, rev_luks
    # Получаем список товаров, добавленных пользователем в корзину
    products = get_products_from_cart(user_id)
    # Проверяем, есть ли товары в корзине
    if not products:
        # Если корзина пуста, просим пользователя добавить товары
        await message.answer("Вы не добавили товары в корзину. Для начала добавьте товары.")
        await message.delete()
    else:
        # Если в корзине есть товары, формируем сообщение с информацией о добавленных товарах
        message_text = "Вы выбрали следующие товары:\n\n"
        summa = 0
        ves = 0
        for i, product in enumerate(products, start=1):
            message_text += f"{i}. {product['Характеристики']['Имя']}\n\t Стоимость: {product['Цена']}₽/шт\n\n"
            summa += float(product['Цена'])
            ves += float(product['Характеристики']['Вес(кг)'])
        else:
            message_text += f"Общая стоимость: {str(summa)} ₽\nОбщий вес: {str(ves)} кг"
        await message.delete()  # удаление сообщения об оформлении заказа
        await message.answer_photo(photo='https://img.lovepik.com/free-png/20210918/lovepik-shopping-cart-png-image_400246975_wh1200.png', caption=message_text, reply_markup=ikb_ready_to_buy)
    


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


@dp.callback_query_handler(lambda c: c.data == 'oformiti_zakaz')
async def proverka_ozn_recomand(callback: types.CallbackQuery):
    await callback.message.edit_media(InputMedia(media='https://korolev.clinic/wp-content/uploads/2020/03/photo_2020-03-17_18-29-15.jpg',
                                                type='photo',
                                                caption='⚠️⚠️⚠️⚠️⚠️⚠️ВАЖНО⚠️⚠️⚠️⚠️⚠️⚠️\nПеред покупкой ревизионного люка необходимо ознакомится с рекомендациями по подготовке проёма'),
                                        reply_markup=ikb_oformiti_zakaz)  
    


@dp.callback_query_handler(lambda c: c.data == 'buy')
async def buy_product(callback: types.CallbackQuery):
    await callback.message.edit_media(InputMedia(media='https://ru-static.z-dn.net/files/d28/2612fb5a49be38d39e1ada7fe046c9c6.jpg',
                                                type='photo',
                                                caption='Пожалуйста напишите в чате одним сообщением данные которые запрашиваются на фото'),
                                        reply_markup=ikb_buy)  




@dp.callback_query_handler(lambda c: c.data == 'mm')
async def back_to_main_menu(callback: types.CallbackQuery):
    # Отправляем новое фото и сообщение
    with open('media/photo_2023-03-09_22-37-54.jpg', 'rb') as photo_logo:
        await callback.message.edit_media(InputMedia(media=photo_logo,
                                                     type='photo'),
                                                     reply_markup=ikb_main_menu)
    

@dp.callback_query_handler(lambda c: c.data == 'rev_luk')
async def show_rev_luk(callback: types.CallbackQuery):
    global current_photo_index
    current_photo_index = 0
    with open(arr_photos_razmeri[current_photo_index], 'rb') as video_razmera:
        await callback.message.edit_media(InputMediaVideo(media=video_razmera,
                                                    type='photo',
                                                    caption=captions_photos_razmeri[current_photo_index]),
                                            reply_markup=ikb_rev_luke)   
    




@dp.callback_query_handler(lambda c: c.data == 'san_uzel')
async def show_san_uzel(callback: types.CallbackQuery):
    await callback.message.edit_media(InputMedia(media='https://praktikd.ru/application/includes/uploadIMG/276.png',
                                                 type='photo',),
                                                 reply_markup=ikb_san_uzel)

    
@dp.callback_query_handler(lambda c: c.data == 'last_var')
async def show_last_photo(callback: types.CallbackQuery):
    global current_photo_index
    if current_photo_index == 0:
        current_photo_index = len(arr_photos_razmeri) - 1
    else:
        current_photo_index -= 1
    with open(arr_photos_razmeri[current_photo_index], 'rb') as video_razmera:
        await callback.message.edit_media(InputMediaVideo(media=video_razmera,
                                                    type='photo',
                                                    caption=captions_photos_razmeri[current_photo_index]),
                                                reply_markup=ikb_rev_luke)
    

@dp.callback_query_handler(lambda c: c.data == 'next_var')
async def show_next_photo(callback: types.CallbackQuery):
    global current_photo_index
    if current_photo_index == len(arr_photos_razmeri) - 1:
        current_photo_index = 0
    else:
        current_photo_index += 1
    with open(arr_photos_razmeri[current_photo_index], 'rb') as video_razmera:
        await callback.message.edit_media(InputMediaVideo(media=video_razmera,
                                                    type='photo',
                                                    caption=captions_photos_razmeri[current_photo_index]),
                                                reply_markup=ikb_rev_luke)



@dp.callback_query_handler(lambda c: c.data == 'faq_ikb')
async def show_imm_faq(callback: types.CallbackQuery):
    # Заменяем медия вместе с клавиатурой и описанием
    await callback.message.edit_media(InputMedia(media='https://cdn.searchenginejournal.com/wp-content/uploads/2022/07/faq-632c0874710c1-sej.png',
                                                type='photo',
                                                caption='Все вопросы и ответы'),
                                                reply_markup=ikb_faq)
    

@dp.callback_query_handler(lambda c: c.data == 'recomanded_rl')
async def recomanded_text(callback: types.CallbackQuery):
    global curr_photo_recomanded_index
    curr_photo_recomanded_index = 0
    await callback.message.edit_media(InputMedia(media=photo_recomanded[curr_photo_recomanded_index],
                                                type='photo'),
                                        reply_markup=ikb_recomanded_rl)  
    
@dp.callback_query_handler(lambda c: c.data == 'last_rec_photo_rl')
async def show_last_photo(callback: types.CallbackQuery):
    global curr_photo_recomanded_index
    if curr_photo_recomanded_index == 0:
        curr_photo_recomanded_index = len(photo_recomanded) - 1
    else:
        curr_photo_recomanded_index -= 1
    await callback.message.edit_media(InputMedia(media=photo_recomanded[curr_photo_recomanded_index],
                                                type='photo'),
                                            reply_markup=ikb_recomanded_rl)
    

@dp.callback_query_handler(lambda c: c.data == 'next_rec_photo_rl')
async def show_next_photo(callback: types.CallbackQuery):
    global curr_photo_recomanded_index
    if curr_photo_recomanded_index == len(photo_recomanded) - 1:
        curr_photo_recomanded_index = 0
    else:
        curr_photo_recomanded_index += 1
    await callback.message.edit_media(InputMedia(media=photo_recomanded[curr_photo_recomanded_index],
                                                type='photo'),
                                            reply_markup=ikb_recomanded_rl)

@dp.callback_query_handler(lambda c: c.data == 'recomanded_b')
async def recomanded_text(callback: types.CallbackQuery):
    global curr_photo_recomanded_index
    curr_photo_recomanded_index = 0
    await callback.message.edit_media(InputMedia(media=photo_recomanded[curr_photo_recomanded_index],
                                                type='photo'),
                                        reply_markup=ikb_recomanded_buy)  
    
@dp.callback_query_handler(lambda c: c.data == 'last_rec_photo_b')
async def show_last_photo(callback: types.CallbackQuery):
    global curr_photo_recomanded_index
    if curr_photo_recomanded_index == 0:
        curr_photo_recomanded_index = len(photo_recomanded) - 1
    else:
        curr_photo_recomanded_index -= 1
    await callback.message.edit_media(InputMedia(media=photo_recomanded[curr_photo_recomanded_index],
                                                type='photo'),
                                            reply_markup=ikb_recomanded_buy)
    

@dp.callback_query_handler(lambda c: c.data == 'next_rec_photo_b')
async def show_next_photo(callback: types.CallbackQuery):
    global curr_photo_recomanded_index
    if curr_photo_recomanded_index == len(photo_recomanded) - 1:
        curr_photo_recomanded_index = 0
    else:
        curr_photo_recomanded_index += 1
    await callback.message.edit_media(InputMedia(media=photo_recomanded[curr_photo_recomanded_index],
                                                type='photo'),
                                            reply_markup=ikb_recomanded_buy)



@dp.callback_query_handler(lambda c: c.data == 'vibrati')
async def vibran_razmer(callback: types.CallbackQuery):
    global current_photo_index
    global arr_photos_razmeri
    if current_photo_index == 0:
        with open(arr_photos_razmeri[current_photo_index], 'rb') as video_razmera:
            await callback.message.edit_media(InputMediaVideo(media=video_razmera,
                                                    type='photo',
                                                    caption='Выберите точный размер необходимого люка'),
                                                    reply_markup=ikb_small_luke)
    elif current_photo_index == 1:
        with open(arr_photos_razmeri[current_photo_index], 'rb') as video_razmera:
            await callback.message.edit_media(InputMediaVideo(media=video_razmera,
                                                    type='photo',
                                                    caption='Выберите точный размер необходимого люка'),
                                                    reply_markup=ikb_midle_luke)
    elif current_photo_index == 2:
        with open(arr_photos_razmeri[current_photo_index], 'rb') as video_razmera:
            await callback.message.edit_media(InputMediaVideo(media=video_razmera,
                                                    type='photo',
                                                    caption='Выберите точный размер необходимого люка'),
                                                    reply_markup=ikb_big_luke)



@dp.callback_query_handler(lambda c: c.data == '3d_project')
async def pokazati_3d_project(callback: types.CallbackQuery):
    global vibrannii_tovar
    with open(rev_luks[vibrannii_tovar]['Медиа'].get('3DПроект'), 'rb') as curr_gif_url:
        caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
        await callback.message.edit_media(InputMediaVideo(media=curr_gif_url,
                                                             caption=caption),
                                            reply_markup=ikb_vibrati_var)


@dp.callback_query_handler(lambda c: c.data == 'gotovie_raboti')
async def pokazati_3d_project(callback: types.CallbackQuery):
    global vibrannii_tovar
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Готовое')
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                        reply_markup=ikb_vibrati_var)
    

@dp.callback_query_handler(lambda c: c.data == 'harakteristiki')
async def pokazati_3d_project(callback: types.CallbackQuery):
    global vibrannii_tovar
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Чертёж')
    caption = f"Характеристики:\n"
    for key, value in rev_luks[vibrannii_tovar]['Характеристики'].items():
        caption += f"▪️ \t{key}: {value}\n"
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                      reply_markup=ikb_vibrati_var)
    

@dp.callback_query_handler(lambda c: c.data == 'chertej')
async def show_rev_luk(callback: types.CallbackQuery):
    global curr_photo_shema_index
    global vibrannii_tovar
    curr_photo_shema_index = 0
    await callback.message.edit_media(InputMedia(media=photo_shema[curr_photo_shema_index],
                                                type='photo'),
                                        reply_markup=ikb_chertej)



@dp.callback_query_handler(lambda c: c.data == 'back_to_vv')
async def pokazati_3d_project(callback: types.CallbackQuery):
    global vibrannii_tovar
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Чертёж')
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                      reply_markup=ikb_vibrati_var)

    
@dp.callback_query_handler(lambda c: c.data == 'dalee')
async def show_next_photo(callback: types.CallbackQuery):
    global curr_photo_shema_index
    if curr_photo_shema_index == len(photo_shema) - 1:
        curr_photo_shema_index = 0
    else:
        curr_photo_shema_index += 1
    await callback.message.edit_media(InputMedia(media=photo_shema[curr_photo_shema_index],
                                                type='photo'),
                                            reply_markup=ikb_chertej)
    
@dp.callback_query_handler(lambda c: c.data == 'obratno')
async def show_next_photo(callback: types.CallbackQuery):
    global curr_photo_shema_index
    if curr_photo_shema_index == len(photo_shema) - 1:
        curr_photo_shema_index = 0
    else:
        curr_photo_shema_index -= 1
    await callback.message.edit_media(InputMedia(media=photo_shema[curr_photo_shema_index],
                                                type='photo'),
                                            reply_markup=ikb_chertej)

@dp.callback_query_handler(lambda c: c.data == 'dobaviti_v_korzinu')
async def dob_v_korzinu(callback: types.CallbackQuery):
    global vibrannii_tovar, korzina
    korzina.append(rev_luks[vibrannii_tovar])
    await callback.answer('✅ Товар добавлен в корзину ✅')


@dp.callback_query_handler(lambda c: c.data == 'udal_iz_korz')
async def udaliti_iz_korzini(callback: types.CallbackQuery):
    global korzina
    korzina = []
    with open('media/photo_2023-03-09_22-37-54.jpg', 'rb') as photo_logo:
        await callback.message.edit_media(InputMedia(media=photo_logo,
                                                     type='photo'),
                                                     reply_markup=ikb_main_menu)
    await callback.answer('✅Корзина очищена✅')

##############################################################################################################
@dp.callback_query_handler(lambda c: c.data in ['200x200', '200x300', '300x300', '300x400', '300x500', '300x600', '400x200', '400x300',
                                                '400x400', '400x500', '400x600', '400x700', '400x800', '400x700', '400x800', '400x900',
                                                '400x1000', '400x1200', '500x300', '500x400', '500x500', '500x600', '500x700', '500x800',
                                                '500x900', '500x1000', '500x1100', '500x1200', '600x300','600x400', '600x500', '600x600',
                                                '600x700', '600x800', '600x900', '600x1000', '600x1100', '600x1200'])
async def rev_luks_200x200(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)






##############################################################################################################





# @dp.callback_query_handler(lambda c: c.data == 'otpraviti_zakaz')
# async def order(callback_query: types.CallbackQuery):
#     bot = dp.bot
#     message = callback_query.message
#     await bot.send_invoice(chat_id=message.chat.id,
#                            title='Покупка через телеграм бот',
#                            description='Пробуем оплату',
#                            payload='Инфа для статистики',
#                            provider_token='381764678:TEST:53130',
#                            currency='rub',
#                            prices=LabeledPrice(label='Доступ к секретной информации',
#                                                amount=15000),
#                             start_parameter='parametr_start',
#                             provider_data=None,
#                             photo_url='https://htstatic.imgsmail.ru/pic_image/b35d56a4ee75c0ffd021c7b0f8088a8a/840/359/1911653/',
#                             photo_size=100,
#                             photo_width=800,
#                             photo_height=450,
#                             need_name=True,
#                             need_phone_number=True,
#                             need_email=True,
#                             need_shipping_address=True,
#                             send_phone_number_to_provider=False,
#                             send_email_to_provider=False,
#                             is_flexible=False,
#                             disable_notification=False,
#                             protect_content=False,
#                             reply_to_message_id=None,
#                             allow_sending_without_reply=True,
#                             reply_markup=ikb_oplata,
#                             request_timeout=15)


# @dp.pre_checkout_query_handler(lambda c: c.data == 'oplatiti')
# async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
#     await bot.answer_pre_checkout_query(pre_checkout_query_id=pre_checkout_query, ok=True)


# async def successful_payment(message: Message):
#     msg = f'Спасибо за оплату {message.successful_payment.total_amount // 100} {message.successful_payment.currency}.'
#     await message.answer(msg)


executor.start_polling(dp, on_startup=start_on, skip_updates=True)