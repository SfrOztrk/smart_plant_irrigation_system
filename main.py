import RPi.GPIO as GPIO
import time

MOISTURE_SENSOR = 11
WATER_PUMP = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(MOISTURE_SENSOR, GPIO.IN)
GPIO.setup(WATER_PUMP, GPIO.OUT)

try:
	while True:
		moisture_value = GPIO.input(MOISTURE_SENSOR)

		if moisture_value == 0:
			GPIO.output(WATER_PUMP, True)
			print("The soil is dry. The water pump started to pump water!")
		else:
			GPIO.output(WATER_PUMP, False)
			print("The soil is wet. The water pump stopped pumping water!")
		time.sleep(0.5)

finally:
	print("\nSystem has been stopped")
	GPIO.cleanup()
