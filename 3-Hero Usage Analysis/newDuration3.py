#!/usr/bin/python

import d2slib										#winxp's script
import sys											#don't know
import cPickle										#file input and output

class matchDetails:
	winner = bool()
	players = []
	duration = int()
	matchID = int()
	
class matchPlayer:
	team = bool()
	heroName = int()
	win = bool()		
	
heroList = "modheroList2.txt"
heroListObject = open(heroList, 'rb')
heroList = cPickle.load(heroListObject)
heroListObject.close()

baseFile = "[6.80][N]"
inputFile = baseFile + "DurClass.txt"
outputFile = baseFile + "DurExcel2.txt"

fileObject = open(inputFile,'r')
matches = cPickle.load(fileObject)
fileObject.close()

a = open(outputFile, "w")

all = []

overallAvg = 0
overallCount = 0

for match in matches:
	all.append(match.duration)

all.sort()
divider = len(all)/3

lowLimit = all[divider]
highLimit = all[divider*2]

lowLimit = 1800
highLimit = 2400

holder1 = lowLimit/float(60)
holder2 = highLimit/float(60)

a.write('%.2f' % holder1)
a.write(',')
a.write('%.2f' % holder2)
a.write('\n\n')

print lowLimit
print highLimit

for hero in heroList:
	game = 0
	win = 0
	lowGame = 0
	lowWin = 0
	midGame = 0
	midWin = 0
	highGame = 0
	highWin = 0
	
	for match in matches:
		for player in match.players:
			if player.heroName == hero:
				game = game + 1
				if player.win == True:
					win = win + 1
				if match.duration < lowLimit:
					lowGame = lowGame + 1
					if player.win == True:
						lowWin = lowWin + 1
				elif match.duration < highLimit:
					midGame = midGame + 1
					if player.win == True:
						midWin = midWin + 1
				else:
					highGame = highGame + 1
					if player.win == True:
						highWin = highWin + 1
						
	winRate = float(win)/game
	lowWinRate = float(lowWin)/lowGame
	midWinRate = float(midWin)/midGame
	highWinRate = float(highWin)/highGame
	
	# if hero == 'Doom Bringer':
		# print lowGame
		# print lowWin
		# print lowWinRate
		# print midGame
		# print midWin
		# print midWinRate
		# print highGame
		# print highWin
		# print highWinRate
		# print lowGame+midGame+highGame
		# break
		
	
	a.write(hero)
	a.write(',')
	a.write(`game`)
	a.write(',')
	a.write('%.4f' % winRate)
	a.write(',,')
	a.write('%.4f' % lowWinRate)
	a.write(',')
	a.write('%.4f' % midWinRate)
	a.write(',')
	a.write('%.4f' % highWinRate)
	a.write('\n')
	
a.close()
	
	
# overallAvg = float(overallAvg) / (overallCount*60)
	
# a.write("Overall,")
# a.write('%.2f' % overallAvg)
# a.write('\n')

# for hero in heroList:
	# avg = 0
	# total = 0
	# avgWin = 0
	# win = 0
	# avgLoss = 0
	# loss = 0
	# for match in matches:
		# for player in match.players:
			# if player.heroName == hero:
				# avg = avg + match.duration
				# total = total + 1
				# if player.win == True:
					# avgWin = avgWin + match.duration
					# win = win + 1
				# else:
					# avgLoss = avgLoss + match.duration
					# loss = loss + 1
	
	# avg = float(avg) / (total*60)
	# avgWin = float(avgWin) / (win*60)
	# avgLoss = float(avgLoss) / (loss*60)
	
	# a.write(hero)
	# a.write(',')
	# a.write('%.2f' % avg)
	# a.write(',')
	# a.write('%.2f' % avgWin)
	# a.write(',')
	# a.write('%.2f' % avgLoss)
	# a.write(',,')
	# a.write(`win`)
	# a.write(',')
	# a.write(`total`)
	# a.write('\n')

# a.close()

