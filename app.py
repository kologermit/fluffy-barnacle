import logging, sys, datetime, os

from data.logger import setup_logger
from aiogram import executor
from db import init
from handlers import dp
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

async def on_startup(_):
    await setup_logger()
    await init()
    await on_startup_notify(dp)
    logging.info('Бот запущен')
    await set_default_commands(dp)
    await dp.bot.delete_webhook()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)


