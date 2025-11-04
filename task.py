import http.server
import socketserver
import threading
import requests
import re
import time
from dotenv import load_dotenv
import os

load_dotenv()  # load .env variables

API_URL = os.getenv("API_URL")
PORT = int(os.getenv("PORT", 8000))
MSG = os.getenv("MSG", "Hello")
TIMEOUT = int(os.getenv("TIMEOUT", 20))
PUBLIC_URL = os.getenv("PUBLIC_URL")

part2_data = None


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        global part2_data
        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length).decode()
        print(f"\n[+] Received POST: {body}")

        match = re.search(r'"part2"\s*:\s*"([A-Za-z0-9\-]+)"', body)
        if match:
            part2_data = match.group(1)
            print(f"[+] part2 captured: {part2_data}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"ok")


def run_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"[+] Listening on port {PORT} for part2...")
        httpd.serve_forever()


def main():
    global part2_data

    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()

    time.sleep(1)

    payload = {"msg": MSG, "url": PUBLIC_URL}
    print("[1] Sending POST to API...")
    res = requests.post(API_URL, json=payload)
    res.raise_for_status()
    part1 = res.json().get("part1", "").strip()
    print(f"Part 1 received: {part1}")

    print("[2] Waiting for part2...")

    start = time.time()
    while part2_data is None and time.time() - start < TIMEOUT:
        time.sleep(0.5)

    if part2_data is None:
        print("Timeout: part2 not received")
        return

    full_code = part1 + part2_data
    print(f"Combined code: {full_code}")

    print("[3] Sending GET to verify...")
    r = requests.get(API_URL, params={"code": full_code})
    r.raise_for_status()
    message = r.text.strip()

    print("\nFinal Message:", message)
    print("Combined Code:", full_code)


if __name__ == "__main__":
    main()
