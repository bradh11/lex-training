import json, os
from botocore.vendored import requests

header = {"Accept": "application/json"}
url = "https://icanhazdadjoke.com/"


def get_joke():
    response = requests.get(url, headers=header)
    joke_data = json.loads(response.text)
    response_body = joke_data.get("joke")

    return response_body


def lambda_handler(event, context):
    print("received request: " + str(event))

    joke = get_joke()

    response = {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {"contentType": "SSML", "content": joke},
        }
    }
    print("result: " + str(response))

    return response


if __name__ == "__main__":
    # Local test code
    print(get_joke())
