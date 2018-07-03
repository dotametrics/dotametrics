#!/usr/bin/python

import sys											
import cPickle										#file input and output
import collections									#used for Counter
import gc

def bracketSwitcher(i):							#Used to change the input file so all three brackets are tested sequentially
	baseStr = '[' + '6.78' + ']'
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
		
# files = ['[6.79][N][1.7]Exp.txt', '[6.79][N][1.8]Exp.txt', '[6.79][N][1.9]Exp.txt', '[6.79][N][1.10]Exp.txt', '[6.79][N][1.11]Exp.txt', '[6.79][N][1.12]Exp.txt', '[6.79][N][1.13]Exp.txt', '[6.79][N][1.14]Exp.txt', '[6.79][N][1.15]Exp.txt', '[6.79][N][1.16]Exp.txt']
# files = ['[6.79][H][1.7]Exp.txt', '[6.79][H][1.8]Exp.txt', '[6.79][H][1.9]Exp.txt', '[6.79][H][1.10]Exp.txt', '[6.79][H][1.11]Exp.txt', '[6.79][H][1.12]Exp.txt', '[6.79][H][1.13]Exp.txt', '[6.79][H][1.14]Exp.txt', '[6.79][H][1.15]Exp.txt', '[6.79][H][1.16]Exp.txt']
# files = ['[6.79][VH][1.7]Exp.txt', '[6.79][VH][1.8]Exp.txt', '[6.79][VH][1.9]Exp.txt', '[6.79][VH][1.10]Exp.txt', '[6.79][VH][1.11]Exp.txt', '[6.79][VH][1.12]Exp.txt', '[6.79][VH][1.13]Exp.txt', '[6.79][VH][1.14]Exp.txt', '[6.79][VH][1.15]Exp.txt', '[6.79][VH][1.16]Exp.txt']

# files = ["[6.80][N][1.30]Exp.txt", "[6.80][N][1.31]Exp.txt", "[6.80][N][2.1]Exp.txt", "[6.80][N][2.2]Exp.txt", "[6.80][N][2.3]Exp.txt", "[6.80][N][2.4]Exp.txt",  "[6.80][N][2.5]Exp.txt"]
# files = ["[6.80][H][1.30]Exp.txt", "[6.80][H][1.31]Exp.txt", "[6.80][H][2.1]Exp.txt", "[6.80][H][2.2]Exp.txt", "[6.80][H][2.3]Exp.txt", "[6.80][H][2.4]Exp.txt",  "[6.80][H][2.5]Exp.txt"]
files = ["[6.80][VH][1.30]Exp.txt", "[6.80][VH][1.31]Exp.txt", "[6.80][VH][2.1]Exp.txt", "[6.80][VH][2.2]Exp.txt", "[6.80][VH][2.3]Exp.txt", "[6.80][VH][2.4]Exp.txt",  "[6.80][VH][2.5]Exp.txt"]

# rank = 'N'
# rank = 'H'
rank = 'V'
		
com = ','		
a = open("[6.80]playerDataV.csv", "w")
a.write('MatchID')
a.write(com)
a.write('Duration')
a.write(com)
a.write('Bracket')
a.write(com)
a.write('Hero')
a.write(com)
a.write('Radiant')
a.write(com)
a.write('Winner')
a.write(com)
a.write('Kills')
a.write(com)
a.write('Deaths')
a.write(com)
a.write('Assists')
a.write(com)
a.write('GPM')
a.write(com)
a.write('XPM')
a.write(com)
a.write('cs')
a.write(com)
a.write('denies')
a.write(com)
a.write('Level')
a.write(com)
a.write('Hero Damage')
a.write(com)
a.write('Item1')
a.write(com)
a.write('Item2')
a.write(com)
a.write('Item3')
a.write(com)
a.write('Item4')
a.write(com)
a.write('Item5')
a.write(com)
a.write('Item6')
a.write('\n')
		
# for i in range(1,2):
	# fileName = bracketSwitcher(i)
	# fileObject = open(fileName,'r')
	# print fileName
	# matchDetails = cPickle.load(fileObject)
	# fileObject.close()
	
	# if i == 1:
		# rank = 'N'
	# elif i == 2:
		# rank = 'H'
	# elif i == 3:
		# rank = 'V'

for file in files:
	fileName = file
	fileObject = open(fileName,'r')
	print fileName
	matchDetails = cPickle.load(fileObject)
	fileObject.close()
	
	for match in matchDetails:
		if match.mode != 18:
			if len(match.players) == 10:
				for player in match.players:
					a.write(`match.matchID`)
					a.write(com)
					a.write(`match.duration`)
					a.write(com)
					a.write(rank)
					a.write(com)
					a.write(player.heroName)
					a.write(com)
					a.write(`player.team`)
					a.write(com)
					a.write(`player.win`)
					a.write(com)
					a.write(`player.kills`)
					a.write(com)
					a.write(`player.deaths`)
					a.write(com)
					a.write(`player.assists`)
					a.write(com)
					a.write(`player.gpm`)
					a.write(com)
					a.write(`player.xpm`)
					a.write(com)
					a.write(`player.cs`)
					a.write(com)
					a.write(`player.denies`)
					a.write(com)
					a.write(`player.level`)
					a.write(com)
					a.write(`player.heroDmg`)
					a.write(com)
					a.write(`player.items[0]`)
					a.write(com)
					a.write(`player.items[1]`)
					a.write(com)
					a.write(`player.items[2]`)
					a.write(com)
					a.write(`player.items[3]`)
					a.write(com)
					a.write(`player.items[4]`)
					a.write(com)
					a.write(`player.items[5]`)
					a.write('\n')
