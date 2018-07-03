#!/usr/bin/python								

import d2slib										#winxp's script
import sys											#don't know
import cPickle										#file input and output

# files = ['[6.74][N]Exp.txt']
# files = ['[6.74][H]Exp.txt']
# files = ['[6.74][VH]Exp.txt']

# files = ['[6.77][N]Exp.txt']
# files = ['[6.77][H]Exp.txt']
# files = ['[6.77][VH]Exp.txt']

# files = ['[6.78][N]Exp.txt']
# files = ['[6.78][VH][10.8to12]Exp.txt']

# files = ['[6.79][N][1.7]Exp.txt', '[6.79][N][1.8]Exp.txt', '[6.79][N][1.9]Exp.txt', '[6.79][N][1.10]Exp.txt', '[6.79][N][1.11]Exp.txt', '[6.79][N][1.12]Exp.txt', '[6.79][N][1.13]Exp.txt', '[6.79][N][1.14]Exp.txt', '[6.79][N][1.15]Exp.txt', '[6.79][N][1.16]Exp.txt']
# files = ['[6.79][H][1.7]Exp.txt', '[6.79][H][1.8]Exp.txt', '[6.79][H][1.9]Exp.txt', '[6.79][H][1.10]Exp.txt', '[6.79][H][1.11]Exp.txt', '[6.79][H][1.12]Exp.txt', '[6.79][H][1.13]Exp.txt', '[6.79][H][1.14]Exp.txt', '[6.79][H][1.15]Exp.txt', '[6.79][H][1.16]Exp.txt']
# files = ['[6.79][VH][1.7]Exp.txt', '[6.79][VH][1.8]Exp.txt', '[6.79][VH][1.9]Exp.txt', '[6.79][VH][1.10]Exp.txt', '[6.79][VH][1.11]Exp.txt', '[6.79][VH][1.12]Exp.txt', '[6.79][VH][1.13]Exp.txt', '[6.79][VH][1.14]Exp.txt', '[6.79][VH][1.15]Exp.txt', '[6.79][VH][1.16]Exp.txt']

# files = ["[6.80][N][1.30]Exp.txt", "[6.80][N][1.31]Exp.txt", "[6.80][N][2.1]Exp.txt", "[6.80][N][2.2]Exp.txt", "[6.80][N][2.3]Exp.txt", "[6.80][N][2.4]Exp.txt",  "[6.80][N][2.5]Exp.txt"]
# files = ["[6.80][H][1.30]Exp.txt", "[6.80][H][1.31]Exp.txt", "[6.80][H][2.1]Exp.txt", "[6.80][H][2.2]Exp.txt", "[6.80][H][2.3]Exp.txt", "[6.80][H][2.4]Exp.txt",  "[6.80][H][2.5]Exp.txt"]
# files = ["[6.80][VH][1.30]Exp.txt", "[6.80][VH][1.31]Exp.txt", "[6.80][VH][2.1]Exp.txt", "[6.80][VH][2.2]Exp.txt", "[6.80][VH][2.3]Exp.txt", "[6.80][VH][2.4]Exp.txt",  "[6.80][VH][2.5]Exp.txt"]

# files = ["[6.81][VH][6.19][1]Exp.txt", "[6.81][VH][6.19][2]Exp.txt", "[6.81][VH][6.19][3]Exp.txt"]

# files = ["[6.82][VH][9.25]Exp.txt"]
# files = ["[6.82][VH][9.27]Exp.txt"]
# files = ["[6.82][VH][9.28]Exp.txt"]
files = ["[6.82][VH][9.29]Exp.txt"]

files = ["[6.81][VH][6.19][1]Exp.txt", "[6.82][VH][9.25]Exp.txt", "[6.82][VH][9.27]Exp.txt", "[6.82][VH][9.28]Exp.txt", "[6.82][VH][9.29]Exp.txt"]

# class matchData:
	# matchWin = bool()
	# matchDur = int()
	
# finalData = []

# totalDur = 0
# count = 0

a = open('[avgMatchStats][6.82].txt', "w") 						#EDIT MANUALLY								

for file in files:
	print file
	fileName = file										
	fileObject = open(fileName,'r')
	matchDetails = cPickle.load(fileObject)	
	fileObject.close()
	
	count = 0
	
	KpM = 0
	ApM = 0
	CSpM = 0
	GPM = 0
	XPM = 0
	
	KpMWin = 0
	ApMWin = 0
	CSpMWin = 0
	GPMWin = 0
	XPMWin = 0

	KpMLoss = 0
	ApMLoss = 0
	CSpMLoss = 0
	GPMLoss = 0
	XPMLoss = 0	
	
	for match in matchDetails:
		if len(match.players) == 10:					#Cuts out all the < 9 player games in the normal samples
			if match.mode != 21:
				if match.mode != 18: 
					if match.mode != 20:
						if match.duration > 1800:
							if match.duration < 2400:
								for player in match.players:
									count = count + 1
									if player.kills == 0:
										pass
									else:
										KpM = KpM + float(player.kills)/(match.duration/600)
									if player.assists == 0:
										pass
									else:
										ApM = ApM + float(player.assists)/(match.duration/600)
									if player.cs == 0:
										pass
									else:
										CSpM = CSpM + float(player.cs)/(match.duration/60)
									GPM = GPM + player.gpm
									XPM = XPM + player.xpm
									
									if player.win == True:
										if player.kills == 0:
											pass
										else:
											KpMWin = KpMWin + float(player.kills)/(match.duration/600)
										if player.assists == 0:
											pass
										else:
											ApMWin = ApMWin + float(player.assists)/(match.duration/600)
										if player.cs == 0:
											pass
										else:
											CSpMWin = CSpMWin + float(player.cs)/(match.duration/60)
										GPMWin = GPMWin + player.gpm
										XPMWin = XPMWin + player.xpm					
									elif player.win == False:
										if player.kills == 0:
											pass
										else:
											KpMLoss = KpMLoss + float(player.kills)/(match.duration/600)
										if player.assists == 0:
											pass
										else:
											ApMLoss = ApMLoss + float(player.assists)/(match.duration/600)
										if player.cs == 0:
											pass
										else:
											CSpMLoss = CSpMLoss + float(player.cs)/(match.duration/60)
										GPMLoss = GPMLoss + player.gpm
										XPMLoss = XPMLoss + player.xpm
	KpM = KpM/count
	ApM = ApM/count
	CSpM = CSpM/count
	GPM = GPM/count
	XPM = XPM/count
	
	KpMWin = KpMWin/(count/2)
	ApMWin = ApMWin/(count/2)
	CSpMWin = CSpMWin/(count/2)
	GPMWin = GPMWin/(count/2)
	XPMWin = XPMWin/(count/2)
	
	KpMLoss = KpMLoss/(count/2)
	ApMLoss = ApMLoss/(count/2)
	CSpMLoss = CSpMLoss/(count/2)
	GPMLoss = GPMLoss/(count/2)
	XPMLoss = XPMLoss/(count/2)
	
	a.write(`KpM` + ',' + `ApM` + ',' + `CSpM` + ',' + `GPM` + ',' + `XPM` + ',,' + `KpMWin` + ',' + `ApMWin` + ',' + `CSpMWin` + ',' + `GPMWin` + ',' + `XPMWin` + ',,' + `KpMLoss` + ',' + `ApMLoss` + ',' + `CSpMLoss` + ',' + `GPMLoss` + ',' + `XPMLoss` + '\n')
	
	del matchDetails[:]
	# fileObject.close()
	
# totalDur = float(totalDur)/(count*60)
	
# totalCount = 0
# totalWin = 0
# count0 = 0
# winCount0 = 0
# count20 = 0
# winCount20 = 0
# count30 = 0
# winCount30 = 0
# count40 = 0
# winCount40 = 0
# count50 = 0
# winCount50 = 0
# count60 = 0
# winCount60 = 0
	
# for entry in finalData:
	# totalCount = totalCount + 1
	# if entry.matchDur < 1200:
		# count0 = count0 + 1
		# if entry.matchWin == True:
			# totalWin = totalWin + 1
			# winCount0 = winCount0 + 1
	# elif entry.matchDur < 1800:
		# count20 = count20 + 1
		# if entry.matchWin == True:
			# totalWin = totalWin + 1
			# winCount20 = winCount20 + 1
	# elif entry.matchDur < 2400:
		# count30 = count30 + 1
		# if entry.matchWin == True:
			# totalWin = totalWin + 1
			# winCount30 = winCount30 + 1
	# elif entry.matchDur < 3000:
		# count40 = count40 + 1
		# if entry.matchWin == True:
			# totalWin = totalWin + 1
			# winCount40 = winCount40 + 1
	# elif entry.matchDur < 3600:
		# count50 = count50 + 1
		# if entry.matchWin == True:
			# totalWin = totalWin + 1
			# winCount50 = winCount50 + 1
	# else:
		# count60 = count60 + 1
		# if entry.matchWin == True:
			# totalWin = totalWin + 1
			# winCount60 = winCount60 + 1

# perc0 = float(winCount0)/count0 * 100
# perc0 = str('%.2f' % perc0) + '%,'
# perc20 = float(winCount20)/count20 * 100
# perc20 = str('%.2f' % perc20) + '%,'
# perc30 = float(winCount30)/count30 * 100
# perc30 = str('%.2f' % perc30) + '%,'
# perc40 = float(winCount40)/count40 * 100
# perc40 = str('%.2f' % perc40) + '%,'
# try:
	# perc50 = float(winCount50)/count50 * 100
	# perc50 = str('%.2f' % perc50) + '%,'
# except:
	# perc50 = str('0%,')
# try:
	# perc60 = float(winCount60)/count60 * 100
	# perc60 = str('%.2f' % perc60) + '%,'
# except:
	# perc60 = str('0%,')
# percTotal = float(totalWin)/totalCount * 100
# percTotal = str('%.2f' % percTotal) + '%,'
				
# a = open('[RadiantDuration][6.82]4.txt', "w") 						#EDIT MANUALLY

# a.write(perc0 + perc20 + perc30 + perc40 + perc50 + perc60 + percTotal + '\n')
# a.write(`count0` + ',' + `count20` + ',' + `count30` + ',' + `count40` + ',' + `count50` + ',' + `count60` + ',' + `totalCount` + ',,' + `totalDur`)

# a.close()

