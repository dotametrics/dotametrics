#!/usr/bin/python

# Copyright 2012 Matt Ventura

# Requites minidom and urllib2
import xml.dom.minidom as minidom
import urllib2
import cPickle
import time

global lastRequestTime

lastRequestTime = time.time()


global heroList

try:
	heroListFile = open("heroList2", "rb")
	heroList = cPickle.load(heroListFile)
	heroListFile.close()
except:
	print "There was a problem reading the hero list. \nAre you sure you ran generateHeroList.py?"


# Put your steam API key here
global apiKey
apiKey = ""

# Function used to convert a single slot number to
# a team and team position. Returns (team, position)
# Position is 0-4, team is true=radiant, false=dire. 
def getSlotInfo(playerSlot):
	if (playerSlot > 127):
		team = False
	else:
		team = True
	slot = playerSlot%128
	return((team, slot))
	
def waitForRequest():
	global lastRequestTime
	curTime = time.time()
	#print str(lastRequestTime)+" "+str(curTime)
	if (lastRequestTime + 1 > curTime):
		sleepTime = lastRequestTime + 1 - curTime
		#print sleepTime
		time.sleep(sleepTime)
	lastRequestTime = time.time()
	return()

# Class for a player within a match
class matchPlayer:
	accID = int()
	playerName = str()
	playerSlot = int()
	team = bool()
	slot = int()
	hero = int()
	items = []
	skills = []																#comment out when parsing matches before Feb 2013
	kills = int()
	deaths = int()
	assists = int()
	leaverStatus = int()
	endingGold = int()
	cs = int()
	denies = int()
	gpm = int()
	xpm = int()
	goldSpent = int()
	heroDmg = int()
	towerDmg = int()
	heroHeal = int()
	level = int()
	heroName = int()
	win = bool()															#I added this to easily determine whether each player entry won or lost their game
	# team = str()						#mine for International, comment outside of Int

# Class for an individual match
class matchDetails:
	winner = bool()
	players = []
	# season = int()					#Disabled for NA vs Europe tests; missing in 194109804
	duration = int()
	startTime = int()
	matchID = int()
	towersR = int()
	towersD = int()
	raxR = int()
	raxD = int()
	cluster = int()
	fbTime = int()
	replaySalt = int()
	lobbyType = int()
	humanPlayers = int()
	league = int()
	mode = int()
	# radiantTeam = str()					#mine for International, comment outside of Int
	# direTeam = str()					#mine for International, comment outside of Int
	# posVotes = int()					#mine for International, comment outside of Int
	# negVotes = int()					#mine for International, comment outside of Int


def getHeroName(heroID):
	return heroList[int(heroID)-1]

# Get the last 25 matches played by playerID. Returns a list of match IDs. 
def getMatches(**args):

	urlBase = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?"
	argString = "format=XML&key=%s" % apiKey

	if "playerID" in args:
		argString = argString + "&account_ID=" + str(args['playerID'])

	if "skill" in args:
		argString = argString + "&skill=" + str(args['skill'])

	if "hero" in args: 
		argString = argString + "&hero_id=" + str(args['hero'])

	if "dateMin" in args: 
		argString = argString + "&date_min=" + str(args['dateMin'])
	
	if "dateMax" in args: 
		argString = argString + "&date_max=" + str(args['dateMax'])

	if "league" in args: 
		argString = argString + "&league_id=" + str(args['league'])
	
	if "startID" in args: 
		argString = argString + "&start_at_match_id=" + str(args['startID'])
	
	if "numReq" in args:
		argString = argString + "&matches_requested=" + str(args['numReq'])

	waitForRequest()
	# print urlBase+argString														#I added this to check that the url modifications are correct
	hfile = urllib2.urlopen(urlBase + argString )
	hdata=hfile.read()
	hfile.close()

	hdom = minidom.parseString(hdata)

	matchIDs = []
	
	for match in hdom.getElementsByTagName('match'):
		matchID = match.getElementsByTagName('match_id')[0].firstChild.data
		lobby = match.getElementsByTagName('lobby_type')[0].firstChild.data
		if lobby == '0' or lobby == '7' or lobby == '8':										#flushes anything not public matchmaking  ###MODIFIED FOR WRAITH NIGHT, RETURN TO 0 FOR REGULAR USE###
			matchIDs.append(matchID)											#PS ###7 IS NOW RANKED MATCHMAKING###

	return matchIDs


def findMatchSkillLevel(matchID):
	matchData = parseMatch(getMatchDetails(matchID))
	playerOne = matchData.players[0].accID
	normalMatches = getMatches(playerID = playerOne, startID = matchID, skill = 1)
	highMatches = getMatches(playerID = playerOne, startID = matchID, skill = 2)
	veryHighMatches = getMatches(playerID = playerOne, startID = matchID, skill = 3)

	if int(matchID)==int(normalMatches[0]):
		return 1
	elif int(matchID)==int(highMatches[0]):
		return 2
	elif int(matchID)==int(veryHighMatches[0]):
		return 3
	else:
		return 0

# Download the data for an individual match
def getMatchDetails(matchID):

	waitForRequest()
	hfile = urllib2.urlopen('https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?key=%s&match_id=%s&format=XML' % (apiKey, matchID))
	hdata = hfile.read()
	hfile.close()

	hdom = minidom.parseString(hdata)
	# print matchID																		#I added this to check that the url modifications are correct

	return hdom

# Parse the data for an individual match. You can feed the output of 
# getMatchDetails() directly into this function. 
def parseMatch(matchData):
	matchResults = matchDetails()
	
	
	#Convert winner to a boolean
	winnerData = matchData.getElementsByTagName('radiant_win')[0].firstChild.data
	if (winnerData == "false"):
		matchResults.winner = False
	else:
		matchResults.winner = True

	# General match data
	# matchResults.season = int(matchData.getElementsByTagName('season')[0].firstChild.data)		#Disabled for NA vs Europe tests; missing in 194109804
	matchResults.duration = int(matchData.getElementsByTagName('duration')[0].firstChild.data)
	matchResults.startTime = int(matchData.getElementsByTagName('start_time')[0].firstChild.data)
	matchResults.matchID = int(matchData.getElementsByTagName('match_id')[0].firstChild.data)
	matchResults.towersR = int(matchData.getElementsByTagName('tower_status_radiant')[0].firstChild.data)
	matchResults.towersD = int(matchData.getElementsByTagName('tower_status_dire')[0].firstChild.data)
	matchResults.raxR = int(matchData.getElementsByTagName('barracks_status_radiant')[0].firstChild.data)
	matchResults.raxD = int(matchData.getElementsByTagName('barracks_status_dire')[0].firstChild.data)
	matchResults.cluster = int(matchData.getElementsByTagName('cluster')[0].firstChild.data)
	matchResults.fbTime = int(matchData.getElementsByTagName('first_blood_time')[0].firstChild.data)
	# matchResults.replaySalt = int(matchData.getElementsByTagName('replay_salt')[0].firstChild.data)	#Currently Disabled in API
	matchResults.lobbyType = int(matchData.getElementsByTagName('lobby_type')[0].firstChild.data)
	matchResults.humanPlayers = int(matchData.getElementsByTagName('human_players')[0].firstChild.data)
	matchResults.league = int(matchData.getElementsByTagName('leagueid')[0].firstChild.data)
	matchResults.mode = int(matchData.getElementsByTagName('game_mode')[0].firstChild.data)
	
	# matchResults.radiantTeam = str(matchData.getElementsByTagName('radiant_name')[0].firstChild.data)	#mine for International, comment outside of Int
	# matchResults.direTeam = str(matchData.getElementsByTagName('dire_name')[0].firstChild.data)			#mine for International, comment outside of Int
	
	# matchResults.posVotes = str(matchData.getElementsByTagName('positive_votes')[0].firstChild.data)	#mine for International, comment outside of Int
	# matchResults.negVotes = str(matchData.getElementsByTagName('negative_votes')[0].firstChild.data)	#mine for International, comment outside of Int

	matchResults.players = []
	# Data regarding each player in a match
	for playerData in matchData.getElementsByTagName('player'):
		newPlayer = matchPlayer()
		newPlayer.accID = int(playerData.getElementsByTagName('account_id')[0].firstChild.data)
		# newPlayer.playerName = playerData.getElementsByTagName('player_name')[0].firstChild.data
		newPlayer.hero = playerData.getElementsByTagName('hero_id')[0].firstChild.data
		newPlayer.heroName = getHeroName(newPlayer.hero)
		

		newPlayer.playerSlot = int(playerData.getElementsByTagName('player_slot')[0].firstChild.data)
		slotData = getSlotInfo(newPlayer.playerSlot)
		newPlayer.team = slotData[0]
		newPlayer.slot = slotData[1]

		
		newPlayer.kills = int(playerData.getElementsByTagName('kills')[0].firstChild.data)
		newPlayer.deaths = int(playerData.getElementsByTagName('deaths')[0].firstChild.data)
		newPlayer.assists = int(playerData.getElementsByTagName('assists')[0].firstChild.data)
		
		newPlayer.endingGold = int(playerData.getElementsByTagName('gold')[0].firstChild.data)
		newPlayer.goldSpent = int(playerData.getElementsByTagName('gold_spent')[0].firstChild.data)
		newPlayer.cs = int(playerData.getElementsByTagName('last_hits')[0].firstChild.data)
		newPlayer.denies = int(playerData.getElementsByTagName('denies')[0].firstChild.data)
		newPlayer.gpm = int(playerData.getElementsByTagName('gold_per_min')[0].firstChild.data)
		newPlayer.xpm = int(playerData.getElementsByTagName('xp_per_min')[0].firstChild.data)
		newPlayer.level = int(playerData.getElementsByTagName('level')[0].firstChild.data)


		newPlayer.heroDmg = int(playerData.getElementsByTagName('hero_damage')[0].firstChild.data)
		newPlayer.towerDamage = int(playerData.getElementsByTagName('tower_damage')[0].firstChild.data)
		newPlayer.heroHeal = int(playerData.getElementsByTagName('hero_healing')[0].firstChild.data)
		
		newPlayer.leaverStatus = int(playerData.getElementsByTagName('leaver_status')[0].firstChild.data)
		
		if newPlayer.team == matchResults.winner:						#newPlayer.team should return True for Radiant, and matchResults.winner should return True for a radiant win
			newPlayer.win = True										#if the values are identical then the player is set as having won the game
		else:
			newPlayer.win = False

		# Player items
		newPlayer.items = []
		for itemNum in range(0,6):
			curItem = int(playerData.getElementsByTagName('item_%s' % itemNum)[0].firstChild.data)
			newPlayer.items.append(curItem)
			
		# testing for Ability System
		newPlayer.skills = []
		
		abilities = playerData.getElementsByTagName('ability')
		
		for ability in abilities:
			try:
				curAbility = int(ability.getElementsByTagName('ability')[0].firstChild.data)
				newPlayer.skills.append(curAbility)
			except:
				pass
		
		matchResults.players.append(newPlayer)
		
		# if newPlayer.team == True:							#mine for International, comment outside of Int
			# newPlayer.team = matchResults.radiantTeam
		# else:
			# newPlayer.team = matchResults.direTeam
	




	return matchResults

