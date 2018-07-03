#!/usr/bin/python

import d2slib										#winxp's script
import sys											#don't know
import cPickle										#file input and output
import collections									#used for Counter

###Produces the server cluster distribution of a sample

def bracketSwitcher(i, sampleName):							#Used to change the input file so all three brackets are tested sequentially
	baseStr = '[' + sampleName + ']'
	if i == 1:											#i stands for iteration.  Iteration 1 = Normal, Iteration 2 = High, Iteration 3 = Very High
		returnStr = baseStr + "NormalExp.txt"
		return returnStr 
	elif i == 2:
		returnStr = baseStr + "HighExp.txt"
		return returnStr 
	elif i == 3:
		returnStr = baseStr + "VeryHighExp.txt"
		return returnStr 
	else:
		print "Error in bracketSwitcher"
		sys.exit()
		
class matchData:
	matchID = int()
	cluster = int()

sampleName = 'Feb'
matchList = []
		
for i in range(1,4):
	fileName = bracketSwitcher(i, sampleName)
	fileObject = open(fileName,'r')
	matchDetails = cPickle.load(fileObject)
	fileObject.close()
	
	bracketData = []
	
	for match in matchDetails:
		bracketData.append(match.cluster)
	matchList.append(bracketData)

for i in range(0,3):
	clusterList = collections.Counter(matchList[i]).most_common(15)
	for x in clusterList:
		print x
	print '\n'