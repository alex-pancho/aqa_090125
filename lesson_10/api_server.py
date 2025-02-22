import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# Демонстраційний контент
content = []

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def _send_response(self, status_code, message):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(message).encode('utf-8'))

    def do_GET(self):
        if self.path == '/content':
            self._send_response(200, {'content': content})
        else:
            self._send_response(404, {'error': 'Not Found'})

    def do_POST(self):
        if self.path == '/content':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            content.append(data)
            self._send_response(201, {'message': 'Content created successfully!'})
        else:
            self._send_response(404, {'error': 'Not Found'})

    def do_PUT(self):
        if self.path.startswith('/content/'):
            try:
                id = int(self.path.split('/')[-1])
                content_length = int(self.headers['Content-Length'])
                put_data = self.rfile.read(content_length)
                data = json.loads(put_data.decode('utf-8'))
                content[id] = data
                self._send_response(200, {'message': 'Content updated successfully!'})
            except (IndexError, ValueError):
                self._send_response(400, {'error': 'Invalid content ID'})
        else:
            self._send_response(404, {'error': 'Not Found'})

    def do_DELETE(self):
        if self.path.startswith('/content/'):
            try:
                id = int(self.path.split('/')[-1])
                del content[id]
                self._send_response(200, {'message': 'Content deleted successfully!'})
            except (IndexError, ValueError):
                self._send_response(400, {'error': 'Invalid content ID'})
        else:
            self._send_response(404, {'error': 'Not Found'})


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()
