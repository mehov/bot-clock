import asyncio
import os
import telegram


class Bot:
    def __init__(self):
        self.bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        self.chat_id = os.getenv('TELEGRAM_CHAT_ID')
        self.telegram_bot = telegram.Bot(token=self.bot_token)
        self.loop = asyncio.new_event_loop()
        # set webhook if HTTP_HOSTNAME present in environment
        hostname = os.getenv('HTTP_HOSTNAME')
        if hostname is not None:
            async def set_webhook():
                webhook_url = f"https://{hostname}/webhook-endpoint"
                await self.telegram_bot.set_webhook(webhook_url)
            asyncio.set_event_loop(self.loop)
            self.loop.run_until_complete(set_webhook())

    def send_message(self, message):
        async def send_message_async():
            await self.telegram_bot.send_message(chat_id=self.chat_id, text=message)
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(send_message_async())
