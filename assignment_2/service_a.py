from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/a":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({
                "service": "A",
                "message": "Hello from Service A"
            }).encode())

server = HTTPServer(("0.0.0.0", 3000), Handler)
print("Service A running on port 3000")
server.serve_forever()