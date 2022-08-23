from http.server import HTTPServer
from prometheus_client import start_http_server

from modules.NeuralHTTP import NeuralHTTP

HOST = ""
PORT_HTTP = 8000
PORT_PROMETHEUS = 8001
start_http_server(PORT_PROMETHEUS)
server = HTTPServer((HOST, PORT_HTTP), NeuralHTTP)
print("Server running on %s:%s" % (HOST, PORT_HTTP))
print("Prometheus metrics  available on port %s /metrics" % PORT_PROMETHEUS)

server.serve_forever()
server.server_close