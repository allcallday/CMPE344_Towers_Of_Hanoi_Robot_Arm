#Description:

#import required libraries
import time
import Adafruit_BBIO.GPIO as GPIO

#initialize GPIO pin modes
GPIO.setup("P8_26",GPIO.IN)	#button input
GPIO.setup("P8_16",GPIO.IN)	#rotary encoder input
GPIO.setup("P9_12",GPIO.OUT)	#claw open direction
GPIO.setup("P9_13",GPIO.OUT)	#claw close direction
GPIO.setup("P9_16",GPIO.OUT)
GPIO.setup("P9_23",GPIO.OUT)	#arm pitch up direction
GPIO.setup("P9_26",GPIO.OUT)	#arm pitch down direction
GPIO.setup("P9_27",GPIO.OUT)
GPIO.setup("P8_9",GPIO.OUT)	#arm yaw right/cw direction
GPIO.setup("P8_12",GPIO.OUT)	#arm yaw left/ccw direction
GPIO.setup("P8_13",GPIO.OUT)

#overall motor control demo method
def work():
	#set L293D enable signals to active
	GPIO.output("P9_16",GPIO.HIGH)
	GPIO.output("P9_27",GPIO.HIGH)
	GPIO.output("P8_13",GPIO.HIGH)
	#test motor1 - claw
	GPIO.output("P9_12",GPIO.HIGH)	#open claw
	time.sleep(0.2)
	GPIO.output("P9_12",GPIO.LOW)
	time.sleep(1)
	GPIO.output("P9_13",GPIO.HIGH)	#close claw
	time.sleep(0.3)
	GPIO.output("P9_13",GPIO.LOW)
	#test motor2 - arm pitch
	GPIO.output("P9_26",GPIO.HIGH)	#lower arm
	time.sleep(0.8)
	GPIO.output("P9_26",GPIO.LOW)
	time.sleep(1)
	GPIO.output("P9_23",GPIO.HIGH)	#raise arm
	time.sleep(0.9)
	GPIO.output("P9_23",GPIO.LOW)
	#test motor3 - arm yaw
	GPIO.output("P8_12",GPIO.HIGH)	#turn arm left/ccw
	time.sleep(1.5)
	GPIO.output("P8_12",GPIO.LOW)
	time.sleep(1)
	GPIO.output("P8_9",GPIO.HIGH)	#turn arm right/cw
	time.sleep(1.6)
	GPIO.output("P8_9",GPIO.LOW)

	return

#lift-drop height testing method
def liftDrop():
	GPIO.output("P9_12",GPIO.HIGH)	#open claw
	time.sleep(0.1)
	GPIO.output("P9_12",GPIO.LOW)
	time.sleep(0.5)
	GPIO.output("P9_26",GPIO.HIGH)	#lower arm
	time.sleep(0.95)
	GPIO.output("P9_26",GPIO.LOW)
	time.sleep(0.5)
	GPIO.output("P9_13",GPIO.HIGH)	#close claw
	time.sleep(0.3)
	GPIO.output("P9_13",GPIO.LOW)
	time.sleep(0.5)
	GPIO.output("P9_23",GPIO.HIGH)	#raise arm
	time.sleep(1.15)
	GPIO.output("P9_23",GPIO.LOW)
	time.sleep(0.5)

	return

#===main()===
#set L293D enable pins to active
GPIO.output("P9_16",GPIO.HIGH)
GPIO.output("P9_27",GPIO.HIGH)
GPIO.output("P8_13",GPIO.HIGH)

GPIO.add_event_detect("P8_26",GPIO.FALLING)
ctrl = 0

while ctrl==0:
	print("Waiting for button signal...")
	if GPIO.event_detected("P8_26"):
		ctrl = 1
		work()
	time.sleep(0.2)
while ctrl==1:
	print("Waiting for second button signal...")
	if GPIO.event_detected("P8_26"):
		ctrl=2
		liftDrop()
	time.sleep(0.2)
print("Program finished")
GPIO.cleanup()
