import pigpio
import time

MOISTURE_SENSOR = 11

pi = pigpio.pi()
pi.set_mode(MOISTURE_SENSOR, pigpio.INPUT)

while true:
    print(pi.read(MOISTURE_SENSOR))
    time.sleep(1)