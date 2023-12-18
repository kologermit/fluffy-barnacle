from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def ikb_im_ready():
    kb_im_ready = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    btn1 = KeyboardButton(text="Я готов!")
    kb_im_ready.add(btn1)
    return kb_im_ready


def ikb_choice_sphere():
    kb_choice_sphere = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    btn1 = KeyboardButton(text="Деньги и карьера 💰")
    btn2 = KeyboardButton(text="Здоровье и жизненная энергия ⚡️")
    btn3 = KeyboardButton(text="Отношения  (в разработке) ❤️ и 🤝")
    btn4 = KeyboardButton(text="Воспитание ребенка 👶")
    btn5 = KeyboardButton(text="Таланты и предназначение ⭐️")
    kb_choice_sphere.add(btn1, btn2, btn3, btn4, btn5)
    return kb_choice_sphere


def ikb_start_right_now():
    kb_start_right_now = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    btn1 = KeyboardButton(text="Начать прямо сейчас")
    kb_start_right_now.add(btn1)
    return kb_start_right_now


def ikb_main_menu():
    kb_main_menu = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    btn1 = KeyboardButton(text="Перейти к программе")
    btn2 = KeyboardButton(text="Пригласить друга")
    kb_main_menu.add(btn1, btn2)
    return kb_main_menu


def ikb_pre_choice_rate():
    kb_choice_rate = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    btn1 = KeyboardButton(text="Готов(а)")
    btn2 = KeyboardButton(text="Проработать другую сферу")
    kb_choice_rate.add(btn1, btn2)
    return kb_choice_rate

def ikb_choice_rate():
    kb_choice_rate = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    btn2 = KeyboardButton(text="Групповой тариф за 4990 рублей")
    btn3 = KeyboardButton(text="Работа с наставником 14990 рублей")
    btn4 = KeyboardButton(text="Познакомиться с наставником 🤑")
    kb_choice_rate.add(btn2, btn3, btn4)
    return kb_choice_rate

def ikb_choice_rate_after_met_head():
    kb_choice_rate = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    btn2 = KeyboardButton(text="Групповой тариф")
    btn3 = KeyboardButton(text="Работа с наставником")
    kb_choice_rate.add(btn2, btn3)
    return kb_choice_rate

def ikb_start_marathon():
    kb_start_right_now = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    btn1 = KeyboardButton(text="Начать свой путь к богатству")
    kb_start_right_now.add(btn1)
    return kb_start_right_now