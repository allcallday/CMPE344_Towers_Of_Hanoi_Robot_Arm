#Description: code to test feedback processing from Lego NXT motor's rotary encoder

import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("P8_16",GPIO.IN)
GPIO.add_event_detect("P8_16",GPIO.RISING)

#declare and initialize variables
ctrl = 0
deg = 0

print("rotate the motor 180 degrees.")
while deg<180:
	if GPIO.event_detected("P8_16"):
		deg += 2
		print(deg)

print("rotate the motor 90 degrees.")
deg = 0
while deg<90:
	if GPIO.event_detected("P8_16"):
		deg += 2
		print(deg)

print("Program finished.")
