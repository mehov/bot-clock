import asyncio
import os
import telegram


class Bot:
    def __init__(self):
        self.bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        self.chat_id = os.getenv('TELEGRAM_CHAT_ID')
        self.telegram_bot = telegram.Bot(token=self.bot_token)
        self.loop = asyncio.new_event_loop()

    def send_message(self, message):
        async def send_message_async():
            await self.telegram_bot.send_message(chat_id=self.chat_id, text=message)
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(send_message_async())
