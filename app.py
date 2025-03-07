import logging
import os
import sys
import threading
from src.Bot import Bot
from src.Http import Http


logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout)])
logging.info(f"Starting {__file__}. The environment is:")
for key, value in os.environ.items():
    logging.info(f"    {key} = {value}")

# Start the HTTP listener
http = Http()
http_thread = threading.Thread(target=http.run, daemon=True)
http_thread.start()

# Start the bot
notifier = Bot()
notifier.run()
