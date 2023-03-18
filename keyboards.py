from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton


                # kb Клавиатура главного меню
kb_main_menu = ReplyKeyboardMarkup(resize_keyboard=True)

btn_mm_o_nas = KeyboardButton(text='🪪 О нас')
btn_mm_call = KeyboardButton(text='📞Позвоните мне', request_contact=True)
btn_mm_oformiti_zakaz = KeyboardButton(text='🛒Корзина')

kb_main_menu.add(btn_mm_o_nas).add(btn_mm_call).insert(btn_mm_oformiti_zakaz)


                # Клавиатура Наши продукты
ikb_main_menu = InlineKeyboardMarkup(row_width=2)

btn_imm_rev_luk = InlineKeyboardButton(text="Ревизионный люк", callback_data='rev_luk')
btn_imm_san_uzel = InlineKeyboardButton(text="Сантехнический узел", callback_data="san_uzel")

ikb_main_menu.add(btn_imm_rev_luk).add(btn_imm_san_uzel)


                # Клавиатура FAQ   
ikb_faq = InlineKeyboardMarkup(row_width=2)

btn_faq_vopros = InlineKeyboardButton(text="Задать свой вопрос", callback_data="zadati_vopros")
btn_faq_back_to_rev_luk = InlineKeyboardButton(text='Назад', callback_data='rev_luk')
btn_faq_mm = InlineKeyboardButton(text='Главное меню', callback_data='mm')

ikb_faq.add(btn_faq_vopros).add(btn_faq_back_to_rev_luk, btn_faq_mm)



                # Клавиатура Корзина с покупками
ikb_ready_to_buy = InlineKeyboardMarkup(row_width=1)

btn_rtb_buy = InlineKeyboardButton(text='Оформить заказ!', callback_data='buy')
btn_rtb_udal_iz_korz = InlineKeyboardButton(text='Убрать товар из корзины', callback_data='udal_iz_korz')
btn_rtb_back = InlineKeyboardButton(text='Назад в главное меню', callback_data='mm')

ikb_ready_to_buy.add(btn_rtb_buy).add(btn_rtb_udal_iz_korz).add(btn_rtb_back)



                # Клавиатура Ревизионный люк
ikb_rev_luke = InlineKeyboardMarkup(row_width=3)

btn_rl_last_var = InlineKeyboardButton(text='👈🏼', callback_data='last_var')
btn_rl_next_var = InlineKeyboardButton(text='👉🏼', callback_data='next_var')
btn_rl_vibrati = InlineKeyboardButton(text='Выбрать', callback_data='vibrati')
btn_rl_back = InlineKeyboardButton(text='Назад в главное меню', callback_data='mm')
btn_rl_recomand = InlineKeyboardButton(text='Рекомендации по подготовке проёма', callback_data='recomanded_rl')
btn_rl_faq = InlineKeyboardButton(text='Вопрос/Ответ', callback_data='faq_ikb')

ikb_rev_luke.add(btn_rl_last_var, btn_rl_vibrati, btn_rl_next_var).add(btn_rl_recomand).add(btn_rl_faq).add(btn_rl_back)




                # Клавиатура Люки маленьких размеров
ikb_small_luke = InlineKeyboardMarkup(row_width=3)

btn_sl_200x200 = InlineKeyboardButton(text='200x200', callback_data='200x200')
btn_sl_200x300 = InlineKeyboardButton(text='200x300', callback_data='200x300')
btn_sl_300x300 = InlineKeyboardButton(text='300x300', callback_data='300x300')
btn_sl_300x400 = InlineKeyboardButton(text='300x400', callback_data='300x400')
btn_sl_300x500 = InlineKeyboardButton(text='300x500', callback_data='300x500')
btn_sl_300x600 = InlineKeyboardButton(text='300x600', callback_data='300x600')
btn_sl_400x200 = InlineKeyboardButton(text='400x200', callback_data='400x200')
btn_sl_400x300 = InlineKeyboardButton(text='400x300', callback_data='400x300')
btn_sl_400x400 = InlineKeyboardButton(text='400x400', callback_data='400x400')
btn_sl_400x500 = InlineKeyboardButton(text='400x500', callback_data='400x500')
btn_sl_500x300 = InlineKeyboardButton(text='500x300', callback_data='500x300')
btn_sl_500x400 = InlineKeyboardButton(text='500x400', callback_data='500x400')
btn_sl_back = InlineKeyboardButton(text='Назад', callback_data='rev_luk')
btn_sl_mm = InlineKeyboardButton(text='Главное меню', callback_data='mm')

ikb_small_luke.add(btn_sl_200x200, btn_sl_200x300, btn_sl_300x300).add(btn_sl_300x400, btn_sl_300x500, btn_sl_300x600)
ikb_small_luke.add(btn_sl_400x200, btn_sl_400x300, btn_sl_400x400).add(btn_sl_400x500, btn_sl_500x300, btn_sl_500x400)
ikb_small_luke.add(btn_sl_back, btn_sl_mm)




                # Клавиатура Люки средних размеров
ikb_midle_luke = InlineKeyboardMarkup(row_width=3)

btn_ml_400x600 = InlineKeyboardButton(text='400x600', callback_data='400x600')
btn_ml_400x700 = InlineKeyboardButton(text='400x700', callback_data='400x700')
btn_ml_400x800 = InlineKeyboardButton(text='400x800', callback_data='400x800')
btn_ml_500x500 = InlineKeyboardButton(text='500x500', callback_data='500x500')
btn_ml_500x600 = InlineKeyboardButton(text='500x600', callback_data='500x600')
btn_ml_500x700 = InlineKeyboardButton(text='500x700', callback_data='500x700')
btn_ml_500x800 = InlineKeyboardButton(text='500x800', callback_data='500x800')
btn_ml_600x300 = InlineKeyboardButton(text='600x300', callback_data='600x300')
btn_ml_600x400 = InlineKeyboardButton(text='600x400', callback_data='600x400')
btn_ml_600x500 = InlineKeyboardButton(text='600x500', callback_data='600x500')
btn_ml_600x600 = InlineKeyboardButton(text='600x600', callback_data='600x600')
btn_ml_600x700 = InlineKeyboardButton(text='600x700', callback_data='600x700')
btn_ml_back = InlineKeyboardButton(text='Назад', callback_data='rev_luk')
btn_ml_mm = InlineKeyboardButton(text='Главное меню', callback_data='mm')

ikb_midle_luke.add(btn_ml_400x600, btn_ml_400x700, btn_ml_400x800).add(btn_ml_500x500, btn_ml_500x600, btn_ml_500x700)
ikb_midle_luke.add(btn_ml_500x800, btn_ml_600x300, btn_ml_600x400).add(btn_ml_600x500, btn_ml_600x600, btn_ml_600x700)
ikb_midle_luke.add(btn_ml_back, btn_ml_mm)




                # Клавиатура Люки больших размеров
ikb_big_luke = InlineKeyboardMarkup(row_width=3)

btn_bl_400x900 = InlineKeyboardButton(text='400x900', callback_data='400x900')
btn_bl_400x1000 = InlineKeyboardButton(text='400x1000', callback_data='400x1000')
btn_bl_400x1200 = InlineKeyboardButton(text='400x1200', callback_data='400x1200')
btn_bl_500x900 = InlineKeyboardButton(text='500x900', callback_data='500x900')
btn_bl_500x1000 = InlineKeyboardButton(text='500x1000', callback_data='500x1000')
btn_bl_500x1100 = InlineKeyboardButton(text='500x1100', callback_data='500x1100')
btn_bl_500x1200 = InlineKeyboardButton(text='500x1200', callback_data='500x1200')
btn_bl_600x800 = InlineKeyboardButton(text='600x800', callback_data='600x800')
btn_bl_600x900 = InlineKeyboardButton(text='600x900', callback_data='600x900')
btn_bl_600x1000 = InlineKeyboardButton(text='600x1000', callback_data='600x1000')
btn_bl_600x1100 = InlineKeyboardButton(text='600x1100', callback_data='600x1100')
btn_bl_600x1200 = InlineKeyboardButton(text='600x1200', callback_data='600x1200')
btn_bl_back = InlineKeyboardButton(text='Назад', callback_data='rev_luk')
btn_bl_mm = InlineKeyboardButton(text='Главное меню', callback_data='mm')

ikb_big_luke.add(btn_bl_400x900, btn_bl_400x1000, btn_bl_400x1200).add(btn_bl_500x900, btn_bl_500x1000, btn_bl_500x1100)
ikb_big_luke.add(btn_bl_500x1200, btn_bl_600x800, btn_bl_600x900).add(btn_bl_600x1000, btn_bl_600x1100, btn_bl_600x1200)
ikb_big_luke.add(btn_bl_back, btn_bl_mm)



                # Клавиатура Выбрать вариант
ikb_vibrati_var = InlineKeyboardMarkup(row_width=3)

btn_vv_3d_project = InlineKeyboardButton(text='3D Проект', callback_data='3d_project')
btn_vv_chertej = InlineKeyboardButton(text='Чертёж', callback_data='chertej')
btn_vv_gotovie_raboti = InlineKeyboardButton(text='Работы', callback_data='gotovie_raboti')
btn_vv_dobaviti_v_korzinu = InlineKeyboardButton(text='Добавить в корзину', callback_data='dobaviti_v_korzinu')
btn_vv_back = InlineKeyboardButton(text='Назад', callback_data='rev_luk')
btn_vv_mm = InlineKeyboardButton(text='Главное меню', callback_data='mm')

ikb_vibrati_var.add(btn_vv_3d_project, btn_vv_chertej, btn_vv_gotovie_raboti)
ikb_vibrati_var.add(btn_vv_dobaviti_v_korzinu).add(btn_vv_back, btn_vv_mm)


                # Клавиатура Убрать товар
ikb_ubrati_tovar = InlineKeyboardMarkup(row_width=3)

btn_ut_minus = InlineKeyboardButton(text='-1', callback_data='minus')
btn_ut_minus = InlineKeyboardButton(text='+1', callback_data='plus')
btn_ut_razmer = InlineKeyboardButton(text='Размер', callback_data='razmer')
btn_ut_back = InlineKeyboardButton(text='Назад', callback_data='back_to_rtb')
btn_ut_mm = InlineKeyboardButton(text='Главное меню', callback_data='mm')


                # Клавиатура Купить
ikb_buy = InlineKeyboardMarkup(row_width=1)

btn_b_otpraviti_zakaz = InlineKeyboardButton(text='Отправить заказ', callback_data='otpraviti_zakaz')
btn_b_back = InlineKeyboardButton(text='Назад', callback_data='back_to_rtb')
btn_b_mm = InlineKeyboardButton(text='Главное меню', callback_data='mm')

ikb_buy.add(btn_b_otpraviti_zakaz).add(btn_b_back, btn_b_mm)


                # Клавиатура Рекомендации по подготовке проёма от ревизионный люк
ikb_recomanded_rl = InlineKeyboardMarkup(row_width=2)

btn_rrl_back = InlineKeyboardButton(text='Назад', callback_data='rev_luk')
btn_rrl_mm = InlineKeyboardButton(text='Главное меню', callback_data='mm')

ikb_recomanded_rl.add(btn_rrl_back, btn_rrl_mm)


                # Клавиатура Рекомендации по подготовке проёма от купить
ikb_recomanded_buy = InlineKeyboardMarkup(row_width=2)

btn_rb_back_to_buy = InlineKeyboardButton(text='Вернуться к покупке', callback_data='rev_luk')

ikb_recomanded_buy.add(btn_rb_back_to_buy)



                #Клавиатура сантехнические узлы
ikb_san_uzel = InlineKeyboardMarkup(row_width=1)

btn_su_back = InlineKeyboardButton(text='Назад в главное меню', callback_data='mm')

ikb_san_uzel.add(btn_su_back)

