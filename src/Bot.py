import asyncio
import datetime
import os
import telegram
import time


class Bot:
    def __init__(self):
        self.bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        self.chat_id = os.getenv('TELEGRAM_CHAT_ID')
        self.telegram_bot = telegram.Bot(token=self.bot_token)

        self.uptime = os.getenv('BOT_UPTIME')
        if self.uptime is None:
            self.uptime = 60

    def get_flag(self, key):
        return f"/tmp/bot{key}.flag"

    def run(self):
        print("bot.run")
        # stop_time = time.time() + (int(self.uptime) * 60)
        # while time.time() < stop_time:
        while True:
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # flag_file = self.get_flag(current_time)
            # if os.path.exists(flag_file):
            #    continue
            self.send_notification(current_time)
            time.sleep(int(self.uptime))

    def send_notification(self, current_time):
        # flag_file = self.get_flag(current_time)
        message = f"It's {current_time} o'clock!\n\nFrom " + __file__

        async def send_message():
            await self.telegram_bot.send_message(chat_id=self.chat_id, text=message)

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(send_message())
        # with open(flag_file, 'w'):
        #    pass
