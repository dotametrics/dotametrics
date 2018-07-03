#!/usr/bin/python

import d2slib										#winxp's script
import sys											#don't know
import cPickle										#file input and output

modheroList = "modheroList2.txt"
heroListObject = open(modheroList, 'r')
heroList = cPickle.load(heroListObject)
heroListObject.close()

# heroList.append('Terrorblade')
heroList.append('Techies')



heroList.sort()

fileName = 'modheroList2.txt'
fileObject = open(fileName,'w')

cPickle.dump(heroList,fileObject)
fileObject.close()