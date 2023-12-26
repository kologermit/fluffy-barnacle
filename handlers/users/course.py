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


@dp.message_handler(text='Начать прямо сейчас')
async def start_right_now_type_person(m: types.Message):
    subject_type_name = ''
    r_s1 = await BaseRegistration.filter(tg_id_user=m.from_user.id).all()
    for item1 in r_s1:
        subject_type_name = item1.subject_type_name
    text = ''
    r_s2 = await TypePersonal_Money.filter(key=subject_type_name).all()
    for item2 in r_s2:
        text = item2.description
    await m.answer(f'<b>Тип личности.</b>\n'
                   f'Короткое видео\n\n'
                   f'{text}', reply_markup=ShareOrReadyAuthority.ikb_text)


@dp.callback_query_handler(text='give_me_task:authority')
async def give_me_task_authority(c: types.CallbackQuery, state: FSMContext):
    subject_type_name = ''
    r_s1 = await BaseRegistration.filter(tg_id_user=c.from_user.id).all()
    for item1 in r_s1:
        subject_type_name = item1.subject_type_name
    hmwrk = ''
    r_s2 = await TypePersonal_Money.filter(key=subject_type_name).all()
    for item2 in r_s2:
        hmwrk = item2.home_work
    await c.message.answer(f'<b>А вот и ваше задание:</b>\n\n'
                           f'{hmwrk}', reply_markup=ShareOrReadyAuthority.ikb_work)


@dp.callback_query_handler(text='ready_first:authority')
async def ready_first_authority(c: types.CallbackQuery, state: FSMContext):
    subject_type_name = ''
    r_s1 = await BaseRegistration.filter(tg_id_user=c.from_user.id).all()
    for item1 in r_s1:
        subject_type_name = item1.subject_type_name
    cong = ''
    r_s2 = await TypePersonal_Money.filter(key=subject_type_name).all()
    for item2 in r_s2:
        cong = item2.congratulation
    await c.message.answer(cong, reply_markup=ShareOrReadyAuthority.ikb_congratulation)


@dp.callback_query_handler(text='go_next:profile')
async def ready_go_next_profile(c: types.CallbackQuery):
    subject_authority_name = ''
    r_s1 = await BaseRegistration.filter(tg_id_user=c.from_user.id).all()
    for item1 in r_s1:
        subject_authority_name = item1.subject_authority_name
    text = ''
    r_s2 = await AuthorityInBusiness_Money.filter(key=subject_authority_name).all()
    for item2 in r_s2:
        text = item2.description
    await c.message.answer(f'<b>Авторитет.</b>\n'
                           f'Короткое видео\n\n'
                           f'{text}', reply_markup=ShareOrReadyProfile.ikb_text)


@dp.callback_query_handler(text='give_me_task:profile')
async def give_me_task_profile(c: types.CallbackQuery, state: FSMContext):
    subject_authority_name = ''
    r_s1 = await BaseRegistration.filter(tg_id_user=c.from_user.id).all()
    for item1 in r_s1:
        subject_authority_name = item1.subject_authority_name
    hmwrk = ''
    r_s2 = await AuthorityInBusiness_Money.filter(key=subject_authority_name).all()
    for item2 in r_s2:
        hmwrk = item2.home_work
    await c.message.answer(f'<b>А вот и ваше задание:</b>\n\n'
                           f'{hmwrk}', reply_markup=ShareOrReadyProfile.ikb_work)


@dp.callback_query_handler(text='ready_first:profile')
async def ready_first_profile(c: types.CallbackQuery, state: FSMContext):
    subject_authority_name = ''
    r_s1 = await BaseRegistration.filter(tg_id_user=c.from_user.id).all()
    for item1 in r_s1:
        subject_authority_name = item1.subject_authority_name
    cong = ''
    r_s2 = await AuthorityInBusiness_Money.filter(key=subject_authority_name).all()
    for item2 in r_s2:
        cong = item2.congratulation
    await c.message.answer(f'.{cong}', reply_markup=ShareOrReadyProfile.ikb_congratulation)


@dp.callback_query_handler(text='go_next:end_and_buy')
async def ready_go_next_profile(c: types.CallbackQuery):
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
    await c.message.answer(f'<b>Профиль.</b>\n'
                           f'Короткое видео\n\n'
                           f'{description}', reply_markup=ShareOrReadyBuy.ikb_text)


@dp.callback_query_handler(text='give_me_task:end_and_buy')
async def give_me_task_profile(c: types.CallbackQuery, state: FSMContext):
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
    await c.message.answer(f'<b>А вот и ваше задание:</b>\n\n'
                           f'{hmwrk}', reply_markup=ShareOrReadyBuy.ikb_work)


@dp.callback_query_handler(text='ready_first:end_and_buy')
async def ready_first_profile(c: types.CallbackQuery, state: FSMContext):
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
    await c.message.answer(f'{cong}', reply_markup=ShareOrReadyBuy.ikb_congratulation)


@dp.callback_query_handler(text='go_next:end_and_buy:finish')
async def end_and_buy(c: types.CallbackQuery, state: FSMContext):
    await c.message.answer(f'Надеюсь, Ты выполнил(а) все задания и уже видишь, как твой <b>денежный потенциал раскрывается</b> 💰\n'
                           f'Но это лишь <b>начало пути</b>. Впереди большая работа, чтобы уверенно встать на свой '
                           f'<b>уникальный путь</b> к деньгам и богатству.\n'
                           f'Ты уже знаешь, что общие шаблоны не работают и тебе нужно <b>знать свои особенности.</b>\n\n'
                           f'Ты готов(а) продолжить работу?', reply_markup=ikb_pre_choice_rate())


@dp.message_handler(text='Готов(а)')
async def iam_ready_pre_choice_rate(m: types.Message):
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
                   "В работу с Кириллом входит <b><u>2 часовых созвона и личный чат</u></b> для вопросов.", reply_markup=ikb_choice_rate_after_met_head())


@dp.message_handler(text='Групповой тариф за 4990 рублей')
@dp.message_handler(text='Групповой тариф')
async def group1(m: types.Message):
    await m.answer("Групповой тариф за 4990 рублей", 
        reply_markup=InlineKeyboardMarkup(1).add(
        InlineKeyboardButton(text="Оплата", url=
        prodamus_create_url({
                "name": "Групповой тариф",
                "price": "4990",
                "quantity": 1,
                "sku": "4990"
            }, "4990", m.from_user.id
        ))))

@dp.message_handler(text='Работа с наставником 14990 рублей')
@dp.message_handler(text='Работа с наставником')
async def choice_rate(m: types.Message):
    await m.answer("Работа с наставником 14990 рублей", 
        reply_markup=InlineKeyboardMarkup(1).add(
        InlineKeyboardButton(text="Оплата", url=
        prodamus_create_url({
                "name": "Работа с наставником",
                "price": "14990",
                "quantity": 1,
                "sku": "14990"
            }, "14990", m.from_user.id
        ))))
    

@dp.message_handler(text='Начать свой путь к богатству')
async def payment(m: types.Message):
    await m.answer('Тут будет начало марафона')
