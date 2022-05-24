import time
from flask import Flask, request, render_template
from flask_restful import Resource, Api, reqparse, inputs
import main
import os
import psutil


status = {
    'pump': 'OFF',
    'moisture': 'WET',
    'pump_pin': main.WATER_PUMP,
    'mois_pin': main.MOISTURE_SENSOR,
    'auto_mode': 'OFF'
}

main.init_pins()
main.set_pump("OFF")



app = Flask(__name__) # Core Flask app.



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', **status)


# turn on or off the pump manually
@app.route('/pump/<toggle>')
def set_pump(toggle):
    status['auto_mode'] = 'OFF'     # turn off the auto mode
    
    main.set_pump(toggle)           # toggle = "ON" or "OFF"
    update_status()
    
    return render_template('index.html', **status)


# turn on or off the auto mode
@app.route('/auto/<toggle>')
def auto(toggle):
    
    status['auto_mode'] = toggle

    running = False
    if status['auto_mode'] == 'ON':
        for process in psutil.process_iter():
            try:
                if process.cmdline()[1] == '/auto_water.py':
                    running = True
            except:
                pass
        if not running:
            os.system("python3 /home/pi/Projects/iot_soil_moisture_project/auto_water.py&")
    else:
        os.system("pkill -f /main.py")

    update_status()
    return render_template('index.html', **status)


def update_status():
    status['pump'] = main.get_pump_status()   # "ON" or "OFF"
    status['moisture'] = main.get_moisture_status()   # "DRY" or "WET"


if __name__ == '__main__':

    app.run(host="0.0.0.0", debug=True)
