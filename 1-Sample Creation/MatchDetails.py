#!/usr/bin/python

import d2slib										#winxp's script
import sys											
import cPickle										#file input and output
import time											#exception pausing for 503 errors


fileName = "[6.82][VH][9.29]Sample.txt"				#MODIFY MANUALLY for different skill levels; normalmatches.txt, highmatches.txt, veryhighmatches.txt
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
			complete = True							#denotes successful datagrab
			counter = counter + 1					
			print counter
			exceptioncounter = 0
			
			# if counter == 40000:
				# fileName = '[6.81][VH][6.19][1]Exp.txt'						#MODIFY MANUALLY for different skill levels; normalexp.txt, highexp.txt, veryhighexp.txt  
				# fileObject = open(fileName,'w')	
				# cPickle.dump(details,fileObject)
				# fileObject.close()
				# del details[:]
			# if counter == 80000:
				# fileName = '[6.81][VH][6.19][2]Exp.txt'						#MODIFY MANUALLY for different skill levels; normalexp.txt, highexp.txt, veryhighexp.txt  
				# fileObject = open(fileName,'w')	
				# cPickle.dump(details,fileObject)
				# fileObject.close()
				# del details[:]
				
		except:
			print "API unavailable"
			time.sleep(5)								
			exceptioncounter = exceptioncounter + 1										
			if exceptioncounter > 2:
				print matchID
				complete = True
				pass
		

fileName = "[6.82][VH][9.29]Exp.txt"							#MODIFY MANUALLY for different skill levels; normalexp.txt, highexp.txt, veryhighexp.txt  
fileObject = open(fileName,'w')							#exp stands for expanded

cPickle.dump(details,fileObject)
fileObject.close()

###

# fileName = '[6.81][H][6.12]TestSample.txt'				#MODIFY MANUALLY for different skill levels; normalmatches.txt, highmatches.txt, veryhighmatches.txt
# fileObject = open(fileName,'r')

# matches = cPickle.load(fileObject)					#matches becomes the list of the match numbers created by aggregator.py and stored in the txt file

# fileObject.close()

# details = []										#list for holding every match object and it's attributes
# complete = False									#forces a d2slib.parseMatch loop until data is successfully grabbed
# counter = 0											#tracks completion rate
# exceptioncounter = 0

# for matchID in matches:
	# complete = False								#each for segment begins with the matchID parsing incomplete
	# while complete == False:
		# try:
			# matchDetails = d2slib.parseMatch(d2slib.getMatchDetails(matchID))
			# details.append(matchDetails)
			# complete = True							#denotes successful datagrab
			# counter = counter + 1					
			# print counter
			# exceptioncounter = 0
		# except:
			# print "API unavailable"
			# time.sleep(5)								
			# exceptioncounter = exceptioncounter + 1										
			# if exceptioncounter > 3:
				# print matchID
				# complete = True
				# pass
		

# fileName = '[6.81][H][6.12]TestExp.txt'						#MODIFY MANUALLY for different skill levels; normalexp.txt, highexp.txt, veryhighexp.txt  
# fileObject = open(fileName,'w')							#exp stands for expanded

# cPickle.dump(details,fileObject)
# fileObject.close()
