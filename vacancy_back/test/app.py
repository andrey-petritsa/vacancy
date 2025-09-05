import requests


class App:
    host = 'http://localhost:5001'

    @classmethod
    def check_health(cls):
        response = requests.get(f"{cls.host}/health_check")
        response.raise_for_status()
        return response.json()
