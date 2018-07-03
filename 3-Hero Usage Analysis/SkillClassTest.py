#!/usr/bin/python

import sys											#don't know
import cPickle										#file input and output
import collections									#used for Counter

# def baseListCreator():
	# csvList = [-1]*54	
	# next = '\n'
	
	# csvList[3] = next
	# csvList[7] = next
	# csvList[11] = next
	# csvList[15] = next
	# csvList[16] = next
	# csvList[20] = next
	# csvList[24] = next
	# csvList[28] = next
	# csvList[32] = next
	# csvList[33] = next
	# csvList[37] = next
	# csvList[41] = next
	# csvList[45] = next
	# csvList[49] = next
	# csvList[50] = next
	
	# return csvList
	
def baseListCreator():
	csvList = [-1]*67	
	next = '\n'
	
	csvList[4] = next
	csvList[9] = next
	csvList[14] = next
	csvList[19] = next
	csvList[20] = next
	csvList[25] = next
	csvList[30] = next
	csvList[35] = next
	csvList[40] = next
	csvList[41] = next
	csvList[46] = next
	csvList[51] = next
	csvList[56] = next
	csvList[61] = next
	csvList[62] = next
	
	return csvList

def ratesByBuild():
	usageList = baseListCreator()
	winList = baseListCreator()
	for i in range (0,4):
		qPrim = 0
		qPrimWin = 0
		qw = 0
		qwWin = 0
		qe = 0
		qeWin = 0
		qSplit = 0
		qSplitWin = 0
		
		wPrim = 0
		wPrimWin = 0
		wq = 0
		wqWin = 0
		we = 0
		weWin = 0
		wSplit = 0
		wSplitWin = 0
		
		ePrim = 0
		ePrimWin = 0
		eq = 0
		eqWin = 0
		ew = 0
		ewWin = 0
		eSplit = 0
		eSplitWin = 0
		
		split = 0
		splitWin = 0
		
		use = len(heroDetails[i])
		
		print use
		
		for entry in heroDetails[i]:
			if entry.build == 'qw':
				qw = qw + 1
				if entry.win == True:
					qwWin = qwWin + 1
			elif entry.build == 'qe':
				qe = qe + 1
				if entry.win == True:
					qeWin = qeWin + 1
			elif entry.build == 'q-':
				qSplit = qSplit + 1
				if entry.win == True:
					qSplitWin = qSplitWin + 1
					
			elif entry.build == 'wq':
				wq = wq + 1
				if entry.win == True:
					wqWin = wqWin + 1
			elif entry.build == 'we':
				we = we + 1
				if entry.win == True:
					weWin = weWin + 1
			elif entry.build == 'w-':
				wSplit = wSplit + 1
				if entry.win == True:
					wSplitWin = wSplitWin + 1
			
			elif entry.build == 'eq':
				eq = eq + 1
				if entry.win == True:
					eqWin = eqWin + 1
			elif entry.build == 'ew':
				ew = ew + 1
				if entry.win == True:
					ewWin = ewWin + 1
			elif entry.build == 'e-':
				eSplit = eSplit + 1
				if entry.win == True:
					eSplitWin = eSplitWin + 1
					
			else:
				split = split + 1
				if entry.win == True:
					splitWin = splitWin + 1
					
		qPrim = qw + qe + qSplit
		qPrimWin = qwWin + qeWin + qSplitWin
		wPrim = wq + we + wSplit
		wPrimWin = wqWin + weWin + wSplitWin
		ePrim = eq + ew + eSplit
		ePrimWin = eqWin + ewWin + eSplitWin
		
		qRate = (float(qPrim)/use)*100
		qRate = str('%.2f' % qRate) + '%,'		
		qWinRate = (float(qPrimWin)/qPrim)*100
		qWinRate = str('%.2f' % qWinRate) + '%,'
		
		if qw == 0:
			qwRate = '0%,'
			qwWinRate = '0%,'
		else:
			qwRate = (float(qw)/qPrim)*100
			qwRate = str('%.2f' % qwRate) + '%,'		
			qwWinRate = (float(qwWin)/qw)*100
			qwWinRate = str('%.2f' % qwWinRate) + '%,'
		
		qeRate = (float(qe)/qPrim)*100
		qeRate = str('%.2f' % qeRate) + '%,'		
		qeWinRate = (float(qeWin)/qe)*100
		qeWinRate = str('%.2f' % qeWinRate) + '%,'
		
		if qSplit == 0:
			qSplitRate = '0%,'
			qSplitWinRate = '0%,'
		else:
			qSplitRate = (float(qSplit)/qPrim)*100
			qSplitRate = str('%.2f' % qSplitRate) + '%,'		
			qSplitWinRate = (float(qSplitWin)/qSplit)*100
			qSplitWinRate = str('%.2f' % qSplitWinRate) + '%,'
		
		wRate = (float(wPrim)/use)*100
		wRate = str('%.2f' % wRate) + '%,'		
		wWinRate = (float(wPrimWin)/wPrim)*100
		wWinRate = str('%.2f' % wWinRate) + '%,'
		
		wqRate = (float(wq)/wPrim)*100
		wqRate = str('%.2f' % wqRate) + '%,'		
		wqWinRate = (float(wqWin)/wq)*100
		wqWinRate = str('%.2f' % wqWinRate) + '%,'
		
		weRate = (float(we)/wPrim)*100
		weRate = str('%.2f' % weRate) + '%,'		
		weWinRate = (float(weWin)/we)*100
		weWinRate = str('%.2f' % weWinRate) + '%,'
		
		wSplitRate = (float(wSplit)/wPrim)*100
		wSplitRate = str('%.2f' % wSplitRate) + '%,'		
		wSplitWinRate = (float(wSplitWin)/wSplit)*100
		wSplitWinRate = str('%.2f' % wSplitWinRate) + '%,'
		
		eRate = (float(ePrim)/use)*100
		eRate = str('%.2f' % eRate) + '%,'		
		eWinRate = (float(ePrimWin)/ePrim)*100
		eWinRate = str('%.2f' % eWinRate) + '%,'
		
		eqRate = (float(eq)/ePrim)*100
		eqRate = str('%.2f' % eqRate) + '%,'		
		eqWinRate = (float(eqWin)/eq)*100
		eqWinRate = str('%.2f' % eqWinRate) + '%,'
		
		if ew == 0:
			ewRate = '0%,'
			ewWinRate = '0%,'
		else:
			ewRate = (float(ew)/ePrim)*100
			ewRate = str('%.2f' % ewRate) + '%,'		
			ewWinRate = (float(ewWin)/ew)*100
			ewWinRate = str('%.2f' % ewWinRate) + '%,'
		
		eSplitRate = (float(eSplit)/ePrim)*100
		eSplitRate = str('%.2f' % eSplitRate) + '%,'		
		eSplitWinRate = (float(eSplitWin)/eSplit)*100
		eSplitWinRate = str('%.2f' % eSplitWinRate) + '%,'
		
		splitRate = (float(split)/use)*100
		splitRate = str('%.2f' % splitRate) + '%,'		
		splitWinRate = (float(splitWin)/split)*100
		splitWinRate = str('%.2f' % splitWinRate) + '%,'
		
		useRates = [qRate, qwRate, qeRate, qSplitRate, wRate, wqRate, weRate, wSplitRate, eRate, eqRate, ewRate, eSplitRate, splitRate]
		winRates = [qWinRate, qwWinRate, qeWinRate, qSplitWinRate, wWinRate, wqWinRate, weWinRate, wSplitWinRate, eWinRate, eqWinRate, ewWinRate, eSplitWinRate, splitWinRate]
		
		usageList[0+i] = useRates[0]
		usageList[5+i] = useRates[1]
		usageList[10+i] = useRates[2]
		usageList[15+i] = useRates[3]
		usageList[21+i] = useRates[4]
		usageList[26+i] = useRates[5]
		usageList[31+i] = useRates[6]
		usageList[36+i] = useRates[7]
		usageList[42+i] = useRates[8]
		usageList[47+i] = useRates[9]
		usageList[52+i] = useRates[10]
		usageList[57+i] = useRates[11]
		usageList[63+i] = useRates[12]
		
		winList[0+i] = winRates[0]
		winList[5+i] = winRates[1]
		winList[10+i] = winRates[2]
		winList[15+i] = winRates[3]
		winList[21+i] = winRates[4]
		winList[26+i] = winRates[5]
		winList[31+i] = winRates[6]
		winList[36+i] = winRates[7]
		winList[42+i] = winRates[8]
		winList[47+i] = winRates[9]
		winList[52+i] = winRates[10]
		winList[57+i] = winRates[11]
		winList[63+i] = winRates[12]
		
	excelStr = '[' + hero + ']Table 1-1' + '.txt'			#names an output .csv file for export to Excel
	a = open(excelStr, "w")
	for item in usageList:
		a.write(item)
	a.close()
	
	excelStr = '[' + hero + ']Table 1-3' + '.txt'			#names an output .csv file for export to Excel
	a = open(excelStr, "w")
	for item in winList:
		a.write(item)
	a.close()

def skillPointByBracket():
	for i in range (0,4):
		
		qNumber=abilityNumbers[0]
		wNumber=abilityNumbers[1]
		eNumber=abilityNumbers[2]
		rNumber=abilityNumbers[3]
		
		use = 0
		
		q0count = 0
		q1count = 0
		q2count = 0
		q3count = 0
		q4count = 0
		q0win = 0
		q1win = 0
		q2win = 0
		q3win = 0
		q4win = 0
		
		w0count = 0
		w1count = 0
		w2count = 0
		w3count = 0
		w4count = 0
		w0win = 0
		w1win = 0
		w2win = 0
		w3win = 0
		w4win = 0
		
		e0count = 0
		e1count = 0
		e2count = 0
		e3count = 0
		e4count = 0
		e0win = 0
		e1win = 0
		e2win = 0
		e3win = 0
		e4win = 0

		for entry in heroDetails[i]:
			if len(entry.skills) < 8:
				pass
			else:				
				use = use + 1			
				holder = entry.skills[0:8]
				
				if holder.count(qNumber) == 0:
					q0count = q0count+1
					if entry.win == True:
						q0win = q0win + 1
				elif holder.count(qNumber) == 1:
					q1count = q1count+1
					if entry.win == True:
						q1win = q1win + 1
				elif holder.count(qNumber) == 2:
					q2count = q2count+1
					if entry.win == True:
						q2win = q2win + 1
				elif holder.count(qNumber) == 3:
					q3count = q3count+1
					if entry.win == True:
						q3win = q3win + 1
				elif holder.count(qNumber) == 4:
					q4count = q4count+1
					if entry.win == True:
						q4win = q4win + 1
				
				if holder.count(wNumber) == 0:
					w0count = w0count+1
					if entry.win == True:
						w0win = w0win + 1
				elif holder.count(wNumber) == 1:
					w1count = w1count+1
					if entry.win == True:
						w1win = w1win + 1
				elif holder.count(wNumber) == 2:
					w2count = w2count+1
					if entry.win == True:
						w2win = w2win + 1
				elif holder.count(wNumber) == 3:
					w3count = w3count+1
					if entry.win == True:
						w3win = w3win + 1
				elif holder.count(wNumber) == 4:
					w4count = w4count+1
					if entry.win == True:
						w4win = w4win + 1
						
				if holder.count(eNumber) == 0:
					e0count = e0count+1
					if entry.win == True:
						e0win = e0win + 1
				elif holder.count(eNumber) == 1:
					e1count = e1count+1
					if entry.win == True:
						e1win = e1win + 1
				elif holder.count(eNumber) == 2:
					e2count = e2count+1
					if entry.win == True:
						e2win = e2win + 1
				elif holder.count(eNumber) == 3:
					e3count = e3count+1
					if entry.win == True:
						e3win = e3win + 1
				elif holder.count(eNumber) == 4:
					e4count = e4count+1
					if entry.win == True:
						e4win = e4win + 1
	
		q0rate = (float(q0count)/use)*100
		q0rate = str('%.2f' % q0rate) + '%,'
		
		q1rate = (float(q1count)/use)*100
		q1rate = str('%.2f' % q1rate) + '%,'
		
		q2rate = (float(q2count)/use)*100
		q2rate = str('%.2f' % q2rate) + '%,'
		
		q3rate = (float(q3count)/use)*100
		q3rate = str('%.2f' % q3rate) + '%,'
		
		q4rate = (float(q4count)/use)*100
		q4rate = str('%.2f' % q4rate) + '%,'
		
		w0rate = (float(w0count)/use)*100
		w0rate = str('%.2f' % w0rate) + '%,'
		
		w1rate = (float(w1count)/use)*100
		w1rate = str('%.2f' % w1rate) + '%,'
		
		w2rate = (float(w2count)/use)*100
		w2rate = str('%.2f' % w2rate) + '%,'
		
		w3rate = (float(w3count)/use)*100
		w3rate = str('%.2f' % w3rate) + '%,'
		
		w4rate = (float(w4count)/use)*100
		w4rate = str('%.2f' % w4rate) + '%,'
		
		e0rate = (float(e0count)/use)*100
		e0rate = str('%.2f' % e0rate) + '%,'
		
		e1rate = (float(e1count)/use)*100
		e1rate = str('%.2f' % e1rate) + '%,'
		
		e2rate = (float(e2count)/use)*100
		e2rate = str('%.2f' % e2rate) + '%,'
		
		e3rate = (float(e3count)/use)*100
		e3rate = str('%.2f' % e3rate) + '%,'
		
		e4rate = (float(e4count)/use)*100
		e4rate = str('%.2f' % e4rate) + '%,'
						
		next = '\n'
		
		if i == 0:
			excelStr = '[' + hero + ']Table 2-1' + '.txt'			#names an output .csv file for export to Excel
			a = open(excelStr, "w")
		else:
			excelStr = '[' + hero + ']Table 2-1' + '.txt'			#names an output .csv file for export to Excel
			a = open(excelStr, "a")
		
		qString = q0rate + q1rate + q2rate + q3rate + q4rate + next
		wString = w0rate + w1rate + w2rate + w3rate + w4rate + next
		eString = e0rate + e1rate + e2rate + e3rate + e4rate + next + next
		
		writeString = qString + wString + eString
		
		a.write(writeString)
		a.close()
		
		if q0count == 0:
			q0rate = 0
		else:
			q0rate = (float(q0win)/q0count)*100
		q0rate = str('%.2f' % q0rate) + '%,'
		
		q1rate = (float(q1win)/q1count)*100
		q1rate = str('%.2f' % q1rate) + '%,'
		
		if q2count == 0:
			q2rate = 0
		else:
			q2rate = (float(q2win)/q2count)*100
		q2rate = str('%.2f' % q2rate) + '%,'
		
		if q3count == 0:
			q3rate = 0
		else:
			q3rate = (float(q3win)/q3count)*100
		q3rate = str('%.2f' % q3rate) + '%,'
		
		if q4count == 0:
			q4rate = 0
		else:
			q4rate = (float(q4win)/q4count)*100
		q4rate = str('%.2f' % q4rate) + '%,'
		
		if w0count == 0:
			w0rate = 0
		else:
			w0rate = (float(w0win)/w0count)*100
		w0rate = str('%.2f' % w0rate) + '%,'
		
		if w1count == 0:
			w1rate = 0
		else:
			w1rate = (float(w1win)/w1count)*100
		w1rate = str('%.2f' % w1rate) + '%,'
		
		w2rate = (float(w2win)/w2count)*100
		w2rate = str('%.2f' % w2rate) + '%,'
		
		if w3count == 0:
			w3rate = 0
		else:
			w3rate = (float(w3win)/w3count)*100
		w3rate = str('%.2f' % w3rate) + '%,'
		
		if w4count == 0:
			w4rate = 0
		else:
			w4rate = (float(w4win)/w4count)*100
		w4rate = str('%.2f' % w4rate) + '%,'
		
		if e0count == 0:
			e0rate = 0
		else:
			e0rate = (float(e0win)/e0count)*100
		e0rate = str('%.2f' % e0rate) + '%,'
		
		if e1count == 0:
			e1rate = 0
		else:
			e1rate = (float(e1win)/e1count)*100
		e1rate = str('%.2f' % e1rate) + '%,'
		
		if e2count == 0:
			e2rate = 0
		else:
			e2rate = (float(e2win)/e2count)*100
		e2rate = str('%.2f' % e2rate) + '%,'
		
		if e3count == 0:
			e3rate = 0
		else:
			e3rate = (float(e3win)/e3count)*100
		e3rate = str('%.2f' % e3rate) + '%,'
		
		if e4count == 0:
			e4rate = 0
		else:
			e4rate = (float(e4win)/e4count)*100
		e4rate = str('%.2f' % e4rate) + '%,'
		
		if i == 0:
			excelStr = '[' + hero + ']Table 2-2' + '.txt'			#names an output .csv file for export to Excel
			a = open(excelStr, "w")
		else:
			excelStr = '[' + hero + ']Table 2-2' + '.txt'			#names an output .csv file for export to Excel
			a = open(excelStr, "a")
		
		qString = q0rate + q1rate + q2rate + q3rate + q4rate + next
		wString = w0rate + w1rate + w2rate + w3rate + w4rate + next
		eString = e0rate + e1rate + e2rate + e3rate + e4rate + next + next
		
		writeString = qString + wString + eString
		
		a.write(writeString)
		a.close()
		
def heartstopperTest():
	excelStr = '[' + hero + ']Heartstopper' + '.txt'			#names an output .csv file for export to Excel
	a = open(excelStr, "w")

	wNumber=abilityNumbers[1]

	for i in range (0,3):
		wTiming = []
		
		for x in range(0,10):
			count = 0
			for entry in heroDetails[i]:
				if len(entry.skills) < 7:
					pass
				if entry.primary != 'q':
					pass
				holder = entry.skills[0:10] 
				if holder.count(wNumber) != 1:
					pass
				else:
					if entry.skills.index(wNumber) == x:
						# count = count + 1
						if entry.win == True:
							count = count + 1
			a.write(`count`)
			a.write('\n')
		a.write('\n'*3)
				 
		# usage = collections.Counter(wTiming).most_common(10)
		# usage.sort()
		# for entry in usage:
			# a.write(`entry[0] + 1`)
			# a.write(',')
			# a.write(`entry[1]`)
			# a.write('\n')
		# a.write('\n')
		
def ultTest():
	excelStr = '[' + hero + ']Ult1' + '.txt'			#names an output .csv file for export to Excel
	a = open(excelStr, "w")
	
	rNumber=abilityNumbers[3]
	
	for i in range (0,3):
		level = 7
		less = 0
		lessWin = 0
		greater = 0
		greaterWin = 0
		use = 0
		
		noUlt = 0
		
		for entry in heroDetails[i]:
			if len(entry.skills) > 5:
				if entry.skills.count(rNumber) > 1:
					use = use + 1
					if entry.skills.index(rNumber) < level:
						less = less + 1
						if entry.win == True:
							lessWin = lessWin + 1
					else:
						greater = greater + 1
						if entry.win == True:
							greaterWin = greaterWin + 1
				else:
					noUlt = noUlt + 1
		lessRate = (float(less)/use)*100
		lessRate = str('%.2f' % lessRate) + '%,'
		greaterRate = (float(greater)/use)*100
		greaterRate = str('%.2f' % greaterRate) + '%,'
		
		lessWinRate = (float(lessWin)/less)*100
		lessWinRate = str('%.2f' % lessWinRate) + '%,'
		greaterWinRate = (float(greaterWin)/greater)*100
		greaterWinRate = str('%.2f' % greaterWinRate) + '%,'
		
		a.write(lessRate + lessWinRate + greaterRate + greaterWinRate + '\n')
		print noUlt
	a.close()
	
def newUltTest():
	excelStr1 = '[' + hero + ']Ult1' + '.txt'			#names an output .csv file for export to Excel
	a = open(excelStr1, "w")
	
	excelStr2 = '[' + hero + ']Ult2' + '.txt'			#names an output .csv file for export to Excel
	b = open(excelStr2, "w")
	
	rNumber=abilityNumbers[3]
	
	for i in range (0,4):	
		ultUse = [0,0,0,0,0,0]
		ultWin = [0,0,0,0,0,0]
		win = 0
		count = 0
		for entry in heroDetails[i]:
			if len(entry.skills) > 11:
				count = count + 1
				if entry.win == True:
					win = win + 1
				if entry.skills[6] == rNumber:
					ultUse[0] = ultUse[0] + 1
					if entry.win == True:
						ultWin[0] = ultWin[0] + 1
				elif entry.skills[7] == rNumber:
					ultUse[1] = ultUse[1] + 1
					if entry.win == True:
						ultWin[1] = ultWin[1] + 1
				elif entry.skills[8] == rNumber:
					ultUse[2] = ultUse[2] + 1
					if entry.win == True:
						ultWin[2] = ultWin[2] + 1
				elif entry.skills[9] == rNumber:
					ultUse[3] = ultUse[3] + 1
					if entry.win == True:
						ultWin[3] = ultWin[3] + 1
				elif entry.skills[10] == rNumber:
					ultUse[4] = ultUse[4] + 1
					if entry.win == True:
						ultWin[4] = ultWin[4] + 1
				else:
					ultUse[5] = ultUse[5] + 1
					if entry.win == True:
						ultWin[5] = ultWin[5] + 1
		print ultUse[5]
		print count
		use6 = ultUse[0]/float(count)*100
		use6 = str('%.2f' % use6) + '%,'
		use7 = ultUse[1]/float(count)*100
		use7 = str('%.2f' % use7) + '%,'
		use8 = ultUse[2]/float(count)*100
		use8 = str('%.2f' % use8) + '%,'
		use9 = ultUse[3]/float(count)*100
		use9 = str('%.2f' % use9) + '%,'
		use10 = ultUse[4]/float(count)*100
		use10 = str('%.2f' % use10) + '%,'
		use11 = ultUse[5]/float(count)*100
		use11 = str('%.2f' % use11) + '%,'

		if ultUse[0] == 0:
			win6 = '0%,'
		else:
			win6 = ultWin[0]/float(ultUse[0])*100
			win6 = str('%.2f' % win6) + '%,'
			
		if ultUse[1] == 0:
			win7 = '0%,'
		else:
			win7 = ultWin[1]/float(ultUse[1])*100
			win7 = str('%.2f' % win7) + '%,'
			
		if ultUse[2] == 0:
			win8 = '0%,'
		else:
			win8 = ultWin[2]/float(ultUse[2])*100
			win8 = str('%.2f' % win8) + '%,'
			
		if ultUse[3] == 0:
			win9 = '0%,'
		else:
			win9 = ultWin[3]/float(ultUse[3])*100
			win9 = str('%.2f' % win9) + '%,'
			
		if ultUse[4] == 0:
			win10 = '0%,'
		else:
			win10 = ultWin[4]/float(ultUse[4])*100
			win10 = str('%.2f' % win10) + '%,'
			
		if ultUse[5] == 0:
			win11 = '0%,'
		else:
			win11 = ultWin[5]/float(ultUse[5])*100
			win11 = str('%.2f' % win11) + '%,'
			
		totalWin = win/float(count)*100
		totalWin = str('%.2f' % totalWin) + '%,'
		
		a.write(use6 + use7 + use8 + use9 + use10 + use11 + '\n')
		b.write(win6 + win7 + win8 + win9 + win10 + win11 + ',' + totalWin + '\n')
	a.close()
	b.close()
			
def skillPointMod():
	for i in range (0,3):
		
		# qNumber=abilityNumbers[0]
		qNumber = 5002
		wNumber=abilityNumbers[1]
		eNumber=abilityNumbers[2]
		# eNumber = 5002									#CONVERTS SLOT INTO STATS
		rNumber=abilityNumbers[3]
		
		use = 0
		count = 0
		
		q0count = 0
		q1count = 0
		q2count = 0
		q3count = 0
		q4count = 0
		q0win = 0
		q1win = 0
		q2win = 0
		q3win = 0
		q4win = 0
		
		w0count = 0
		w1count = 0
		w2count = 0
		w3count = 0
		w4count = 0
		w0win = 0
		w1win = 0
		w2win = 0
		w3win = 0
		w4win = 0
		
		e0count = 0
		e1count = 0
		e2count = 0
		e3count = 0
		e4count = 0
		e0win = 0
		e1win = 0
		e2win = 0
		e3win = 0
		e4win = 0

		for entry in heroDetails[i]:
			if len(entry.skills) < 9:
				pass
			if entry.primary != 'q':
				pass
			else:				
				use = use + 1			
				holder = entry.skills[0:9]
				
				if holder.count(qNumber) == 0:
					q0count = q0count+1
					if entry.win == True:
						q0win = q0win + 1
				elif holder.count(qNumber) == 1:
					q1count = q1count+1
					if entry.win == True:
						q1win = q1win + 1
				elif holder.count(qNumber) == 2:
					q2count = q2count+1
					if entry.win == True:
						q2win = q2win + 1
				elif holder.count(qNumber) == 3:
					q3count = q3count+1
					if entry.win == True:
						q3win = q3win + 1
				elif holder.count(qNumber) == 4:
					q4count = q4count+1
					if entry.win == True:
						q4win = q4win + 1
				
				if holder.count(wNumber) == 0:
					w0count = w0count+1
					if entry.win == True:
						w0win = w0win + 1
				elif holder.count(wNumber) == 1:
					w1count = w1count+1
					if entry.win == True:
						w1win = w1win + 1
				elif holder.count(wNumber) == 2:
					w2count = w2count+1
					if entry.win == True:
						w2win = w2win + 1
				elif holder.count(wNumber) == 3:
					w3count = w3count+1
					if entry.win == True:
						w3win = w3win + 1
				elif holder.count(wNumber) == 4:
					w4count = w4count+1
					if entry.win == True:
						w4win = w4win + 1
						
				if holder.count(eNumber) == 0:
					e0count = e0count+1
					if entry.win == True:
						e0win = e0win + 1
				elif holder.count(eNumber) == 1:
					e1count = e1count+1
					if entry.win == True:
						e1win = e1win + 1
				elif holder.count(eNumber) == 2:
					e2count = e2count+1
					if entry.win == True:
						e2win = e2win + 1
				elif holder.count(eNumber) == 3:
					e3count = e3count+1
					if entry.win == True:
						e3win = e3win + 1
				elif holder.count(eNumber) == 4:
					e4count = e4count+1
					if entry.win == True:
						e4win = e4win + 1
		
		print use
						
		q0rate = (float(q0count)/use)*100
		q0rate = str('%.2f' % q0rate) + '%,'
		
		q1rate = (float(q1count)/use)*100
		q1rate = str('%.2f' % q1rate) + '%,'
		
		q2rate = (float(q2count)/use)*100
		q2rate = str('%.2f' % q2rate) + '%,'
		
		q3rate = (float(q3count)/use)*100
		q3rate = str('%.2f' % q3rate) + '%,'
		
		q4rate = (float(q4count)/use)*100
		q4rate = str('%.2f' % q4rate) + '%,'
		
		w0rate = (float(w0count)/use)*100
		w0rate = str('%.2f' % w0rate) + '%,'
		
		w1rate = (float(w1count)/use)*100
		w1rate = str('%.2f' % w1rate) + '%,'
		
		w2rate = (float(w2count)/use)*100
		w2rate = str('%.2f' % w2rate) + '%,'
		
		w3rate = (float(w3count)/use)*100
		w3rate = str('%.2f' % w3rate) + '%,'
		
		w4rate = (float(w4count)/use)*100
		w4rate = str('%.2f' % w4rate) + '%,'
		
		e0rate = (float(e0count)/use)*100
		e0rate = str('%.2f' % e0rate) + '%,'
		
		e1rate = (float(e1count)/use)*100
		e1rate = str('%.2f' % e1rate) + '%,'
		
		e2rate = (float(e2count)/use)*100
		e2rate = str('%.2f' % e2rate) + '%,'
		
		e3rate = (float(e3count)/use)*100
		e3rate = str('%.2f' % e3rate) + '%,'
		
		e4rate = (float(e4count)/use)*100
		e4rate = str('%.2f' % e4rate) + '%,'
						
		next = '\n'
		
		if i == 0:
			excelStr = '[' + hero + ']Table 2-1sub' + '.txt'			#names an output .csv file for export to Excel
			a = open(excelStr, "w")
		else:
			excelStr = '[' + hero + ']Table 2-1sub' + '.txt'			#names an output .csv file for export to Excel
			a = open(excelStr, "a")
		
		qString = q0rate + q1rate + q2rate + q3rate + q4rate + next
		wString = w0rate + w1rate + w2rate + w3rate + w4rate + next
		eString = e0rate + e1rate + e2rate + e3rate + e4rate + next + next
		
		writeString = qString + wString + eString
		
		a.write(writeString)
		a.close()
		
		if q0count == 0:
			q0rate = 0
		else:
			q0rate = (float(q0win)/q0count)*100
		q0rate = str('%.2f' % q0rate) + '%,'
		
		if q1count == 0:
			q1rate = 0		
		else:
			q1rate = (float(q1win)/q1count)*100
		q1rate = str('%.2f' % q1rate) + '%,'
		
		if q2count == 0:
			q2rate = 0
		else:
			q2rate = (float(q2win)/q2count)*100
		q2rate = str('%.2f' % q2rate) + '%,'
		
		if q3count == 0:
			q3rate = 0
		else:
			q3rate = (float(q3win)/q3count)*100
		q3rate = str('%.2f' % q3rate) + '%,'
		
		if q4count == 0:
			q4rate = 0
		else:
			q4rate = (float(q4win)/q4count)*100
		q4rate = str('%.2f' % q4rate) + '%,'
		
		if w0count == 0:
			w0rate = 0
		else:
			w0rate = (float(w0win)/w0count)*100
		w0rate = str('%.2f' % w0rate) + '%,'
		
		if w1count == 0:
			w1rate = 0
		else:
			w1rate = (float(w1win)/w1count)*100
		w1rate = str('%.2f' % w1rate) + '%,'
		
		if w2count == 0:
			w2rate = 0
		else:
			w2rate = (float(w2win)/w2count)*100
		w2rate = str('%.2f' % w2rate) + '%,'
		
		if w3count == 0:
			w3rate = 0
		else:
			w3rate = (float(w3win)/w3count)*100
		w3rate = str('%.2f' % w3rate) + '%,'
		
		if w4count == 0:
			w4rate = 0
		else:
			w4rate = (float(w4win)/w4count)*100
		w4rate = str('%.2f' % w4rate) + '%,'
		
		if e0count == 0:
			e0rate = 0
		else:
			e0rate = (float(e0win)/e0count)*100
		e0rate = str('%.2f' % e0rate) + '%,'
		
		if e1count == 0:
			e1rate = 0
		else:
			e1rate = (float(e1win)/e1count)*100
		e1rate = str('%.2f' % e1rate) + '%,'
		
		if e2count == 0:
			e2rate = 0
		else:
			e2rate = (float(e2win)/e2count)*100
		e2rate = str('%.2f' % e2rate) + '%,'
		
		if e3count == 0:
			e3rate = 0
		else:
			e3rate = (float(e3win)/e3count)*100
		e3rate = str('%.2f' % e3rate) + '%,'
		
		if e4count == 0:
			e4rate = 0
		else:
			e4rate = (float(e4win)/e4count)*100
		e4rate = str('%.2f' % e4rate) + '%,'
		
		if i == 0:
			excelStr = '[' + hero + ']Table 2-2sub' + '.txt'			#names an output .csv file for export to Excel
			a = open(excelStr, "w")
		else:
			excelStr = '[' + hero + ']Table 2-2sub' + '.txt'			#names an output .csv file for export to Excel
			a = open(excelStr, "a")
		
		qString = q0rate + q1rate + q2rate + q3rate + q4rate + next
		wString = w0rate + w1rate + w2rate + w3rate + w4rate + next
		eString = e0rate + e1rate + e2rate + e3rate + e4rate + next + next
		
		writeString = qString + wString + eString
		
		a.write(writeString)
		a.close()

def winRate():									#finds a hero's total, sub-level 8, and not sub level 8 win rates and creates an export for WinRate tab in Template
	excelStr = '[' + hero + ']Table 1-5' + '.txt'			#names an output .csv file for export to Excel
	a = open(excelStr, "w")
	
	csvOutput = [-1]*11
	next = '\n'
	
	csvOutput[3] = next
	csvOutput[7] = next

	for i in range(0,4):	
		use = 0
		win = 0
		
		underUse = 0
		underWin = 0
		
		overUse = 0
		overWin = 0
			
		for entry in heroDetails[i]:				
			use = use + 1
			if entry.win == True:
				win = win + 1
			if len(entry.skills) < 8:
				underUse = underUse + 1
				if entry.win == True:
					underWin = underWin + 1
			else:
				overUse = overUse + 1
				if entry.win == True:
					overWin = overWin + 1
			
		rate = (float(win)/use)*100
		rate = ('%.2f' % rate) + '%,'
		underRate = (float(underWin)/underUse)*100
		underRate = ('%.2f' % underRate) + '%,'
		overRate = (float(overWin)/overUse)*100
		overRate = ('%.2f' % overRate) + '%,'
		
		# if i == 0:
			# csvOutput[0] = rate
			# csvOutput[4] = underRate
			# csvOutput[8] = overRate
			
		# elif i == 1:
			# csvOutput[1] = rate
			# csvOutput[5] = underRate
			# csvOutput[9] = overRate
			
		# elif i == 2:
			# csvOutput[2] = rate
			# csvOutput[6] = underRate
			# csvOutput[10] = overRate
		
	# for x in range(0,11):
		a.write(rate)	
	a.close()

def winRateMod():
	excelStr = '[' + hero + ']Table 1-sub' + '.txt'			#names an output .csv file for export to Excel
	a = open(excelStr, "w")

	for i in range(0,3):
		use = 0
		qwUse = 0
		qwWin = 0
		notUse = 0
		notWin = 0
		
		for entry in heroDetails[i]:
			use = use + 1
			if entry.primary == 'q':
				qwUse = qwUse + 1
				if entry.win == True:
					qwWin = qwWin + 1
			else:
				notUse = notUse + 1
				if entry.win == True:
					notWin = notWin + 1
					
		qwUseRate = float(qwUse)/use*100
		qwUseRate = str('%.2f' % qwUseRate) + '%,'
		notUseRate = float(notUse)/use*100
		notUseRate = str('%.2f' % notUseRate) + '%,'
		
		qwWinRate = float(qwWin)/qwUse*100
		qwWinRate = str('%.2f' % qwWinRate) + '%,'
		notWinRate = float(notWin)/notUse*100
		notWinRate = str('%.2f' % notWinRate) + '%,'
		
		a.write(qwUseRate)
		a.write(qwWinRate)
		a.write(notUseRate)
		a.write(notWinRate)
		a.write('\n')
	a.close()
	
def winRateMod2():
	excelStr = '[' + hero + ']Table 1-sub' + '.txt'			#names an output .csv file for export to Excel
	a = open(excelStr, "w")

	for i in range(0,3):
		use = 0
		eUse = 0
		eWin = 0
		notUse = 0
		notWin = 0
		
		for entry in heroDetails[i]:
			if entry.primary == 'q':
				if len(entry.skills) > 9:
					use = use + 1
					holder = entry.skills[0:10]
					if holder.count(5272) == 4:
						eUse = eUse + 1
						if entry.win == True:
							eWin = eWin + 1
					elif holder.count(5272) < 2:
						notUse = notUse + 1
						if entry.win == True:
							notWin = notWin + 1				
						
		eUseRate = float(eUse)/use*100
		eUseRate = str('%.2f' % eUseRate) + '%,'
		notUseRate = float(notUse)/use*100
		notUseRate = str('%.2f' % notUseRate) + '%,'
		
		eWinRate = float(eWin)/eUse*100
		eWinRate = str('%.2f' % eWinRate) + '%,'
		notWinRate = float(notWin)/notUse*100
		notWinRate = str('%.2f' % notWinRate) + '%,'
		
		a.write(eUseRate)
		a.write(eWinRate)
		a.write(notUseRate)
		a.write(notWinRate)
		a.write('\n')
	a.close()

def statsNult():	
	qNumber=abilityNumbers[0]
	wNumber=abilityNumbers[1]
	eNumber=abilityNumbers[2]
	rNumber=abilityNumbers[3]

	next = '\n'
	
	usageOutput = [-1]*11
	usageOutput[3] = next
	usageOutput[7] = next
	
	winOutput = [-1]*11
	winOutput[3] = next
	winOutput[7] = next
	
	excelStr = '[' + hero + ']Table 1-2' + '.txt'			#names an output .csv file for export to Excel
	a = open(excelStr, "w")
	
	excelStr = '[' + hero + ']Table 1-4' + '.txt'			#names an output .csv file for export to Excel
	b = open(excelStr, "w")
	
	for i in range(0,3):
	
		use = 0									
		earlyStats = 0
		lateStats = 0
		ultSkip = 0
		
		earlyStatsWin = 0
		lateStatsWin = 0
		ultSkipWin = 0
	
		for entry in heroDetails[i]:
			use = use + 1

			if len(entry.skills) > 8:	
			
				holder = entry.skills[0:8]								#levels 1 through 8		
				for skill in holder:
					if skill == 5002:									#5002 is the code for skilling stats						
						earlyStats = earlyStats+1
						if entry.win == True:
							earlyStatsWin = earlyStatsWin + 1

				holder = entry.skills[8:14]							#levels 9 through 14
				for skill in holder:
					if skill == 5002:															
						lateStats = lateStats+1
						if entry.win == True:
							lateStatsWin = lateStatsWin + 1	
							
				if entry.skills[5] != rNumber:							
					ultSkip = ultSkip + 1
					if entry.win == True:
						ultSkipWin = ultSkipWin + 1
							
		earlyUseRate = (float(earlyStats)/use)*100
		earlyUseRate = str('%.2f' % earlyUseRate) + '%,'
		lateUseRate = (float(lateStats)/use)*100
		lateUseRate = str('%.2f' % lateUseRate) + '%,'

		ultSkipRate = (float(ultSkip)/use)*100
		ultSkipRate = str('%.2f' % ultSkipRate) + '%,'
								
		earlyWinRate = (float(earlyStatsWin)/earlyStats)*100
		earlyWinRate = str('%.2f' % earlyWinRate) + '%,'
		lateWinRate = (float(lateStatsWin)/lateStats)*100
		lateWinRate = str('%.2f' % lateWinRate) + '%,'
		
		ultSkipWinRate = (float(ultSkipWin)/ultSkip)*100
		ultSkipWinRate = str('%.2f' % ultSkipWinRate) + '%,'
		
		usageList = [earlyUseRate, lateUseRate, ultSkipRate]
		winList = [earlyWinRate, lateWinRate, ultSkipWinRate]
		holdingList = [usageList, winList]
	
		if i == 0:
			usageOutput[0] = earlyUseRate
			usageOutput[4] = lateUseRate
			usageOutput[8] = ultSkipRate
			
			winOutput[0] = earlyWinRate
			winOutput[4] = lateWinRate
			winOutput[8] = ultSkipWinRate
		
		elif i == 1:
			usageOutput[1] = earlyUseRate
			usageOutput[5] = lateUseRate
			usageOutput[9] = ultSkipRate
			
			winOutput[1] = earlyWinRate
			winOutput[5] = lateWinRate
			winOutput[9] = ultSkipWinRate
			
		elif i == 2:
			usageOutput[2] = earlyUseRate
			usageOutput[6] = lateUseRate
			usageOutput[10] = ultSkipRate
			
			winOutput[2] = earlyWinRate
			winOutput[6] = lateWinRate
			winOutput[10] = ultSkipWinRate

	for x in range(0,11):
		a.write(usageOutput[x])
		b.write(winOutput[x])
	a.close()

def skillCharts():

	qNumber=abilityNumbers[0]
	wNumber=abilityNumbers[1]
	eNumber=abilityNumbers[2]
	
	for i in range(0,3):
	
		use = 0
		qUse0 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		qWin0 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		qUse1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		qWin1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]		
		qUse2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		qWin2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		qUse3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		qWin3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		qUse4 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		qWin4 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]		
		# wUse = []
		# wWin = []
		# eUse = []
		# eWin = []
		
		for entry in heroDetails[i]:
			use = use + 1
			for x in range(0,14):
				holder = entry.skills[0:x+1]
				if holder.count(qNumber) == 0:
					qUse0[x] = qUse0[x] + 1
					if entry.win == True:
						qWin0[x] = qWin0[x] + 1
				if holder.count(qNumber) == 1:
					qUse1[x] = qUse1[x] + 1
					if entry.win == True:
						qWin1[x] = qWin1[x] + 1
				if holder.count(qNumber) == 2:
					qUse2[x] = qUse2[x] + 1
					if entry.win == True:
						qWin2[x] = qWin2[x] + 1
				if holder.count(qNumber) == 3:
					qUse3[x] = qUse3[x] + 1
					if entry.win == True:
						qWin3[x] = qWin3[x] + 1
				if holder.count(qNumber) == 4:
					qUse4[x] = qUse4[x] + 1
					if entry.win == True:
						qWin4[x] = qWin4[x] + 1
		
		if i == 0:
			excelStr = '[' + hero + ']qUseN' + '.txt'			#names an output .csv file for export to Excel
			useStr = open(excelStr, "w")		
			excelStr = '[' + hero + ']qWinN' + '.txt'			#names an output .csv file for export to Excel
			winStr = open(excelStr, "w")
			
		if i == 1:
			excelStr = '[' + hero + ']qUseH' + '.txt'			#names an output .csv file for export to Excel
			useStr = open(excelStr, "w")		
			excelStr = '[' + hero + ']qWinH' + '.txt'			#names an output .csv file for export to Excel
			winStr = open(excelStr, "w")
			
		if i == 2:
			excelStr = '[' + hero + ']qUseV' + '.txt'			#names an output .csv file for export to Excel
			useStr = open(excelStr, "w")		
			excelStr = '[' + hero + ']qWinV' + '.txt'			#names an output .csv file for export to Excel
			winStr = open(excelStr, "w")
		
		for x in range(0,14):
			useOutput = float(qUse0[x]) / use * 100
			useOutput = str('%.2f' % useOutput) + '%,'
			useStr.write(useOutput)
			
			if qUse0[x] == 0:
				winOutput = 0
				winOutput = str('%.2f' % winOutput) + '%,'
			else:
				winOutput = float(qWin0[x]) / qUse0[x] * 100
				winOutput = str('%.2f' % winOutput) + '%,'
				
			winStr.write(winOutput)
		
		useStr.write('\n')
		winStr.write('\n')
		
		for x in range(0,14):
			useOutput = float(qUse1[x]) / use * 100
			useOutput = str('%.2f' % useOutput) + '%,'
			useStr.write(useOutput)
			
			if qUse1[x] == 0:
				winOutput = 0
				winOutput = str('%.2f' % winOutput) + '%,'
			else:
				winOutput = float(qWin1[x]) / qUse1[x] * 100
				winOutput = str('%.2f' % winOutput) + '%,'
				
			winStr.write(winOutput)
			
		useStr.write('\n')
		winStr.write('\n')
		
		for x in range(0,14):
			useOutput = float(qUse2[x]) / use * 100
			useOutput = str('%.2f' % useOutput) + '%,'
			useStr.write(useOutput)
			
			if qUse2[x] == 0:
				winOutput = 0
				winOutput = str('%.2f' % winOutput) + '%,'
			else:
				winOutput = float(qWin2[x]) / qUse2[x] * 100
				winOutput = str('%.2f' % winOutput) + '%,'
				
			winStr.write(winOutput)
			
		useStr.write('\n')
		winStr.write('\n')
		
		for x in range(0,14):
			useOutput = float(qUse3[x]) / use * 100
			useOutput = str('%.2f' % useOutput) + '%,'
			useStr.write(useOutput)
			
			if qUse3[x] == 0:
				winOutput = 0
				winOutput = str('%.2f' % winOutput) + '%,'
			else:
				winOutput = float(qWin3[x]) / qUse3[x] * 100
				winOutput = str('%.2f' % winOutput) + '%,'
				
			winStr.write(winOutput)
			
		useStr.write('\n')
		winStr.write('\n')
		
		for x in range(0,14):
			useOutput = float(qUse4[x]) / use * 100
			useOutput = str('%.2f' % useOutput) + '%,'
			useStr.write(useOutput)
			
			if qUse4[x] == 0:
				winOutput = 0
				winOutput = str('%.2f' % winOutput) + '%,'
			else:
				winOutput = float(qWin4[x]) / qUse4[x] * 100
				winOutput = str('%.2f' % winOutput) + '%,'
				
			winStr.write(winOutput)
			
		useStr.close()
		winStr.close()
			
			
				
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

class abilityData:
	level = int()
	win = bool()
	skills = []
	primary = str()
	secondary = str()
	build = str()
	matchID = int()
	# sumTeamLevel = int()
	csPm = float()
	kaP10m = float()
	dP10m = float()
	ghost = bool()

fileName = '[MultiPatch][' + hero + ']AbilityData.txt'
fileObject = open(fileName,'r')
heroDetails = cPickle.load(fileObject)
fileObject.close()

ratesByBuild()
skillPointByBracket()
winRate()
# newUltTest()

# statsNult()
# skillPointMod()
# winRateMod2()
# heartstopperTest()
# ultTest()

# skillCharts()

# a = open("[6.77]SlarkStuff1.txt", "w")
# b = open("[6.77]SlarkStuff2.txt", "w")
# c = open("[6.77]SlarkStuff3.txt", "w")

# com = ','

# a = open("[6.78]HuskarFarmDep.txt", "w")

# for i in range(2,3):
	# csTotal = 0
	# counter = 0
	# for entry in heroDetails[i]:
		# if entry.primary == 'e':
			# csTotal = csTotal + entry.kaP10m
			# counter = counter + 1
	# csTotal = csTotal / counter
	# print csTotal
	# winCount = 0
	# for entry in heroDetails[i]:
		# if entry.win == True:
			# winCount = winCount + 1
				
	# heroDetails[i].sort(key = lambda x: x.csPm)

	# divisor = (len(heroDetails[i])/5)
	# firstBreak = len(heroDetails[i])-(divisor*4)
	# secondBreak = len(heroDetails[i])-(divisor*3)
	# thirdBreak = len(heroDetails[i])-(divisor*2)
	# fourthBreak = len(heroDetails[i])-(divisor*1)

	# counter = 0

	# firstCounter = 0
	# secondCounter = 0
	# thirdCounter = 0
	# fourthCounter = 0
	# fifthCounter = 0

	# firstWin = 0
	# secondWin = 0
	# thirdWin = 0
	# fourthWin = 0
	# fifthWin = 0

	# firstAvg = 0
	# fifthAvg = 0

	# for x in xrange(0, firstBreak):
		# counter = counter + 1
		# firstCounter = firstCounter + 1
		# firstAvg = firstAvg + heroDetails[i][x].csPm
		# if heroDetails[i][x].win == True:
			# firstWin = firstWin + 1

	# for x in xrange(firstBreak, secondBreak):
		# counter = counter + 1
		# secondCounter = secondCounter + 1
		# if heroDetails[i][x].win == True:
			# secondWin = secondWin + 1

	# for x in xrange(secondBreak, thirdBreak):
		# counter = counter + 1
		# thirdCounter = thirdCounter + 1
		# if heroDetails[i][x].win == True:
			# thirdWin = thirdWin + 1

	# for x in xrange(thirdBreak, fourthBreak):
		# counter = counter + 1
		# fourthCounter = fourthCounter + 1
		# if heroDetails[i][x].win == True:
			# fourthWin = fourthWin + 1
			
	# for x in xrange(fourthBreak, (len(heroDetails[i]))):
		# counter = counter + 1
		# fifthCounter = fifthCounter + 1
		# fifthAvg = fifthAvg + heroDetails[i][x].csPm
		# if heroDetails[i][x].win == True:
			# fifthWin = fifthWin + 1
			
	# winRate = float(winCount)/len(heroDetails[i])
	# firstWinRate = float(firstWin)/firstCounter
	# secondWinRate = float(secondWin)/secondCounter
	# thirdWinRate = float(thirdWin)/thirdCounter
	# fourthWinRate = float(fourthWin)/fourthCounter
	# fifthWinRate = float(fifthWin)/fifthCounter

	# firstWinMod = (firstWinRate - winRate) 
	# secondWinMod = (secondWinRate - winRate) 
	# thirdWinMod = (thirdWinRate - winRate) 
	# fourthWinMod = (fourthWinRate - winRate) 
	# fifthWinMod = (fifthWinRate - winRate) 


	# a.write(hero + com*2)
	# a.write (`len(heroDetails[i])`)
	# a.write(com)
	# a.write('%.4f' %  winRate)
	# a.write(com*2)
	# a.write('%.4f' %  firstWinMod)
	# a.write(com)
	# a.write('%.4f' %  secondWinMod)
	# a.write(com)
	# a.write('%.4f' %  thirdWinMod)
	# a.write(com)
	# a.write('%.4f' %  fourthWinMod)
	# a.write(com)
	# a.write('%.4f' %  fifthWinMod)
	# a.write('\n')

# for i in range(0,3):
	# use = 0
	# win = 0
	
	# for entry in heroDetails[i]:
		# if entry.primary == 'e':
			# if entry.ghost == True:
				# use = use + 1
				# if entry.win == True:
					# win = win + 1
	# print use
	# if use > 0:
		# print win/float(use)
	

# for i in range(0,3):
	# qCS = []
	# wCS = []
	
	# for entry in heroDetails[i]:	
		# if entry.primary == 'q':
			# qCS.append(entry.csPm)
		# elif entry.primary == 'w':
			# wCS.append(entry.csPm)
			
	# a.write(`sum(qCS)/len(qCS)`)
	# a.write(com)
	# a.write(`sum(wCS)/len(wCS)`)
	# a.write('\n')
	
# for i in range(0,3):
	# qKA = []
	# wKA = []
	
	# for entry in heroDetails[i]:	
		# if entry.primary == 'q':
			# qKA.append(entry.kaP10m)
		# elif entry.primary == 'w':
			# wKA.append(entry.kaP10m)
			
	# b.write(`sum(qKA)/len(qKA)`)
	# b.write(com)
	# b.write(`sum(wKA)/len(wKA)`)
	# b.write('\n')

# for i in range(0,3):
	# qD = []
	# wD = []
	
	# for entry in heroDetails[i]:	
		# if entry.primary == 'q':
			# qD.append(entry.dP10m)
		# elif entry.primary == 'w':
			# wD.append(entry.dP10m)
			
	# c.write(`sum(qD)/len(qD)`)
	# c.write(com)
	# c.write(`sum(wD)/len(wD)`)
	# c.write('\n')

# a.close()
# b.close()
# c.close()
	
# for i in range(0,3):
	# use = 0
	# by7 = 0
	# by7win = 0
	# by8 = 0
	# by8win = 0
	
	# list = []
	# for entry in heroDetails[i]:
		# try:
			# print entry.skills[0]
			# list.append(entry.skills[0])
		# except:
			# pass
	# starter = collections.Counter(list).most_common(3)
	# for x in starter:
		# print x
		
		# if entry.build == 'ew':
			# print entry.matchID
			# if len(entry.skills) > 12:
				# use = use + 1
				# holder = entry.skills[0:14]
				# list.append(holder.count(5271))
				# qList = collections.Counter(list).most_common(5)
	# for entry in qList:
		# print entry
					# by7 = by7 + 1
					# if entry.win == True:
						# by7win = by7win + 1
		# holder = entry.skills[0:8]
		# if holder.count(5273) == 4:
			# # by8 = by8 + 1
			# # if entry.win == True:
				# # by8win = by8win + 1
			# if entry.primary != 'e':
				# print `holder.count(5271)` + '/' + `holder.count(5272)` + '/4/' + `holder.count(5002)`
				# print `entry.win` + '/' + `i`
				# print entry.matchID
				# print '\n'
	# by7use = float(by7)/use
	# by8use = float(by8)/use
	# by7winRate = float(by7win)/by7
	# by8winRate = float(by8win)/by8
	
	# print by7use
	# print by8use
	# print '\n'
	# print by7winRate
	# print by8winRate
	# print '\n'
			

# for i in range(0,3):
	# use = 0
	# win = 0
	# for entry in heroDetails[i]:	
		# holder = entry.skills[0:10]
		# if holder.count(5272) == 4:
			# if holder.count(5273) == 4:
				# use = use + 1
				# if entry.win == True:
					# win = win + 1
	# print use
	# print float(win)/use

# for i in range(0,3):
	# levelRatio = []
	# modList = [s for s in heroDetails[i] if float(s.level)/s.sumTeamLevel < .23]
	# modList = [s for s in heroDetails[i] if float(s.level)/s.sumTeamLevel > .245]
	# print len(modList)
	# heroDetails.append(modList)
	
# del heroDetails[2]
# del heroDetails[1]
# del heroDetails[0]

# for i in range(0,3):
	# statRanks = []
	# for entry in heroDetails[i]:	
		# if entry.build == 'w-':
			# holder = entry.skills[0:11]
			# c = collections.Counter(holder)		
			# statRanks.append(c[5002])
	# for x in range(0,5):
		# print collections.Counter(statRanks).most_common(10)[x]
	# print '\n'

	
	# for entry in heroDetails[i]:
		# avgTeamLevel = float(heroDetails[i][x].sumTeamLevel) / 4
		# ratio = heroDetails[i][x].level/avgTeamLevel
		# if ratio > .91:
			# heroDetails[i].remove
		# avgTeamLevel = float(entry.sumTeamLevel) / 4
		# ratio = entry.level/float(entry.sumTeamLevel)
		# levelRatio.append(ratio)
	# levelRatio.sort()
	# print sum(levelRatio)/len(levelRatio)
	# print levelRatio[2000]
	# print levelRatio[-2000]
	# print '\n'

# for i in range (0,3):
	# ultSkip = 0
	# for entry in heroDetails[i]:
		# if len(entry.skills) > 5:
			# if entry.skills[5] != abilityNumbers[3]:
				# ultSkip = ultSkip + 1
	# print float(ultSkip)/len(heroDetails[i])
	
# for i in range (0,3):
	# builds = []
	# for entry in heroDetails[i]:
		# builds.append(entry.build)
	# buildList = collections.Counter(builds).most_common(30)
	# sum = 0
	# for x in buildList:
		# print x
		# sum = sum + x[1]
	# print '\n'
	# print `sum` + '\n'

# for i in range(0,3):
	# primaryList = []
	# qSecondaryList = []
	# wSecondaryList = []
	# eSecondaryList = []
	# for entry in heroDetails[i]:
		# primaryList.append(entry.primary)
		# if entry.primary == 'q':
			# qSecondaryList.append(entry.secondary)
		# if entry.primary == 'w':
			# wSecondaryList.append(entry.secondary)
		# if entry.primary == 'e':
			# eSecondaryList.append(entry.secondary)
	# print 'Q Primary Count: ' + `primaryList.count('q')`
	# print '\tSecondaries:  W=' + `qSecondaryList.count('w')` + ' // E=' + `qSecondaryList.count('e')`
	# print 'W Primary Count: ' + `primaryList.count('w')`
	# print '\tSecondaries:  Q=' + `wSecondaryList.count('q')` + ' // E=' + `wSecondaryList.count('e')`
	# print 'E Primary Count: ' + `primaryList.count('e')`
	# print '\tSecondaries:  Q=' + `eSecondaryList.count('q')` + ' // W=' + `eSecondaryList.count('w')` + '\n'