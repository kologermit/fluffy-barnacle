from openpyxl import load_workbook

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from keyboards import *
from db import *
from state import *


@dp.callback_query_handler(text='output_sheets')
async def output_sheets(c: types.CallbackQuery):
    await c.message.answer('Хорошо, выберите таблицу:', reply_markup=OutputSheets.ikb)
    await c.clean()

@dp.callback_query_handler(text='output_type_persons')
async def output_type_persons(c: types.CallbackQuery):
    types = await TypePersonal_Money.filter().all()
    await c.message.answer(text='Вот таблица типов личностей:')
    for t in types:
        await c.message.answer(f"""Id: {t.id}
Key: {t.key}
Description: {t.description}
Home Work: {t.home_work}
Congratulations: {t.congratulation}""")
    await c.clean()
        
@dp.callback_query_handler(text='output_authory_in_business')
async def output_authory_in_business(c: types.CallbackQuery):
    authory = await AuthorityInBusiness_Money.filter().all()
    await c.message.answer(text='Вот таблица авторитетов в бизвесе:')
    for a in authory:
        await c.message.answer(f"""Id: {a.id}
Key: {a.key}
Description: {a.descriprion}
Home Work: {a.home_work}
Congratulations: {a.congratulation}""")
    await c.clean()
        
@dp.callback_query_handler(text='output_strategy_profiles')
async def output_strategy_profiles(c: types.CallbackQuery):
    profiles = await StrategyProfiles_Money.filter().all()
    await c.message.answer(text='Вот таблица стратегий')
    for p in profiles:
        await c.message.answer(f"""Id: {p.id}
Key: {p.key}
Name: {p.name}
Description: {p.description}
Home Work: {p.home_work}
Congratulations: {p.congratulation}""")
    await c.clean()
        
@dp.callback_query_handler(text='output_products')
async def output_products(c: types.CallbackQuery):
    products = await Products.filter().all()
    await c.message.answer("Вот таблица товаров")
    for p in products:
        await c.message.answer(text=f"""Id: {p.id}
Name: {p.name}
Price: {p.price}
Description: {p.description}""")
    await c.clean()