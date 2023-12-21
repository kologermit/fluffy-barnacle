from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class AdminMenu:
    btn1 = InlineKeyboardButton(text='Посмотреть записи регистрации (Base)', callback_data='check_recs_regs')
    btn2 = InlineKeyboardButton(text='Загрузка таблиц', callback_data='load_sheets')
    ikb = InlineKeyboardMarkup(1).add(btn1, btn2)

class LoadSheets:
    btns = [
        InlineKeyboardButton(text='Описание по типам личности', callback_data='desc_of_type_persons'),
        InlineKeyboardButton(text='Авторитеты в бизнесе', callback_data='desc_of_authory_in_bussiness'),
        InlineKeyboardButton(text='Стратегия профиля в бизнесе', callback_data='desc_of_strategy_profiles'),
    ]
    ikb = InlineKeyboardMarkup(1).add(*btns)

class TypesBaseRegistration:
    btn1 = InlineKeyboardButton(text='Деньги и карьера 💰', callback_data='type_reg:Деньги')
    btn2 = InlineKeyboardButton(text='Здоровье и жизненная энергия ⚡️', callback_data='type_reg:Здоровье')
    btn3 = InlineKeyboardButton(text='Отношения  (в разработке) ❤️ и 🤝', callback_data='type_reg:Отношения')
    btn4 = InlineKeyboardButton(text='Воспитание ребенка 👶', callback_data='type_reg:Воспитание ребенка')
    btn5 = InlineKeyboardButton(text='Таланты и предназначение ⭐️', callback_data='type_reg:Таланты и предназначение')
    ikb = InlineKeyboardMarkup(1).add(btn1, btn2, btn3, btn4, btn5)