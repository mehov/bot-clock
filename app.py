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

# Start the HTTP listener
HTTP_PORT = int(os.getenv("HTTP_PORT", "80"))
HTTP_HOST = os.getenv("HTTP_HOST", "0.0.0.0")
logging.info(f"Configured to serve on {HTTP_HOST}:{HTTP_PORT}")
with socketserver.TCPServer((HTTP_HOST, HTTP_PORT), Http) as httpd:
    logging.info(f"Serving on {HTTP_HOST}:{HTTP_PORT}")
    httpd.serve_forever()

# Start the bot
notifier = Bot()
notifier.run()
