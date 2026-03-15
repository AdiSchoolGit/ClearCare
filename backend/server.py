from flask import Flask
from flask_pymongo import PyMongo

# above imports appear as errors however do not affect functionality

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/ClearCare"

mongo = PyMongo(app)


@app.route("/", methods=["GET"])
def hello():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)  # <-- for prod only
