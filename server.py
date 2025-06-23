from http.server import SimpleHTTPRequestHandler, HTTPServer

host = "0.0.0.0"
port = 8080

server = HTTPServer((host, port), SimpleHTTPRequestHandler)
print(f"Serving HTTP on {host}:{port}")
server.serve_forever()
