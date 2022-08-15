import time

from http.server import HTTPServer
from urllib.parse import urlparse, parse_qs
from configparser import ConfigParser

from modules.NeuralHTTP import NeuralHTTP

HOST = "localhost"
PORT = 8888

config = ConfigParser()
config.read("config")

config_data = config["default"]

server = HTTPServer((HOST, PORT), NeuralHTTP)
print("Server running on %s:%s" % (HOST, PORT))

server.serve_forever()
server.server_close