#Description: code testing Adafruit GPIO digital input functionality

import Adafruit_BBIO.GPIO as GPIO
import time
GPIO.setup("P8_26",GPIO.IN)
GPIO.setup("P8_16",GPIO.OUT)
GPIO.setup("P8_13",GPIO.OUT)
GPIO.setup("P8_12",GPIO.OUT)

ctrl = 0
GPIO.add_event_detect("P8_26",GPIO.FALLING)

while ctrl != 1:
	print("waiting for button signal...")
	if GPIO.event_detected("P8_26"):
		print("Event detected. Now running motor for 3 sec.")
		GPIO.output("P8_16",GPIO.HIGH)
		GPIO.output("P8_12",GPIO.HIGH)
		time.sleep(2)
		print("Now running motor in other direction for 2 sec.")
		GPIO.output("P8_12",GPIO.LOW)
		GPIO.output("P8_13",GPIO.HIGH)
		time.sleep(1)
		GPIO.output("P8_13",GPIO.LOW)
		GPIO.output("P8_16",GPIO.LOW)
		ctrl = 1
	time.sleep(0.1)
GPIO.cleanup()
