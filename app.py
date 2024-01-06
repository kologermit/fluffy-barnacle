import logging

from aiogram import executor
from db import init
from handlers import dp
from data.logger import *
from webhook.setup import setup_webhook
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(_):
    await init()
    await on_startup_notify(dp)
    await setup_logger()
    await setup_webhook()
    print('Start Bot')
    await set_default_commands(dp)
    await dp.bot.delete_webhook()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

list1 = {'status': 1,
         'descr': 'Authorized',
         'data':
             {'header':
                  {'city': 'Москва, Россия',
                   'local_birthdate': '1998-8-12 12:30',
                   'api_url': 'bodygraph_fractal_min.php',
                   'bodygraph_id': '34450'},
              'details':
                  {'subject_type_id': '4',
                   'subject_type_name': 'Генератор',
                   'personal_line_id': '1',
                   'personal_line_name': 'Исследователь',
                   'design_line_id': '3',
                   'design_line_name': 'Мученик',
                   'profile_id': '1',
                   'profile_name': 'Исследователь - Мученик',
                   'subject_authority_id': '2',
                   'subject_authority_name': 'Эмоциональный авторитет'}
              },
         'request':
             {'dkey': 'test_public_key',
              'ddate': '1998-8-12',
              'dtime': '12:30',
              'dcity': '15',
              'received_at':
                  '2023-12-23 16:33:59',
              'received_from': '88.80.60.183'
              }
         }