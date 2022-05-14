import RPi.GPIO as GPIO
import time

humidity_sensor = 11
water_pump = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(humidity_sensor, GPIO.IN)
GPIO.setup(water_pump, GPIO.OUT)

try:
	while True:
		humidity_value = GPIO.input(humidity_sensor)

		if humidity_value == 0:
			GPIO.output(water_pump, True)
			print("The soil is dry. The water pump started to pump water!")
		else:
			GPIO.output(water_pump, False)
			print("The soil is wet. The water pump stopped pumping water!")
		time.sleep(0.5)

finally:
	print("\nSystem has been stopped")
	GPIO.cleanup()
