import datetime
import time
import threading
from flask import Flask
import logging
import sys
import os


logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout)])
logging.info(f"Starting {__file__}. The environment is:")
for key, value in os.environ.items():
    logging.info(f"    {key} = {value}")


# Your bot code that runs in a loop
def run_bot():
    while True:
        # Simulate bot task (replace with actual bot logic)
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logging.info(f"Bot is running... {current_time}")
        time.sleep(10)  # Simulating bot activity


# Create Flask app to handle the HTTP requests for Azure
app = Flask(__name__)


# Simple endpoint that responds to Azure ping
@app.route('/')
def home():
    return "Azure is keeping me alive!", 200


# Run the bot in a separate thread
if __name__ == '__main__':
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.daemon = True  # This ensures the bot thread will stop when the main thread exits
    bot_thread.start()

    # Run the Flask server (WSGI)
    app.run(host='0.0.0.0', port=80)
