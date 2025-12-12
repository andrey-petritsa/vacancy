from flask import request

def setup_cors(app):
    @app.after_request
    def add_cors_headers(response):
        origin = request.headers.get("Origin")
        allowed_origins = {"http://localhost:5173", "http://localhost"}

        if origin in allowed_origins:
            response.headers["Access-Control-Allow-Origin"] = origin

        response.headers["Access-Control-Allow-Methods"] = "GET,POST,OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization,X-Client,X-TOKEN"
        response.headers["Access-Control-Allow-Credentials"] = "true"
        return response