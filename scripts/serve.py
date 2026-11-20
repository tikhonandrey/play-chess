"""Serve the bundled chessboard on a loopback port."""
import argparse
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

BOARD_PATH = Path(__file__).resolve().parents[1] / "assets" / "chess.html"


class BoardHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_board(include_body=True)

    def do_HEAD(self):
        self.send_board(include_body=False)

    def send_board(self, include_body):
        if urlsplit(self.path).path not in {"/", "/chess.html"}:
            self.send_error(HTTPStatus.NOT_FOUND)
            return

        board = BOARD_PATH.read_bytes()
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(board)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        if include_body:
            self.wfile.write(board)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--opponent", choices=("computer", "codex"), default="computer")
    parser.add_argument("--port", type=int, default=0, help="reuse a previous game's port")
    args = parser.parse_args()
    if not 0 <= args.port <= 65535:
        parser.error("--port must be between 0 and 65535")

    with ThreadingHTTPServer(("127.0.0.1", args.port), BoardHandler) as server:
        host, port = server.server_address
        print(f"http://{host}:{port}/chess.html?opponent={args.opponent}", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
