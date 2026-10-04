# Simple local development server
import http.server, socketserver, os, sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))
PORT = 3000

socketserver.TCPServer.allow_reuse_address = True
handler = http.server.SimpleHTTPRequestHandler

print(f'Serving GDG QR Studio on http://localhost:{PORT}')
with socketserver.TCPServer(('127.0.0.1', PORT), handler) as httpd:
    httpd.serve_forever()
