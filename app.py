import datetime
import logging
import os
import sys
from flask import Flask, jsonify
from src.Bot import Bot

logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout)])
logging.info(f"Starting {__file__}. The environment is:")
for key, value in os.environ.items():
    logging.info(f"    {key} = {value}")


app = Flask(__name__)
bot = Bot()


@app.route('/')
def home():
    return jsonify(
        route='home',
        now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ), 200


@app.route('/keepalive')
def keepalive():
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = f"It's {current_time} o'clock!\n\nSent from " + __file__
    bot.send_message(message)
    return jsonify(
        route='keepalive',
        now=current_time
    ), 200


if __name__ == '__main__':
    app.run(host=os.getenv("HTTP_IP", "0.0.0.0"), port=int(os.getenv("HTTP_PORT", 80)))
