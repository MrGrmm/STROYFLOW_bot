from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton


                # kb Клавиатура главного меню
kb_main_menu = ReplyKeyboardMarkup(resize_keyboard=True)

btn_mm_call = KeyboardButton(text='📞 Запросить звонок', request_contact=True)
btn_mm_o_nas = KeyboardButton(text='О нас')
btn_mm_oformiti_zakaz = KeyboardButton(text='✅ Оформить заказ')

kb_main_menu.add(btn_mm_o_nas).add(btn_mm_call).insert(btn_mm_oformiti_zakaz)


                # Клавиатура главной страницы
ikb_main_menu = InlineKeyboardMarkup(row_width=2)

btn_imm_rev_luk = InlineKeyboardButton(text="Ревизионный люк", callback_data='rev_luk')
btn_imm_san_uzel = InlineKeyboardButton(text="Сантехнический узел", callback_data="san_uzel")

ikb_main_menu.add(btn_imm_rev_luk).add(btn_imm_san_uzel)


                # Клавиатура FAQ   
ikb_faq = InlineKeyboardMarkup(row_width=2)

btn_faq_faq = InlineKeyboardButton(text='Частые вопросы', callback_data='faq')
btn_faq_vopros = InlineKeyboardButton(text="Задать свой вопрос", callback_data="zadati_vopros")
btn_faq_back = InlineKeyboardButton(text='Назад в главное меню', callback_data='mm')

ikb_faq.add(btn_faq_faq, btn_faq_vopros).add(btn_faq_back)



                # Клавиатура оформить заказ
ikb_ready_to_buy = InlineKeyboardMarkup(row_width=1)

btn_rtb_buy = InlineKeyboardButton(text='Купить!', callback_data='buy')
btn_rtb_udal_iz_korz = InlineKeyboardButton(text='Убрать товар из корзины', callback_data='udal_iz_korz')
btn_rtb_back = InlineKeyboardButton(text='Назад в главное меню', callback_data='mm')

ikb_ready_to_buy.add(btn_rtb_buy).add(btn_rtb_udal_iz_korz).add(btn_rtb_back)



                # Клавиатура Ревизионный люк
ikb_rev_luke = InlineKeyboardMarkup(row_width=3)

btn_rl_last_var = InlineKeyboardButton(text='👈🏼', callback_data='last_var')
btn_rl_next_var = InlineKeyboardButton(text='👉🏼', callback_data='next_var')
btn_rl_vibrati = InlineKeyboardButton(text='Выбрать категорию', callback_data='vibrati')
btn_rl_back = InlineKeyboardButton(text='Назад в главное меню', callback_data='mm')
btn_rl_recomand = InlineKeyboardButton(text='Рекомендации по подготовке проёма', callback_data='recomanded')
btn_rl_faq = InlineKeyboardButton(text='Вопрос/Ответ', callback_data='faq_ikb')

ikb_rev_luke.add(btn_rl_last_var, btn_rl_vibrati, btn_rl_next_var).add(btn_rl_back).add(btn_rl_recomand).add(btn_rl_faq)




                # Клавиатура Люки маленьких размеров
ikb_small_luke = InlineKeyboardMarkup(row_width=3)

btn_sl_200x200 = InlineKeyboardButton(text='200x200', callback_data='200x200')
btn_sl_200x300 = InlineKeyboardButton(text='200x200', callback_data='200x300')
btn_sl_200x400 = InlineKeyboardButton(text='200x200', callback_data='200x400')
btn_sl_200x500 = InlineKeyboardButton(text='200x200', callback_data='200x500')
btn_sl_300x200 = InlineKeyboardButton(text='200x200', callback_data='300x200')
btn_sl_400x200 = InlineKeyboardButton(text='200x200', callback_data='400x200')
btn_sl_500x200 = InlineKeyboardButton(text='200x200', callback_data='500x200')
btn_sl_300x300 = InlineKeyboardButton(text='200x200', callback_data='300x300')
btn_sl_300x400 = InlineKeyboardButton(text='200x200', callback_data='300x400')
btn_sl_podtverditi = InlineKeyboardButton(text='Подтвердить выбор', callback_data='podtverditi')
btn_sl_back = InlineKeyboardButton(text='Назад', callback_data='back_to_rl')
btn_sl_mm = InlineKeyboardButton(text='Главное меню', callback_data='mm')

ikb_small_luke.add(btn_sl_200x200, btn_sl_200x300, btn_sl_200x400).add(btn_sl_200x500, btn_sl_300x200, btn_sl_400x200)
ikb_small_luke.add(btn_sl_500x200, btn_sl_300x300, btn_sl_300x400).add(btn_sl_podtverditi).add(btn_sl_back, btn_sl_mm)




                # Клавиатура Люки средних размеров
ikb_midle_luke = InlineKeyboardMarkup(row_width=3)

btn_ml_400x400 = InlineKeyboardButton(text='200x200', callback_data='400x400')
btn_ml_400x500 = InlineKeyboardButton(text='200x200', callback_data='400x500')
btn_ml_400x600 = InlineKeyboardButton(text='200x200', callback_data='400x600')
btn_ml_500x400 = InlineKeyboardButton(text='200x200', callback_data='500x400')
btn_ml_500x500 = InlineKeyboardButton(text='200x200', callback_data='500x500')
btn_ml_500x600 = InlineKeyboardButton(text='200x200', callback_data='500x600')
btn_ml_600x400 = InlineKeyboardButton(text='200x200', callback_data='600x400')
btn_ml_600x500 = InlineKeyboardButton(text='200x200', callback_data='600x500')
btn_ml_600x600 = InlineKeyboardButton(text='200x200', callback_data='600x600')
btn_ml_podtverditi = InlineKeyboardButton(text='Подтвердить выбор', callback_data='podtverditi')
btn_ml_back = InlineKeyboardButton(text='Назад', callback_data='back_to_rl')
btn_ml_mm = InlineKeyboardButton(text='Главное меню', callback_data='mm')

ikb_midle_luke.add(btn_ml_400x400, btn_ml_400x500, btn_ml_400x600).add(btn_ml_500x400, btn_ml_500x500, btn_ml_500x600)
ikb_midle_luke.add(btn_ml_600x400, btn_ml_600x500, btn_ml_600x600).add(btn_ml_podtverditi).add(btn_ml_back, btn_ml_mm)




                # Клавиатура Люки больших размеров
ikb_big_luke = InlineKeyboardMarkup(row_width=3)

btn_bl_700x500 = InlineKeyboardButton(text='200x200', callback_data='700x500')
btn_bl_700x600 = InlineKeyboardButton(text='200x200', callback_data='700x600')
btn_bl_700x700 = InlineKeyboardButton(text='200x200', callback_data='700x700')
btn_bl_500x700 = InlineKeyboardButton(text='200x200', callback_data='500x700')
btn_bl_500x800 = InlineKeyboardButton(text='200x200', callback_data='500x800')
btn_bl_500x900 = InlineKeyboardButton(text='200x200', callback_data='500x900')
btn_bl_600x700 = InlineKeyboardButton(text='200x200', callback_data='600x700')
btn_bl_600x800 = InlineKeyboardButton(text='200x200', callback_data='600x800')
btn_bl_600x900 = InlineKeyboardButton(text='200x200', callback_data='600x900')
btn_bl_podtverditi = InlineKeyboardButton(text='Подтвердить выбор', callback_data='podtverditi')
btn_bl_back = InlineKeyboardButton(text='Назад', callback_data='back_to_rl')
btn_bl_mm = InlineKeyboardButton(text='Главное меню', callback_data='mm')

ikb_midle_luke.add(btn_bl_700x500, btn_bl_700x600, btn_bl_700x700).add(btn_bl_500x700, btn_bl_500x800, btn_bl_500x900)
ikb_midle_luke.add(btn_bl_600x700, btn_bl_600x800, btn_bl_600x900).add(btn_bl_podtverditi).add(btn_bl_back, btn_bl_mm)




                # Клавиатура Выбрать вариант
ikb_vibrati_var = InlineKeyboardMarkup(row_width=3)

btn_vv_3d_project = InlineKeyboardButton(text='3D Проект', callback_data='3d_project')
btn_vv_chertej = InlineKeyboardButton(text='Чертёж', callback_data='chertej')
btn_vv_gotovie_raboti = InlineKeyboardButton(text='Готовые работы', callback_data='gotovie_raboti')
btn_vv_recomand = InlineKeyboardButton(text='Рекомендации по подготовке проёма', callback_data='recomanded')
btn_vv_dobaviti_v_korzinu = InlineKeyboardButton(text='Добавить в корзину')
btn_vv_back = InlineKeyboardButton(text='Назад', callback_data='back_to_rl')
btn_vv_mm = InlineKeyboardButton(text='Главное меню', callback_data='mm')

ikb_vibrati_var.add(btn_vv_3d_project, btn_vv_chertej, btn_vv_gotovie_raboti)
ikb_vibrati_var.add(btn_vv_recomand).add(btn_vv_dobaviti_v_korzinu).add(btn_vv_back, btn_vv_mm)

                # Клавиатура Убрать товар

#TODO Создать эту клавиатуру внутри хэндлера с тем количеством кнопок скольок товаров добавил пользователь в корзину


                # Клавиатура Купить
ikb_buy = InlineKeyboardMarkup(row_width=1)

btn_b_otpraviti_zakaz = InlineKeyboardButton(text='Отправить заказ', callback_data='otpraviti_zakaz')
btn_b_recomand = InlineKeyboardButton(text='ВАЖНО! Подготовка проёма', callback_data='recomanded')
btn_b_back = InlineKeyboardButton(text='Назад', callback_data='back_to_rtb')
btn_b_mm = InlineKeyboardButton(text='Главное меню', callback_data='mm')

ikb_buy.add(btn_b_otpraviti_zakaz).add(btn_b_recomand).add(btn_b_back, btn_b_mm)