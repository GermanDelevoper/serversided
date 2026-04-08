import json
import requests
from http.server import BaseHTTPRequestHandler

WEBHOOK_URL = "https://discord.com/api/webhooks/1487215192440967289/nBR6Y1d4IAWMrW_Da7tQ2F6aPIOiLMnhwHUoMrPmk0clwA7KF4Wge7o4x0aGQ64BoPGh"

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)

            data = json.loads(body.decode("utf-8"))

            # отправка в webhook
            requests.post(WEBHOOK_URL, json={
                "content": str(data)
            })

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()

            self.wfile.write(b'{"status":"ok"}')

        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b'{"error":"server error"}')
