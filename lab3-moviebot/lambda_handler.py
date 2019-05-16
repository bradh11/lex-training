import json, os
from botocore.vendored import requests

api_key = os.environ["api_key"]
url = "http://www.omdbapi.com/"


def get_movie_data(movie_name):
    query_string = {"apikey": api_key, "t": movie_name}
    response = requests.get(url, params=query_string)
    movie_data = json.loads(response.text)
    print(movie_data)

    return movie_data


def movie_resonse(movie_data, movie_intent):
    movie_title = movie_data.get("Title")
    movie_date = movie_data.get("Released")
    movie_plot = movie_data.get("Plot")
    movie_rating = movie_data.get("Rated")
    movie_runtime = movie_data.get("Runtime")
    movie_poster = movie_data.get("Poster")

    # TODO: CHALLENGE -> modify below to return genre based on intent

    if movie_intent == "movieReleaseDate":
        response_body = f"{movie_title} was released on {movie_date}"
    elif movie_intent == "moviePlot":
        response_body = f"{movie_title}: {movie_plot}"
    elif movie_intent == "moviePoster":
        response_body = movie_poster
    elif movie_intent == "movieRating":
        response_body = f"{movie_title} is rated {movie_rating}"
    elif movie_intent == "movieRuntime":
        response_body = f"{movie_title} has a runtime of {movie_runtime}"
    else:
        response_body = f"I'm sorry, I didnt quite understand your request."

    return response_body


def lambda_handler(event, context):
    print("received request: " + str(event))
    movie = event["currentIntent"]["slots"]["movie"]
    movie_intent = event["currentIntent"]["name"]
    movie_data = get_movie_data(movie)

    movie_response = movie_resonse(movie_data, movie_intent)

    response = {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {"contentType": "SSML", "content": movie_response},
        }
    }
    print("result = " + str(response))
    return response


if __name__ == "__main__":
    # Local Test code...
    movie_data = get_movie_data("Avengers")
    print(movie_resonse(movie_data=movie_data, movie_intent="movieReleaseDate"))
