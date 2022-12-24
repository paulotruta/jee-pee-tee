import requests


class Client:
    ENDPOINT = "https://api.openai.com/v1/completions"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_chat_response(self, message: str) -> str:
        payload = {
            "model": "text-davinci-003",
            "prompt": message,
        }

        response = requests.post(
            self.ENDPOINT, json=payload, headers=self._default_headers()
        )
        response.raise_for_status()

        return response.json()["choices"][0]["text"]

    def _default_headers(self) -> dict:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
