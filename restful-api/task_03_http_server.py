import http.server
import json

# Create a subclass of BaseHTTPRequestHandler
class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    
    # Method to handle GET requests
    def do_GET(self):
        # Check the request path to route to different endpoints
        if self.path == "/":
            # Response for root path
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        
        elif self.path == "/data":
            # Response for /data endpoint (JSON)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))
        
        elif self.path == "/status":
            # Response for /status endpoint
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            status_data = {"status": "OK"}
            self.wfile.write(json.dumps(status_data).encode('utf-8'))
        
        else:
            # Handle undefined endpoints
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found: Endpoint not found.")

# Set up the server
def run(server_class=http.server.HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8000)  # Listen on port 8000
    httpd = server_class(server_address, handler_class)
    print("Starting http server on port 8000...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
