#!/usr/bin/env python
#--coding:utf-8--

from http.server import BaseHTTPRequestHandler, HTTPServer
from os import path

curdir = path.dirname(path.realpath(__file__))
sep = '/'

# MIME-TYPE
mimedic = [
						('.html', 'text/html'),
						('.htm', 'text/html'),
						('.js', 'application/javascript'),
						('.css', 'text/css'),
						('.json', 'application/json'),
						('.png', 'image/png'),
						('.jpg', 'image/jpeg'),
						('.gif', 'image/gif'),
						('.txt', 'text/plain'),
						('.avi', 'video/x-msvideo'),
					]

class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
	# GET
	def do_GET(self):
		sendReply = False
		if self.path.endswith('/'):
			self.path += 'index.html'
		filename, fileext = path.splitext(self.path)
		for e in mimedic:
			if e[0] == fileext:
				mimetype = e[1]
				sendReply = True

		if sendReply == True:
			print(path.realpath(curdir + sep + self.path))
			try:
				with open(path.realpath(curdir + sep + self.path),'rb') as f:
					content = f.read()
					self.send_response(200)
					self.send_header('Content-type',mimetype)
					self.end_headers()
					self.wfile.write(content)
			except IOError:
				self.send_error(404,'File Not Found: %s' % self.path)

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