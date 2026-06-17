import os

from flask import Flask, render_template

app = Flask(__name__)

# Background colour is supplied at runtime via an environment variable,
# e.g. `docker run -e MY_COLOR=lightblue ...`. Defaults to white if unset.
color = os.environ.get("MY_COLOR", "white")


@app.route("/")
def index():
    return render_template(
        "index.html",
        mytitle="MyPage",
        mycontent="Welcome to my custom page",
        mycolor=color,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
