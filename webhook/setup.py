from aiohttp import web
import logging, aiohttp, prodamuspy
from loader import dp
from data.config import prodamus as conf

async def handle(request: aiohttp.web_request.Request):
    try:
        headers = request.headers
        post = await request.post()
        prodamus = prodamuspy.ProdamusPy(conf["token"])
        bodyDict = dict(headers)
        checkSign = prodamus.sign(bodyDict)
        if not checkSign:
            return web.Response(text="Uncheck")
        signIsGood = prodamus.verify(bodyDict, checkSign)
        if signIsGood:
            print("Signature is awesome")
        else:
            print("Signature is incorrect")
        print("Headers", dict(headers))
        print("Post", dict(post))
        print("UI", post.get("_param_user_tg_id", None))
        if post.get("_param_user_tg_id", None) is None:
            return web.Response(text='User id not found')
        user_id = post.get("_param_user_tg_id")
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