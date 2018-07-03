#!/usr/bin/python

import d2slib										#winxp's script
import sys											
import cPickle										#file input and output
import time											#exception pausing for 503 errors

filePrefix = '6.79][Ursa'

def bracketSwitcher(i):									#Used to change the output file so all three brackets are produced sequentially
	baseStr = '[' + filePrefix + ']'
	if i == 1:											#i stands for iteration.  Iteration 1 = Normal, Iteration 2 = High, Iteration 3 = Very High
		returnStr = baseStr + "Normal"
		return returnStr 
	elif i == 2:
		returnStr = baseStr + "High"
		return returnStr 
	elif i == 3:
		returnStr = baseStr + "VeryHigh"
		return returnStr 
	else:
		print "Error in bracketSwitcher"
		sys.exit()
		
for i in range(1,4):
	fileName = bracketSwitcher(i) + 'Sample.txt'
	fileObject = open(fileName,'r')
	
	print fileName															#Progression Tracking
	
	matches = cPickle.load(fileObject)					#matches becomes the list of the match numbers created by aggregator.py and stored in the txt file

	fileObject.close()

	details = []										#list for holding every match object and it's attributes
	complete = False									#forces a d2slib.parseMatch loop until data is successfully grabbed
	counter = 0											#tracks completion rate
	exceptioncounter = 0
	
	for matchID in matches:
		complete = False								#Resets each loop to incomplete
		while complete == False:
			try:
				matchDetails = d2slib.parseMatch(d2slib.getMatchDetails(matchID))
				details.append(matchDetails)
				complete = True							#Marks loop as complete
				counter = counter + 1					
				print counter
				exceptioncounter = 0
			except:
				print "API unavailable"
				time.sleep(30)								
				exceptioncounter = exceptioncounter + 1										
				if exceptioncounter > 2:
					complete = True
					pass
					# print "Server is down"
					# sys.exit()
					
	fileName = bracketSwitcher(i) + 'Exp.txt'	
	fileObject = open(fileName,'w')							

	cPickle.dump(details,fileObject)
	fileObject.close()