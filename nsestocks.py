"""
    This module provides handlers for Alexa SDK calls and
    obtains NSE stock data from NSE library.
"""

__author__      = "Chrys Kattirisetti"
__copyright__ = "Copyright 2019 International Womens Hackathon Project"
__credits__ = ["Anahita Gottipati", "Sheryl Gomes", "Chrys Kattirisetti"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Chrys Kattirisetti"
__email__ = "chryscat@gmail.com"

import json
import os
import logging
from nsetools import Nse
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard

""" Initialize the logger """
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def stock_price(symbol):
    """
    This function returns the last
	price of the given symbol.
	None if the symbol is not valid.
	"""
    nse = Nse()
    if nse.is_valid_code(symbol):
        q = nse.get_quote(symbol)
        return q.get('lastPrice', None)
    else:
        logger.error("Unknown symbol " + symbol)
        return None

class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "Welcome to NSE Stocks skill!"

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("NSE Stocks", speech_text)).set_should_end_session(
            False)
        return handler_input.response_builder.response


class NSEStockIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("NSEStockIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        slots = handler_input.request_envelope.request.intent.slots
        stock = slots["Stock"].value

        if not stock is None:
            price = stock_price(stock)
            speech_text = "NSE stock price of " + stock + " is " + str(price)
        else:
            speech_text = "I don't know this stock. Please retry " + stock

        logger.info(speech_text)
        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("NSE stock", speech_text)).set_should_end_session(
            True)

        return handler_input.response_builder.response

class HelpIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "You can ask price of any stock traded in NSE"

        handler_input.response_builder.speak(speech_text).ask(speech_text).set_card(
            SimpleCard("NSE stock", speech_text))
        return handler_input.response_builder.response


class CancelAndStopIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.CancelIntent")(handler_input) \
               or is_intent_name("AMAZON.StopIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "Goodbye!"

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("NSE stock", speech_text))
        return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # any cleanup logic goes here

        return handler_input.response_builder.response


from ask_sdk_core.dispatch_components import AbstractExceptionHandler

class AllExceptionHandler(AbstractExceptionHandler):

    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        # Log the exception in CloudWatch Logs
        print(exception)

        speech = "Sorry, I didn't get it. Can you please say it again?"
        handler_input.response_builder.speak(speech).ask(speech)
        return handler_input.response_builder.response


sb = SkillBuilder()
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(NSEStockIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelAndStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())

sb.add_exception_handler(AllExceptionHandler())

handler = sb.lambda_handler()