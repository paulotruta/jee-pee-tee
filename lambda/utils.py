import json
from os.path import exists

from chatgpt import Client

CONFIG_FILE = "config.json"


def load_config() -> dict:
    if not exists(CONFIG_FILE):
        raise ValueError(f"Config file does not exist")

    with open(CONFIG_FILE) as f:
        return json.load(f)


def get_client() -> Client:
    config = load_config()
    return Client(config["api_key"])
