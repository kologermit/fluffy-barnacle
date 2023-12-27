from aiohttp import web
import logging, aiohttp, prodamuspy
from loader import dp
from data.config import prodamus as conf
from data.config import admin_id as admins

async def handle(request: aiohttp.web_request.Request):
    try:
        headers = request.headers
        post = await request.post()
        prodamus = prodamuspy.ProdamusPy(conf["token"])
        bodyDict = dict(headers)
        checkSign = prodamus.sign(bodyDict)
        if not checkSign:
            return web.Response(text="Uncheck")
        print("Post:", post)
        signIsGood = prodamus.verify(bodyDict, checkSign)
        if not signIsGood:
            print("Signature is incorrect")
        if post.get("_param_user_tg_id", None) is None:
            return web.Response(text='User id not found')
        user_id = post.get("_param_user_tg_id")
        try:
            await dp.bot.send_message(user_id, 
f"""Оплата принята
Товар: {post['products[0][name]']}
Сумма: {post['sum']}""")
            for admin in admins:
                await dp.bot.send_message(admin, f"""Сообщение для админа: Пользователь оплатил товар
ТоварId: {post['_param_product_id']}
Цена: {post['sum']}
Имя: {post['products[0][name]']}
Статус оплаты: {post['payment_status']}

Пользователь: {post['_param_user_name']}
Ссылка: @{post['_param_user_username']}
ТГ номер: {user_id}
Почта: {post['customer_email']}
Телефон: {post['customer_phone']}
""")
        except Exception as err:
            logging.exception(err)
            return web.Response(text='Failed to send message')
        return web.Response(text="success webhook")
    except Exception as err:
        logging.exception(err)
        return web.Response(text="server Error")

async def setup_webhook():
    app = web.Application()
    app.router.add_get('/', handle)
    app.router.add_post('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host="0.0.0.0", port=80)  
    await site.start()