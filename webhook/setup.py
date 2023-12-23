from aiohttp import web
import logging, aiohttp
from loader import dp

async def handle(request: aiohttp.web_request.Request):
    try:
        print("Output")
        post = await request.headers()
        for key, value in post.items():
            print("Key", key, "Value", value)
        order_id = post.get("order_id", "-1")
        order_num = post.get("order_num", "-1")
        user_id = post.get("_param_user_tg_id")
        if not user_id:
            msg = 'User id napam not found'
            print(msg)
            return web.Response(text=msg)
        try:
            await dp.bot.send_message(user_id, "Оплата принята")
        except Exception as err:
            logging.exception(err)
            msg = 'Failed to send message'
            print(msg)
            return web.Response(text=msg)
        msg = "success webhook"
        print(msg)
        return web.Response(text=msg)
    except Exception as err:
        logging.exception(err)
        msg = "server Error"
        print(msg)
        return web.Response(text=msg)

async def setup_webhook():
    app = web.Application()
    app.router.add_get('/', handle)
    app.router.add_post('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host="0.0.0.0", port=80)  
    await site.start()