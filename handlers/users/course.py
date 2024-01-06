import requests, logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import dp
from keyboards import *
from db import *
from prodamus.prodamus import prodamus_create_url

rates = '<b>Наши тарифы:</b>\n\n' \
        '<b>1. Самостоятельный тариф.</b>\n' \
        'Пошаговое самостоятельное изучение.\n' \
        'Задания раз в три дня.\n' \
        '<b>2. Групповой с кураторами.</b>\n' \
        'Пошаговое изучение.\n' \
        'Общение в общем чате для обмена опытом и инсайтами.\n' \
        'Групповые созвоны с кураторами для ответов на вопросы\n' \
        '<b>3. Персональное сопровождение.</b>\n' \
        'Открыты все шаги\n' \
        'Групповой чат + персональная работа с создателем проекта Кириллом Чеузовым\n\n\n' \
        '<b><i>Короткое видео</i></b>'


@dp.message_handler(text='Начать прямо сейчас', state=Steps.authority1)
async def start_right_now_type_person(m: types.Message, state: FSMContext):
    logging.info(await state.get_state())
    ikb = await UniversalIKB.get_data_from_ikb(state)
    subject_type_name = ''
    r_s1 = await BaseRegistration.filter(tg_id_user=m.from_user.id).all()
    for item1 in r_s1:
        subject_type_name = item1.subject_type_name
    text = ''
    r_s2 = await TypePersonal_Money.filter(key=subject_type_name).all()
    for item2 in r_s2:
        text = item2.description
    await state.set_state(Steps.authority2.state)
    await m.answer(f'<b>Тип личности.</b>\n'
                   f'Короткое видео\n\n'
                   f'{text}', reply_markup=ikb)


@dp.callback_query_handler(text='give_me_task:authority', state=Steps.authority2)
async def give_me_task_authority(c: types.CallbackQuery, state: FSMContext):
    ikb = await UniversalIKB.get_data_from_ikb(state)
    subject_type_name = ''
    r_s1 = await BaseRegistration.filter(tg_id_user=c.from_user.id).all()
    for item1 in r_s1:
        subject_type_name = item1.subject_type_name
    hmwrk = ''
    r_s2 = await TypePersonal_Money.filter(key=subject_type_name).all()
    for item2 in r_s2:
        hmwrk = item2.home_work
    await state.set_state(Steps.profile.state)
    await c.message.answer(f'<b>А вот и ваше задание:</b>\n\n'
                           f'{hmwrk}', reply_markup=ikb)


@dp.callback_query_handler(text='ready_first:authority', state=Steps.profile)
async def ready_first_authority(c: types.CallbackQuery, state: FSMContext):
    ikb = await UniversalIKB.get_data_from_ikb(state)
    subject_type_name = ''
    r_s1 = await BaseRegistration.filter(tg_id_user=c.from_user.id).all()
    for item1 in r_s1:
        subject_type_name = item1.subject_type_name
    cong = ''
    r_s2 = await TypePersonal_Money.filter(key=subject_type_name).all()
    for item2 in r_s2:
        cong = item2.congratulation
    if cong == "":
        cong = "-"
    await state.set_state(Steps.profile1.state)
    await c.message.answer(cong, reply_markup=ikb)


@dp.callback_query_handler(text='go_next:profile', state=Steps.profile1)
async def ready_go_next_profile(c: types.CallbackQuery, state: FSMContext):
    ikb = await UniversalIKB.get_data_from_ikb(state)
    subject_authority_name = ''
    r_s1 = await BaseRegistration.filter(tg_id_user=c.from_user.id).all()
    for item1 in r_s1:
        subject_authority_name = item1.subject_authority_name
    text = ''
    r_s2 = await AuthorityInBusiness_Money.filter(key=subject_authority_name).all()
    for item2 in r_s2:
        text = item2.description
    await state.set_state(Steps.profile2.state)
    await c.message.answer(f'<b>Авторитет.</b>\n'
                           f'Короткое видео\n\n'
                           f'{text}', reply_markup=ikb)
    await c.answer()


@dp.callback_query_handler(text='give_me_task:profile', state=Steps.profile2)
async def give_me_task_profile(c: types.CallbackQuery, state: FSMContext):
    ikb = await UniversalIKB.get_data_from_ikb(state)
    subject_authority_name = ''
    r_s1 = await BaseRegistration.filter(tg_id_user=c.from_user.id).all()
    for item1 in r_s1:
        subject_authority_name = item1.subject_authority_name
    hmwrk = ''
    r_s2 = await AuthorityInBusiness_Money.filter(key=subject_authority_name).all()
    for item2 in r_s2:
        hmwrk = item2.home_work
    await state.set_state(Steps.end_and_buy.state)
    await c.message.answer(f'<b>А вот и ваше задание:</b>\n\n'
                           f'{hmwrk}', reply_markup=ikb)
    await c.answer()


@dp.callback_query_handler(text='ready_first:profile', state=Steps.end_and_buy)
async def ready_first_profile(c: types.CallbackQuery, state: FSMContext):
    ikb = await UniversalIKB.get_data_from_ikb(state)
    subject_authority_name = ''
    r_s1 = await BaseRegistration.filter(tg_id_user=c.from_user.id).all()
    for item1 in r_s1:
        subject_authority_name = item1.subject_authority_name
    cong = ''
    r_s2 = await AuthorityInBusiness_Money.filter(key=subject_authority_name).all()
    for item2 in r_s2:
        cong = item2.congratulation
    if cong == "":
        cong = "-"
    await state.set_state(Steps.end_and_buy1.state)
    await c.message.answer(f'{cong}', reply_markup=ikb)


@dp.callback_query_handler(text='go_next:end_and_buy', state=Steps.end_and_buy1)
async def ready_go_next_profile(c: types.CallbackQuery, state: FSMContext):
    ikb = await UniversalIKB.get_data_from_ikb(state)
    personal_line_id = ''
    design_line_id = ''
    r_s1 = await BaseRegistration.filter(tg_id_user=c.from_user.id).all()
    for item1 in r_s1:
        personal_line_id = item1.personal_line_id
        design_line_id = item1.design_line_id
    description = ''
    r_s2 = await StrategyProfiles_Money.filter(key=f'"{personal_line_id}/{design_line_id}"').all()
    for item2 in r_s2:
        description = item2.description
    await state.set_state(Steps.end_and_buy2.state)
    await c.message.answer(f'<b>Профиль.</b>\n'
                           f'Короткое видео\n\n'
                           f'{description}', reply_markup=ikb)


@dp.callback_query_handler(text='give_me_task:end_and_buy', state=Steps.end_and_buy2)
async def give_me_task_profile(c: types.CallbackQuery, state: FSMContext):
    ikb = await UniversalIKB.get_data_from_ikb(state)
    personal_line_id = ''
    design_line_id = ''
    r_s1 = await BaseRegistration.filter(tg_id_user=c.from_user.id).all()
    for item1 in r_s1:
        personal_line_id = item1.personal_line_id
        design_line_id = item1.design_line_id
    hmwrk = ''
    r_s2 = await StrategyProfiles_Money.filter(key=f'"{personal_line_id}/{design_line_id}"').all()
    for item2 in r_s2:
        hmwrk = item2.home_work
    await state.set_state(Steps.end_and_buy_finish.state)
    await c.message.answer(f'<b>А вот и ваше задание:</b>\n\n'
                           f'{hmwrk}', reply_markup=ikb)
    await c.answer()


@dp.callback_query_handler(text='ready_first:end_and_buy', state=Steps.end_and_buy_finish)
async def ready_first_profile(c: types.CallbackQuery, state: FSMContext):
    ikb = await UniversalIKB.get_data_from_ikb(state)
    personal_line_id = ''
    design_line_id = ''
    r_s1 = await BaseRegistration.filter(tg_id_user=c.from_user.id).all()
    for item1 in r_s1:
        personal_line_id = item1.personal_line_id
        design_line_id = item1.design_line_id
    cong = ''
    r_s2 = await StrategyProfiles_Money.filter(key=f'"{personal_line_id}/{design_line_id}"').all()
    for item2 in r_s2:
        cong = item2.congratulation
    if cong == "":
        cong = "-"
    await c.message.answer(f'{cong}', reply_markup=ikb)
    await c.answer()


@dp.callback_query_handler(text='go_next:end_and_buy_finish', state=Steps.end_and_buy_finish)
async def end_and_buy(c: types.CallbackQuery, state: FSMContext):
    await c.message.answer(
        f'Надеюсь, Ты выполнил(а) все задания и уже видишь, как твой <b>денежный потенциал раскрывается</b> 💰\n'
        f'Но это лишь <b>начало пути</b>. Впереди большая работа, чтобы уверенно встать на свой '
        f'<b>уникальный путь</b> к деньгам и богатству.\n'
        f'Ты уже знаешь, что общие шаблоны не работают и тебе нужно <b>знать свои особенности.</b>\n\n'
        f'Ты готов(а) продолжить работу?', reply_markup=ikb_pre_choice_rate())
    await c.answer()
    await state.finish()

@dp.message_handler(text='Готов(а)')
async def iam_ready_pre_choice_rate(m: types.Message):
    await m.answer(text='Курсы', reply_markup=ikb_products(await Products.filter().all()))
    await m.answer(f'Это верное решение!\n'
                   f'Через год <b>Ты скажешь себе "спасибо"</b>, что принял(а) его сейчас. И нам 🥰\n\n'
                   f'На следующем этапе Ты получишь ещё 6 шагов и заданий, которые дадут тебе <b>глубокое понимание</b> '
                   f'своей природы и <b>четкие руководства</b> для раскрытия денежного потенциала 💰\n\n'
                   f'Тебе осталось <b>выбрать тариф:</b>\n'
                   f'🫂 <b>Групповой</b>, на котором Ты сможешь продолжить общаться с другими участниками программы, которые '
                   f'так же в процессе самопознания и выстраивания взаимоотношений с деньгами.\n\n'
                   f'🔝 <b><u>Персональный с наставником</u></b>, с которым Ты сможешь <b>лично обсудить</b> свою ситуацию '
                   f'и задать вопросы о своём "денежном дизайне". Общение в группе так же входит в тариф 👍',
                   reply_markup=ikb_choice_rate())


@dp.message_handler(text='Познакомиться с наставником 🤑')
async def met_head(m: types.Message):
    await m.answer("Познакомиться с наставником: моё фото или лучше видео.\n"
                   "Твоим наставником будет <b><u>Кирилл Чеузов</u></b> - создатель проекта \"FractalHD.House\" и \"6 систем "
                   "самопознания\". Предприниматель-миллионер, опытный коуч и проводник в  мир духовных практик 🙏\n\n"
                   "В работу с Кириллом входит <b><u>2 часовых созвона и личный чат</u></b> для вопросов.",
                   reply_markup=ikb_choice_rate_after_met_head())


@dp.callback_query_handler(regexp="product[0-9]+")
async def group1(c: types.CallbackQuery, state: FSMContext):
    product = await Products.filter(id=int(c.data.replace("product", ""))).all()
    if len(product) == 0:
        await c.message.answer("Такой товар не найден")
        return
    p = product[0]
    await c.message.answer(p.name, 
        reply_markup=InlineKeyboardMarkup(1).add(
        InlineKeyboardButton(text="Оплата", url=
        prodamus_create_url({
                "id": p.id,
                "name": p.name,
                "price": p.price,
                "quantity": 1,
                "sku": p.price
            }, p.description, c.from_user
        ),
        callback_data="maraphone")))
    await c.answer()

@dp.callback_query_handler(text='maraphone')
async def maraphone(c: types.CallbackQuery, state: FSMContext):
    await c.message.answer('Тут будет начало марафона')
    await c.answer()

@dp.message_handler(text='Начать свой путь к богатству')
async def payment(m: types.Message):
    d_date_zero = ''
    d_time = ''
    d_city = ''
    for item in await BaseRegistration.filter(tg_id_user=m.from_user.id).all():
        d_date_zero = item.born_date
        d_time = item.born_time
        d_city = item.born_city_id
    print("d_date", d_date_zero)
    print("d_time", d_time)
    print("d_city", d_city)
    ddate_y = '.'.join(str(d_date_zero).split('.')[2:3])
    ddate_m = '.'.join(str(d_date_zero).split('.')[1:2])
    ddate_d = '.'.join(str(d_date_zero).split('.')[0:1])
    d_date = f'{ddate_y}-{ddate_m}-{ddate_d}'
    r = requests.get(
        f'https://bodygraph.online/api_v1/bodygraph_fractal.php?dkey=test_public_key&ddate={d_date}&dtime={d_time}&dcity={d_city}')
    soup = r.json()
    print(soup['data']['header']['image'])
    await m.answer_photo(photo=soup['data']['header']['image'])
    print(soup['data']['header']['details'])
    print(soup['data']['header']['centers'])
    print(soup['data']['header']['channels'])
    print(soup['data']['header']['planets'])
    await m.answer('Что продавать - текст')


max_d = {'status': 1,
         'descr': 'Authorized',
         'data':
             {'header':
                  {'paid': 'paid',
                   'paid_at': '2023-12-23 23:13:05',
                   'city': 'Ноябрьск (Ямало-Ненецкий Автономный Округ), Россия',
                   'local_birthdate': '2004-07-15 12:00',
                   'image': 'https://bodygraph.online/bodygraphs/65847aa89e4445.68742549.png',
                   'api_url': 'bodygraph_fractal.php',
                   'bodygraph_id': '34281'},
              'details':
                  {'subject_type_id': '4',
                   'subject_type_name': 'Генератор',
                   'personal_line_id': '3',
                   'personal_line_name': 'Мученик',
                   'design_line_id': '5',
                   'design_line_name': 'Еретик',
                   'profile_id': '5',
                   'profile_name': 'Мученик - Еретик',
                   'subject_authority_id': '2',
                   'subject_authority_name': 'Эмоциональный авторитет',
                   'subject_certainty_id': '3',
                   'subject_certainty_name': 'Тройная определенность'},
              'centers':
                  {
                      '1': {'center_name': 'Теменной центр',
                            'center_state': 'set'},
                      '2': {'center_name': 'Аджна центр',
                            'center_state': 'set'},
                      '3': {'center_name': 'Горловой центр',
                            'center_state': 'unset'},
                      '4': {'center_name': 'Джи центр',
                            'center_state': 'unset'},
                      '5': {'center_name': 'Эго центр',
                            'center_state': 'set'},
                      '6': {'center_name': 'Сакральный центр',
                            'center_state': 'set'},
                      '7': {'center_name': 'Корневой центр',
                            'center_state': 'set'},
                      '8': {'center_name': 'Селезеночный центр',
                            'center_state': 'set'},
                      '9': {'center_name': 'Центр солнечного сплетения',
                            'center_state': 'set'}},
              'channels': {
                  '23': {'id': 23,
                         'channel_gates': '24-61',
                         'channel_desc_name': 'Канал Осознания',
                         'cirquit_name': 'Индивидуальные',
                         'is_os16': False},
                  '25': {'id': 25,
                         'channel_gates': '26-44',
                         'channel_desc_name': 'Канал Передачи',
                         'cirquit_name': 'Племенные',
                         'is_os16': False},
                  '33': {'id': 33,
                         'channel_gates': '37-40',
                         'channel_desc_name': 'Канал Общины',
                         'cirquit_name': 'Племенные',
                         'is_os16': False},
                  '35': {'id': 35,
                         'channel_gates': '42-53',
                         'channel_desc_name': 'Канал Созревания',
                         'cirquit_name': 'Коллективные',
                         'is_os16': False}
                  },
              'planets': {
                  '1': {'id': 1,
                        'planet_name': 'Солнце',
                        'Личность': {
                            '62':
                                {'gate': '62',
                                 'gate_name': 'Ворота Деталей',
                                 'gate_line': '3',
                                 'is_penta': False}
                        },
                        'Дизайн': {
                            '42':
                                {'gate': '42',
                                 'gate_name': 'Ворота Роста',
                                 'gate_line': '5',
                                 'is_penta': False}
                        }
                        },
                  '2': {'id': 2,
                        'planet_name': 'Земля',
                        'Личность': {
                            '61':
                                {'gate': '61',
                                 'gate_name': 'Ворота Тайны',
                                 'gate_line': '3',
                                 'is_penta': False}
                        },
                        'Дизайн': {
                            '32':
                                {'gate': '32',
                                 'gate_name': 'Ворота Преемственности',
                                 'gate_line': '5',
                                 'is_penta': False}
                        }
                        },
                  '3': {'id': 3,
                        'planet_name': 'Луна',
                        'Личность': {
                            '15':
                                {'gate': '15',
                                 'gate_name': 'Ворота Крайностей',
                                 'gate_line': '1',
                                 'is_penta': True}
                        },
                        'Дизайн':
                            {'30':
                                 {'gate': '30',
                                  'gate_name': 'Ворота Признания Чувств',
                                  'gate_line': '4',
                                  'is_penta': False}
                             }
                        },
                  '4': {'id': 4,
                        'planet_name': 'Северный узел',
                        'Личность': {
                            '24':
                                {'gate': '24',
                                 'gate_name': 'Ворота Рационализации',
                                 'gate_line': '1',
                                 'is_penta': False}
                        },
                        'Дизайн': {
                            '24':
                                {'gate': '24',
                                 'gate_name': 'Ворота Рационализации',
                                 'gate_line': '4',
                                 'is_penta': False}
                        }
                        },
                  '5': {'id': 5,
                        'planet_name': 'Южный узел',
                        'Личность': {
                            '44':
                                {'gate': '44',
                                 'gate_name': 'Ворота Бдительности',
                                 'gate_line': '1',
                                 'is_penta': False}
                        },
                        'Дизайн': {
                            '44':
                                {'gate': '44',
                                 'gate_name': 'Ворота Бдительности',
                                 'gate_line': '4',
                                 'is_penta': False}
                        }
                        },
                  '6': {'id': 6,
                        'planet_name': 'Меркурий',
                        'Личность': {
                            '7':
                                {'gate': '7',
                                 'gate_name': 'Ворота Роли Я',
                                 'gate_line': '5',
                                 'is_penta': True}
                        },
                        'Дизайн': {
                            '3':
                                {'gate': '3',
                                 'gate_name': 'Ворота Упорядочивания',
                                 'gate_line': '3',
                                 'is_penta': False}
                        }
                        },
                  '7': {'id': 7,
                        'planet_name': 'Венера',
                        'Личность': {
                            '35':
                                {'gate': '35',
                                 'gate_name': 'Ворота Перемен',
                                 'gate_line': '3',
                                 'is_penta': False}
                        },
                        'Дизайн': {
                            '16':
                                {'gate': '16',
                                 'gate_name': 'Ворота Навыков',
                                 'gate_line': '5',
                                 'is_penta': False}
                        }
                        },
                  '8': {'id': 8,
                        'planet_name': 'Марс',
                        'Личность': {
                            '7':
                                {'gate': '7',
                                 'gate_name': 'Ворота Роли Я',
                                 'gate_line': '1',
                                 'is_penta': True}
                        },
                        'Дизайн': {
                            '35':
                                {'gate': '35',
                                 'gate_name': 'Ворота Перемен',
                                 'gate_line': '5',
                                 'is_penta': False}
                        }
                        },
                  '9': {'id': 9,
                        'planet_name': 'Юпитер',
                        'Личность': {
                            '64':
                                {'gate': '64',
                                 'gate_name': 'Ворота Замешательства',
                                 'gate_line': '5',
                                 'is_penta': False}
                        },
                        'Дизайн': {
                            '40':
                                {'gate': '40',
                                 'gate_name': 'Ворота Одиночества',
                                 'gate_line': '5',
                                 'is_penta': False}
                        }
                        },
                  '10': {'id': 10,
                         'planet_name': 'Сатурн',
                         'Личность': {
                             '53':
                                 {'gate': '53',
                                  'gate_name': 'Ворота Начинаний',
                                  'gate_line': '3',
                                  'is_penta': False}
                         },
                         'Дизайн': {
                             '52':
                                 {'gate': '52',
                                  'gate_name': 'Ворота Бездействия',
                                  'gate_line': '4',
                                  'is_penta': False}
                         }
                         },
                  '11': {'id': 11,
                         'planet_name': 'Уран',
                         'Личность': {
                             '37':
                                 {'gate': '37',
                                  'gate_name': 'Ворота Дружбы',
                                  'gate_line': '1',
                                  'is_penta': False}
                         },
                         'Дизайн': {
                             '55':
                                 {'gate': '55',
                                  'gate_name': 'Ворота Духа',
                                  'gate_line': '6',
                                  'is_penta': False}
                         }
                         },
                  '12': {'id': 12,
                         'planet_name': 'Нептун',
                         'Личность': {
                             '13':
                                 {'gate': '13',
                                  'gate_name': 'Ворота Слушателя',
                                  'gate_line': '2',
                                  'is_penta': True}
                         },
                         'Дизайн': {
                             '13':
                                 {'gate': '13',
                                  'gate_name': 'Ворота Слушателя',
                                  'gate_line': '2',
                                  'is_penta': True}
                         }
                         },
                  '13': {'id': 13,
                         'planet_name': 'Плутон',
                         'Личность': {
                             '26':
                                 {'gate': '26',
                                  'gate_name': 'Ворота Эгоиста',
                                  'gate_line': '4',
                                  'is_penta': False}
                         },
                         'Дизайн': {
                             '26':
                                 {'gate': '26',
                                  'gate_name': 'Ворота Эгоиста',
                                  'gate_line': '6',
                                  'is_penta': False}
                         }
                         },
                  '14': {'id': 14,
                         'planet_name': 'Хирон',
                         'Личность': {
                             '61':
                                 {'gate': '61',
                                  'gate_name': 'Ворота Тайны',
                                  'gate_line': '3',
                                  'is_penta': False}
                         },
                         'Дизайн': {
                             '61':
                                 {'gate': '61',
                                  'gate_name': 'Ворота Тайны',
                                  'gate_line': '6',
                                  'is_penta': False}
                         }
                         }
                  }
              },
         'request': {
             'dkey': 'test_public_key',
             'ddate': '2004-07-15',
             'dtime': '12:00',
             'dcity': '3559',
             'received_at': '2023-12-23 23:13:05',
             'received_from': '88.80.60.183'}
         }
