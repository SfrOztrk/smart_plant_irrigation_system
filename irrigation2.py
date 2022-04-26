import RPi.GPIO as GPIO
import time

humidity_sensor = 11
engine = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(humidity_sensor, GPIO.IN)
GPIO.setup(engine, GPIO.OUT)

try:
	while True:
		x = GPIO.input(11)
		print(x)
		if x == 0:
			GPIO.output(7, True)
		else:
			GPIO.output(7, False)
		time.sleep(0.1)

finally:
	print("\nSystem has been stopped")
	GPIO.cleanup()
