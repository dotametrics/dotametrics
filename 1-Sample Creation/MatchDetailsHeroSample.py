#!/usr/bin/python

import d2slib										#winxp's script
import sys											
import cPickle										#file input and output
import time											#exception pausing for 503 errors

fileName = "[TreantProtector677c]VeryHighSample.txt"	#MODIFY MANUALLY for different skill levels; normalmatches.txt, highmatches.txt, veryhighmatches.txt
fileObject = open(fileName,'r')

matches = cPickle.load(fileObject)					#matches becomes the list of the match numbers created by aggregator.py and stored in the txt file

fileObject.close()

details = []										#list for holding every match object and it's attributes
complete = False									#forces a d2slib.parseMatch loop until data is successfully grabbed
counter = 0											#tracks completion rate
exceptioncounter = 0

for matchID in matches:
	complete = False								#each for segment begins with the matchID parsing incomplete
	while complete == False:
		try:
			matchDetails = d2slib.parseMatch(d2slib.getMatchDetails(matchID))
			details.append(matchDetails)
			complete = True;							#denotes successful datagrab
			counter = counter + 1					
			print counter
			exceptioncounter = 0
		except:
			print "API unavailable"
			time.sleep(30)								
			exceptioncounter = exceptioncounter + 1										
			if exceptioncounter > 8:
				print "Server is down"
				sys.exit()		

fileName = "[TreantProtector677c]VeryHighExp.txt"								#MODIFY MANUALLY for different skill levels; normalexp.txt, highexp.txt, veryhighexp.txt  
fileObject = open(fileName,'w')							#exp stands for expanded

cPickle.dump(details,fileObject)
fileObject.close()
#########################################################

fileName = "[TreantProtector677c]HighSample.txt"		#MODIFY MANUALLY for different skill levels; normalmatches.txt, highmatches.txt, veryhighmatches.txt
fileObject = open(fileName,'r')

matches = cPickle.load(fileObject)					#matches becomes the list of the match numbers created by aggregator.py and stored in the txt file

fileObject.close()

hdetails = []										#list for holding every match object and it's attributes
complete = False									#forces a d2slib.parseMatch loop until data is successfully grabbed
counter = 0											#tracks completion rate

for matchID in matches:
	complete = False								#each for segment begins with the matchID parsing incomplete
	while complete == False:
		try:
			matchDetails = d2slib.parseMatch(d2slib.getMatchDetails(matchID))
			hdetails.append(matchDetails)
			complete = True;							#denotes successful datagrab
			counter = counter + 1					
			print counter
			exceptioncounter = 0
		except:
			print "API unavailable"
			time.sleep(30)								#pauses 15 seconds after a 503 error
			exceptioncounter = exceptioncounter + 1										
			if exceptioncounter > 8:
				print "Server is down"
				sys.exit()

fileName = "[TreantProtector677c]HighExp.txt"		#MODIFY MANUALLY for different skill levels; normalexp.txt, highexp.txt, veryhighexp.txt  
fileObject = open(fileName,'w')							#exp stands for expanded

cPickle.dump(hdetails,fileObject)
fileObject.close()

#####################################################

fileName = "[TreantProtector677c]NormalSample.txt"	#MODIFY MANUALLY for different skill levels; normalmatches.txt, highmatches.txt, veryhighmatches.txt
fileObject = open(fileName,'r')

matches = cPickle.load(fileObject)					#matches becomes the list of the match numbers created by aggregator.py and stored in the txt file

fileObject.close()

vdetails = []										#list for holding every match object and it's attributes
complete = False									#forces a d2slib.parseMatch loop until data is successfully grabbed
counter = 0											#tracks completion rate

for matchID in matches:
	complete = False								#each for segment begins with the matchID parsing incomplete
	while complete == False:
		try:
			matchDetails = d2slib.parseMatch(d2slib.getMatchDetails(matchID))
			vdetails.append(matchDetails)
			complete = True;							#denotes successful datagrab
			counter = counter + 1					
			print counter
			exceptioncounter = 0
		except:
			print "API unavailable"
			time.sleep(30)								#pauses 15 seconds after a 503 error
			exceptioncounter = exceptioncounter + 1										
			if exceptioncounter > 8:
				print "Server is down"
				sys.exit()

fileName = "[TreantProtector677c]NormalExp.txt"		#MODIFY MANUALLY for different skill levels; normalexp.txt, highexp.txt, veryhighexp.txt  
fileObject = open(fileName,'w')							#exp stands for expanded

cPickle.dump(vdetails,fileObject)
fileObject.close()