import time

from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

from  modules.sqlite import SQLite

class NeuralHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/hello':
            self.do_HELLO()
        elif self.path.startswith("/user"):
            parse_param = urlparse(self.path)
            dict_params = parse_qs(parse_param.query)
            if "name" in  dict_params.keys():
                self.do_USER_PROCESSING(dict_params)

    def do_POST(self):
        if self.path.startswith("/user"):
            parse_param = urlparse(self.path)
            dict_params = parse_qs(parse_param.query)
            if "name" in  dict_params.keys():
                self.do_USER_PROCESSING(dict_params)
            else:
                self.do_USER_ERROR()

    def do_USER_PROCESSING(self, dict_data):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(bytes("Request was processed", "utf-8"))
        self.write_DATA(dict_data)
        db_data = SQLite()
        db_data.write_DATA_SQLITE(dict_data)

    def do_USER_ERROR(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(bytes("Request wasn't processed", "utf-8"))

    def do_HELLO(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(bytes("Hello Page", "utf-8"))

    #FORMAT name: hh:mm:ss - dd.mm.yyyy
    def write_DATA(self, dict_data):
        date = time.strftime("%H:%M:%S - %d.%m.%y")
        with open("data.txt", "w") as f:
            f.write(dict_data["name"][0]+ ": " + date)