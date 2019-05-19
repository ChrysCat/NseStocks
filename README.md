# Stock prices from NSE

This library is for building an Alexa skill for real time stock prices from NationalStock Exchange of India using Alexa.
The library tries to guess the name of the stock from the name uttered by the user and fetches the last price of the stock.

##Getting Started
The github repository forms the AWS Lambda function you'd need to deploy. Checkout the code and build a zip file with the code.

###Prerequisites
You would need basic familiarity in building Alexa skills using Python. For some examples, refer to https://developer.amazon.com/alexa-skills-kit/alexa-skill-python-tutorial
To try some examples or to deploy this code:
1. You would need an Alexa developer account to set up the intents. Build your intents using a few slots for stock symbols.
2. You would need an AWS account to deploy the Lambda code.

###Installing
1. Once your intents are built, test them using utterance profiler.
2. Open AWS console and create a python Lamba function with Python 3.x. Choose Alexa skills kit.
3. In the function code, upload the zip file containing the source code in the git repository.
4. Use "nsestocks.handler" handler. 
5. In the basic settings choose 1200 MB and 7 sec timeout.
6. Save the settings. Copy the ARN from the top of this page.
7. Open Alexa skills page and enter the ARN copied above in the end point of your skill.
8. On the same end point page, copy the Alexa skill ID.
9. Save the skill and build it.
10. Enter the Alexa Skill ID you copied in step 8 in the AWS Lamba function page under the Alexa skills kit.
10. Save the Lambda function.

###Testing 

1. In the Alexa developer console, select your skill.
2. Select Test tab and choose development.
3. Type or speak in the device.

To start the skill say "open india stocks" or the invocation phrase you mentioned for your skill.
Follow with "price of <stockname>"

You can also say "open india stocks price for XXX"

Alexa skill will give you the real time price of the Indian stock.

##Built With
Python3.x\
Alexa SDK\
AWS SDK\
nsetools library

###Author
Chrys Kattirisetti

###Contributors
Anahita Gottipati\
Sheryl Gomes

###License
This project is licensed under the MIT License - see the LICENSE.md file for details

###Acknowledgments
Inspired by nsetools python library https://github.com/vsjha18/nsetools
