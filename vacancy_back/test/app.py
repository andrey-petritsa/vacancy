import os

import requests


class App:
    url = os.getenv("URL", "http://localhost")

    @classmethod
    def check_back_health(cls):
        response = requests.get(f"{cls.url}:5001/health_check")
        response.raise_for_status()
        return response.json()

    @classmethod
    def check_front_health(cls):
        resp = requests.get(f"{cls.url}:80")
        resp.raise_for_status()
        return resp.status_code == 200
