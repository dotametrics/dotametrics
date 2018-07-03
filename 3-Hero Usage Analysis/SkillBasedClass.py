#!/usr/bin/python

import sys											#don't know
import cPickle										#file input and output
import collections									#used for Counter

# def bracketSwitcher(i, hero):							#Used to change the input file so all three brackets are tested sequentially
	# baseStr = '[' + hero + '678]'
	# baseStr = '[6.79][Earth Spirit]'
	# if i == 1:											#i stands for iteration.  Iteration 1 = Normal, Iteration 2 = High, Iteration 3 = Very High
		# returnStr = baseStr + "NormalExp.txt"
		# return returnStr 
	# elif i == 2:
		# returnStr = baseStr + "HighExp.txt"
		# return returnStr 
	# elif i == 3:
		# returnStr = baseStr + "VeryHighExp.txt"
		# return returnStr 
	# else:
		# print "Error in bracketSwitcher"
		# sys.exit()
		

# hero = 'Alchemist'
# abilityNumbers = [5365, 5366, 5368, 5369]
		
# hero = 'Ancient Apparition'
# abilityNumbers = [5345, 5346, 5347, 5348]

# hero = 'Axe'
# abilityNumbers = [5007, 5008, 5009, 5010]

# hero = 'Bloodseeker'
# abilityNumbers = [5015, 5016, 5017, 5018]

# hero = 'Bristleback'
# abilityNumbers = [5548, 5549, 5550, 5551]

# hero = 'Crystal Maiden'
# abilityNumbers = [5126, 5127, 5128, 5129]

# hero = 'Dazzle'
# abilityNumbers = [5233, 5234, 5235, 5236]

# hero = 'Drow Ranger'
# abilityNumbers = [5019, 5020, 5021, 5022]

# hero = 'Earth Spirit'
# abilityNumbers = [5608, 5609, 5610, 5612]

# hero = 'Ember Spirit'
# abilityNumbers = [5603, 5604, 5605, 5606]

# hero = 'Huskar'
# abilityNumbers = [5271, 5272, 5273, 5274]

# hero = 'Jakiro'
# abilityNumbers = [5297, 5298, 5299, 5300]

# hero = 'Legion Commander'
# abilityNumbers = [5595, 5596, 5597, 5598]

# hero = 'Lifestealer'
# abilityNumbers = [5249, 5250, 5251, 5252]

# hero = 'Medusa'
# abilityNumbers = [5504, 5505, 5506, 5507]

# hero = 'Necrolyte'
# abilityNumbers = [5158, 5159, 5160, 5161]

# hero = 'Phoenix'
# abilityNumbers = [5623, 5625, 5626, 5630]

# hero = 'Riki'
# abilityNumbers = [5142, 5143, 5144, 5145]

# hero = 'Silencer'
# abilityNumbers = [5377, 5378, 5379, 5380]

# hero = 'Slark'
# abilityNumbers = [5494, 5495, 5496, 5497]

# hero = 'Sniper'
# abilityNumbers = [5154, 5155, 5156, 5157]

# hero = 'Spectre'
# abilityNumbers = [5334, 5335, 5336, 5337]

# hero = 'Terrorblade'
# abilityNumbers = [5619, 5620, 5621, 5622]

# hero = 'Tinker'
# abilityNumbers = [5150, 5151, 5152, 5153]

# hero = 'Treant Protector'
# abilityNumbers = [5434, 5435, 5436, 5437]

# hero = 'Ursa'
# abilityNumbers = [5357, 5358, 5359, 5360]

# hero = 'Venomancer'
# abilityNumbers = [5178, 5179, 5180, 5181]

hero = 'Viper'
abilityNumbers = [5218, 5219, 5220, 5221]

# hero = 'Windrunner'
# abilityNumbers = [5130, 5131, 5132, 5133]


qNumber=abilityNumbers[0]
wNumber=abilityNumbers[1]
eNumber=abilityNumbers[2]
rNumber=abilityNumbers[3]

# files = ['[6.78][VH][10.8to12]Exp.txt']
# files = ['[6.79][VH][1.7]Exp.txt', '[6.79][VH][1.8]Exp.txt', '[6.79][VH][1.9]Exp.txt', '[6.79][VH][1.10]Exp.txt', '[6.79][VH][1.11]Exp.txt', '[6.79][VH][1.12]Exp.txt', '[6.79][VH][1.13]Exp.txt', '[6.79][VH][1.14]Exp.txt', '[6.79][VH][1.15]Exp.txt', '[6.79][VH][1.16]Exp.txt']
# files = ["[6.80][VH][1.30]Exp.txt", "[6.80][VH][1.31]Exp.txt", "[6.80][VH][2.1]Exp.txt", "[6.80][VH][2.2]Exp.txt", "[6.80][VH][2.3]Exp.txt", "[6.80][VH][2.4]Exp.txt",  "[6.80][VH][2.5]Exp.txt"]
files = ["[6.81][VH][6.19][1]Exp.txt", "[6.81][VH][6.19][2]Exp.txt", "[6.81][VH][6.19][3]Exp.txt"]

class abilityData:
	level = int()
	win = bool()
	skills = []
	primary = str()
	secondary = str()
	build = str()
	matchID = int()
	csPm = float()
	kaP10m = float()
	dP10m = float()
	killPart = float()
	items = []
	
# allData = []
heroData = []

fileName = '[MultiPatch][' + hero + ']AbilityData' + '.txt'			#names an output .csv file for export to Excel
fileObject = open(fileName,'r')
allData = cPickle.load(fileObject)
fileObject.close()
	
for file in files:
	fileName = file
	fileObject = open(fileName,'r')
	matchDetails = cPickle.load(fileObject)
	fileObject.close()
	print file

	for match in matchDetails:
		if len(match.players) == 10 and match.mode != 18 and match.duration > 0:
			for player in match.players:
				if player.heroName == hero:
					playerData = abilityData()
					playerData.level = player.level
					playerData.matchID = match.matchID
					playerData.win = player.win
					playerData.skills = list(player.skills)
					playerData.items = list(player.items)
					
					playerData.csPm = player.cs*60/float(match.duration)					
					playerData.kaP10m = (player.kills+player.assists)*600/float(match.duration)
					playerData.dP10m = (player.deaths)*600/float(match.duration)
					
					holder = player.skills[0:8]
					
					if holder.count(qNumber) == 4:
						playerData.primary = 'q'
						holder = player.skills[0:10]
						if holder.count(wNumber) == 4:
							playerData.secondary = 'w'
						elif holder.count(eNumber) == 4:
							playerData.secondary = 'e'
						else:
							playerData.secondary = '-'
							
					elif holder.count(wNumber) == 4:
						playerData.primary = 'w'
						holder = player.skills[0:10]
						if holder.count(qNumber) == 4:
							playerData.secondary = 'q'
						elif holder.count(eNumber) == 4:
							playerData.secondary = 'e'
						else:
							playerData.secondary = '-'
							
					elif holder.count(eNumber) == 4:
						playerData.primary = 'e'
						holder = player.skills[0:10]
						if holder.count(qNumber) == 4:
							playerData.secondary = 'q'
						elif holder.count(wNumber) == 4:
							playerData.secondary = 'w'
						else:
							playerData.secondary = '-'
					else:
						playerData.primary = '-'
						playerData.secondary = '-'
						
					build = playerData.primary + playerData.secondary
					playerData.build = build

					# sumTeamLevel = 0
					
					# teamList = [0,1,2,3,4]
					# teamList.remove(player.slot)
					# if player.team == False:
						# for x in range(0,4):
							# teamList[x] = teamList[x]+5
					# for x in teamList:
						# sumTeamLevel = sumTeamLevel + match.players[x].level
					# playerData.sumTeamLevel = sumTeamLevel

					heroData.append(playerData)
	del matchDetails[:]
allData.append(heroData)

print len(allData)
print len(allData[-1])

					
fileName = '[MultiPatch][' + hero + ']AbilityData' + '.txt'			#names an output .csv file for export to Excel
fileObject = open(fileName,'w')
cPickle.dump(allData,fileObject)
fileObject.close()



# qPrim = 0
# qPrimWin = 0
# qw = 0
# qwWin = 0
# qe = 0
# qeWin = 0
# qSplit = 0
# qSplitWin = 0

# wPrim = 0
# wPrimWin = 0
# wq = 0
# wqWin = 0
# we = 0
# weWin = 0
# wSplit = 0
# wSplitWin = 0

# ePrim = 0
# ePrimWin = 0
# eq = 0
# eqWin = 0
# ew = 0
# ewWin = 0
# eSplit = 0
# eSplitWin = 0

# split = 0
# splitWin = 0

# use = len(bracketData)

# for entry in bracketData:
	# if entry.build == 'qw':
		# qw = qw + 1
		# if entry.win == True:
			# qwWin = qwWin + 1
	# elif entry.build == 'qe':
		# qe = qe + 1
		# if entry.win == True:
			# qeWin = qeWin + 1
	# elif entry.build == 'q-':
		# qSplit = qSplit + 1
		# if entry.win == True:
			# qSplitWin = qSplitWin + 1
			
	# elif entry.build == 'wq':
		# wq = wq + 1
		# if entry.win == True:
			# wqWin = wqWin + 1
	# elif entry.build == 'we':
		# we = we + 1
		# if entry.win == True:
			# weWin = weWin + 1
	# elif entry.build == 'w-':
		# wSplit = wSplit + 1
		# if entry.win == True:
			# wSplitWin = wSplitWin + 1
	
	# elif entry.build == 'eq':
		# eq = eq + 1
		# if entry.win == True:
			# eqWin = eqWin + 1
	# elif entry.build == 'ew':
		# ew = ew + 1
		# if entry.win == True:
			# ewWin = ewWin + 1
	# elif entry.build == 'e-':
		# eSplit = eSplit + 1
		# if entry.win == True:
			# eSplitWin = eSplitWin + 1
			
	# else:
		# split = split + 1
		# if entry.win == True:
			# splitWin = splitWin + 1
			
# qPrim = qw + qe + qSplit
# qPrimWin = qwWin + qeWin + qSplitWin
# wPrim = wq + we + wSplit
# wPrimWin = wqWin + weWin + wSplitWin
# ePrim = eq + ew + eSplit
# ePrimWin = eqWin + ewWin + eSplitWin

# qRate = (float(qPrim)/use)*100
# qRate = str('%.2f' % qRate) + '%,'		
# qWinRate = (float(qPrimWin)/qPrim)*100
# qWinRate = str('%.2f' % qWinRate) + '%,'

# if qw == 0:
	# qwRate = '0%,'
	# qwWinRate = '0%,'
# else:
	# qwRate = (float(qw)/qPrim)*100
	# qwRate = str('%.2f' % qwRate) + '%,'		
	# qwWinRate = (float(qwWin)/qw)*100
	# qwWinRate = str('%.2f' % qwWinRate) + '%,'

# qeRate = (float(qe)/qPrim)*100
# qeRate = str('%.2f' % qeRate) + '%,'		
# qeWinRate = (float(qeWin)/qe)*100
# qeWinRate = str('%.2f' % qeWinRate) + '%,'

# if qSplit == 0:
	# qSplitRate = '0%,'
	# qSplitWinRate = '0%,'
# else:
	# qSplitRate = (float(qSplit)/qPrim)*100
	# qSplitRate = str('%.2f' % qSplitRate) + '%,'		
	# qSplitWinRate = (float(qSplitWin)/qSplit)*100
	# qSplitWinRate = str('%.2f' % qSplitWinRate) + '%,'

# wRate = (float(wPrim)/use)*100
# wRate = str('%.2f' % wRate) + '%,'		
# wWinRate = (float(wPrimWin)/wPrim)*100
# wWinRate = str('%.2f' % wWinRate) + '%,'

# wqRate = (float(wq)/wPrim)*100
# wqRate = str('%.2f' % wqRate) + '%,'		
# wqWinRate = (float(wqWin)/wq)*100
# wqWinRate = str('%.2f' % wqWinRate) + '%,'

# weRate = (float(we)/wPrim)*100
# weRate = str('%.2f' % weRate) + '%,'		
# weWinRate = (float(weWin)/we)*100
# weWinRate = str('%.2f' % weWinRate) + '%,'

# wSplitRate = (float(wSplit)/wPrim)*100
# wSplitRate = str('%.2f' % wSplitRate) + '%,'		
# wSplitWinRate = (float(wSplitWin)/wSplit)*100
# wSplitWinRate = str('%.2f' % wSplitWinRate) + '%,'

# eRate = (float(ePrim)/use)*100
# eRate = str('%.2f' % eRate) + '%,'		
# eWinRate = (float(ePrimWin)/ePrim)*100
# eWinRate = str('%.2f' % eWinRate) + '%,'

# eqRate = (float(eq)/ePrim)*100
# eqRate = str('%.2f' % eqRate) + '%,'		
# eqWinRate = (float(eqWin)/eq)*100
# eqWinRate = str('%.2f' % eqWinRate) + '%,'

# if ew == 0:
	# ewRate = '0%,'
	# ewWinRate = '0%,'
# else:
	# ewRate = (float(ew)/ePrim)*100
	# ewRate = str('%.2f' % ewRate) + '%,'		
	# ewWinRate = (float(ewWin)/ew)*100
	# ewWinRate = str('%.2f' % ewWinRate) + '%,'

# eSplitRate = (float(eSplit)/ePrim)*100
# eSplitRate = str('%.2f' % eSplitRate) + '%,'		
# eSplitWinRate = (float(eSplitWin)/eSplit)*100
# eSplitWinRate = str('%.2f' % eSplitWinRate) + '%,'

# splitRate = (float(split)/use)*100
# splitRate = str('%.2f' % splitRate) + '%,'		
# splitWinRate = (float(splitWin)/split)*100
# splitWinRate = str('%.2f' % splitWinRate) + '%,'

# useRates1 = [qRate, qwRate, qeRate, qSplitRate]
# useRates2 = [wRate, wqRate, weRate, wSplitRate]
# useRates3 = [eRate, eqRate, ewRate, eSplitRate]
# useRates4 = [splitRate]
# winRates1 = [qWinRate, qwWinRate, qeWinRate, qSplitWinRate]
# winRates2 = [wWinRate, wqWinRate, weWinRate, wSplitWinRate]
# winRates3 = [eWinRate, eqWinRate, ewWinRate, eSplitWinRate]
# winRates4 = [splitWinRate]

# print useRates1
# print useRates2
# print useRates3
# print useRates4
# print winRates1
# print winRates2
# print winRates3
# print winRates4