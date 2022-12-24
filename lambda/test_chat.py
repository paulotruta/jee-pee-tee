import sys

from utils import get_client

if len(sys.argv) != 2:
    print("You must provide text")
    sys.exit(1)

text = sys.argv[1]

print(f"Asking ChatGPT '{text}'")

chatgpt = get_client()
response = chatgpt.get_chat_response(text)

print(response)
