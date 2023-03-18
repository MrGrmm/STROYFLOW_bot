
import random
from aiogram.utils.exceptions import MessageToDeleteNotFound, MessageToEditNotFound
from aiogram import Dispatcher, Bot, types, executor
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, InputMedia, InputMediaAnimation
from keyboards import kb_main_menu, ikb_faq, ikb_main_menu, ikb_ready_to_buy, ikb_rev_luke, ikb_buy, ikb_small_luke, ikb_midle_luke, ikb_big_luke, ikb_recomanded_rl, ikb_vibrati_var, ikb_recomanded_buy, ikb_san_uzel

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

p = {
    'name': 'Название товара',
    'description': 'Описание товара',
    'price': 1000000, # цена товара, указывается числом 
}
p1 = {
    'name': 'Название товара',
    'description': 'Описание товара',
    'price': 1000000, # цена товара, указывается числом
}
korzina = []


arr_photos_razmeri = ['https://liveam.tv/assets/images/2021/malenkie-yu.jpg',
                    'https://porosenka.net/uploads/og/3521.png',
                    'https://torg-retail.ru/wp-content/uploads/2016/04/5.jpg']
captions_photos_razmeri = ['Люки небольшого размера\n200x200 - 500x400','Люки среднего размера\n400x600 - 600x700','Люки большого размера\n400x900 - 600x1200']
current_photo_index = 0


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
    else:
        # Если в корзине есть товары, формируем сообщение с информацией о добавленных товарах
        message_text = "Вы выбрали следующие товары:\n\n"
        for i, product in enumerate(products, start=1):
            message_text += f"{i}. {product['Характеристики']['Имя']}\n\t Стоимость: {product['Цена']}₽/шт\n\n"
        await message.delete()  # удаление сообщения об оформлении заказа
        await message.answer_photo(photo='https://img.lovepik.com/free-png/20210918/lovepik-shopping-cart-png-image_400246975_wh1200.png', caption=message_text, reply_markup=ikb_ready_to_buy)
    print(products)

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




@dp.callback_query_handler(text='buy')
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
    await callback.message.edit_media(InputMedia(media=arr_photos_razmeri[current_photo_index],
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
    await callback.message.edit_media(InputMedia(media=arr_photos_razmeri[current_photo_index],
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
    await callback.message.edit_media(InputMedia(media=arr_photos_razmeri[current_photo_index],
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
    await callback.message.edit_media(InputMedia(media='https://d2gg9evh47fn9z.cloudfront.net/800px_COLOURBOX18304060.jpg',
                                                type='photo',
                                                caption='Рекомендации по подготовке проёма'),
                                                reply_markup=ikb_recomanded_rl)
    
@dp.callback_query_handler(lambda c: c.data == 'recomanded_b')
async def recomanded_text(callback: types.CallbackQuery):
    await callback.message.edit_media(InputMedia(media='https://d2gg9evh47fn9z.cloudfront.net/800px_COLOURBOX18304060.jpg',
                                                type='photo',
                                                caption='Рекомендации по подготовке проёма'),
                                                reply_markup=ikb_recomanded_buy)


@dp.callback_query_handler(lambda c: c.data == 'vibrati')
async def vibran_razmer(callback: types.CallbackQuery):
    global current_photo_index
    if current_photo_index == 0:
        await callback.message.edit_media(InputMedia(media='https://liveam.tv/assets/images/2021/malenkie-yu.jpg',
                                                type='photo',
                                                caption='Выберите точный размер необходимого люка'),
                                                reply_markup=ikb_small_luke)
    elif current_photo_index == 1:
        await callback.message.edit_media(InputMedia(media='https://porosenka.net/uploads/og/3521.png',
                                                type='photo',
                                                caption='Выберите точный размер необходимого люка'),
                                                reply_markup=ikb_midle_luke)
    elif current_photo_index == 2:
        await callback.message.edit_media(InputMedia(media='https://torg-retail.ru/wp-content/uploads/2016/04/5.jpg',
                                                type='photo',
                                                caption='Выберите точный размер необходимого люка'),
                                                reply_markup=ikb_big_luke)


@dp.callback_query_handler(lambda c: c.data == 'podtverditi')
async def obzor_vibrannogo_varianta(callback: types.CallbackQuery):
    await callback.message.edit_media(InputMedia(media='https://shag-ma.ru/upload/iblock/494/f949z2ctc01o46htsz63rvqhcweup9ej.jpg',
                                                 type='photo'),
                                                 reply_markup=ikb_vibrati_var)


@dp.callback_query_handler(lambda c: c.data == '3d_project')
async def pokazati_3d_project(callback: types.CallbackQuery):
    global vibrannii_tovar
    curr_gif_url = rev_luks[vibrannii_tovar]['Медиа'].get('3DПроект')
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    await callback.message.edit_media(InputMediaAnimation(media=curr_gif_url,
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
    

@dp.callback_query_handler(lambda c: c.data == 'chertej')
async def pokazati_3d_project(callback: types.CallbackQuery):
    global vibrannii_tovar
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Чертёж')
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    

@dp.callback_query_handler(lambda c: c.data == 'dobaviti_v_korzinu')
async def dob_v_korzinu(callback: types.CallbackQuery):
    global vibrannii_tovar, korzina
    korzina.append(rev_luks[vibrannii_tovar])
    await callback.answer('✅ Товар добавлен в корзину ✅')


@dp.callback_query_handler(lambda c: c.data == '200x200')
async def rev_luks_200x200(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '200x300')
async def rev_luks_200x300(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '300x300')
async def rev_luks_300x300(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '300x400')
async def rev_luks_300x400(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '300x500')
async def rev_luks_300x500(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '300x600')
async def rev_luks_300x600(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '400x200')
async def rev_luks_400x200(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '400x300')
async def rev_luks_400x300(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '400x400')
async def rev_luks_400x400(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '400x500')
async def rev_luks_400x500(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '400x600')
async def rev_luks_400x600(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '400x700')
async def rev_luks_400x700(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '400x800')
async def rev_luks_400x800(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '400x700')
async def rev_luks_400x700(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '400x800')
async def rev_luks_400x800(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '400x900')
async def rev_luks_400x900(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '400x1000')
async def rev_luks_400x1000(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '400x1200')
async def rev_luks_400x1200(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '500x300')
async def rev_luks_500x300(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '500x400')
async def rev_luks_500x400(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '500x500')
async def rev_luks_500x500(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '500x600')
async def rev_luks_500x600(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '500x700')
async def rev_luks_500x700(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '500x800')
async def rev_luks_500x800(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '500x900')
async def rev_luks_500x900(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '500x1000')
async def rev_luks_500x1000(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '500x1100')
async def rev_luks_500x1100(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '500x1200')
async def rev_luks_500x1200(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '600x300')
async def rev_luks_600x300(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '600x400')
async def rev_luks_600x400(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '600x500')
async def rev_luks_600x500(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '600x600')
async def rev_luks_600x600(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '600x700')
async def rev_luks_600x700(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '600x800')
async def rev_luks_600x800(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '600x900')
async def rev_luks_600x900(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '600x1000')
async def rev_luks_600x1000(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '600x1100')
async def rev_luks_600x1100(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)
    
@dp.callback_query_handler(lambda c: c.data == '600x1200')
async def rev_luks_600x1200(callback: types.CallbackQuery):
    global rev_luks, vibrannii_tovar
    vibrannii_tovar = callback.data
    caption = f"{rev_luks[vibrannii_tovar]['Характеристики']['Имя']}\n\t{rev_luks[vibrannii_tovar]['Цена']}₽/шт"
    curr_photo_url = rev_luks[vibrannii_tovar]['Медиа'].get('Фото')
    await callback.message.edit_media(InputMedia(media=curr_photo_url,
                                                 type='photo',
                                                 caption=caption),
                                                 reply_markup=ikb_vibrati_var)


executor.start_polling(dp, on_startup=start_on, skip_updates=True)