import asyncio
import time
from multiprocessing import Process, Value
from src.Http import http as app
from src.Bot import Bot

# If Azure is running something like gunicorn -b 0.0.0.0:8000 app:app, then it expects an app variable in app.py.


def run_bot():
    bot = Bot()
    asyncio.run(bot.run())


if __name__ == "__main__":
    p = Process(target=run_bot)
    p.start()
    app.run(debug=True, use_reloader=False)
    p.join()
