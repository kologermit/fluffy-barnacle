from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand('start', 'Запуск/Перезапуск бота'),
            types.BotCommand('admin', 'Открыть панель администратора'),
            types.BotCommand('test', 'Отправить тестовую ссылку на оплату'),
        ]
    )
