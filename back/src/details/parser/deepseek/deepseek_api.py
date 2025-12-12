import requests

class DeepseekApi:
    @classmethod
    def get_chat_response(cls, messages, token):
        url = "https://api.deepseek.com/chat/completions"
        headers = {"Content-Type": "application/json","Authorization": f"Bearer {token}"}

        data = {
            "model": "deepseek-chat",
            "messages":messages,
            "stream": False,
            "temperature": 0
        }

        response = requests.post(url, json=data, headers=headers)
        if not response.ok:
            raise Exception(response.text)

        return response