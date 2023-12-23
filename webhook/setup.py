from aiohttp import web
import logging, aiohttp

async def handle(request: aiohttp.web_request.Request):
    post = await request.post()
    for key, value in post.items():
        logging.info("-------------------")
        logging.info("key") 
        logging.info(key)
        logging.info("value") 
        logging.info(value)
        logging.info("-------------------")
    
    return web.Response(text='Hello world')

async def setup_webhook():
    app = web.Application()
    app.router.add_get('/', handle)
    app.router.add_post('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host="0.0.0.0", port=80)  
    await site.start()