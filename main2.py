import pigpio
import time
import signal

MOISTURE_SENSOR = 11
WATER_PUMP = 7

pi = pigpio.pi()

pi.set_mode(MOISTURE_SENSOR, pigpio.INPUT)
pi.set_mode(WATER_PUMP, pigpio.OUTPUT)

try:
	while True:
		moisture_value = pi.read(MOISTURE_SENSOR)

		if moisture_value == 0:
			pi.write(WATER_PUMP, 1)
			print("The soil is dry. The water pump started to pump water!")
		else:
			pi.write(WATER_PUMP, 0)
			print("The soil is wet. The water pump stopped pumping water!")
		time.sleep(0.5)

finally:
	print("\nSystem has been stopped")
	signal.pause()
