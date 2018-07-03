import d2slib										#winxp's script
import sys											
import cPickle										#file input and output
import collections									#used for Counter

###Used to combine 3 months of samples into a single file

# def bracketSwitcher(i, sampleName):							#Used to change the input file so all three brackets are tested sequentially
	# baseStr = '[' + sampleName + ']'
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
		
# samples = ['Jan', 'Feb', 'Mar']

# for i in range(1,4):
	# matchData = []
	# for j in range (0,3):
		# sampleName = samples[j]
		# fileName = bracketSwitcher(i, sampleName)
		# fileObject = open(fileName,'r')
		# matchDetails = cPickle.load(fileObject)
		# fileObject.close()
		# matchData.extend(matchDetails)
	
	# if i == 1:
		# fileSuffix = "NormalExp.txt"
	# elif i == 2:
		# fileSuffix = "HighExp.txt"
	# elif i == 3:
		# fileSuffix = "VeryHighExp.txt"	
		
	# fileName = '[6.77]' + fileSuffix
	# fileObject = open(fileName,'w')

	# cPickle.dump(matchData,fileObject)
	# fileObject.close()
	
sampleList = ['[6.79][N][10.22]Exp.txt', '[6.79][N][10.23]Exp.txt', '[6.79][N][10.24]Exp.txt', '[6.79][N][10.25]Exp.txt', '[6.79][N][10.26]Exp.txt']
matchData = []

for file in sampleList:
	fileName = file
	fileObject = open(fileName,'r')
	matchDetails = cPickle.load(fileObject)
	fileObject.close()
	matchData.extend(matchDetails)
	del matchDetails[:]
	
fileName = '[6.79][N]10.22to26]Exp.txt'
fileObject = open(fileName,'w')

cPickle.dump(matchData,fileObject)
fileObject.close()