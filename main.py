import RPi.GPIO as GPIO
import time
import app

MOISTURE_SENSOR = 11
WATER_PUMP = 7

auto_mode = 'OFF'	# default value is OFF

def init_pins():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(MOISTURE_SENSOR, GPIO.IN)
	GPIO.setup(WATER_PUMP, GPIO.OUT)

def get_moisture_status():
	if GPIO.input(MOISTURE_SENSOR) == 1:
		return 'WET'
	else:
		return 'DRY'

def get_pump_status():
	if GPIO.input(WATER_PUMP) == 0:
		return 'ON'
	else:
		return 'OFF'

def set_pump(state):
	if state == 'ON':
		GPIO.output(WATER_PUMP, 0)
	elif state == 'OFF':
		GPIO.output(WATER_PUMP, 1)

def irrigation(delay):
	try:
		while auto_mode=='ON':

			if get_moisture_status() == 0:
				set_pump('ON')
				print("The soil is dry. The water pump started to pump water!")
			else:
				set_pump('OFF')
				print("The soil is wet. The water pump stopped pumping water!")
			
			app.index()
			time.sleep(delay)
	
	except KeyboardInterrupt:  	# If CTRL+C is pressed, exit cleanly:
		GPIO.cleanup() 			# cleanup all GPI