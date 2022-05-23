"""
A HTTP RESTFul API server to control the water pump built using Flask-RESTful.

Dependencies:
  pip3 install gpiozero pigpio flask-restful

"""

from threading import Thread
import RPi.GPIO as GPIO
import time
from flask import Flask, request, render_template
from flask_restful import Resource, Api, reqparse, inputs


GPIO.setwarnings(False)


# Global variables
WATER_PUMP = 7
#HUMIDITY_SENSOR = 40
MOISTURE_SENSOR = 11
state = {
    'level': 1	# state of the water pump. 1:off, 0:on
}

GPIO.setmode(GPIO.BOARD)
GPIO.setup(WATER_PUMP, GPIO.OUT)
GPIO.setup(MOISTURE_SENSOR, GPIO.IN)
GPIO.output(WATER_PUMP, state['level'])
#GPIO.setup(humidity_sensor, GPIO.IN)



# Flask & Flask-RESTful instance variables
app = Flask(__name__) # Core Flask app.
api = Api(app) # Flask-RESTful extension wrapper


# @app.route applies to the core Flask instance (app).
# Here we are serving a simple web page.
@app.route('/', methods=['GET'])
def index():
    """Make sure inde.html is in the templates folder
    relative to this Python file."""
    return render_template('index_api_client.html', pin=WATER_PUMP)


# Flask-restful resource definitions.
# A 'resource' is modeled as a Python Class.
class PumpControl(Resource):

    def __init__(self):
        self.args_parser = reqparse.RequestParser()

        self.args_parser.add_argument(
            name='level',	# Name of arguement
            required=True,  	# Mandatory arguement
            type=inputs.int_range(0, 1),	# Allowed 0 or 1
            help='Set level of the water pump {error_msg}',
            default=None)

        


    def get(self):
        """ Handles HTTP GET requests to return current water pump level."""
        return state


    def post(self):
        """Handles HTTP POST requests to set water pump level."""
        global state

        args = self.args_parser.parse_args()

        state['level'] = args.level
        GPIO.output(WATER_PUMP, state['level'])
        return state


# Register Flask-RESTful resource and mount to server end point /pump
api.add_resource(PumpControl, '/pump')


# not working yet
def auto():
    try:
        while state['auto'] == 1:
            moisture_value = GPIO.input(MOISTURE_SENSOR)
            if (moisture_value == 0):  # dry
                state['level'] = 0     # on
                GPIO.output(WATER_PUMP, 0)
                print("The soil is dry. The water pump started to pump water!")
            else:
                state['level'] = 1   # off
                GPIO.output(WATER_PUMP, 1)
                print("The soil is wet. The water pump stopped pumping water!")
            time.sleep(1)
        return state

    finally:
        print("\nSystem has been stopped")
        GPIO.cleanup()

if __name__ == '__main__':

    # If you have debug=True and receive the error "OSError: [Errno 8] Exec format error", then:
    # remove the execuition bit on this file from a Terminal, ie:
    # chmod -x flask_api_server.py
    #
    # Flask GitHub Issue: https://github.com/pallets/flask/issues/3189

    app.run(host="0.0.0.0", debug=True)

    
