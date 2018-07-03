#!/usr/bin/python

import d2slib										#winxp's script
import sys											#don't know
import cPickle										#file input and output

fileName = '[6.80][H][2.5]Exp.txt'
fileObject = open(fileName,'r')

# fileName = '[6.81][VH][6.19][2]Exp.txt'	
# fileObject = open(fileName,'r')

matchDetails = cPickle.load(fileObject)

durationTotal = 0
count = 0
# totalDeaths = 0
subTen = 0
fifteen = 0
twenty = 0
twentyfive = 0
thirty = 0
thirtyfive = 0
forty = 0
fortyfive = 0
fifty = 0
fiftyfive = 0
sixty = 0
overSixty = 0

for match in matchDetails:
	if len(match.players) == 10 and match.mode != 18:
		durationTotal = durationTotal + match.duration						
		count = count + 1
		
		# for player in match.players:
			# totalDeaths = totalDeaths + player.deaths
			
		if match.duration < 600:
			subTen = subTen + 1
		elif match.duration < 900:
			fifteen = fifteen + 1
		elif match.duration < 1200:
			twenty = twenty + 1
		elif match.duration < 1500:
			twentyfive = twentyfive + 1
		elif match.duration < 1800:
			thirty = thirty + 1
		elif match.duration < 2100:
			thirtyfive = thirtyfive + 1
		elif match.duration < 2400:
			forty = forty + 1
		elif match.duration < 2700:
			fortyfive = fortyfive + 1
		elif match.duration < 3000:
			fifty = fifty + 1
		elif match.duration < 3300:
			fiftyfive = fiftyfive + 1
		elif match.duration < 3600:
			sixty = sixty + 1
		else:
			overSixty = overSixty + 1
					
subTen = float(subTen)/count * 100
subTen = str('%.2f' % subTen) + '%,'

fifteen = float(fifteen)/count * 100
fifteen = str('%.2f' % fifteen) + '%,'

twenty = float(twenty)/count * 100
twenty = str('%.2f' % twenty) + '%,'

twentyfive = float(twentyfive)/count * 100
twentyfive = str('%.2f' % twentyfive) + '%,'

thirty = float(thirty)/count * 100
thirty = str('%.2f' % thirty) + '%,'

thirtyfive = float(thirtyfive)/count * 100
thirtyfive = str('%.2f' % thirtyfive) + '%,'

forty = float(forty)/count * 100
forty = str('%.2f' % forty) + '%,'

fortyfive = float(fortyfive)/count * 100
fortyfive = str('%.2f' % fortyfive) + '%,'

fifty = float(fifty)/count * 100
fifty = str('%.2f' % fifty) + '%,'

fiftyfive = float(fiftyfive)/count * 100
fiftyfive = str('%.2f' % fiftyfive) + '%,'

sixty = float(sixty)/count * 100
sixty = str('%.2f' % sixty) + '%,'

overSixty = float(overSixty)/count * 100
overSixty = str('%.2f' % overSixty) + '%,'
	
print 'Under 10 minutes:  ' + subTen
print '10 to 15 minutes: ' + fifteen
print '15 to 20 minutes: ' + twenty
print '20 to 25 minutes: ' + twentyfive
print '25 to 30 minutes: ' + thirty
print '30 to 35 minutes: ' + thirtyfive
print '35 to 40 minutes: ' + forty
print '40 to 45 minutes: ' + fortyfive
print '45 to 50 minutes: ' + fifty
print '50 to 55 minutes: ' + fiftyfive
print '55 to 60 minutes: ' + sixty
print 'over 60 minutes: ' + overSixty

# print subTen + fifteen + twenty + twentyfive + thirty + thirtyfive + forty + fortyfive + fifty + fiftyfive + sixty + overSixty
print count

# print durationTotal
print float(durationTotal)/(count)

# print totalDeaths
# print float(totalDeaths)*60/durationTotal