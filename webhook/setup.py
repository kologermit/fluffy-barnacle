from aiohttp import web
import logging, aiohttp
from loader import dp

async def handle(request: aiohttp.web_request.Request):
    try:
        headers = request.headers
        user_id = headers.get("_param_user_tg_id")
        print(dict(headers))
        if not user_id:
            return web.Response(text='User id napam not found')
        try:
            await dp.bot.send_message(user_id, "Оплата принята")
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