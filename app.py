from datetime import datetime
from zoneinfo import ZoneInfo

from flask import Flask, render_template

app = Flask(__name__)
TZ = ZoneInfo("Europe/Prague")


@app.route("/")
def index():
    now = datetime.now(TZ)
    return render_template(
        "index.html",
        hour=now.hour,
        minute=now.minute,
        second=now.second,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
