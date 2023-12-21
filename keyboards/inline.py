from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class ShareOrReadyAuthority:
    btn1 = InlineKeyboardButton(text='Обсудить в общем чате 🗣', url='https://t.me/c/2142529593/2')
    btn2 = InlineKeyboardButton(text='Получить задание 📝', callback_data='give_me_task:authority')
    ikb_text = InlineKeyboardMarkup(1).add(btn1, btn2)

    btn3 = InlineKeyboardButton(text='Выполнил!', callback_data='ready_first:authority')
    ikb_work = InlineKeyboardMarkup(1).add(btn3)

    btn4 = InlineKeyboardButton(text='Поделиться опытом 👍', url='https://t.me/c/2142529593/2')
    btn5 = InlineKeyboardButton(text='Идём дальше 🚀', callback_data='go_next:profile')
    ikb_congratulation = InlineKeyboardMarkup(1).add(btn4, btn5)

class ShareOrReadyProfile:
    btn1 = InlineKeyboardButton(text='Обсудить в общем чате 🗣', url='https://t.me/c/2142529593/2')
    btn2 = InlineKeyboardButton(text='Получить задание 📝', callback_data='give_me_task:profile')
    ikb_text = InlineKeyboardMarkup(1).add(btn1, btn2)

    btn3 = InlineKeyboardButton(text='Выполнил!', callback_data='ready_first:profile')
    ikb_work = InlineKeyboardMarkup(1).add(btn3)

    btn4 = InlineKeyboardButton(text='Поделиться опытом 👍', url='https://t.me/c/2142529593/2')
    btn5 = InlineKeyboardButton(text='Идём дальше 🚀', callback_data='go_next:end_and_buy')
    ikb_congratulation = InlineKeyboardMarkup(1).add(btn4, btn5)

class ShareOrReadyBuy:
    btn1 = InlineKeyboardButton(text='Обсудить в общем чате 🗣', url='https://t.me/c/2142529593/2')
    btn2 = InlineKeyboardButton(text='Получить задание 📝', callback_data='give_me_task:end_and_buy')
    ikb_text = InlineKeyboardMarkup(1).add(btn1, btn2)

    btn3 = InlineKeyboardButton(text='Выполнил!', callback_data='ready_first:end_and_buy')
    ikb_work = InlineKeyboardMarkup(1).add(btn3)

    btn4 = InlineKeyboardButton(text='Поделиться опытом 👍', url='https://t.me/c/2142529593/2')
    btn5 = InlineKeyboardButton(text='Идём дальше 🚀', callback_data='go_next:end_and_buy:finish')
    ikb_congratulation = InlineKeyboardMarkup(1).add(btn4, btn5)

class NewOrOldData:
    btns = [
        InlineKeyboardButton(text='Ввести новые данные', callback_data='start:sphere:new_data'),
        InlineKeyboardButton(text='Выбрать старые данные', callback_data='start:sphere:new_data'),
    ]
    ikb = InlineKeyboardMarkup(1).add(*btns)

class SendOrDelData:
    btn1 = InlineKeyboardButton(text='Удалить❌', callback_data='del_data')
    btn2 = InlineKeyboardButton(text='Отправить✅', callback_data='send_data')
    ikb = InlineKeyboardMarkup(1).add(btn1, btn2)