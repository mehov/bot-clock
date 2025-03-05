import os
import socketserver
from src.Bot import Bot
from src.Http import Http


notifier = Bot()
notifier.run()

if os.getenv("HTTP_PORT") is not None:
    HTTP_PORT = int(os.getenv("HTTP_PORT"))
    with socketserver.TCPServer(("", HTTP_PORT), Http) as httpd:
        print(f"Serving on port {HTTP_PORT}")
        httpd.serve_forever()
