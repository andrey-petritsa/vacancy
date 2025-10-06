import os

import requests


class App:
    @classmethod
    def check_back_health(cls):
        response = requests.get(f"{get_back_url()}/health_check")
        response.raise_for_status()
        return response.json()

    @classmethod
    def check_front_health(cls):
        resp = requests.get(get_front_url())
        resp.raise_for_status()
        return resp.status_code == 200

def get_back_url():
    return os.getenv("BACK_URL", "http://127.0.0.1:5001")

def get_front_url():
    return os.getenv("FRONT_URL", "http://127.0.0.1:80")
