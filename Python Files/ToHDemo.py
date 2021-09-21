#import required libraries
import time
import Adafruit_BBIO.GPIO as GPIO

#define functions
# methods to plan move order
def ToHMoves(moveOrder):
	ToHAlgorithm(moveOrder,3,1,2,3)
	return moveOrder

def ToHAlgorithm(moveOrder,N,beg,other,tgt):
	if (N==1):
		if (beg==1 and tgt==2):
			toAppend = 1
		if(beg==1 and tgt==3):
			toAppend = 2
		if(beg==2 and tgt==1):
			toAppend = 3
		if(beg==2 and tgt==3):
			toAppend = 4
		if(beg==3 and tgt==1):
			toAppend = 5
		if(beg==3 and tgt==2):
			toAppend = 6
		moveOrder.extend(toAppend)
	else:
		ToHAlgorithm(moveOrder,N-1,beg,tgt,other)
		ToHAlgorithm(moveOrder,1,beg,other,tgt)
		ToHAlgorithm(moveOrder,N-1,other,beg,tgt)
	return

# method to loop through moveOrder list and physically execute moves
def ToHWork(moveOrder):
	s = pythonSwitch()
	for index in range(len(moveOrder)):
		if (index%2)==1:
			continue
		s.switch(moveOrder[index])
	return

# method to operate claw and arm-pitch motors to pick up or drop a piece
def liftDrop(moveType):
	if moveType==1:
		GPIO.output("P9_12",GPIO.HIGH)	#open claw
		time.sleep(0.1)
		GPIO.output("P9_12",GPIO.LOW)
		time.sleep(0.5)
	GPIO.output("P9_26",GPIO.HIGH)	#lower arm
	time.sleep(0.95)
	GPIO.output("P9_26",GPIO.LOW)
	time.sleep(0.5)
	if moveType==0:
		GPIO.output("P9_13",GPIO.HIGH)	#close claw
		time.sleep(0.2)
		GPIO.output("P9_13",GPIO.LOW)
		time.sleep(0.5)
	GPIO.output("P9_26",GPIO.HIGH)	#raise arm
	time.sleep(1.15)
	GPIO.output("P9_26",GPIO.LOW)
	time.sleep(0.5)
	return

# swtich method
def switch(num):
	if (num==1):	#move from left to mid
		liftDrop(0)
		#move yaw to mid
		GPIO.output("P8_9",GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output("P8_9",GPIO.LOW)
		time.sleep(0.5)
		liftDrop(1)
		#return arm to left
		GPIO.output("P8_12",GPIO.HIGH)
		time.sleep(0.45)
		GPIO.output("P8_12",GPIO.LOW)
		time.sleep(0.5)
		return
	if (num==2):	#move from left to right
		liftDrop(0)
		#move yaw to right
		GPIO.output("P8_9",GPIO.HIGH)
		time.sleep(1)
		GPIO.output("P8_9",GPIO.LOW)
		time.sleep(0.5)
		liftDrop(1)
		#return arm to left
		GPIO.output("P8_12",GPIO.HIGH)
		time.sleep(0.95)
		GPIO.output("P8_12",GPIO.LOW)
		time.sleep(0.5)
		return
	if (num==3):	#move from mid to left
		#move arm to mid
		GPIO.output("P8_9",GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output("P8_9",GPIO.LOW)
		time.sleep(0.5)
		liftDrop(0)
		#move yaw to left
		GPIO.output("P8_12",GPIO.HIGH)
		time.sleep(0.45)
		GPIO.output("P8_12",GPIO.LOW)
		time.sleep(0.45)
		liftDrop(1)
		return
	if (num==4):	#move from mid to right
		#move arm to mid
		GPIO.output("P8_9",GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output("P8_9",GPIO.LOW)
		time.sleep(0.5)
		liftDrop(0)
		#move arm to right
		GPIO.output("P8_9",GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output("P8_9",GPIO.LOW)
		time.sleep(0.5)
		liftDrop(1)
		#return arm to left
		GPIO.output("P8_12",GPIO.HIGH)
		time.sleep(0.95)
		GPIO.output("P8_12",GPIO.LOW)
		time.sleep(0.5)
		return
	if (num==5):	#move from right to left
		#move arm to right
		GPIO.output("P8_9",GPIO.HIGH)
		time.sleep(1)
		GPIO.output("P8_9",GPIO.LOW)
		time.sleep(0.5)
		liftDrop(0)
		#move arm to left
		GPIO.output("P8_12",GPIO.HIGH)
		time.sleep(0.95)
		GPIO.output("P8_12",GPIO.LOW)
		time.sleep(0.5)
		liftDrop(1)
		return
	if (num==6):	#move from right to mid
		#move arm to right
		GPIO.output("P8_9",GPIO.HIGH)
		time.sleep(1)
		GPIO.output("P8_9",GPIO.LOW)
		time.sleep(0.5)
		liftDrop(0)
		#move arm to mid
		GPIO.output("P8_12",GPIO.HIGH)
		time.sleep(0.45)
		GPIO.output("P8_12",GPIO.LOW)
		time.sleep(0.5)
		liftDrop(1)
		#return arm to left
		GPIO.output("P8_12",GPIO.HIGH)
		time.sleep(0.45)
		GPIO.output("P8_12",GPIO.LOW)
		time.sleep(0.5)
		return

		

#=== main() ===
#declare variable
moveOrder = []

#initialize GPIO pin modes
GPIO.setup("P8_26",GPIO.IN)
GPIO.setup("P9_12",GPIO.OUT)
GPIO.setup("P9_13",GPIO.OUT)
GPIO.setup("P9_16",GPIO.OUT)
GPIO.setup("P9_23",GPIO.OUT)
GPIO.setup("P9_26",GPIO.OUT)
GPIO.setup("P9_27",GPIO.OUT)
GPIO.setup("P8_9",GPIO.OUT)
GPIO.setup("P8_12",GPIO.OUT)
GPIO.setup("P8_13",GPIO.OUT)
GPIO.add_event_detect("P8_26",GPIO.RISING)
GPIO.output("P9_16",GPIO.HIGH)
GPIO.output("P9_27",GPIO.HIGH)
GPIO.output("P8_13",GPIO.HIGH)

#wait for start signal from button
ctrl = 0
while ctrl==0:
	if GPIO.event_detected("P8_26"):
		ctrl = 1
		ToHMoves(moveOrder)
		ToHWork(moveOrder)
	time.sleep(0.2)
print("Program finished.")
GPIO.cleanup()
