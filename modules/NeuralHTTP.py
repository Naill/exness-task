import time
import pandas

from configparser import ConfigParser
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from prometheus_client import Counter

from  modules.sqlite import SQLite

class NeuralHTTP(BaseHTTPRequestHandler):
    """
    HTTP server for test task in Exness company.
    You can use GET, POST request on this webserver.
    With GET you can retrieve data from db.
    With POST you can safe data to file, db.

    """

    get_counter = Counter('get_counter', 'How many times get request was called')
    post_counter = Counter('post_counter', 'How many times post request was called')

    def do_GET(self):
        self.get_counter.inc()
        if self.path == '/hello':
            self.hello_GET()
        elif self.path.startswith("/user") and self._check_TYPE_STORE():
            parse_param = urlparse(self.path)
            dict_params = parse_qs(parse_param.query)
            if "name" in  dict_params.keys():
                self.user_GET(dict_params["name"][0])
        else:
            self.request_ERROR()

    def do_POST(self):
        self.post_counter.inc()
        if self.path.startswith("/user"):
            parse_param = urlparse(self.path)
            dict_params = parse_qs(parse_param.query)
            if "name" in  dict_params.keys():
                self.user_POST(dict_params)
            else:
                self.request_ERROR()
        else:
            self.request_ERROR()

    def user_POST(self, dict_data):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes("Request was processed", "utf-8"))
        if self._check_TYPE_STORE():
            db_data = SQLite()
            db_data.write_DATA_SQLITE(dict_data)
        else:
            self._write_DATA_FILE(dict_data)
        

    def user_GET(self, user):
        db_data = SQLite()
        user_data = db_data.fetch_DATA_SQLITE(user)
        self.send_response(200)
        self.end_headers()
        user_listsorted = pandas.DataFrame(user_data, columns=["username", "timestamp"])
        self.wfile.write(bytes(str(user_listsorted), "utf-8"))

    def request_ERROR(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes("Request wasn't processed. Check params or request", "utf-8"))

    def hello_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes("Hello Page", "utf-8"))

    #FORMAT name: hh:mm:ss - dd.mm.yyyy
    def _write_DATA_FILE(self, dict_data):
        date = time.strftime("%H:%M:%S - %d.%m.%y")
        with open("data.txt", "w") as f:
            f.write(dict_data["name"][0]+ ": " + date)

    def _check_TYPE_STORE(self):
        config = ConfigParser()
        config.read("config")
        if config['default']['db_safe'] == 'True':
            return True
        else:
            return False
