from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from aiogram.dispatcher import FSMContext

from state import Steps


class UniversalIKB:

    @staticmethod
    async def get_data_from_ikb(state: FSMContext):
        check_on_keyboard = ':'.join(str(await state.get_state()).split(':')[1:2])
        key = f"{':'.join(str(await state.get_state()).split(':')[1:2])[:-1] if ':'.join(str(await state.get_state()).split(':')[1:2])[-1:].isdigit() else ':'.join(str(await state.get_state()).split(':')[1:2])}"
        ikb = []
        if str(check_on_keyboard)[-1:].isdigit():
            if str(check_on_keyboard)[-1:] == '1':
                btn1 = InlineKeyboardButton(text='Обсудить в общем чате 🗣', url='https://t.me/c/2142529593/2')
                btn2 = InlineKeyboardButton(text='Получить задание 📝', callback_data=f'give_me_task:{key}')
                ikb = InlineKeyboardMarkup(1).add(btn1, btn2)
            if str(check_on_keyboard)[-1:] == '2':
                btn3 = InlineKeyboardButton(text='Выполнил!', callback_data=F'ready_first:{key}')
                ikb = InlineKeyboardMarkup(1).add(btn3)
        else:
            btn4 = InlineKeyboardButton(text='Поделиться опытом 👍', url='https://t.me/c/2142529593/2')
            btn5 = InlineKeyboardButton(text='Идём дальше 🚀', callback_data=f'go_next:{key}')
            ikb = InlineKeyboardMarkup(1).add(btn4, btn5)
        return ikb


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