from flask import Flask, render_template, redirect, url_for
import psutil
import datetime
import water
import os

app = Flask(__name__)

status = {
        'time_now' : datetime.datetime.now().strftime("%d %b %Y, %X"),
        'text' : '',
        'time_watered' : water.get_last_irrigation(),
        }

def update_status(text = ""):
    now = datetime.datetime.now()

    status = {
        'time_now' : now.strftime("%d %b %Y, %X"),
        'text' : text,
        'time_watered' : water.get_last_irrigation()
        }

    return status


@app.route("/")
def hello():
    status = update_status()
    return render_template('main.html', **status)


@app.route("/sensor")
def action():
    moisture_value = water.get_moisture()
    
    message = ""
    if (moisture_value == 1):
        message = "Soil is dry, need water!"
    else:
        message = "Soil is wet!"

    status = update_status(text = message)
    return render_template('main.html', **status)

@app.route("/water")
def action2():
    water.pump_on()
    status = update_status(text = "Watered Once")
    return render_template('main.html', **status)

@app.route("/auto/water/<toggle>")
def auto_water(toggle):
    running = False
    if toggle == "ON":
        status = update_status(text = "Smart Irrigation is Enabled")
        
        for process in psutil.process_iter():
            try:
                if process.cmdline()[1] == 'auto_water.py':
                    status = update_status(text = "Already running")
                    running = True
            except:
                pass
        if not running:
            os.system("python3 auto_water.py&")
    else:
        status = update_status(text = "Smart Irrigation is Disabled")
        os.system("pkill -f water.py")

    return render_template('main.html', **status)



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)