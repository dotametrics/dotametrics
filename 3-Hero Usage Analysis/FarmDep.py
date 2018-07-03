#!/usr/bin/python

import d2slib										#winxp's script
import sys											#don't know
import cPickle										#file input and output
import math
import collections

class playerData:
	heroUsed = str()
	CSpM = int()
	win = bool()

finalData = []

# fileName = '[6.79][Legion Commander]VeryHigh.txt'	
# fileObject = open(fileName,'r')

# matchDetails = cPickle.load(fileObject)
# fileObject.close()

# files = ['[6.79][N][1.7]Exp.txt', '[6.79][N][1.8]Exp.txt', '[6.79][N][1.9]Exp.txt', '[6.79][N][1.10]Exp.txt', '[6.79][N][1.11]Exp.txt', '[6.79][N][1.12]Exp.txt', '[6.79][N][1.13]Exp.txt', '[6.79][N][1.14]Exp.txt', '[6.79][N][1.15]Exp.txt', '[6.79][N][1.16]Exp.txt']
# files = ['[6.79][H][1.7]Exp.txt', '[6.79][H][1.8]Exp.txt', '[6.79][H][1.9]Exp.txt', '[6.79][H][1.10]Exp.txt', '[6.79][H][1.11]Exp.txt', '[6.79][H][1.12]Exp.txt', '[6.79][H][1.13]Exp.txt', '[6.79][H][1.14]Exp.txt', '[6.79][H][1.15]Exp.txt', '[6.79][H][1.16]Exp.txt']
# files = ['[6.79][VH][1.7]Exp.txt', '[6.79][VH][1.8]Exp.txt', '[6.79][VH][1.9]Exp.txt', '[6.79][VH][1.10]Exp.txt', '[6.79][VH][1.11]Exp.txt', '[6.79][VH][1.12]Exp.txt', '[6.79][VH][1.13]Exp.txt', '[6.79][VH][1.14]Exp.txt', '[6.79][VH][1.15]Exp.txt', '[6.79][VH][1.16]Exp.txt']

files = ['[6.80][4Day][Phoenix]VeryHigh.txt']

a = open("[6.80][VH]PhoenixFarmDep.txt", "w")

for file in files:
	print file
	fileName = file										#EDIT MANUALLY
	fileObject = open(fileName,'r')
	matchDetails = cPickle.load(fileObject)	

	for match in matchDetails:
		if len(match.players) == 10:
			if match.duration > 899:
				duration = match.duration / float(60)
				for player in match.players:
					CSpM = player.cs/duration
					if CSpM > 0:
						playerInfo = playerData()
						playerInfo.heroUsed = player.heroName
						if player.win == True:
							playerInfo.win = True
						else:
							player.win = False
						playerInfo.CSpM = CSpM
						finalData.append(playerInfo)						
	
	
	
# heroList = "heroList2"
# heroListObject = open(heroList, 'rb')
# heroList = cPickle.load(heroListObject)
# heroListObject.close()

heroList = ['Phoenix']

tab = '\t'
com = ','

for hero in heroList:
	heroStats = []
	winCount = 0
	for entry in finalData:
		if hero == entry.heroUsed:
			heroStats.append(entry)
			if entry.win == True:
				winCount = winCount + 1
	if len(heroStats) == 0:
		pass
	else:
				
		heroStats.sort(key = lambda x: x.CSpM)
		
		divisor = (len(heroStats)/5)
		firstBreak = len(heroStats)-(divisor*4)
		secondBreak = len(heroStats)-(divisor*3)
		thirdBreak = len(heroStats)-(divisor*2)
		fourthBreak = len(heroStats)-(divisor*1)
		
		counter = 0
		
		firstCounter = 0
		secondCounter = 0
		thirdCounter = 0
		fourthCounter = 0
		fifthCounter = 0
		
		firstWin = 0
		secondWin = 0
		thirdWin = 0
		fourthWin = 0
		fifthWin = 0
		
		firstAvg = 0
		fifthAvg = 0
		
		print hero
		
		for x in xrange(0, firstBreak):
			counter = counter + 1
			firstCounter = firstCounter + 1
			firstAvg = firstAvg + heroStats[x].CSpM
			if heroStats[x].win == True:
				firstWin = firstWin + 1
				

		firstAvg = firstAvg/firstCounter
		for x in xrange(firstBreak, secondBreak):
			counter = counter + 1
			secondCounter = secondCounter + 1
			if heroStats[x].win == True:
				secondWin = secondWin + 1
		
		for x in xrange(secondBreak, thirdBreak):
			counter = counter + 1
			thirdCounter = thirdCounter + 1
			if heroStats[x].win == True:
				thirdWin = thirdWin + 1
		
		for x in xrange(thirdBreak, fourthBreak):
			counter = counter + 1
			fourthCounter = fourthCounter + 1
			if heroStats[x].win == True:
				fourthWin = fourthWin + 1
				
		for x in xrange(fourthBreak, (len(heroStats))):
			counter = counter + 1
			fifthCounter = fifthCounter + 1
			fifthAvg = fifthAvg + heroStats[x].CSpM
			if heroStats[x].win == True:
				fifthWin = fifthWin + 1
		

		fifthAvg = fifthAvg/fifthCounter
		print firstAvg
		print fifthAvg
		
		firstAvg = fifthAvg/fifthCounter
		winRate = float(winCount)/len(heroStats)
		firstWinRate = float(firstWin)/firstCounter
		secondWinRate = float(secondWin)/secondCounter
		thirdWinRate = float(thirdWin)/thirdCounter
		fourthWinRate = float(fourthWin)/fourthCounter
		fifthWinRate = float(fifthWin)/fifthCounter
		
		firstWinMod = (firstWinRate - winRate) 
		secondWinMod = (secondWinRate - winRate) 
		thirdWinMod = (thirdWinRate - winRate) 
		fourthWinMod = (fourthWinRate - winRate) 
		fifthWinMod = (fifthWinRate - winRate) 
		
		print '\n'
		
		a.write(hero + com*2)
		a.write (`len(heroStats)`)
		a.write(com)
		a.write('%.4f' %  winRate)
		a.write(com*2)
		a.write('%.4f' %  firstWinMod)
		a.write(com)
		a.write('%.4f' %  secondWinMod)
		a.write(com)
		a.write('%.4f' %  thirdWinMod)
		a.write(com)
		a.write('%.4f' %  fourthWinMod)
		a.write(com)
		a.write('%.4f' %  fifthWinMod)
		a.write('\n')