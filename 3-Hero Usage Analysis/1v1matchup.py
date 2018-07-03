#!/usr/bin/python									###THIS IS FOR CREATING A 1V1 MATCHUP CHART

import d2slib										#winxp's script
import sys											#don't know
import cPickle										#file input and output


modheroList = "1v1heroList.txt"						#List of top 25 popular 1v1 heroes
heroListObject = open(modheroList, 'r')
heroList = cPickle.load(heroListObject)				#for use in for loop

fileName = "[6.81][VH][6.19][1v1]Exp.txt"										#EDIT MANUALLY
fileObject = open(fileName,'r')
matchDetails = cPickle.load(fileObject)

fileObject.close()

class matchData:
	opp = str()
	win = bool()	

a = open('[6.81][VH]1v1MatchupChart.txt', "w")
b = open('[6.81][VH]1v1MatchupCount.txt', "w")

a.write(',')
b.write(',') 
for hero in heroList:						
	a.write(hero)
	a.write(',')
	b.write(hero)
	b.write(',')
a.write('\n')
b.write('\n')

for hero in heroList:
	a.write(hero)
	a.write(',')
	b.write(hero)
	b.write(',')
	
	matchList = []
	
	mirrorCount = 0
	
	for match in matchDetails:
		if match.players[0].heroName == match.players[1].heroName and match.players[0].heroName == hero:
			mirrorCount = mirrorCount + 1
		elif match.players[0].heroName == hero:
			matchInfo = matchData()
			matchInfo.opp = match.players[1].heroName
			if match.players[0].win == True:
				matchInfo.win = True
			else:
				matchInfo.win = False
			matchList.append(matchInfo)
		elif match.players[1].heroName == hero:
			matchInfo = matchData()
			matchInfo.opp = match.players[0].heroName
			if match.players[1].win == True:
				matchInfo.win = True
			else:
				matchInfo.win = False
			matchList.append(matchInfo)
			
	matchSum = mirrorCount + len(matchList)
	print hero + ': ' + `matchSum`
	
	for opponent in heroList:
		if opponent == hero:
			a.write('---,')
			b.write(`mirrorCount` + ',')
		else:
			count = 0
			win = 0
		
			for match in matchList:
				if match.opp == opponent:
					count = count + 1
					if match.win == True:
						win = win + 1
			if count == 0:
				a.write('N/A,')
				b.write(`count` + ',')
			else:
				printStr = float(win)/count * 100
				printStr = str('%.2f' % printStr) + '%,'
				
				a.write(printStr)
				b.write(`count` + ',')
	a.write('\n')
	b.write('\n')

a.close()
b.close()