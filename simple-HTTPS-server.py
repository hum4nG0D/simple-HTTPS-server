import http.server
import ssl

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        http.server.SimpleHTTPRequestHandler.end_headers(self)

class SecureHTTPServer(http.server.HTTPServer):
    def __init__(self, server_address, HandlerClass):
        super().__init__(server_address, HandlerClass)
        self.socket = ssl.wrap_socket(self.socket, certfile='/path/to/server.pem', server_side=True)

port = 4443
server_address = ('0.0.0.0', port)
httpd = SecureHTTPServer(server_address, CORSRequestHandler)
print("Serving at port: ", port)
httpd.serve_forever()