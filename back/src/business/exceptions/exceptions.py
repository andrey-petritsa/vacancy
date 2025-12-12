class AppException(Exception):
    status_code = 500

class NotAVacancyException(AppException):
    status_code = 400

class UserNotFoundException(AppException):
    status_code = 404

class VacancyNotFoundException(AppException):
    status_code = 404
