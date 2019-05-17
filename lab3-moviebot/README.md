# Lab3 - moviebot

## Prerequisite - get an API key for open movie database
1. Click here to sign up for an [omdb api key]("https://www.omdbapi.com/apikey.aspx?__EVENTTARGET=freeAcct&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwUKLTIwNDY4MTIzNQ9kFgYCAQ9kFggCAQ8QDxYCHgdDaGVja2VkZ2RkZGQCAw8QDxYCHwBoZGRkZAIFDxYCHgdWaXNpYmxlZ2QCBw8WAh8BaGQCAg8WAh8BaGQCAw8WAh8BaGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgMFC3BhdHJlb25BY2N0BQhmcmVlQWNjdAUIZnJlZUFjY3S0gwjl9jaVfARil8Yy9nisxxBo9QY1d1aRp4k6s2f83g%3D%3D&__VIEWSTATEGENERATOR=5E550F58&__EVENTVALIDATION=%2FwEdAAW77Mkj8S6lO0evPKayW3ucmSzhXfnlWWVdWIamVouVTzfZJuQDpLVS6HZFWq5fYpioiDjxFjSdCQfbG0SWduXFd8BcWGH1ot0k0SO7CfuulGmtD1h9A7%2B3Av2cTK2Z2qbhaCErXs89aADzZLPwy5pm&at=freeAcct&Email=")

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