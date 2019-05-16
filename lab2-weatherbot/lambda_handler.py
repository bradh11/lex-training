import json, os
from botocore.vendored import requests

app_id = os.environ['app_id']
url = "http://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    query_string = {"APPID": app_id, "country": "us", "q": city}
    response = requests.get(url, params=query_string)
    weather_data = json.loads(response.text)
    # print(weather_data)
    if weather_data.get("cod") == "404":
        response_body = (
            f"I am really sorry, but {city} could not be found in the database"
        )
    else:
        todays_weather = weather_data["weather"][0]["description"]
        response_body = f"The current weather in {city} is {todays_weather}."
    return response_body


def lambda_handler(event, context):
    print("received request: " + str(event))
    city = event["currentIntent"]["slots"]["Location"]
    weather = get_weather(city)

    response = {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {"contentType": "SSML", "content": weather},
        }
    }
    print("result = " + str(response))
    return response


if __name__ == "__main__":
    print(get_weather("Boston"))
