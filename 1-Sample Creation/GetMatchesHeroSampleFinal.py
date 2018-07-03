#!/usr/bin/python

import d2slib													#winxp's script
import sys														
import cPickle													#file input and output
import collections												#checks for duplicates
import time														#exception pausing for 503 errors

sampleName = '6.79][Ursa'											#Names the output file
endingDate = 1384473600									#Set to 12 AM of the day after the final day of the sample period using UTC // http://www.mbari.org/staff/rich/utccalc.htm
heroID = 70												#Sets the hero of the sample.  ID numbers can be looked up in heroList2
sampleSize = 10000											#Sets the size of the sample; I recommend a multiple of 500

def bracketSwitcher(i):									#Used to change the output file so all three brackets are produced sequentially
	baseStr = '[' + sampleName + ']'
	if i == 1:											#i stands for iteration.  Iteration 1 = Normal, Iteration 2 = High, Iteration 3 = Very High
		returnStr = baseStr + "NormalSample.txt"
		return returnStr 
	elif i == 2:
		returnStr = baseStr + "HighSample.txt"
		return returnStr 
	elif i == 3:
		returnStr = baseStr + "VeryHighSample.txt"
		return returnStr 
	else:
		print "Error in bracketSwitcher"
		sys.exit()
		
for i in range(1,4):
	fileName = bracketSwitcher(i)
	fileObject = open(fileName,'w')
	
	print fileName															#Progression Tracking

	matches = d2slib.getMatches(hero=heroID, skill=i, dateMax=endingDate)
	start = int(matches[-1]) - 1											#This is for setting the startID to something lower than the 25th entry of each getMatches call
	timer = endingDate														#Used in the while loop to track what day we're on
	
	counter = 100															#Tracks how far we are into the 500 game per day sample
	totalcounter = 0														#Tracks how far we are into the total sample
	exceptioncounter = 0
	
	while (totalcounter < sampleSize):
		while (counter < 500):	
			try:
				morematches = d2slib.getMatches(hero=heroID, skill=i, startID=start, dateMax=timer)		#morematches is a temporary holder for each page
				matches.extend(morematches)													#Adds the 25 matches grabbed each loop to the back of the entire match collection
				counter = counter + 100														#Adds 25 to counter for each page that is completed
				start = int(morematches[-1]) - 1													
			except:
				print "API Unavailable"
				time.sleep(30)								
				exceptioncounter = exceptioncounter + 1										
				if exceptioncounter > 9:
					print "Server is down"
					sys.exit()															#pauses 15 seconds after a 503 error
		totalcounter = totalcounter + 500													#Adds 500 to totalcounter to represent a completed day of the sample
		print totalcounter																		#Progression Tracking
		counter = 0																			#Resets the progress counter to 0 after every successful 500 match segment
		timer = (timer - (86400))															#Sets the next batch to a dateMax that's 24 hours earlier
		
	print len(matches)					#Checks the number of matches that have been grabbed; should equal the desired sample size for High and Very High, but will be slightly small for Normal

	y = collections.Counter(matches)														#Checks for duplicates, somehow, was on internet must be true
	print [i for i in y if y[i]>1]

	cPickle.dump(matches,fileObject)
	fileObject.close()