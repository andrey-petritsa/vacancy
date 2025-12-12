from flask import jsonify

from business.exceptions.exceptions import AppException


def setup_error_handlers(app):
    @app.errorhandler(AppException)
    def handle_app_exception(error: AppException):
        response = jsonify({
            "error": error.__class__.__name__,
            "message": str(error),
        })
        response.status_code = getattr(error, "status_code")
        return response