from flask import Flask

app = Flask(__name__)

import routes

if __name__ == "__main__":
    app.config["JSON_SORT_KEYS"] = False
    app.run(debug=True, host="0.0.0.0")
