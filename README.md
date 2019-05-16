# Amazon LEX / Lambda Training - Lab materials
This GitHub repository has been created to help illustrate the create of LEX Intents and leverage AWS Lambda serverless functions for fulfillment.

## Lab Agenda
* create a jokebot which responds to you and makes a REST API call to return a joke.
* create a weatherbot which can check the weather for whatever city/location you provide using REST API to a weather service
* create a moviebot which can return facts about a given movie via the open movie online database.  Examples of criteria to ask for: release year, description, rating
* modify the original jokebot from Lab 1 and have it give different responses for Dad Joke or Chuck Norris joke requests.

## Getting Started
### AWS Console
1. log in to [Amazon Lex console](https://console.aws.amazon.com/lex) with your Amazon account
2. In a separate browser tab open up the [Amazon Lambda console](https://console.aws.amazon.com/lambda)
3. Congratulations, you have taken your first step towards learning Amazon Lex services.

## Lab Guidance
1. Lab 1 - simple jokebot.  This lab explores a single intent with no slots, and triggers an API call to Dad jokes REST API.
2. Lab 2 - weatherbot.  This lab explores creating a bot with an intent which captures a location in a slot.  The location is then parsed in a Lambda function which then grabs the current weather based on that location.
3. Lab 3 - moviebot.  This lab explores multiple intents each with multiple slots to return specific facts about a movie.
4. Lab 4 - enhanced jokebot.  This lab enhances the original jokebot and asks the user to decide whether they want Dad jokes, or Chuck Norris jokes.

### API Resources
* [Open Movie Database API](http://www.omdbapi.com)
* [open weather API](https://openweathermap.org/api)
* [Dad jokes API](https://icanhazdadjoke.com/api)
* [Chuck Norris Jokes API](https://api.chucknorris.io/jokes/random)
