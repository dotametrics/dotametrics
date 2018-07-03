#!/usr/bin/python

import d2slib													#winxp's script
import sys														
import cPickle													#file input and output
import collections												#checks for duplicates
import time														#exception pausing for 503 errors

fileName = "[TreantProtector677]VeryHighSample.txt"				#MODIFY MANUALLY for different skill levels
fileObject = open(fileName,'w')									

matches = d2slib.getMatches(hero=83, skill=3, dateMax=1362441600)   #MODIFY MANUALLY for different skill levels; normal: skill=1, high: skill=2, veryhigh: skill=3
																	#hero=83 is Treant Protector.  Figure out a way to automate this in the future using heroList2
start = int(matches[-1]) - 1									#This is for setting the startID to something lower than the 25th entry of each getMatches call
timer = 1362441600 												#March 5th 2012 0:00 AM GMT

																#We're getting the first 500 matches for every 6 hour window
counter = 25													#This keeps track of how far you are into the 500 match loop														
totalcounter = 0												#This is used to determine when a sufficient number of matches have been grabbed
exceptioncounter = 0											#used exclusively for exception shutdown


while (totalcounter < 5000):
	while (counter < 500):	
		try:
			morematches = d2slib.getMatches(hero=83, skill=3, startID=start, dateMax=timer)		#MODIFY MANUALLY; morematches is a temporary holder for each page
			matches.extend(morematches)													#Adds the 25 matches grabbed each loop to the back of the entire match collection
			counter = counter + 25														#Basically adds 25 to counter unless something unexpected is going on in getMatches
			start = int(morematches[-1]) - 1
			exceptioncounter = 0				
		except:
			time.sleep(5)																#pauses 15 seconds after a 503 error
			exceptioncounter = exceptioncounter + 1										#each 503 error in a row increments the exception counter
			if exceptioncounter > 9:
				print "Server is down"
				sys.exit()															#pauses 15 seconds after a 503 error
	totalcounter = totalcounter + 500
	print totalcounter		
	counter = 0																			#Resets the progress counter to 0 after every successful 500 match segment
	timer = (timer - (86400))															#Sets the next batch to a dateMax that's 24 hours earlier
	


	
print len(matches)																		#Checks the number of matches that have been grabbed

y = collections.Counter(matches)														#Checks for duplicates, somehow, was on internet must be true
print [i for i in y if y[i]>1]

cPickle.dump(matches,fileObject)
fileObject.close()
####################################  IGNORE COMMENTS AFTER THIS POINT

fileName = "[TreantProtector677]HighSample.txt"				#MODIFY MANUALLY for different skill levels
fileObject = open(fileName,'w')									

matches = d2slib.getMatches(hero=83, skill=2, dateMax=1362441600)   #MODIFY MANUALLY for different skill levels; normal: skill=1, high: skill=2, veryhigh: skill=3
																	# hero=75 is Silencer.  Figure out a way to automate this in the future using heroList2
start = int(matches[-1]) - 1									#This is for setting the startID to something lower than the 25th entry of each getMatches call
timer = 1362441600 												#February 14th 2012 0:00 AM GMT

																#We're getting the first 500 matches for every 6 hour window
counter = 25													#This keeps track of how far you are into the 500 match loop														
totalcounter = 0												#This is used to determine when a sufficient number of matches have been grabbed


while (totalcounter < 5000):
	while (counter < 500):	
		try:
			morematches = d2slib.getMatches(hero=83, skill=2, startID=start, dateMax=timer)		#MODIFY MANUALLY; morematches is a temporary holder for each page
			matches.extend(morematches)													#Adds the 25 matches grabbed each loop to the back of the entire match collection
			counter = counter + 25														#Basically adds 25 to counter unless something unexpected is going on in getMatches
			start = int(morematches[-1]) - 1																											
		except:
			print "API unavailable"
			time.sleep(15)																#pauses 15 seconds after a 503 error
	totalcounter = totalcounter + 500
	print totalcounter		
	counter = 0																			#Resets the progress counter to 0 after every successful 500 match segment
	timer = (timer - (86400))															#Sets the next batch to a dateMax that's 24 hours earlier
	


	
print len(matches)																		#Checks the number of matches that have been grabbed

y = collections.Counter(matches)														#Checks for duplicates, somehow, was on internet must be true
print [i for i in y if y[i]>1]

cPickle.dump(matches,fileObject)
fileObject.close()
####################################

fileName = "[TreantProtector677]NormalSample.txt"				#MODIFY MANUALLY for different skill levels
fileObject = open(fileName,'w')									

matches = d2slib.getMatches(hero=83, skill=1, dateMax=1362441600)   #MODIFY MANUALLY for different skill levels; normal: skill=1, high: skill=2, veryhigh: skill=3
																	# hero=75 is Silencer.  Figure out a way to automate this in the future using heroList2
start = int(matches[-1]) - 1									#This is for setting the startID to something lower than the 25th entry of each getMatches call
timer = 1362441600 												#February 14th 2012 0:00 AM GMT

																# We're getting the first 500 matches for every 6 hour window
counter = 25													#This keeps track of how far you are into the 500 match loop														
totalcounter = 0												#This is used to determine when a sufficient number of matches have been grabbed


while (totalcounter < 5000):
	while (counter < 500):	
		try:
			morematches = d2slib.getMatches(hero=83, skill=1, startID=start, dateMax=timer)		#MODIFY MANUALLY; morematches is a temporary holder for each page
			matches.extend(morematches)													#Adds the 25 matches grabbed each loop to the back of the entire match collection
			counter = counter + 25														#Basically adds 25 to counter unless something unexpected is going on in getMatches
			start = int(morematches[-1]) - 1																										
		except:
			print "API unavailable"
			time.sleep(15)																#pauses 15 seconds after a 503 error
	totalcounter = totalcounter + 500
	print totalcounter		
	counter = 0																			#Resets the progress counter to 0 after every successful 500 match segment
	timer = (timer - (86400))															#Sets the next batch to a dateMax that's 24 hours earlier
	


	
print len(matches)																		#Checks the number of matches that have been grabbed

y = collections.Counter(matches)														#Checks for duplicates, somehow, was on internet must be true
print [i for i in y if y[i]>1]

cPickle.dump(matches,fileObject)
fileObject.close()