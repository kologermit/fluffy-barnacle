import os, json

try:
    from .env import *
    BOT_TOKEN = TOKEN
    admin_id = ADMINS
    prodamus = PRODAMUS
except:
    BOT_TOKEN = os.getenv("TOKEN", "5469643644:AAGswk4CVHLOTVx6ZwsVglcKcxkLQeMd030")
    admin_id = json.loads(f"[{os.getenv('ADMINS', '847721936')}]")
    prodamus = {
        "token": os.getenv("PRODAMUS_TOKEN", ""),
        "url": os.getenv("PRODAMUS_URL", ""),
        "demo_mode": 1,
    }