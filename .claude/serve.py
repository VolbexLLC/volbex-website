import http.server, socketserver

PORT = 3456
DIRECTORY = "/Users/mo/Desktop/volbex-website"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    def log_message(self, format, *args):
        pass  # silence logs

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving Volbex on http://localhost:{PORT}", flush=True)
    httpd.serve_forever()
