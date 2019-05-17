# Lab3 - moviebot

## Prerequisite - get an API key for open movie database
1. Click the [omdb link](https://www.omdbapi.com/apikey.aspx) and sign up for a free api key

## Getting started
1. create a new bot in LEX called moviebot
2. create a welcome intent with your bot greeting called `movieHelp` (utterances: Help, Hi, Hello)
3. create a new intent for `moviePlot` (Utterances: What is the plot of {movie}?, etc...)
4. Add a slot variable called "movie" with a slot type of AMAZON.movie and a question of "What Movie?"
5. create more intents for `movieReleaseDate`, `movieRuntime`, and `movieRating` - 
   1. add slot for movie in each one with prompt of "What movie?"
   2. and Utterances for each for example: "What was the release date of {movie}, how long is {movie}, what was {movie} rated
6. From Lambda console create a new function called getMovie using defaults (Python 3.7)
7. add `api_key` environment variable with your openmovie DB API key
   1. within the Lamda function, find the section of code that has the if, elif statements:
```python
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
```
   2. modify the lines which mention ```movie_intent == "":``` - change what is in the "" to match the intent name you used in LEX
   3. save the Lambda function after any changes to the python code
8. Paste the Python code into the Lambda Function
9.  In Lex intent, set fulfillment to Lambda function
10.    Save, Build, and Test