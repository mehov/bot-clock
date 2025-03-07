import threading
from flask import Flask
import logging
import sys
import asyncio
import datetime
import os
import telegram
import time


logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout)])


class Bot:
    def __init__(self):
        self.bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        self.chat_id = os.getenv('TELEGRAM_CHAT_ID')
        self.telegram_bot = telegram.Bot(token=self.bot_token)
        self.uptime = os.getenv('BOT_UPTIME')

    def run(self):
        while True:
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            message = f"It's {current_time} o'clock!\n\nSent from " + __file__
            self.send_notification(message)
            time.sleep(int(self.uptime))

    def send_notification(self, message):

        async def send_message():
            await self.telegram_bot.send_message(chat_id=self.chat_id, text=message)

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(send_message())


bot = Bot()
app = Flask(__name__)


# Simple endpoint that responds to Azure ping
@app.route('/')
def home():
    return "Hello World!", 200


# Run the bot in a separate thread
if __name__ == '__main__':
    bot_thread = threading.Thread(target=bot.run)
    bot_thread.daemon = True  # This ensures the bot thread will stop when the main thread exits
    bot_thread.start()
    app.run(host=os.getenv("HTTP_HOST", "0.0.0.0"), port=int(os.getenv("HTTP_PORT")))
