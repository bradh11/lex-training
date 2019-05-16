# Lab2 - weatherbot

## Getting started
1. create a new bot in LEX called weatherbot
2. create a welcome intent with your bot greeting (utterances: Help, Hi, Hello)
3. create a new intent for getWeather (Utterances: What is the weather?, etc...)
4. Add a slot variable called `Location` with a question of "What City?"
5. Add some more utterances: What is the weather in {Location}, Tell me the weather for {Location}, etc...
6. From Lambda console create a new function called getWeather using defaults (Python 3.7)
7. Paste the Python code to the Lambda Function
8. add api_key environment variable with your openweather API key
9. In Lex intent, set fulfillment to Lambda function
10. Save, Build, and Test