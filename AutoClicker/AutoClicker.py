import datetime
import random
import time

var = raw_input("Please enter something: ")
print "you entered", var

times = 5

random.seed(datetime.datetime.now().microsecond)

for c in range(0, times):
	sleepTime = random.uniform(0.3, 0.7)
	print "Sleeping for ", sleepTime
	time.sleep(sleepTime)