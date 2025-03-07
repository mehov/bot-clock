import multiprocessing
from src.Http import http as app
from src.Bot import Bot

# If Azure is running something like gunicorn -b 0.0.0.0:8000 app:app, then it expects an app variable in app.py.


bot = Bot()

def start_bot():
    import asyncio
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(bot.run())


if __name__ == '__main__':
    bot_process = multiprocessing.Process(target=start_bot, daemon=True)
    bot_process.start()  # Start bot in a separate process
    app.run()