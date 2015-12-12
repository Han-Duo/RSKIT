import datetime
import random
import time
import pyautogui


# get desired click count
clickCount = int(raw_input("Enter click count: "))

for count in range(0, clickCount):
	# Set seed
	random.seed(datetime.datetime.now().microsecond)

	# sleep time
	sleepTime = random.uniform(0.4, 1)
	print "Sleeping for ", sleepTime
	time.sleep(sleepTime)

	# send one mouse click
	pyautogui.click()
	print "Completed click: ", countaw
