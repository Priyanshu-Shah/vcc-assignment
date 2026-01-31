from http.server import BaseHTTPRequestHandler, HTTPServer
import json, urllib.request

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api":
            a = urllib.request.urlopen("http://192.168.100.11:3000/a").read()
            b = urllib.request.urlopen("http://192.168.100.12:3000/b").read()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({
                "service_a": json.loads(a),
                "service_b": json.loads(b)
            }).encode())

server = HTTPServer(("0.0.0.0", 4000), Handler)
print("Gateway running on port 4000")
server.serve_forever()