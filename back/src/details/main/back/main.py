from flask import Flask

from details.main.back.cors import setup_cors
from details.main.back.routes import bp as routes_bp
from details.main.back.error_handler import setup_error_handlers

app = Flask(__name__)
setup_cors(app)
setup_error_handlers(app)
app.register_blueprint(routes_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)