from aiogram import types

from db import BaseRegistration
from data.config import admin_id
from loader import dp
from keyboards import AdminMenu, TypesBaseRegistration


@dp.message_handler(commands=['admin'])
async def admin_start(m: types.Message):
    if m.from_user.id in admin_id:
        await m.answer('Добрый день!\n'
                       'Выберите действия:', reply_markup=AdminMenu.ikb)


@dp.callback_query_handler(text='check_recs_regs')
async def check_recs_regs(c: types.CallbackQuery):
    await c.message.answer('Хорошо, выберите категорию', reply_markup=TypesBaseRegistration.ikb)


@dp.callback_query_handler(text_startswith='type_reg:')
async def choice_sphere(c: types.CallbackQuery):
    sphere_reg = c.data[9:]
    r_s = await BaseRegistration.filter(sphere=sphere_reg).all()
    for item in r_s:
        await c.message.answer(f'<b>Короткая ссылка:</b> @{item.tg_un_user}\n'
                               f'<b>Сфера:</b> {item.sphere}\n'
                               f'<b>Дата рождения:</b> {item.born_date}\n'
                               f'<b>Время рождения:</b> {item.born_time}\n'
                               f'<b>Город рождения:</b> {item.born_city}')

