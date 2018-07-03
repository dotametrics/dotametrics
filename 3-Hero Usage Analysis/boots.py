#!/usr/bin/python

import d2slib										#winxp's script
import sys											#don't know
import cPickle										#file input and output

###Creates an Excel export of the boot purchase percentages of every hero

modheroList = "modheroList2.txt"
heroListObject = open(modheroList, 'r')

heroList = cPickle.load(heroListObject)

heroListObject.close()

fileName = "[6.79][VH][10.22to26]Exp.txt"
fileObject = open(fileName,'r')

matchDetails = cPickle.load(fileObject)

class playerData:
	heroName = str()
	playerWin = bool()
	
	playerBoots = 0				#item ID 29
	playerTreads = 0			#item ID 63
	playerPhase = 0				#item ID 50
	playerArcane = 0			#item ID 180
	playerTranq = 0				#item ID 214
	playerTravel = 0			#item ID 48
	
finalData = []

for match in matchDetails:
	if len(match.players) == 10:
		for player in match.players:
			playerInfo = playerData()
			playerInfo.heroName = player.heroName
			if player.win == True:
				playerInfo.playerWin = True
			else:
				playerInfo.playerWin = False
			for item in player.items:
				if item == 29:
					playerInfo.playerBoots = playerInfo.playerBoots + 1
				if item == 63:
					playerInfo.playerTreads = playerInfo.playerTreads + 1
				if item == 50:
					playerInfo.playerPhase = playerInfo.playerPhase + 1				
				if item == 180:
					playerInfo.playerArcane = playerInfo.playerArcane + 1
				if item == 214:
					playerInfo.playerTranq = playerInfo.playerTranq + 1
				if item == 48:
					playerInfo.playerTravel = playerInfo.playerTravel + 1

			finalData.append(playerInfo)


a = open("BootsVHigh.txt", "w")

com = ','

for hero in heroList:
	counter = 0
	BootsUse = 0
	BootsWin = 0
	TreadsUse = 0
	TreadsWin = 0
	PhaseUse = 0
	PhaseWin = 0
	ArcaneUse = 0
	ArcaneWin = 0
	TranqUse = 0
	TranqWin = 0
	TravelUse = 0
	TravelWin = 0
	for player in finalData:
		if player.heroName == hero:
			counter = counter + 1
			if player.playerBoots > 0:
				BootsUse = BootsUse + 1
				if player.playerWin == True:
					BootsWin = BootsWin + 1
			if player.playerTreads > 0:
				TreadsUse = TreadsUse + 1
				if player.playerWin == True:
					TreadsWin = TreadsWin + 1
			if player.playerPhase > 0:
				PhaseUse = PhaseUse + 1
				if player.playerWin == True:
					PhaseWin = PhaseWin + 1
			if player.playerArcane > 0:
				ArcaneUse = ArcaneUse + 1
				if player.playerWin == True:
					ArcaneWin = ArcaneWin + 1
			if player.playerTranq > 0:
				TranqUse = TranqUse + 1
				if player.playerWin == True:
					TranqWin = TranqWin + 1
			if player.playerTravel > 0:
				TravelUse = TravelUse + 1
				if player.playerWin == True:
					TravelWin = TravelWin + 1
	printString = hero + com + `counter` + com + 'Boots' + com + `BootsUse` + '\n'
	printString = printString + com + `counter` + com + 'Treads' + com + `TreadsUse` + '\n'
	printString = printString + com + `counter` + com + 'Phase' + com + `PhaseUse`+ '\n'
	printString = printString + com + `counter` + com + 'Arcane' + com + `ArcaneUse`+ '\n'
	printString = printString + com + `counter` + com + 'Tranq' + com + `TranqUse`+ '\n'
	printString = printString + com + `counter` + com + 'Travel' + com + `TravelUse`+ '\n' + '\n'
	a.write(printString)
			

