import json
import logging
from os.path import exists

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

CONFIG_FILE = "config.json"


def load_config() -> dict:
    if not exists(CONFIG_FILE):
        raise ValueError("Config file does not exist")

    with open(CONFIG_FILE) as f:
        return json.load(f)


def clean_chat_response(response: dict) -> str:
    """Cleans the chat response from ChatGPT.

    Args:
        response (str): The response object from ChatGPT.

    Returns:
        str: The cleaned response.
    """
    error_messages = {
        "server_error": "I'm sorry, ChatGPT is having problem at this moment. Please try again later.",
        "invalid_session": "I'm sorry, your session has expired. Please reconfigure the skill with a new session token.",
        "invalid_request_error": "I'm sorry, it appears you configured the skill with an incorrect API Key. Please reconfigure the skill with a new API and try again.",
        "unexpected_error": "I'm sorry, an unexpected communication problem occured. Please try again later.",
    }

    try:
        error = response.get("detail", {}).get("type", "")
        if error:
            logger.warning(f"ChatGPT Error caught: {error}")
            logger.info(response)
            return error_messages.get(error, error_messages["unexpected_error"])

        chat_response = response.get("message")
        if chat_response:
            logger.info("ChatGPT says: " + chat_response)
            return chat_response
        else:
            logger.warning("ChatGPT Error caught: unexpected_error")
            logger.info(response)
            return error_messages["unexpected_error"]

    except (Exception, ValueError) as e:
        logger.warning(f"Error caught: {e}")
        return error_messages["unexpected_error"]
