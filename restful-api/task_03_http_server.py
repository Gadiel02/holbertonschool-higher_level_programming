import http.server
import json
from http import HTTPStatus

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Define responses for different paths
        if self.path == "/":
            # Root endpoint, send a simple text response
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            # /data endpoint, send JSON response
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            # Convert the dictionary to JSON and send it
            self.wfile.write(json.dumps(data).encode())
        elif self.path == "/status":
            # /status endpoint, send OK status
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            status = {"status": "OK"}
            self.wfile.write(json.dumps(status).encode())
        elif self.path == "/info":
            # /info endpoint, send API version info
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode())
        else:
            # Handle undefined endpoints
            self.send_response(HTTPStatus.NOT_FOUND)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error_message = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error_message).encode())

if __name__ == "__main__":
    port = 8000
    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Serving on port {port}")
    httpd.serve_forever()
