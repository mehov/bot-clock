import http.server
import logging
import os
import socketserver


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello world!")


class Http:
    def run(self):
        if os.getenv("HTTP_PORT") is None:
            return
        HTTP_PORT = int(os.getenv("HTTP_PORT"))
        HTTP_HOST = os.getenv("HTTP_HOST", "0.0.0.0")
        logging.info(f"Configured to serve on {HTTP_HOST}:{HTTP_PORT}")
        with socketserver.TCPServer((HTTP_HOST, HTTP_PORT), Handler) as httpd:
            logging.info(f"Serving on {HTTP_HOST}:{HTTP_PORT}")
            httpd.serve_forever()
