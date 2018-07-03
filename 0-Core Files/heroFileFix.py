#!/usr/bin/python

import sys											
import cPickle										#file input and output


# heroListFile = open("heroList", "rb")
# heroList = cPickle.load(heroListFile)
# heroListFile.close()

# heroList.append('Medusa')
# heroList.append('Troll Warlord')
# heroList.append('Centaur Warrunner')
# heroList.append('Magnus')
# heroList.append('Timbersaw')

# fileName = "heroList2"									
# fileObject = open(fileName,'wb')	

# cPickle.dump(heroList,fileObject)

heroListFile = open("heroList2", "rb")
heroList = cPickle.load(heroListFile)
heroListFile.close()

print len(heroList)

for hero in heroList:
	print hero

# print heroList[105]

# heroList[107] = ''
# heroList[108] = 'Terrorblade'
# heroList[104] = 'Techies'

# for x in heroList:
	# print x


# heroList.append('')
# heroList.append('Terrorblade')
# heroList.append('Phoenix')
# heroList.append('Oracle')
# heroList.append('Winter Wyvern')

# counter = 1

# for x in heroList:
	# print counter
	# print x
	# counter = counter + 1


# for hero in heroList:
	# print hero
	
# heroList.append("Skywrath Mage")
# heroList.append("Placeholder")
# heroList.append("Elder Titan")
# print len(heroList)

# fileName = "heroList2"									
# fileObject = open(fileName,'wb')	

# cPickle.dump(heroList,fileObject)