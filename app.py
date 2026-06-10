import os
import socket
import time
import webbrowser
from threading import Thread

from flask import Flask, render_template, request
from game import play_round

app = Flask(__name__)
HOST = "127.0.0.1"
PORT = 5000
URL = f"http://{HOST}:{PORT}"


@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        user_choice = request.form.get("choice", "")
        result = play_round(user_choice)

    return render_template("index.html", result=result)

def open_browser():
    try:
        if os.name == "nt":
            os.startfile(URL)
        else:
            webbrowser.open(URL)
    except OSError:
        webbrowser.open(URL)


def wait_for_server_then_open():
    for _ in range(50):
        try:
            with socket.create_connection((HOST, PORT), timeout=0.3):
                open_browser()
                return
        except OSError:
            time.sleep(0.2)


if __name__ == "__main__":
    print(f"\n  Game running at: {URL}")
    print("  Use this exact link (not localhost):")
    print(f"  {URL}\n")

    Thread(target=wait_for_server_then_open, daemon=True).start()
    app.run(host=HOST, port=PORT, debug=True, use_reloader=False, threaded=True)
