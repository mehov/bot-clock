import datetime
import hashlib
import logging
import os
import sys
from flask import Flask, jsonify, request
from src.Bot import Bot

logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout)])
logging.info(f"Starting {__file__}. The environment is:")
for key, value in os.environ.items():
    logging.info(f"    {key} = {value}")

app = Flask(__name__)
bot = Bot()


@app.route('/')
async def home():
    return jsonify(
        route='home',
        now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ), 200


@app.route('/keepalive')
async def keepalive():
    def get_flag(flag_key):
        flag_key = hashlib.md5(flag_key.encode()).hexdigest()
        return f"/tmp/bot-clock-{flag_key}.flag"

    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    flag_file = get_flag(current_time)
    if os.path.exists(flag_file) is not True:
        with open(flag_file, 'w'):
            pass
        message = f"It's {current_time} o'clock!\n\nSent from " + __file__
        bot.send_message(message)
    return jsonify(
        route='keepalive',
        now=current_time
    ), 200


@app.route('/webhook-endpoint', methods=['POST'])
async def webhook_endpoint():
    bot.send_message(request.data.decode('utf-8'))
    return jsonify(
        route='webhook-endpoint',
        data=request.data.decode('utf-8'),
        now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ), 200


if __name__ == '__main__':
    http_port = os.getenv("HTTP_PORT")
    if http_port is not None:
        app.run(host=os.getenv("HTTP_IP", "0.0.0.0"), port=int(http_port))
