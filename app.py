import time
from flask import Flask, request, render_template
from flask_restful import Resource, Api, reqparse, inputs
import main


status = {
    'pump': "OFF",
    'moisture': "WET",
    'pump_pin': main.WATER_PUMP,
    'mois_pin': main.MOISTURE_SENSOR
}

main.init_pins()
main.set_pump("OFF")



app = Flask(__name__) # Core Flask app.



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', **status)


# get the status 
@app.route('/status', methods=['GET'])
def get_pump():
    update_status()
    return status


# turn on or off the pump manually
@app.route('/pump/<toggle>')
def set_pump(toggle):
    main.set_pump(toggle)    # toggle = "ON" or "OFF"
    update_status()
    return render_template('index.html', **status)



def update_status():
    status["pump"] = main.get_pump_status   # "ON" or "OFF"
    status["moisture"] = main.get_moisture_status   # "DRY" or "WET"


if __name__ == '__main__':

    app.run(host="0.0.0.0", debug=True)
