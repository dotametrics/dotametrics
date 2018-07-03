#!/usr/bin/python

import d2slib													#winxp's script
import sys														
import cPickle													#file input and output
import collections												#checks for duplicates
import time														#exception pausing for 503 errors

fileName = "[6.80][VH][1.30]Sample.txt"							#MODIFY MANUALLY for skill level and date
fileObject = open(fileName,'w')									

matches = d2slib.getMatches(skill=3, dateMax=1391040000)		#MODIFY MANUALLY for different skill levels; normal: skill=1, high: skill=2, veryhigh: skill=3
start = int(matches[-1]) - 1

timer = 1391040000 												#January 30th 2014 12:00 AM UTC

																#We're getting the first 500 matches for every 6 hour window
counter = 25													#This keeps track of how far you are into the 500 match loop														#This is for setting the startID to something lower than the 25th entry of each getMatches call
totalcounter = len(matches)										#This determines when 10,000 matches have been grabbed
exceptioncounter = 0											#used exclusively for exception shutdown


while (totalcounter < 500):
	while (counter < 500):	
		try:
			morematches = d2slib.getMatches(skill=3, startID=start, dateMax=timer)		#MODIFY MANUALLY for different skill levels; normal: skill=1, high: skill=2, veryhigh: skill=3
			matches.extend(morematches)													#Adds the 25 matches grabbed each loop to the back of the entire match collection
			counter = counter + 100														#Basically adds 25 to counter unless something unexpected is going on in getMatches
			start = int(morematches[-1]) - 1											
			exceptioncounter = 0														#resets script shutdown counter	
		except:
			print "API Unavailable"
			time.sleep(5)																#pauses 15 seconds after a 503 error
			exceptioncounter = exceptioncounter + 1										#each 503 error in a row increments the exception counter
			if exceptioncounter > 9:
				print "Server is down"
				sys.exit()																#Assumes the API server is down after 10 503 failures and cancels the program
	totalcounter = totalcounter + 500	
	counter = 0																			#Resets the progress counter to 0 after every successful 500 match segment
	timer = (timer - (86400))															#Sets the next batch to a dateMax that's 24 hours earlier
	


	
print len(matches)																		#Checks that precisely 10,000 matches have been grabbed

y = collections.Counter(matches)														#Checks for duplicates, somehow, was on internet must be true
print [i for i in y if y[i]>1]

cPickle.dump(matches,fileObject)