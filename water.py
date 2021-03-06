
# External module imp
import RPi.GPIO as GPIO
import datetime
import time

init = False

GPIO.setmode(GPIO.BOARD)

def init_output(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    GPIO.output(pin, GPIO.HIGH)

def get_last_irrigation():
    try:
        f = open("last_watered.txt", "r")
        return f.readline()
    except:
        return "NEVER!"
      
def get_moisture(pin = 11):
    GPIO.setup(pin, GPIO.IN) 
    return GPIO.input(pin)

    
def auto_water(delay = 5, pump_pin = 7, water_sensor_pin = 11):
    init_output(pump_pin)
    print("Here we go! Press CTRL+C to exit")

    counter = 0     # for safety
    try:
        while counter < 10:
            time.sleep(delay)

            if get_moisture(pin = water_sensor_pin) == 1:   # dry
                if counter < 5:
                    pump_on(pump_pin)
                counter += 1
            else:
                counter = 0
    
    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        GPIO.output(pump_pin, GPIO.LOW)
        GPIO.cleanup() # cleanup all GPI
    
    finally:
        GPIO.output(pump_pin, GPIO.LOW)
        GPIO.cleanup()

def pump_on(pump_pin = 7, delay = 1):
    init_output(pump_pin)
    f = open("last_watered.txt", "w")
    f.write(datetime.datetime.now().strftime(" %d %b %Y, %X"))
    f.close()
    GPIO.output(pump_pin, GPIO.LOW)
    time.sleep(1)
    GPIO.output(pump_pin, GPIO.HIGH)
