import asyncio
import os
import threading
from src.Http import http as app
from src.Bot import Bot

# If Azure is running something like gunicorn -b 0.0.0.0:8000 app:app, then it expects an app variable in app.py.


# app.run() # no need for this as Azure has a separate launcher

bot = Bot()


def start_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(bot.run())


threading.Thread(target=start_bot, daemon=True).start()

app.run()