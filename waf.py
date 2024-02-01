from http.server import BaseHTTPRequestHandler, HTTPServer
import re

class WAFRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello, world!")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        post_data_str = post_data.decode('utf-8')

        # Example of a simple SQL Injection protection
        if re.search(r'\b(select|union|insert|update|delete|drop)\b', post_data_str, re.IGNORECASE):
            self.block_request("SQL Injection detected!")
            return

        # Additional checks can be added here to block other attacks.

        # If no attacks are detected, process the request
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Request successfully processed.")

    def block_request(self, reason):
        self.send_response(403)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(f"Access Denied: {reason}".encode('utf-8'))

def run(server_class=HTTPServer, handler_class=WAFRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting WAF on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
