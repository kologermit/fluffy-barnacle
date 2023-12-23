from aiohttp import web
import logging

async def handle(request):
    logging.info(request)
    text = 'Hello, world'
    return web.Response(text=text)

async def setup_webhook():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host="0.0.0.0", port=80)  
    await site.start()