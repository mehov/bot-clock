import logging
import os
from wsgiref.simple_server import make_server


class Handler:
    def run(environ, start_response):
        status = "200 OK"
        headers = [("Content-type", "text/plain; charset=utf-8")]
        start_response(status, headers)
        return [b"Hello world!"]


class Http:
    def run(self):
        if os.getenv("HTTP_PORT") is None:
            return
        HTTP_PORT = int(os.getenv("HTTP_PORT"))
        HTTP_HOST = os.getenv("HTTP_HOST", "0.0.0.0")
        logging.info(f"Configured to serve on {HTTP_HOST}:{HTTP_PORT}")
        with make_server(HTTP_HOST, HTTP_PORT, Handler.run) as server:
            logging.info(f"Serving on {HTTP_HOST}:{HTTP_PORT}")
            server.serve_forever()