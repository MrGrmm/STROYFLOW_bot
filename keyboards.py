from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton


# Клавиатура главного меню

kb_main_menu = ReplyKeyboardMarkup(resize_keyboard=True)

btn_mm_help = KeyboardButton(text='/help')
btn_mm_description = KeyboardButton(text='/description')

kb_main_menu.add(btn_mm_help, btn_mm_description)

# Клавиатура главной страницы
ikb_oficial_page = InlineKeyboardMarkup()

btn_op_catalog = InlineKeyboardButton(text="Каталог", callback_data='catalog')
btn_op_our_works = InlineKeyboardButton(text="Наши работы", callback_data='our_works')
btn_op_buy = InlineKeyboardButton(text="Где купить", callback_data='where_to_buy')
btn_op_company = InlineKeyboardButton(text="Компания", callback_data='company')
btn_op_contacts = InlineKeyboardButton(text="Контакты", callback_data='contacts')

ikb_oficial_page.add(btn_op_catalog, btn_op_our_works, btn_op_buy, btn_op_company, btn_op_contacts) 

# Клавиатура каталога
ikb_catalog = InlineKeyboardMarkup()

btn_catalog_rev_luk = InlineKeyboardButton(text="Ревизионный люк", callback_data='rev_luk')
btn_catalog_san_uzel = InlineKeyboardButton(text="Сантехнический узел", callback_data="san_uzel")
btn_catalog_mm = InlineKeyboardButton(text="Главное меню", callback_data="mm")

ikb_catalog.add(btn_catalog_rev_luk, btn_catalog_san_uzel).add(btn_catalog_mm)

# Клавиатура ревизионный люк
ikb_rev_luk = InlineKeyboardMarkup()

btn_rl_odnost = InlineKeyboardButton(text="Одностворчатый люк",callback_data="ondonst")
btn_rl_dvust = InlineKeyboardButton(text="Двустворчатый люк", callback_data="dvust")
btn_rl_gobrazn = InlineKeyboardButton(text="Г-образный люк", callback_data="gobrazn")
btn_rl_pobrazn = InlineKeyboardButton(text="П-образный люк", callback_data="pobrazn")
btn_rl_podvannu = InlineKeyboardButton(text="Люки под ванну", callback_data="podvannu")
btn_rl_lukdver = InlineKeyboardButton(text="Люки-двери", callback_data="lukdver")
btn_rl_back = InlineKeyboardButton(text="Назад", callback_data="back")
btn_rl_mm = InlineKeyboardButton(text="Главное меню", callback_data="mm")

ikb_rev_luk.add(btn_rl_odnost, btn_rl_dvust).add(btn_rl_gobrazn, btn_rl_pobrazn).add(btn_rl_podvannu, btn_rl_lukdver).add(btn_rl_back, btn_rl_mm)

# Клавиатура выбора своего люка

ikb_view_buy = InlineKeyboardMarkup()

btn_vb_v1 = InlineKeyboardButton(text='Вариант №1', callback_data="v1")
btn_vb_v2 = InlineKeyboardButton(text='Вариант №2', callback_data="v2")
btn_vb_v3 = InlineKeyboardButton(text='Вариант №3', callback_data="v3")
btn_vb_v4 = InlineKeyboardButton(text='Вариант №4', callback_data="v4")
btn_vb_v5 = InlineKeyboardButton(text='Вариант №5', callback_data="v5")
btn_vb_v6 = InlineKeyboardButton(text='Вариант №6', callback_data="v6")
btn_vb_back = InlineKeyboardButton(text='Назад', callback_data="back")
btn_vb_mm = InlineKeyboardButton(text='Главное меню', callback_data="mm")

ikb_view_buy.add(btn_vb_v1, btn_vb_v2, btn_vb_v3).add(btn_vb_v4, btn_vb_v5, btn_vb_v6).add(btn_vb_back, btn_vb_mm)