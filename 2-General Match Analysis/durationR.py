#!/usr/bin/python

import d2slib										#winxp's script
import sys											#don't know
import cPickle										#file input and output
import math

fileName = "normexp.txt"
fileObject = open(fileName,'r')

matchDetailsNorm = cPickle.load(fileObject)

fileObject.close()

fileName = "highexp.txt"
fileObject = open(fileName,'r')

matchDetailsHigh = cPickle.load(fileObject)

fileObject.close()

fileName = "veryhighexp.txt"
fileObject = open(fileName,'r')

matchDetailsVeryHigh = cPickle.load(fileObject)

fileObject.close()

a = open("durListNorm.txt", "w")
b = open("durListHigh.txt", "w")
c = open("durListVeryHigh.txt", "w")

a.write('matchID,duration,gpm,xpm,deaths,assists\n')
b.write('matchID,duration,gpm,xpm,deaths,assists\n')
c.write('matchID,duration,gpm,xpm,deaths,assists\n')


# winnerGPM = []
# loserGPM = []
# winnerXPM = []
# loserXPM = []
# winnerCSpM = []
# loserCSpM = []
# winnerDeaths = []
# loserDeaths = []
# winnerAssists = []
# loserAssists = []

for match in matchDetailsNorm:
	if len(match.players) == 10:
		if match.duration > 600:
			duration = `match.duration / float(60)`
			matchID = `match.matchID`
			gpm = 0
			xpm = 0
			deaths = 0
			assists = 0
			for player in match.players:
				gpm = gpm + player.gpm
				xpm = xpm + player.xpm
				deaths = deaths + player.deaths
				assists = assists + player.assists
			gpm = `gpm / float(10)`
			xpm = `xpm / float(10)`
			deaths = `deaths / float(10)`
			assists = `assists / float(10)`
			a.write(matchID + ',' + duration + ',' + gpm + ',' + xpm + ',' + deaths + ',' + assists + '\n')
		
a.close()

for match in matchDetailsHigh:
	if len(match.players) == 10:
		if match.duration > 600:
			duration = `match.duration / float(60)`
			matchID = `match.matchID`
			gpm = 0
			xpm = 0
			deaths = 0
			assists = 0
			for player in match.players:
				gpm = gpm + player.gpm
				xpm = xpm + player.xpm
				deaths = deaths + player.deaths
				assists = assists + player.assists
			gpm = `gpm / float(10)`
			xpm = `xpm / float(10)`
			deaths = `deaths / float(10)`
			assists = `assists / float(10)`
			b.write(matchID + ',' + duration + ',' + gpm + ',' + xpm + ',' + deaths + ',' + assists + '\n')
		
b.close()

for match in matchDetailsVeryHigh:
	if len(match.players) == 10:
		if match.duration > 600:
			duration = `match.duration / float(60)`
			matchID = `match.matchID`
			gpm = 0
			xpm = 0
			deaths = 0
			assists = 0
			for player in match.players:
				gpm = gpm + player.gpm
				xpm = xpm + player.xpm
				deaths = deaths + player.deaths
				assists = assists + player.assists
			gpm = `gpm / float(10)`
			xpm = `xpm / float(10)`
			deaths = `deaths / float(10)`
			assists = `assists / float(10)`
			c.write(matchID + ',' + duration + ',' + gpm + ',' + xpm + ',' + deaths + ',' + assists + '\n')
		
c.close()						
			# winnerCSlist.sort(reverse=True)
			# loserCSlist.sort(reverse=True)
			
			# for player in match.players:
				# entry = matchPlayer()
				# entry.heroName = player.heroName
				# entry.win = player.win
				# entry.cs = player.cs/duration
				
				# if entry.win == True:
					# if entry.cs == winnerCSlist[0]:
						# entry.placing = 1
					# elif entry.cs == winnerCSlist[1]:
						# entry.placing = 2
					# elif entry.cs == winnerCSlist[2]:
						# entry.placing = 3
					# elif entry.cs == winnerCSlist[3]:
						# entry.placing = 4
					# elif entry.cs == winnerCSlist[4]:
						# entry.placing = 5
						
				# elif entry.win == False:
					# if entry.cs == loserCSlist[0]:
						# entry.placing = 1
					# elif entry.cs == loserCSlist[1]:
						# entry.placing = 2
					# elif entry.cs == loserCSlist[2]:
						# entry.placing = 3
					# elif entry.cs == loserCSlist[3]:
						# entry.placing = 4
					# elif entry.cs == loserCSlist[4]:
						# entry.placing = 5
				
				# players.append(entry)
				
# modheroList = "modheroList.txt"
# heroListObject = open(modheroList, 'r')

# heroList = cPickle.load(heroListObject)

# heroListObject.close()

# abs = open("CarryAbsVeryHigh.txt", "w")
# rel = open("CarryRelVeryHigh.txt", "w")

# absWin = open("CarryAbsWinVeryHigh.txt", "w")
# relWin = open("CarryRelWinVeryHigh.txt", "w")

# for hero in heroList:
	# heroString = hero + '\t\t'
	
	# count = 0
	# wins = 0
	
	# first = 0
	# first_win = 0
	# second = 0
	# second_win = 0
	# third = 0
	# third_win = 0
	# fourth = 0
	# fourth_win = 0
	# fifth = 0
	# fifth_win = 0
	
	# range_sub_one = 0
	# range_sub_one_win =0
	# range_one = 0
	# range_one_win =0
	# range_one_half = 0
	# range_one_half_win =0
	# range_two = 0
	# range_two_win =0
	# range_two_half = 0
	# range_two_half_win =0
	# range_three = 0
	# range_three_win =0
	# range_three_half = 0
	# range_three_half_win =0
	# range_four = 0
	# range_four_win =0
	# range_four_half = 0
	# range_four_half_win =0
	# range_five = 0
	# range_five_win =0
	# range_five_half = 0
	# range_five_half_win =0
	# range_six = 0
	# range_six_win =0
		
	# for player in players:
		# if hero == player.heroName:
			# count = count + 1
			# if player.win == True:
				# wins = wins + 1
			
			# if player.placing == 1:
				# first = first + 1
				# if player.win == True:
					# first_win = first_win + 1
			# elif player.placing == 2:
				# second = second + 1
				# if player.win == True:
					# second_win = second_win + 1
			# elif player.placing == 3:
				# third = third + 1
				# if player.win == True:
					# third_win = third_win + 1
			# elif player.placing == 4:
				# fourth = fourth + 1
				# if player.win == True:
					# fourth_win = fourth_win + 1
			# elif player.placing == 5:
				# fifth = fifth + 1
				# if player.win == True:
					# fifth_win = fifth_win + 1
					
			# if player.cs < 1:
				# range_sub_one = range_sub_one + 1
				# if player.win == True:
					# range_sub_one_win = range_sub_one_win + 1
			# elif player.cs < 1.5:
				# range_one = range_one + 1
				# if player.win == True:
					# range_one_win = range_one_win + 1
			# elif player.cs < 2:
				# range_one_half = range_one_half + 1
				# if player.win == True:
					# range_one_half_win = range_one_half_win + 1
			# elif player.cs < 2.5:
				# range_two = range_two + 1
				# if player.win == True:
					# range_two_win = range_two_win + 1
			# elif player.cs < 3:
				# range_two_half = range_two_half + 1
				# if player.win == True:
					# range_two_half_win = range_two_half_win + 1
			# elif player.cs < 3.5:
				# range_three = range_three + 1
				# if player.win == True:
					# range_three_win = range_three_win + 1
			# elif player.cs < 4:
				# range_three_half = range_three_half + 1
				# if player.win == True:
					# range_three_half_win = range_three_half_win + 1
			# elif player.cs < 4.5:
				# range_four = range_four + 1
				# if player.win == True:
					# range_four_win = range_four_win + 1
			# elif player.cs < 5:
				# range_four_half = range_four_half + 1
				# if player.win == True:
					# range_four_half_win = range_four_half_win + 1
			# elif player.cs < 5.5:
				# range_five = range_five + 1
				# if player.win == True:
					# range_five_win = range_five_win + 1
			# elif player.cs < 6:
				# range_five_half = range_five_half + 1
				# if player.win == True:
					# range_five_half_win = range_five_half_win + 1
			# else:
				# range_six = range_six + 1
				# if player.win == True:
					# range_six_win = range_six_win + 1

	# count = float(count)				
	
	# heroStringRelWin = heroString + str(wins/count) + '\t\t' + str(first_win/float(first)) + '\t' + str(second_win/float(second)) + '\t' + str(third_win/float(third)) + '\t' + str(fourth_win/float(fourth)) + '\t' + str(fifth_win/float(fifth)) + '\n'
	
	# relWin.write(heroStringRelWin)
	
	# heroStringRel = heroString + str(count) + '\t\t' + str(first/count) + '\t' + str(second/count) + '\t' + str(third/count) + '\t' + str(fourth/count) + '\t' + str(fifth/count) + '\n'
	
	# rel.write(heroStringRel)
	
	# if range_sub_one == 0:
		# sub_one = 0
	# else:
		# sub_one = range_sub_one_win/float(range_sub_one)
		
	# if range_one == 0:
		# one = 0
	# else:
		# one = range_one_win/float(range_one)
		
	# if range_one_half == 0:
		# one_half = 0
	# else:
		# one_half = range_one_half_win/float(range_one_half)
		
	# if range_two == 0:
		# two = 0
	# else:
		# two = range_two_win/float(range_two)
		
	# if range_two_half == 0:
		# two_half = 0
	# else:
		# two_half = range_two_half_win/float(range_two_half)
		
	# if range_three == 0:
		# three = 0
	# else:
		# three = range_three_win/float(range_three)
		
	# if range_three_half == 0:
		# three_half = 0
	# else:
		# three_half = range_three_half_win/float(range_three_half)
		
	# if range_four == 0:
		# four = 0
	# else:
		# four = range_four_win/float(range_four)
		
	# if range_four_half == 0:
		# four_half = 0
	# else:
		# four_half = range_four_half_win/float(range_four_half)
		
	# if range_five == 0:
		# five = 0
	# else:
		# five = range_five_win/float(range_five)
		
	# if range_five_half == 0:
		# five_half = 0
	# else:
		# five_half = range_five_half_win/float(range_five_half)
		
	# if range_six == 0:
		# six = 0
	# else:
		# six = range_six_win/float(range_six)
	
	# heroStringAbsWin = heroString + str(wins/count) + '\t\t' + str(sub_one) + '\t' + str(one) + '\t' + str(one_half) + '\t'
	# heroStringAbsWin = heroStringAbsWin + str(two) + '\t' + str(two_half) + '\t' + str(three) + '\t' + str(three_half) + '\t'
	# heroStringAbsWin = heroStringAbsWin + str(four) + '\t' + str(four_half) + '\t' + str(five) + '\t' + str(five_half) + '\t' + str(six) + '\n'
	
	# absWin.write(heroStringAbsWin)
	
	# heroStringAbs = heroString + str(count) + '\t\t' + str(range_sub_one/count) + '\t' + str(range_one/count) + '\t' + str(range_one_half/count) + '\t'
	# heroStringAbs = heroStringAbs + str(range_two/count) + '\t' + str(range_two_half/count) + '\t' + str(range_three/count) + '\t' + str(range_three_half/count) + '\t'
	# heroStringAbs = heroStringAbs + str(range_four/count) + '\t' + str(range_four_half/count) + '\t' + str(range_five/count) + '\t' + str(range_five_half/count) + '\t' + str(range_six/count) + '\n'
	
	# abs.write(heroStringAbs)
	
# relWin.close()
# absWin.close()