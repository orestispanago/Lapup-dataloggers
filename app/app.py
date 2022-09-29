from flask import Flask
import json

app = Flask(__name__)

import routes

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
