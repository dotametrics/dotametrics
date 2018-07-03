#!/usr/bin/python									###THIS IS FOR GETTING HERO WIN RATES RATES OUT OF A MULTI-PART MATCH AGGREGATION

import d2slib										#winxp's script
import sys											#don't know
import cPickle										#file input and output


modheroList = "modheroList2.txt"						#List of current heroes
heroListObject = open(modheroList, 'r')

heroList = cPickle.load(heroListObject)				#for use in for loop

# files = ['[6.79][N][1.7]Exp.txt', '[6.79][N][1.8]Exp.txt', '[6.79][N][1.9]Exp.txt', '[6.79][N][1.10]Exp.txt', '[6.79][N][1.11]Exp.txt', '[6.79][N][1.12]Exp.txt', '[6.79][N][1.13]Exp.txt', '[6.79][N][1.14]Exp.txt', '[6.79][N][1.15]Exp.txt', '[6.79][N][1.16]Exp.txt']
# files = ['[6.79][H][1.7]Exp.txt', '[6.79][H][1.8]Exp.txt', '[6.79][H][1.9]Exp.txt', '[6.79][H][1.10]Exp.txt', '[6.79][H][1.11]Exp.txt', '[6.79][H][1.12]Exp.txt', '[6.79][H][1.13]Exp.txt', '[6.79][H][1.14]Exp.txt', '[6.79][H][1.15]Exp.txt', '[6.79][H][1.16]Exp.txt']
# files = ['[6.79][VH][1.7]Exp.txt', '[6.79][VH][1.8]Exp.txt', '[6.79][VH][1.9]Exp.txt', '[6.79][VH][1.10]Exp.txt', '[6.79][VH][1.11]Exp.txt', '[6.79][VH][1.12]Exp.txt', '[6.79][VH][1.13]Exp.txt', '[6.79][VH][1.14]Exp.txt', '[6.79][VH][1.15]Exp.txt', '[6.79][VH][1.16]Exp.txt']

# files = ["[6.80][N][1.30]Exp.txt", "[6.80][N][1.31]Exp.txt", "[6.80][N][2.1]Exp.txt", "[6.80][N][2.2]Exp.txt", "[6.80][N][2.3]Exp.txt", "[6.80][N][2.4]Exp.txt",  "[6.80][N][2.5]Exp.txt"]
# files = ["[6.80][H][1.30]Exp.txt", "[6.80][H][1.31]Exp.txt", "[6.80][H][2.1]Exp.txt", "[6.80][H][2.2]Exp.txt", "[6.80][H][2.3]Exp.txt", "[6.80][H][2.4]Exp.txt",  "[6.80][H][2.5]Exp.txt"]
# files = ["[6.80][VH][1.30]Exp.txt", "[6.80][VH][1.31]Exp.txt", "[6.80][VH][2.1]Exp.txt", "[6.80][VH][2.2]Exp.txt", "[6.80][VH][2.3]Exp.txt", "[6.80][VH][2.4]Exp.txt",  "[6.80][VH][2.5]Exp.txt"]

# files = ["[6.81][VH][6.19]Exp1.txt", "[6.81][VH][6.19]Exp2.txt", "[6.81][VH][6.19]Exp3.txt"]
# files = ["[6.81][VH][6.19][1v1]Exp.txt"]
# files = ["[6.81][VH][6.19][RAD]Exp.txt"]

# files = ["[6.82][VH][9.25]Exp.txt"]
# files = ["[6.82][VH][9.27]Exp.txt"]
files = ["[6.82][VH][9.28]Exp.txt"]

# fileName = '[6.79][VH][1.8]Exp.txt'					#EDIT MANUALLY
# fileObject = open(fileName,'r')

# matchDetails = cPickle.load(fileObject)				#List of games in testing

class heroData:
	heroName = str()
	heroUse = int()
	heroWin = int()
	
finalData = []											#List of heroes, total uses, and total wins for display and file export
	
for hero in heroList:
	heroInfo = heroData()								#Creates an object for every hero in the game
	heroInfo.heroName = hero							#Names the hero
	heroInfo.heroUse = 0
	heroInfo.heroWin = 0
	finalData.append(heroInfo)
														#preps for Excel export
def padString(string, length):							#places spaces after the entry
	return(string + (" " * (length - len(string))))

def padString2(string, length):							#places spaces before the entry
	return((" " * (length - len(string))) + string)								

# useCount = 0
# winCount = 0

# wins = 0												#These values are for completion checking.  They do not get reset on a hero by hero basis
# plays = 0

for file in files:
	print file
	fileName = file										#EDIT MANUALLY
	fileObject = open(fileName,'r')
	matchDetails = cPickle.load(fileObject)	
	
	for match in matchDetails:
		if len(match.players) == 10:					#Cuts out all the < 9 player games in the normal samples
		# if match.mode == 21:
			for player in match.players:
				holder = player.heroName
				for entry in finalData:
					if entry.heroName == holder:
						entry.heroUse = entry.heroUse+1
						if player.win == True:
							entry.heroWin = entry.heroWin + 1
				# if hero == holder:						#Checks each player to see if they're playing the hero that is being tested this loop
					# useCount = useCount + 1
					# plays = plays + 1
					# if player.win == True:
						# winCount = winCount + 1
						# wins = wins + 1
	# heroInfo.heroWin = winCount							#after looping all the matches, we put the final counts in the hero data
	# heroInfo.heroUse = useCount
	# if useCount > 0:
		# finalData.append(heroInfo)						#Places the finished hero in the final list
	# winCount = 0										#resets the counts for the next hero
	# useCount = 0
	# del matchDetails[:]
	fileObject.close()

				
a = open('[6.82][VH]HeroDist3.txt', "w") 						#EDIT MANUALLY

for entry in finalData:
	heroString = entry.heroName + ','
	winString = `entry.heroWin` + ','
	useString = `entry.heroUse` + ','
	a.write(heroString + winString + useString + '\n')			#creates the excel export file
	print (entry.heroName, entry.heroWin, entry.heroUse)		#prints to screen to manually check for obvious errors

# for entry in finalData:
	# heroString = padString(str(entry.heroName), 19) + ','
	# winString = padString2(str(entry.heroWin), 4) + ','
	# useString = padString2(str(entry.heroUse), 7) + ','
	# a.write(heroString + winString + useString + '\n')			#creates the excel export file
	# print (entry.heroName, entry.heroWin, entry.heroUse)		#prints to screen to manually check for obvious errors

# print wins														
# print plays														#Completion of a sample of x matches should return 5x wins and 10x plays (unless sample is normal)