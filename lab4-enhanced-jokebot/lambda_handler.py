import json, os
from botocore.vendored import requests

header = {"Accept": "application/json"}
dad_joke_url = "https://icanhazdadjoke.com/"
chuck_joke_url = "https://api.chucknorris.io/jokes/random"


def get_dad_joke():
    response = requests.get(dad_joke_url, headers=header)
    joke_data = json.loads(response.text)
    response_body = joke_data.get("joke")

    return response_body


def get_chuck_joke():
    response = requests.get(chuck_joke_url, headers=header)
    joke_data = json.loads(response.text)
    # print(joke_data)
    response_body = joke_data.get("value")

    return response_body


def lambda_handler(event, context):
    print("received request: " + str(event))

    # TODO: CHALLENGE -> modify below to choose dad jokes, or chuck norris jokes based on LEX intent
    joke = get_dad_joke()

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
    print(get_chuck_joke())
