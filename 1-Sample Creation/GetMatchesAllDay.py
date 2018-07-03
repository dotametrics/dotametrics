#!/usr/bin/python

import d2slib													#winxp's script
import sys														
import cPickle													#file input and output
import collections												#checks for duplicates
import time

fileName = "[6.84][VH][4.30]Sample.txt"									
fileObject = open(fileName,'w')

# fileName = "[6.84][VH][4.30]Sample.txt"									
# fileObj = open(fileName,'w')	

start_time = time.time()

# normal = []
# high = []
vhigh = []

it = 'Iteration: '


for i in range (1,32):
	# for x in range(1,4):
		# bracket = x
		# matches = d2slib.getMatches(skill=bracket)
		# if bracket == 1:
			# normal.extend(matches)
		# elif bracket == 2:
			# high.extend(matches)
		# elif bracket == 3:
			# vhigh.extend(matches)
	for j in range(1,113):
		print it + `i` + ', hero: ' + `j`
		if j == 24 or j == 108:
			pass
		else:	
			for b in range(3,4):	
				for x in range(0,5):
					complete = False
					exceptioncounter = 0
					while complete == False:
						try:
							if x == 0:
								matches = d2slib.getMatches(hero=j, skill=b)
								if b == 2:
									high.extend(matches)
									high = sorted(set(high))
									hStart = int(matches[-1]) - 1
								if b == 3:
									vhigh.extend(matches)
									vhigh = sorted(set(vhigh))
									vStart = int(matches[-1]) - 1
								complete = True
							else:
								if b == 2:
									matches = d2slib.getMatches(hero=j, skill=b, startID=hStart)
									high.extend(matches)
									high = sorted(set(high))
									hStart = int(matches[-1]) - 1
								if b == 3:
									matches = d2slib.getMatches(hero=j, skill=b, startID=vStart)
									vhigh.extend(matches)
									vhigh = sorted(set(vhigh))
									vStart = int(matches[-1]) - 1
								complete = True
						except:
							print "API unavailable"
							time.sleep(20)								
							exceptioncounter = exceptioncounter + 1
							if exceptioncounter > 30:
								elapsed_time = time.time() - start_time
								print float(elapsed_time)/60
								# print len(high)
								print len(vhigh)
								# high = sorted(set(high))
								vhigh = sorted(set(vhigh))
								# print len(high)
								print len(vhigh)
								# cPickle.dump(high,fileObj)
								cPickle.dump(vhigh,fileObject)
								# fileObj.close()
								fileObject.close()
								sys.exit()															#?m per iteration
	
elapsed_time = time.time() - start_time

print float(elapsed_time)/60

# print len(normal)
# print len(high)
print len(vhigh)

# y = collections.Counter(normal)														#Checks for duplicates, somehow, was on internet must be true
# print [i for i in y if y[i]>1]
# y = collections.Counter(high)														#Checks for duplicates, somehow, was on internet must be true
# print [i for i in y if y[i]>1]
# y = collections.Counter(vhigh)														#Checks for duplicates, somehow, was on internet must be true
# print [i for i in y if y[i]>1]

# normal = sorted(set(normal))
# high = sorted(set(high))
vhigh = sorted(set(vhigh))

# print len(normal)
# print len(high)
print len(vhigh)

# cPickle.dump(high,fileObj)
cPickle.dump(vhigh,fileObject)

# fileObj.close()
fileObject.close()