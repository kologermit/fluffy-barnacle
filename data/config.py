import os, json

try:
    from .env import TOKEN, ADMINS
    BOT_TOKEN = TOKEN
    admin_id = ADMINS
except:
    BOT_TOKEN = os.getenv("TOKEN", "5469643644:AAGswk4CVHLOTVx6ZwsVglcKcxkLQeMd030")
    admin_id = json.loads(f"[{os.getenv('ADMINS', '847721936')}]")