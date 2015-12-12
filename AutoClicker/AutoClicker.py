import datetime
import random
import time
import pyautogui
import math

# get desired click count
clickCount = int(raw_input("Enter click count: "))

xPos = pyautogui.position()[0];
yPos = pyautogui.position()[1];

def isOutOfBound():
	newXPos = pyautogui.position()[0];
	newYPos = pyautogui.position()[1];

	return math.fabs(xPos - newXPos) > 15 or math.fabs(yPos - newYPos) > 15

for count in range(0, clickCount):
	# Set seed
	random.seed(datetime.datetime.now().microsecond)

	# sleep time
	sleepTime = random.uniform(0.3, 0.85)
	print "Sleeping for ", sleepTime
	time.sleep(sleepTime)

	# check if user moved the mouse
	if(isOutOfBound()):
		print "Process stopped since mouse is out of initial range"
		break

	# send one mouse click
	# mouse down
	pyautogui.mouseDown(x=xPos, y=yPos, button='left')
	
	#sleep while mouse is down
	sleepTime = random.uniform(0.08, 0.25)
	print "Mouse down and sleep for ", sleepTime
	time.sleep(sleepTime)

	# check if user moved the mouse
	if(isOutOfBound()):
		#get new range
		xPos = pyautogui.position()[0];
		yPos = pyautogui.position()[1];
		pyautogui.mouseUp(x=xPos, y=yPos, button='left')
		print "Process stopped since mouse is out of initial range"
		break

	#mouse up
	pyautogui.mouseUp(x=xPos, y=yPos, button='left')

	print "Completed click: ", count
