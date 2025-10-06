from flask import Flask, jsonify

from vacancy.main.app_setuper import init_directories

app = Flask(__name__)

@app.route("/health_check", methods=["GET"])
def health_check():
    return jsonify(True)

if __name__ == "__main__":
    init_directories()
    app.run(host="0.0.0.0", port=5000)