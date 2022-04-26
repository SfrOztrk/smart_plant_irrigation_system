import RPi.GPIO as GPIO
import time
import datetime

humidity_sensor = 11
engine = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(humidity_sensor, GPIO.IN)
GPIO.setup(engine, GPIO.OUT)

try:

	worktime=""

	while True:
		x = GPIO.input(11)
		print(x)
		if x == 0:
			GPIO.output(7, True)
		else:
			GPIO.output(7, False)
			time.sleep(0.4)

			worktime = datetime.datetime.now()
			file = str(worktime.day) + "-" + str(worktime.month) + "-" + str(worktime.year) + ".txt"
			f = open(file, "a")
			f.write("\n")
			f.write("Engine has been worked at " + str(worktime.hour) + ":" + str(worktime.minute) + ":" + str(worktime.second) + " on " + str(worktime.day) + "." + str(worktime.month) + "." + str(worktime.year))
			f.write("\n")
			f.write("-"*60)
		time.sleep(0.1)

finally:
	print("\nSystem has been stopped")
	GPIO.cleanup()
