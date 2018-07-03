#!/usr/bin/python

import d2slib													#winxp's script
import sys														#Don't know
import cPickle													#file input and output
import collections												#checks for duplicates
import time														#exception pausing for 503 errors

endingDate = 1391558400											#Set to Jan 8, 12 AM // http://www.mbari.org/staff/rich/utccalc.htm
sampleSize = 500												#Sets the size of the sample PER HERO; I recommend a multiple of 500; every 500 adds an additional day

patch = '[6.80]'
sample = '[2.5]Sample.txt'

for x in range(1,4):
	bracketID = x
	if bracketID == 1:
		bracket = '[N]'
	if bracketID == 2:
		bracket = '[H]'
	if bracketID == 3:
		bracket = '[VH]'

	fileName = patch+bracket+sample											#Names the output file										
	fileObject = open(fileName,'w')											#1 for Normal, 2 for High, 3 for Very High

	fullSample = []
	
	print fileName

	for i in range(1,111):
		if i == 24 or i == 105 or i == 108:
			pass
		else:
			matches = d2slib.getMatches(hero=i, skill=bracketID, dateMax=endingDate)
			start = int(matches[-1]) - 1											#This is for setting the startID to something lower than the 25th entry of each getMatches call
			timer = endingDate														#Used in the while loop to track what day we're on
			
			counter = 100															#Tracks how far we are into the 500 game per day sample
			totalcounter = 0														#Tracks how far we are into the total sample
			
			while (totalcounter < sampleSize):
				while (counter < 500):
					try:
						morematches = d2slib.getMatches(hero=i, skill=bracketID, startID=start, dateMax=timer)		#morematches is a temporary holder for each page
						matches.extend(morematches)													#Adds the 25 matches grabbed each loop to the back of the entire match collection
						counter = counter + 100														#Adds 25 to counter for each page that is completed
						start = int(morematches[-1]) - 1													
					except:
						print "API Unavailable"
						time.sleep(5)																	#pauses 15 seconds after a 503 error
				totalcounter = totalcounter + 500													#Adds 500 to totalcounter to represent a completed day of the sample								
				counter = 0																			#Resets the progress counter to 0 after every successful 500 match segment
				timer = (timer - (86400))															#Sets the next batch to a dateMax that's 24 hours earlier
			
			fullSample.extend(matches)
			del matches[:]
			
			print '%d out of 110 complete' % i

	print len(fullSample)
	fullSample = list(set(fullSample))
	print len(fullSample)

	y = collections.Counter(fullSample)														#Checks for duplicates, somehow, was on internet must be true
	print [i for i in y if y[i]>1]

	cPickle.dump(fullSample,fileObject)
	fileObject.close()