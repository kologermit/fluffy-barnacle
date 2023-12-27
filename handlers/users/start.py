import requests
from aiogram.dispatcher import FSMContext
from aiogram.utils.deep_linking import get_start_link, decode_payload

from db import *
from loader import dp
from keyboards import *
from state import *
from .logger import *


@dp.message_handler(commands=['start'])
@dp.message_handler(commands=['start'], state=Start.states)
async def start(m: types.Message, state: FSMContext):
    await state.finish()
    args = m.get_args()
    reference = decode_payload(args)
    tg_id_ref_ = ''
    r_s = await ReferalProgram.filter(tg_un_ref=reference).all()
    for item in r_s:
        tg_id_ref_ = item.tg_id_ref
    if tg_id_ref_ == m.from_user.id:
        await m.answer('Извините но отрывать свою же реферальную ссылку запрещено!', reply_markup=ikb_main_menu())
        return
    r_s = await ReferalProgram.filter(sell_invited=m.from_user.id).all()
    if len(r_s) != 0:
        await m.answer('Открывать реферальную ссылку можно только 1 раз!', reply_markup=ikb_main_menu())
        return

    async def answer_photo():
        await m.answer_photo(
            photo='https://sun9-11.userapi.com/impg/ORM9shXVuyn4TF_RBWvGCSzaZwBOLaOYX9haTQ/ksZDIASRC6U.jpg?size=1024x768&quality=95&sign=8d22b1842fc51480520e4e0e243660ae&type=album',
            caption=f'{m.from_user.first_name.capitalize()}, добрый день ☀️\n\n'
                    f'Я - Фракталик 🪬 Бот от создателей проекта @Fractal_HD ✨\n\n'
                    f'Я смогу показать тебе твой персональный путь к счастью, любви и богатству 🙌\n'
                    f'И помогу гармонизировать свою жизнь во всех её сферах:\n'
                    f'- Деньгах 💰\n'
                    f'- Отношениях 💞\n'
                    f'- Талантах ⭐️\n'
                    f'- Здоровье 🧬\n'
                    f'- Воспитании детей 👶\n\n'
                    f'Персонально. Понятно. Практично!\n\n'
                    f'Просто выбери сферу и введи данные о рождении 📆\n'
                    f'И Я дам пошаговый алгоритм действий 👣\n\n'
                    f'Твой Фракталик 🫶', reply_markup=ikb_im_ready())

    try:
        await ReferalProgram.filter(tg_id_ref=tg_id_ref_, sell_invited=1).delete()
        await ReferalProgram.create(tg_id_ref=tg_id_ref_,
                                    tg_un_ref=reference,
                                    sell_invited=m.from_user.id)
        await answer_photo()
        await m.answer(f'Отлично, рад что наша семья пополняется!\n Бонусы уже отправлены вашему приглашенному!')
        await dp.bot.send_message(tg_id_ref_, 'Привет, по твоей ссылке перешел человек!')
        return
    except Exception:
        await answer_photo()


@dp.message_handler(text='Пригласить друга')
async def add_friend(m: types.Message):
    message_logger(m, "start:referal_friend")
    link = await get_start_link(str(m.from_user.username), encode=True)
    await m.answer(f'Предложение пригласить в марафон друга и получить 20% от его покупки.\n\n'
                   f'<b>Ваша персональная ссылка:</b>\n'
                   f'{link}')
    await ReferalProgram.create(tg_id_ref=m.from_user.id,
                                tg_un_ref=m.from_user.username,
                                sell_invited=True)


@dp.message_handler(text='Перейти к программе')
async def go_to_program(m: types.Message):
    message_logger(m, "start:tap_to_start")
    await m.answer('Нажмите ниже чтобы начать!', reply_markup=ikb_im_ready())


@dp.message_handler(text='Я готов!')
async def im_ready(m: types.Message, state: FSMContext):
    message_logger(m, "start:ready")
    if len(await BaseRegistration.filter(tg_id_user=m.from_user.id).all()) != 0:
        await m.answer("Какие данные загрузить?", reply_markup=ikb_start_new_or_old_data())
        await state.set_state(Start.new_or_old_data.state)
        return
    await m.answer('Выберите сферу жизни, которую мы будет улучшать', reply_markup=ikb_choice_sphere())
    await state.set_state(Start.sphere.state)


@dp.message_handler(state=Start.sphere)
async def wht_sphere(m: types.Message, state: FSMContext):
    message_logger(m, "start:sphere")
    if m.text == 'Деньги и карьера 💰':
        await m.answer_photo(
            photo='https://sun9-13.userapi.com/impg/6pXf4tiBwDZYdd3mfPmRZjVK7Cqd3w1koO-j2Q/KsubM2CGFWY.jpg?size=1280x853&quality=95&sign=3b604ae521ed0ea0effb37f3d8b7e0f2&type=album',
            caption='Введите данные о человеке, который будет проходить марафон')
    if m.text == 'Здоровье и жизненная энергия ⚡️':
        await m.answer_photo(
            photo='https://sun9-2.userapi.com/impg/oJ51HViXpLcbtv5CdhcRblG3dHt6LmS0JcICNg/eTWVQ-cxxfM.jpg?size=1024x768&quality=95&sign=d398f1cbc0f8b23e6744b800914de740&type=album',
            caption='Введите данные о человеке, который будет проходить марафон')
    if m.text == 'Отношения  (в разработке) ❤️ и 🤝':
        await m.answer_photo(
            photo='https://sun9-52.userapi.com/impg/lvKJ75Klkwf6OPAZEc3AFDWh2K8n9wDiw_bYVA/zyQOwIV390o.jpg?size=1024x768&quality=95&sign=e2644870c57dd7438e1d7e32b4549a75&type=album',
            caption='Введите данные о человеке, который будет проходить марафон')
    if m.text == 'Воспитание ребенка 👶':
        await m.answer_photo(
            photo='https://sun9-40.userapi.com/impg/lgYJCOjvS2Dim707_YkZOA35GmmH9sncaNDqgQ/9f6eDoz9-AQ.jpg?size=1024x768&quality=95&sign=4e11bac3dc704767011cc823eaa64d0a&type=album',
            caption='Введите данные о человеке, который будет проходить марафон')
    if m.text == 'Таланты и предназначение ⭐️':
        await m.answer_photo(
            photo='https://sun9-15.userapi.com/impg/4CCv99AN3l75Mz-vnGe0Q8SN0dzonFlqXhPtFQ/cIHXhUrFYiU.jpg?size=1024x768&quality=95&sign=1280832c8adebf72ef3f76ed168a59b5&type=album',
            caption='Введите данные о человеке, который будет проходить марафон')
    await state.update_data(sphere=m.text)

    await m.answer('Введите <b>ИМЯ</b> человека, который будет менять свою жизнь 🚀')
    await state.set_state(Start.name.state)


@dp.message_handler(state=Start.new_or_old_data)
async def new_or_old_data(m: types.Message, state: FSMContext):
    message_logger(m, "start:new_or_old_data")
    if m.text == 'Выбрать старые данные':
        ikb_choice_data = types.InlineKeyboardMarkup(inline_keyboard=[])
        for item in await BaseRegistration.filter(tg_id_user=m.from_user.id).all():
            ikb_choice_data.add(types.InlineKeyboardButton(text=f'{item.name} {item.born_date}',
                                                           callback_data=f'choice_data:{item.id}'))
        await state.finish()
        await m.answer('Выберите данные по кнопке ниже:', reply_markup=ikb_choice_data)
        return
    if m.text == 'Ввести новые данные':
        await state.update_data(is_new_data=True)
        await m.answer('Выберите сферу жизни, которую мы будет улучшать', reply_markup=ikb_choice_sphere())
        await state.set_state(Start.sphere.state)
        return


@dp.message_handler(state=Start.name)
async def name_s(m: types.Message, state: FSMContext):
    message_logger(m, "start:name")
    await m.answer('Отлично, теперь введите его <b>дату</b> рождения в формате ДД.ММ.ГГГГ:\n'
                   '<b>Например 12.08.1990</b>')
    await state.update_data(name=m.text)
    await state.set_state(Start.born_date.state)


@dp.message_handler(state=Start.born_date)
async def date_born(m: types.Message, state: FSMContext):
    message_logger(m, "start:born_date")
    if len(m.text) != 10:
        await m.answer('К сожалению, Я не понимаю дату 😒\n'
                       'Введи, пожалуйста, в таком виде\n'
                       '👉 День.Месяц.Год 📆\n\n'
                       'Твой Фракталик 🫶')
        return
    if any(item in "йцукенгшщзхъфывапролджэячсмитьбюqwertyuiopasdfghjklzxcvbnm-,:;!_*+()/#¤%&)" for item in m.text):
        await m.answer('К сожалению, Я не понимаю дату 😒\n'
                       'Введи, пожалуйста, в таком виде\n'
                       '👉 День.Месяц.Год 📆\n\n'
                       'Твой Фракталик 🫶')
        return
    if any(item not in ".1234567890" for item in m.text):
        await m.answer('К сожалению, Я не понимаю дату 😒\n'
                       'Введи, пожалуйста, в таком виде\n'
                       '👉 День.Месяц.Год 📆\n\n'
                       'Твой Фракталик 🫶')
        return
    await state.update_data(born_date=m.text)
    await m.answer('Отлично, теперь <b>время</b> его рождения в формате ЧЧ:ММ:\n'
                   '<b>Например: 13:30</b>')
    await state.set_state(Start.born_time.state)


@dp.message_handler(state=Start.born_time)
async def time_born(m: types.Message, state: FSMContext):
    message_logger(m, "start:born_time")
    if len(m.text) != 5 or \
            any(item in "йцукенгшщзхъфывапролджэячсмитьбюqwertyuiopasdfghjklzxcvbnm.,;!_*+()/#¤%&)" for item in
                m.text) or \
            any(item not in ":1234567890" for item in m.text):
        await m.answer('К сожалению, Я не понимаю время, которое Ты написал 😢\n'
                       'Введи, пожалуйста, время в таком виде\n'
                       '👉 Часы:Минуты ⏰\n\n'
                       'Твой Фракталик 🫶')
        return
    await state.update_data(born_time=m.text)
    await m.answer('А сейчас напишите его <u><b>город рождения</b></u> (современное название) 🌇\n'
                   'Например: Москва или Санкт-Петербург (не Ленинград).\n\n'
                   'P.S.: Если этот город совсем не большой, то напиши <b><u>ближайший крупный город в том же часовом поясе 🌐</u></b>')
    await state.set_state(Start.born_city.state)


@dp.message_handler(state=Start.born_city)
async def city_born(m: types.Message, state: FSMContext):
    message_logger(m, "start:born_city")
    if any(item in ".,:;!_*+()/#¤%&)1234567890" for item in m.text):
        await m.answer('К сожалению, Я не могу понять про какой город ты говоришь 😕\n'
                       'Введи, пожалуйста, официальное название города и без спецсимволов и цифр\n'
                       'Например: Москва или Санкт-Петербург 🌏\n\n'
                       'Твой Фракталик 🫶')
        return
    await state.update_data(born_city=m.text)
    c_d = await state.get_data()
    await m.answer(f'<b>Проверьте ваши данные и затем нажмите на соответствующую кнопку!</b>\n\n'
                   f'<b>Сфера:</b> {c_d["sphere"]}\n'
                   f'<b>Имя человека:</b> {c_d["name"]}\n'
                   f'<b>Дата рождения:</b> {c_d["born_date"]}\n'
                   f'<b>Время рождения:</b> {c_d["born_time"]}\n'
                   f'<b>Город рождения:</b> {c_d["born_city"]}',
                   reply_markup=SendOrDelData.ikb)


@dp.callback_query_handler(text='del_data', state=Start.born_city)
async def del_data(c: types.CallbackQuery, state: FSMContext):
    callback_logger(c, "start:del_data")
    await c.message.delete()
    await c.message.answer('Хорошо, ваши данные удалены!')
    await state.finish()
    await c.clean()


@dp.callback_query_handler(text='send_data', state=Start.born_city)
async def send_data(c: types.CallbackQuery, state: FSMContext):
    callback_logger(c, "start:send_data")
    c_d = await state.get_data()
    print(c_d.values())
    r = requests.get('https://bodygraph.online/api_v1/city_list.php?dkey=test_public_key')
    soup = r.json()
    city_id = 0
    text_city = f'{c_d["born_city"]}'
    list_country = {'AU', 'AT', 'AZ', 'DZ', 'AO', 'AR', 'AM', 'BY', 'BE', 'BG', 'BR', 'GB', 'HU', 'VE', 'VN', 'GH',
                    'GN', 'DE', 'GR', 'GE', 'DK', 'CD', 'DO', 'EG', 'ZW', 'IL', 'IN', 'ID', 'IQ', 'IR', 'IE', 'ES',
                    'IT', 'KZ', 'CM', 'CA', 'KE', 'CY', 'CN', 'CO', 'CI', 'CU', 'KG', 'LV', 'LB', 'LT', 'LU', 'MG',
                    'MK', 'MY', 'MT', 'MA', 'MX', 'MZ', 'MD', 'MC', 'NG', 'NL', 'NZ', 'NO', 'AE', 'PK', 'PY', 'PE',
                    'PL', 'PT', 'RU', 'RO', 'SM', 'SA', 'KP', 'SN', 'RS', 'SG', 'SY', 'SK', 'SI', 'US', 'TJ', 'TH',
                    'TW', 'TZ', 'TN', 'TM', 'TR', 'UZ', 'UA', 'UY', 'PH', 'FI', 'FR', 'HR', 'ME', 'CZ', 'CL', 'CH',
                    'SE', 'EC', 'EE', 'ET', 'KR', 'JP'}
    for item_country in list_country:
        for item in soup['data']['country'][item_country]['сities']:
            if text_city in str(soup['data']['country'][item_country]['сities'][item]):
                if soup['data']['country'][item_country]['сities'][item]['city_name_rus'] == text_city:
                    city_id = soup['data']['country'][item_country]['сities'][item]['id']

    ddate_y = '.'.join(str(c_d["born_date"]).split('.')[2:3])
    ddate_m = '.'.join(str(c_d["born_date"]).split('.')[1:2])
    ddate_d = '.'.join(str(c_d["born_date"]).split('.')[0:1])
    if str(ddate_m[:1]) == '0':
        ddate_m = ddate_m[1:]
    ddate = f'{ddate_y}-{ddate_m}-{ddate_d}'
    dtime = str(c_d["born_time"])
    city_id = str(city_id)
    r = requests.get(
        f'https://bodygraph.online/api_v1/bodygraph_fractal_min.php?dkey=test_public_key&ddate={ddate}&dtime={dtime}&dcity={city_id}')
    soup = r.json()
    print(soup)
    status = soup['status']
    descr = soup['descr']
    # === data
    # header
    city = soup['data']['header']['city']
    local_birthdate = soup['data']['header']['local_birthdate']
    api_url = soup['data']['header']['api_url']
    bodygraph_id = soup['data']['header']['bodygraph_id']
    # details
    subject_type_id = soup['data']['details']['subject_type_id']
    subject_type_name = soup['data']['details']['subject_type_name']
    personal_line_id = soup['data']['details']['personal_line_id']
    personal_line_name = soup['data']['details']['personal_line_name']
    design_line_id = soup['data']['details']['design_line_id']
    design_line_name = soup['data']['details']['design_line_name']
    profile_id = soup['data']['details']['profile_id']
    profile_name = soup['data']['details']['profile_name']
    subject_authority_id = soup['data']['details']['subject_authority_id']
    subject_authority_name = soup['data']['details']['subject_authority_name']
    # === request
    dkey = soup['request']['dkey']
    ddate = soup['request']['ddate']
    dtime = soup['request']['dtime']
    dcity = soup['request']['dcity']
    received_at = soup['request']['received_at']
    received_from = soup['request']['received_from']
    for user in await BaseRegistration.filter(tg_id_user=c.from_user.id):
        await user.delete()
    await BaseRegistration.create(tg_id_user=c.from_user.id,
                                  tg_un_user=c.from_user.username,
                                  name=c_d["name"],
                                  sphere=c_d["sphere"],
                                  born_date=c_d["born_date"],
                                  born_time=c_d["born_time"],
                                  born_city=f'{c_d["born_city"]} - {city_id}',
                                  subject_type_id=subject_type_id,
                                  subject_type_name=subject_type_name,
                                  personal_line_id=personal_line_id,
                                  personal_line_name=personal_line_name,
                                  design_line_id=design_line_id,
                                  design_line_name=design_line_name,
                                  profile_id=profile_id,
                                  profile_name=profile_name,
                                  subject_authority_id=subject_authority_id,
                                  subject_authority_name=subject_authority_name
                                  )
    if design_line_name == "Мученик":
        await c.message.answer(
            f'<b>{c_d["name"]}</b> - {str(subject_authority_name).capitalize().replace(" авторитет", "")} {str(subject_type_name).capitalize()}\n'
            f'{personal_line_id}/{design_line_id} ({str(personal_line_name).capitalize()}/Экспериментатор)')
    else:
        await c.message.answer(
            f'<b>{c_d["name"]}</b> - {str(subject_authority_name).capitalize().replace(" авторитет", "")} {str(subject_type_name).capitalize()}\n'
            f'{personal_line_id}/{design_line_id} ({str(personal_line_name).capitalize()}/{str(design_line_name).capitalize()})')
    if c_d["sphere"] == "Деньги и карьера 💰":
        await c.message.answer(f'Благодарю за доверие 🙏\n\n'
                               f'Теперь Я смогу подобрать для тебя твои персональные ключики к раскрытию твоего денежного потенциала 💰\n\n'
                               f'Давай начнем прямо сейчас?\n\n'
                               f'Твой Фракталик 🫶',
                               reply_markup=ikb_start_right_now())
    if c_d["sphere"] == "Здоровье и жизненная энергия ⚡️":
        pass
    if c_d["sphere"] == "Отношения  (в разработке) ❤️ и 🤝":
        pass
    if c_d["sphere"] == "Таланты и предназначение ⭐️":
        pass
    if c_d["sphere"] == "Воспитание ребенка 👶":
        pass
    await state.finish()
    await c.clean()


@dp.callback_query_handler(text_startswith='choice_data')
async def choice_data(c: types.CallbackQuery, state: FSMContext):
    id_check = ':'.join(str(c.data).split(':')[1:2])
    for item in await BaseRegistration.filter(id=id_check).all():
        if item.design_line_name == "Мученик":
            await c.message.answer(
                f'<b>{item.name}</b> - {str(item.subject_authority_name).capitalize().replace(" авторитет", "")} {str(item.subject_type_name).capitalize()}\n'
                f'{item.personal_line_id}/{item.design_line_id} ({str(item.personal_line_name).capitalize()}/Экспериментатор)')
        else:
            await c.message.answer(
                f'<b>{item.name}</b> - {str(item.subject_authority_name).capitalize().replace(" авторитет", "")} {str(item.subject_type_name).capitalize()}\n'
                f'{item.personal_line_id}/{item.design_line_id} ({str(item.personal_line_name).capitalize()}/{str(item.design_line_name).capitalize()})')
        if item.sphere == "Деньги и карьера 💰":
            await c.message.answer(f'Благодарю за доверие 🙏\n\n'
                                   f'Теперь Я смогу подобрать для тебя твои персональные ключики к раскрытию твоего денежного потенциала 💰\n\n'
                                   f'Давай начнем прямо сейчас?\n\n'
                                   f'Твой Фракталик 🫶',
                                   reply_markup=ikb_start_right_now())
        if item.sphere == "Здоровье и жизненная энергия ⚡️":
            pass
        if item.sphere == "Отношения  (в разработке) ❤️ и 🤝":
            pass
        if item.sphere == "Таланты и предназначение ⭐️":
            pass
        if item.sphere == "Воспитание ребенка 👶":
            pass
    await c.clean()
