import logging
import os
import socketserver
import sys
from src.Bot import Bot
from src.Http import Http


logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout)])
logging.info(f"Starting {__file__}. The environment is:")
for key, value in os.environ.items():
    logging.info(f"    {key} = {value}")

notifier = Bot()
notifier.run()

if os.getenv("HTTP_PORT") is not None:
    HTTP_PORT = int(os.getenv("HTTP_PORT"))
    HTTP_HOST = os.getenv("HTTP_HOST", "0.0.0.0")
    with socketserver.TCPServer((HTTP_HOST, HTTP_PORT), Http) as httpd:
        print(f"Serving on {HTTP_HOST}:{HTTP_PORT}")
        httpd.serve_forever()
