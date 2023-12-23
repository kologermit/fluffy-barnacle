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
