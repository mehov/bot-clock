import datetime
import time
import threading
from flask import Flask
import logging
import sys
import os
from src.Bot import Bot

logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout)])
logging.info(f"Starting {__file__}. The environment is:")
for key, value in os.environ.items():
    logging.info(f"    {key} = {value}")


bot = Bot()
app = Flask(__name__)


# Simple endpoint that responds to Azure ping
@app.route('/')
def home():
    return "Azure is keeping me alive!", 200


# Run the bot in a separate thread
if __name__ == '__main__':
    bot_thread = threading.Thread(target=bot.run)
    bot_thread.daemon = True  # This ensures the bot thread will stop when the main thread exits
    bot_thread.start()
    app.run()
