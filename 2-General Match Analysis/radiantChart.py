#!/usr/bin/python

import d2slib										#winxp's script
import sys											#don't know
import cPickle										#file input and output

def bracketSwitcher(i, sampleName):							#Used to change the input file so all three brackets are tested sequentially
	baseStr = '[' + sampleName + ']'
	if i == 1:											#i stands for iteration.  Iteration 1 = Normal, Iteration 2 = High, Iteration 3 = Very High
		returnStr = baseStr + "NormalExp.txt"
		return returnStr 
	elif i == 2:
		returnStr = baseStr + "HighExp.txt"
		return returnStr 
	elif i == 3:
		# returnStr = baseStr + "VeryHighExp.txt"
		returnStr = '[6.78][VH][10.22]Exp.txt'
		return returnStr 
	else:
		print "Error in bracketSwitcher"
		sys.exit()
		
class matchData:
	matchID = int()
	winner = bool()
	duration = int()
	skill = str()

sampleName = 'Feb'
matchList = []
		
for i in range(3,4):
	fileName = bracketSwitcher(i, sampleName)
	fileObject = open(fileName,'r')
	matchDetails = cPickle.load(fileObject)
	fileObject.close()
	
	for match in matchDetails:
		matchInfo = matchData()
		matchInfo.matchID = match.matchID
		matchInfo.winner = match.winner
		matchInfo.duration = match.duration
		if i == 1:
			matchInfo.skill = 'n'
		elif i == 2:
			matchInfo.skill = 'h'
		elif i == 3:
			matchInfo.skill = 'v'
		matchList.append(matchInfo)

baseStr = '[' + sampleName + ']'
baseStr = baseStr + "RadiantChart.txt"
a = open(baseStr, "w")

game = 0

for x in range(3,12):
	gameCount = 0
	radWin = 0
	for match in matchList:
		if match.duration < x*60*5:
			pass
		elif match.duration < (x+1)*60*5:
			gameCount = gameCount + 1
			if match.winner == True:
				radWin = radWin + 1
			game = game + 1
	if gameCount == 0:
		radWinPerc = 'N/A'
	else:
		radWinPerc = radWin/float(gameCount)*100
		radWinPerc = str('%.2f' % radWinPerc) + '%,'
	writeStr = radWinPerc
	# a.write(`gameCount` + ',')
	a.write(writeStr)

	print game