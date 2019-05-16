# Lab3 - moviebot

## Getting started
1. create a new bot in LEX called moviebot
2. create a welcome intent with your bot greeting called `movieHelp` (utterances: Help, Hi, Hello)
3. Add a slot variable called "movie" with a slot type of AMAZON.movie and a question of "What Movie?"
4. create a new intent for moviePlot (Utterances: What is the plot of {movie}?, etc...)
5. create more intents for `movieReleaseDate`, `movieRuntime`, and `movieRating` - add appropriate slots, and Utterances for each
6. From Lambda console create a new function called getMovie using defaults (Python 3.7)
7. Paste the Python code into the Lambda Function
8. add `api_key` environment variable with your openmovie DB API key
9.  In Lex intent, set fulfillment to Lambda function
10. Save, Build, and Test