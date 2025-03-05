import os
import socketserver
from src.Bot import Bot
from src.Http import Http


notifier = Bot()
notifier.run()

if os.getenv("HTTP_PORT") is not None:
    HTTP_PORT = int(os.getenv("HTTP_PORT"))
    HTTP_HOST = os.getenv("HTTP_HOST", "0.0.0.0")
    with socketserver.TCPServer((HTTP_HOST, HTTP_PORT), Http) as httpd:
        print(f"Serving on {HTTP_HOST}:{HTTP_PORT}")
        httpd.serve_forever()
