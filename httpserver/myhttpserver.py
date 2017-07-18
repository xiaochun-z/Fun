#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
from os import path
from urllib.parse import urlparse

curdir = path.dirname(path.realpath(__file__))
sep = '/'


# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    # GET
    def do_GET(self):
        self.handle_http_request()

    def do_POST(self):
        self.handle_http_request();

    def handle_http_request(self):
        sendReply = False
        querypath = urlparse(self.path)
        filepath, query = querypath.path, querypath.query
        if filepath.endswith('/'):
            filepath += 'index.html'
        if filepath.endswith(".html"):
            mimetype = 'text/html'
            sendReply = True
        if filepath.endswith(".jpg"):
            mimetype = 'image/jpg'
            sendReply = True
        if filepath.endswith(".gif"):
            mimetype = 'image/gif'
            sendReply = True
        if filepath.endswith(".js"):
            mimetype = 'application/javascript'
            sendReply = True
        if filepath.endswith(".css"):
            mimetype = 'text/css'
            sendReply = True
        if filepath.endswith(".json"):
            mimetype = 'application/json'
            sendReply = True
        if filepath.endswith(".woff"):
            mimetype = 'application/x-font-woff'
            sendReply = True
        if sendReply == True:
            # Open the static file requested and send it
            try:
                with open(path.realpath(curdir + sep + filepath), 'rb') as f:
                    content = f.read()
                    self.send_response(200)
                    self.send_header('Content-type', mimetype)
                    self.end_headers()
                    self.wfile.write(content)
            except IOError:
                self.send_error(404, 'File Not Found: %s' % self.path)


def run():
    port = 8000
    print('starting server, port', port)

    # Server settings
    server_address = ('', port)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()
