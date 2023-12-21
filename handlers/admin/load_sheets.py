from openpyxl import load_workbook

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from keyboards import LoadSheets
from db import *
from state import *


@dp.callback_query_handler(text='load_sheets')
async def load_sheets(c: types.CallbackQuery):
    await c.message.answer('Хорошо, выберите таблицу:', reply_markup=LoadSheets.ikb)


@dp.callback_query_handler(text='desc_of_type_persons')
async def desc_of_type_persons(c: types.CallbackQuery, state: FSMContext):
    await c.message.answer('Отлично, отправьте нужную таблицу:')
    await state.set_state(TypePersonal_Money_State.stating.state)

@dp.callback_query_handler(text='desc_of_authory_in_bussiness')
async def desc_of_authory_in_bussiness(c: types.CallbackQuery, state: FSMContext):
    await c.message.answer('Отлично, отправьте нужную таблицу:')
    await state.set_state(AuthorityInBusiness_Money_State.stating.state)

@dp.message_handler(state=TypePersonal_Money_State.stating, content_types=types.ContentTypes.DOCUMENT)
async def desc_of_type_persons_load(m: types.Message, state: FSMContext):
    load_message = await m.answer("Началась загрузка базы сообщений...")
    try:
        await TypePersonal_Money.all().delete()
        file = await dp.bot.get_file(m.document.file_id)
        await dp.bot.download_file(file.file_path, "menu.xlsx")
        wb = load_workbook("menu.xlsx")
        sheet = wb.active
        for cells in sheet.iter_rows():
            item = [cell for cell in cells]
            key = item[0].value
            text = item[1].value
            home_work = item[2].value
            congratulation = item[3].value
            await TypePersonal_Money.create(key=key, text=text, home_work=home_work, congratulation=congratulation)
        await dp.bot.edit_message_text(
            "Отлично база сообщений загружена!",
            chat_id=m.chat.id,
            message_id=load_message.message_id
        )
    except Exception as e:
        await m.answer(e)
        await dp.bot.edit_message_text(
            "При загрузке базы сообщений произошла ошибка. Проверьте структуру файла и повторите попытку.",
            chat_id=m.chat.id,
            message_id=load_message.message_id
        )
    await state.finish()

@dp.message_handler(state=AuthorityInBusiness_Money_State.stating, content_types=types.ContentTypes.DOCUMENT)
async def desc_of_authory_in_bussiness_load(m: types.Message, state: FSMContext):
    load_message = await m.answer("Началась загрузка базы сообщений...")
    try:
        await AuthorityInBusiness_Money.all().delete()
        file = await dp.bot.get_file(m.document.file_id)
        await dp.bot.download_file(file.file_path, "menu.xlsx")
        wb = load_workbook("menu.xlsx")
        sheet = wb.active
        for cells in sheet.iter_rows():
            item = [cell for cell in cells]
            key = item[0].value
            text = item[1].value
            home_work = item[2].value
            congratulation = item[3].value
            await AuthorityInBusiness_Money.create(key=key, text=text, home_work=home_work, congratulation=congratulation)
        await dp.bot.edit_message_text(
            "Отлично база сообщений загружена!",
            chat_id=m.chat.id,
            message_id=load_message.message_id
        )
    except Exception as e:
        await m.answer(e)
        await dp.bot.edit_message_text(
            "При загрузке базы сообщений произошла ошибка. Проверьте структуру файла и повторите попытку.",
            chat_id=m.chat.id,
            message_id=load_message.message_id
        )
    await state.finish()
