# Description: uses Adafruit GPIO library to manipulate pinouts of a BeagleBone
#		Black to provide control signals to an L293D circuit to control how a DC
#		motor runs

import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P9_27",GPIO.OUT)	#connected to L293D pin1
GPIO.setup("P9_23",GPIO.OUT)	#connected to L293D pin2
GPIO.setup("P9_26",GPIO.OUT)	#connected to L293D pin7
	#additional L293D pin connection info:
	#	* 5V VDD into pin16	-	supplies power to L293D
	#	* GND into any of pins 4,5,12,13	-	electrical ground
	#	* 7V into pin8	-	supplies driving power to motors, same ground as others

GPIO.output("P9_27",GPIO.HIGH)	#enable L293D H-bridge for pins1-7
GPIO.output("P9_23",GPIO.HIGH)	#run motor in one direction for 5 sec
time.sleep(5)
GPIO.output("P9_23",GPIO.LOW)
GPIO.output("P9_26",GPIO.HIGH)	#run motor in other direction for 3 sec
time.sleep(3)
GPIO.output("P9_26",GPIO.LOW)
GPIO.output("P9_27",GPIO.LOW)
GPIO.cleanup()
