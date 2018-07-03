#!/usr/bin/python

import d2slib										#winxp's script
import sys											#don't know
import cPickle										#file input and output

fileName = '[6.80][4Day][Phoenix]VeryHigh.txt'
fileObject = open(fileName,'r')

matchDetails = cPickle.load(fileObject)

class playerData:
	playerWin = bool()
	
	playerBoots = 0				#item ID 29
	playerTreads = 0			#item ID 63
	playerPhase = 0				#item ID 50
	playerArcane = 0			#item ID 180
	playerTranq = 0				#item ID 214
	playerTravel = 0			#item ID 48
	
	playerBlink = 0				#item ID 1
	playerForce = 0				#item ID 102
	
	playerWand = 0				#item ID 36
	playerGhost = 0				#item ID 37
	playerBottle = 0			#item ID 41
	playerSoulring = 0			#item ID 178
	
	playerMidas = 0				#item ID 65
	
	playerPMS = 0				#item ID 71
	playerVanguard = 0			#item ID 125
	
	playerBracer = 0			#item ID 73
	playerDrum = 0				#item ID 185

	playerNull = 0				#item ID 77
	playerDagon1 = 0			#item ID 104
	playerDagon2 = 0			#item ID 201
	playerDagon3 = 0			#item ID 202
	playerDagon4 = 0			#item ID 203
	playerDagon5 = 0			#item ID 204
	
	playerNecro1 = 0			#item ID 106
	playerNecro2 = 0			#item ID 193
	playerNecro3 = 0			#item ID 194
	
	playerBasi = 0				#item ID 88
	playerVlad = 0				#item ID 81
	playerAquila = 0			#item ID 212
	playerWraith = 0			#item ID 75
	
	playerUrn = 0				#item ID 92
	playerMedallion = 0			#item ID 187
	playerMek = 0				#item ID 79
	playerPipe = 0				#item ID 90
	playerHood = 0				#item ID 131
	playerCloak = 0				#item ID 31
	
	playerSheep = 0				#item ID 96
	playerOrchid = 0			#item ID 98
	playerEuls = 0				#item ID 100
	playerRefresher = 0			#item ID 110
	playerBloodstone = 0		#item ID 121
	playerSoulboost = 0			#item ID 129
	playerVeil = 0				#item ID 190
	playerAtos = 0				#item ID 206
	
	playerAghs = 0				#item ID 108
	
	playerBKB = 0				#item ID 116
	playerAssault = 0			#item ID 112
	playerHeart = 0				#item ID 114
	playerShiva = 0				#item ID 119
	playerLinkens = 0			#item ID 123
	playerBlademail = 0			#item ID 127
	
	playerDivine = 0			#item ID 133
	playerMKB = 0				#item ID 135
	playerRadiance = 0			#item ID 137
	playerButterfly = 0			#item ID 139
	playerDaed = 0				#item ID 141
	playerCryst = 0				#item ID 149
	playerBasher = 0			#item ID 143
	playerAbyssal = 0			#item ID 208
	playerBattlefury = 0		#item ID 145
	playerManta = 0				#item ID 147
	playerYasha = 0				#item ID 170
	playerDiffusal1 = 0			#item ID 174
	playerDiffusal2 = 0			#item ID 196
	playerArmlet = 0			#item ID 151
	playerSnY = 0				#item ID 154
	playerSange = 0				#item ID 162
	playerHalberd = 0			#item ID 210
	playerSatanic = 0			#item ID 156
	playerHotD = 0				#item ID 164
	playerMoM = 0				#item ID 172
	playerMjollnir = 0			#item ID 158
	playerMaelstrom = 0			#item ID 166
	playerDesolator = 0			#item ID 168
	playerEthereal = 0			#item ID 176
	playerSkadi = 0				#item ID 160
	
	playerShadowblade = 0		#item ID 152

	
finalData = []

for match in matchDetails:
	if len(match.players) == 10:
		for player in match.players:
			if player.heroName == 'Phoenix':											#Set the Hero you're looking at here; turn this to a input variable later
				playerInfo = playerData()
				if player.win == True:
					playerInfo.playerWin = True
				else:
					playerInfo.playerWin = False
				for item in player.items:
					if item == 29:
						playerInfo.playerBoots = playerInfo.playerBoots + 1
					if item == 63:
						playerInfo.playerTreads = playerInfo.playerTreads + 1
					if item == 50:
						playerInfo.playerPhase = playerInfo.playerPhase + 1				
					if item == 180:
						playerInfo.playerArcane = playerInfo.playerArcane + 1
					if item == 214:
						playerInfo.playerTranq = playerInfo.playerTranq + 1
					if item == 48:
						playerInfo.playerTravel = playerInfo.playerTravel + 1
						
					if item == 1:
						playerInfo.playerBlink = playerInfo.playerBlink + 1
					if item == 102:
						playerInfo.playerForce = playerInfo.playerForce + 1

					if item == 36:
						playerInfo.playerWand = playerInfo.playerWand + 1
					if item == 37:
						playerInfo.playerGhost = playerInfo.playerGhost + 1
					if item == 41:
						playerInfo.playerBottle = playerInfo.playerBottle + 1
					if item == 178:
						playerInfo.playerSoulring = playerInfo.playerSoulring + 1
						
					if item == 65:
						playerInfo.playerMidas = playerInfo.playerMidas + 1
						
					if item == 71:
						playerInfo.playerPMS = playerInfo.playerPMS + 1
					if item == 125:
						playerInfo.playerVanguard = playerInfo.playerVanguard + 1
					
					if item == 73:
						playerInfo.playerBracer = playerInfo.playerBracer + 1
					if item == 185:
						playerInfo.playerDrum = playerInfo.playerDrum + 1

					if item == 77:
						playerInfo.playerNull = playerInfo.playerNull + 1
					if item == 104:
						playerInfo.playerDagon1 = playerInfo.playerDagon1 + 1
					if item == 201:
						playerInfo.playerDagon2 = playerInfo.playerDagon2 + 1
					if item == 202:
						playerInfo.playerDagon3 = playerInfo.playerDagon3 + 1
					if item == 203:
						playerInfo.playerDagon4 = playerInfo.playerDagon4 + 1				
					if item == 204:
						playerInfo.playerDagon5 = playerInfo.playerDagon5 + 1
						
					if item == 106:
						playerInfo.playerNecro1 = playerInfo.playerNecro1 + 1
					if item == 193:
						playerInfo.playerNecro2 = playerInfo.playerNecro2 + 1
					if item == 194:
						playerInfo.playerNecro3 = playerInfo.playerNecro3 + 1
						
					if item == 88:
						playerInfo.playerBasi = playerInfo.playerBasi + 1
					if item == 81:
						playerInfo.playerVlad = playerInfo.playerVlad + 1
					if item == 212:
						playerInfo.playerAquila = playerInfo.playerAquila + 1
					if item == 75:
						playerInfo.playerWraith = playerInfo.playerWraith + 1

					if item == 92:
						playerInfo.playerUrn = playerInfo.playerUrn + 1
					if item == 187:
						playerInfo.playerMedallion = playerInfo.playerMedallion + 1
					if item == 79:
						playerInfo.playerMek = playerInfo.playerMek + 1
					if item == 90:
						playerInfo.playerPipe = playerInfo.playerPipe + 1
					if item == 131:
						playerInfo.playerHood = playerInfo.playerHood + 1
					if item == 31:
						playerInfo.playerCloak = playerInfo.playerCloak + 1
						
					if item == 96:
						playerInfo.playerSheep = playerInfo.playerSheep + 1
					if item == 98:
						playerInfo.playerOrchid = playerInfo.playerOrchid + 1
					if item == 100:
						playerInfo.playerEuls = playerInfo.playerEuls + 1
					if item == 110:
						playerInfo.playerRefresher = playerInfo.playerRefresher + 1
					if item == 121:
						playerInfo.playerBloodstone = playerInfo.playerBloodstone + 1
					if item == 129:
						playerInfo.playerSoulboost = playerInfo.playerSoulboost + 1
					if item == 190:
						playerInfo.playerVeil = playerInfo.playerVeil + 1
					if item == 206:
						playerInfo.playerAtos = playerInfo.playerAtos + 1

					if item == 108:
						playerInfo.playerAghs = playerInfo.playerAghs + 1

					if item == 116:
						playerInfo.playerBKB = playerInfo.playerBKB + 1
					if item == 112:
						playerInfo.playerAssault = playerInfo.playerAssault + 1
					if item == 114:
						playerInfo.playerHeart = playerInfo.playerHeart + 1
					if item == 119:
						playerInfo.playerShiva = playerInfo.playerShiva + 1
					if item == 123:
						playerInfo.playerLinkens = playerInfo.playerLinkens + 1
					if item == 127:
						playerInfo.playerBlademail = playerInfo.playerBlademail + 1
						
					if item == 133:
						playerInfo.playerDivine = playerInfo.playerDivine + 1
					if item == 135:
						playerInfo.playerMKB = playerInfo.playerMKB + 1
					if item == 137:
						playerInfo.playerRadiance = playerInfo.playerRadiance + 1
					if item == 139:
						playerInfo.playerButterfly = playerInfo.playerButterfly + 1
					if item == 141:
						playerInfo.playerDaed = playerInfo.playerDaed + 1
					if item == 149:
						playerInfo.playerCryst = playerInfo.playerCryst + 1
					if item == 143:
						playerInfo.playerBasher = playerInfo.playerBasher + 1
					if item == 208:
						playerInfo.playerAbyssal = playerInfo.playerAbyssal + 1
					if item == 145:
						playerInfo.playerBattlefury = playerInfo.playerBattlefury + 1
					if item == 147:
						playerInfo.playerManta = playerInfo.playerManta + 1
					if item == 170:
						playerInfo.playerYasha = playerInfo.playerYasha + 1
					if item == 174:
						playerInfo.playerDiffusal1 = playerInfo.playerDiffusal1 + 1
					if item == 196:
						playerInfo.playerDiffusal2 = playerInfo.playerDiffusal2 + 1
					if item == 151:
						playerInfo.playerArmlet = playerInfo.playerArmlet + 1
					if item == 154:
						playerInfo.playerSnY = playerInfo.playerSnY + 1
					if item == 162:
						playerInfo.playerSange = playerInfo.playerSange + 1
					if item == 210:
						playerInfo.playerHalberd = playerInfo.playerHalberd + 1
					if item == 156:
						playerInfo.playerSatanic = playerInfo.playerSatanic + 1
					if item == 164:
						playerInfo.playerHotD = playerInfo.playerHotD + 1
					if item == 172:
						playerInfo.playerMoM = playerInfo.playerMoM + 1
					if item == 158:
						playerInfo.playerMjollnir = playerInfo.playerMjollnir + 1
					if item == 166:
						playerInfo.playerMaelstrom = playerInfo.playerMaelstrom + 1
					if item == 168:
						playerInfo.playerDesolator = playerInfo.playerDesolator + 1
					if item == 176:
						playerInfo.playerEthereal = playerInfo.playerEthereal + 1
					if item == 160:
						playerInfo.playerSkadi = playerInfo.playerSkadi + 1
						
					if item == 152:
						playerInfo.playerShadowblade = playerInfo.playerShadowblade + 1
							


				finalData.append(playerInfo)

print len(finalData)

BootsUse = 0
BootsWin = 0
TreadsUse = 0
TreadsWin = 0
PhaseUse = 0
PhaseWin = 0
ArcaneUse = 0
ArcaneWin = 0
TranqUse = 0
TranqWin = 0
TravelUse = 0
TravelWin = 0

BlinkUse = 0
BlinkWin = 0
ForceUse = 0
ForceWin = 0
WandUse = 0
WandWin = 0
GhostUse = 0
GhostWin = 0
BottleUse = 0
BottleWin = 0
SoulringUse = 0
SoulringWin = 0
MidasUse = 0
MidasWin = 0
PMSUse = 0
PMSWin = 0
VanguardUse = 0
VanguardWin = 0
BracerUse = 0
BracerWin = 0
DrumUse = 0
DrumWin = 0
NullUse = 0
NullWin = 0
Dagon1Use = 0
Dagon1Win = 0
Dagon2Use = 0
Dagon2Win = 0
Dagon3Use = 0
Dagon3Win = 0
Dagon4Use = 0
Dagon4Win = 0
Dagon5Use = 0
Dagon5Win = 0
Necro1Use = 0
Necro1Win = 0
Necro2Use = 0
Necro2Win = 0
Necro3Use = 0
Necro3Win = 0
BasiUse = 0
BasiWin = 0
VladUse = 0
VladWin = 0
AquilaUse = 0
AquilaWin = 0
WraithUse = 0
WraithWin = 0
UrnUse = 0
UrnWin = 0
MedallionUse = 0
MedallionWin = 0
MekUse = 0
MekWin = 0
PipeUse = 0
PipeWin = 0
HoodUse = 0
HoodWin = 0
CloakUse = 0
CloakWin = 0
SheepUse = 0
SheepWin = 0
OrchidUse = 0
OrchidWin = 0
EulsUse = 0
EulsWin = 0
RefresherUse = 0
RefresherWin = 0
BloodstoneUse = 0
BloodstoneWin = 0
SoulboostUse = 0
SoulboostWin = 0
VeilUse = 0
VeilWin = 0
AtosUse = 0
AtosWin = 0
AghsUse = 0
AghsWin = 0
BKBUse = 0
BKBWin = 0
AssaultUse = 0
AssaultWin = 0
HeartUse = 0
HeartWin = 0
ShivaUse = 0
ShivaWin = 0
LinkensUse = 0
LinkensWin = 0
BlademailUse = 0
BlademailWin = 0
DivineUse = 0
DivineWin = 0
MKBUse = 0
MKBWin = 0
RadianceUse = 0
RadianceWin = 0
ButterflyUse = 0
ButterflyWin = 0
DaedUse = 0
DaedWin = 0
CrystUse = 0
CrystWin = 0
BasherUse = 0
BasherWin = 0
AbyssalUse = 0
AbyssalWin = 0
BattlefuryUse = 0
BattlefuryWin = 0
MantaUse = 0
MantaWin = 0
YashaUse = 0
YashaWin = 0
Diffusal1Use = 0
Diffusal1Win = 0
Diffusal2Use = 0
Diffusal2Win = 0
ArmletUse = 0
ArmletWin = 0
SnYUse = 0
SnYWin = 0
SangeUse = 0
SangeWin = 0
HalberdUse = 0
HalberdWin = 0
SatanicUse = 0
SatanicWin = 0
HotDUse = 0
HotDWin = 0
MoMUse = 0
MoMWin = 0
MjollnirUse = 0
MjollnirWin = 0
MaelstromUse = 0
MaelstromWin = 0
DesolatorUse = 0
DesolatorWin = 0
EtherealUse = 0
EtherealWin = 0
SkadiUse = 0
SkadiWin = 0
ShadowbladeUse = 0
ShadowbladeWin = 0

for player in finalData:

	if player.playerBoots > 0:
		BootsUse = BootsUse + 1
		if player.playerWin == True:
			BootsWin = BootsWin + 1
	if player.playerTreads > 0:
		TreadsUse = TreadsUse + 1
		if player.playerWin == True:
			TreadsWin = TreadsWin + 1
	if player.playerPhase > 0:
		PhaseUse = PhaseUse + 1
		if player.playerWin == True:
			PhaseWin = PhaseWin + 1
	if player.playerArcane > 0:
		ArcaneUse = ArcaneUse + 1
		if player.playerWin == True:
			ArcaneWin = ArcaneWin + 1
	if player.playerTranq > 0:
		TranqUse = TranqUse + 1
		if player.playerWin == True:
			TranqWin = TranqWin + 1
	if player.playerTravel > 0:
		TravelUse = TravelUse + 1
		if player.playerWin == True:
			TravelWin = TravelWin + 1
	if player.playerBlink > 0:
		BlinkUse = BlinkUse + 1
		if player.playerWin == True:
			BlinkWin = BlinkWin + 1
	if player.playerForce > 0:
		ForceUse = ForceUse + 1
		if player.playerWin == True:
			ForceWin = ForceWin + 1
	if player.playerWand > 0:
		WandUse = WandUse + 1
		if player.playerWin == True:
			WandWin = WandWin + 1
	if player.playerGhost > 0:
		GhostUse = GhostUse + 1
		if player.playerWin == True:
			GhostWin = GhostWin + 1
	if player.playerBottle > 0:
		BottleUse = BottleUse + 1
		if player.playerWin == True:
			BottleWin = BottleWin + 1
	if player.playerSoulring > 0:
		SoulringUse = SoulringUse + 1
		if player.playerWin == True:
			SoulringWin = SoulringWin + 1
	if player.playerMidas > 0:
		MidasUse = MidasUse + 1
		if player.playerWin == True:
			MidasWin = MidasWin + 1
	if player.playerPMS > 0:
		PMSUse = PMSUse + 1
		if player.playerWin == True:
			PMSWin = PMSWin + 1
	if player.playerVanguard > 0:
		VanguardUse = VanguardUse + 1
		if player.playerWin == True:
			VanguardWin = VanguardWin + 1
	if player.playerBracer > 0:
		BracerUse = BracerUse + 1
		if player.playerWin == True:
			BracerWin = BracerWin + 1
	if player.playerDrum > 0:
		DrumUse = DrumUse + 1
		if player.playerWin == True:
			DrumWin = DrumWin + 1
	if player.playerNull > 0:
		NullUse = NullUse + 1
		if player.playerWin == True:
			NullWin = NullWin + 1
	if player.playerDagon1 > 0:
		Dagon1Use = Dagon1Use + 1
		if player.playerWin == True:
			Dagon1Win = Dagon1Win + 1
	if player.playerDagon2 > 0:
		Dagon2Use = Dagon2Use + 1
		if player.playerWin == True:
			Dagon2Win = Dagon2Win + 1
	if player.playerDagon3 > 0:
		Dagon3Use = Dagon3Use + 1
		if player.playerWin == True:
			Dagon3Win = Dagon3Win + 1
	if player.playerDagon4 > 0:
		Dagon4Use = Dagon4Use + 1
		if player.playerWin == True:
			Dagon4Win = Dagon4Win + 1
	if player.playerDagon5 > 0:
		Dagon5Use = Dagon5Use + 1
		if player.playerWin == True:
			Dagon5Win = Dagon5Win + 1
	if player.playerNecro1 > 0:
		Necro1Use = Necro1Use + 1
		if player.playerWin == True:
			Necro1Win = Necro1Win + 1
	if player.playerNecro2 > 0:
		Necro2Use = Necro2Use + 1
		if player.playerWin == True:
			Necro2Win = Necro2Win + 1
	if player.playerNecro3 > 0:
		Necro3Use = Necro3Use + 1
		if player.playerWin == True:
			Necro3Win = Necro3Win + 1
	if player.playerBasi > 0:
		BasiUse = BasiUse + 1
		if player.playerWin == True:
			BasiWin = BasiWin + 1
	if player.playerVlad > 0:
		VladUse = VladUse + 1
		if player.playerWin == True:
			VladWin = VladWin + 1
	if player.playerAquila > 0:
		AquilaUse = AquilaUse + 1
		if player.playerWin == True:
			AquilaWin = AquilaWin + 1
	if player.playerWraith > 0:
		WraithUse = WraithUse + 1
		if player.playerWin == True:
			WraithWin = WraithWin + 1
	if player.playerUrn > 0:
		UrnUse = UrnUse + 1
		if player.playerWin == True:
			UrnWin = UrnWin + 1
	if player.playerMedallion > 0:
		MedallionUse = MedallionUse + 1
		if player.playerWin == True:
			MedallionWin = MedallionWin + 1
	if player.playerMek > 0:
		MekUse = MekUse + 1
		if player.playerWin == True:
			MekWin = MekWin + 1
	if player.playerPipe > 0:
		PipeUse = PipeUse + 1
		if player.playerWin == True:
			PipeWin = PipeWin + 1
	if player.playerHood > 0:
		HoodUse = HoodUse + 1
		if player.playerWin == True:
			HoodWin = HoodWin + 1
	if player.playerCloak > 0:
		CloakUse = CloakUse + 1
		if player.playerWin == True:
			CloakWin = CloakWin + 1
	if player.playerSheep > 0:
		SheepUse = SheepUse + 1
		if player.playerWin == True:
			SheepWin = SheepWin + 1
	if player.playerOrchid > 0:
		OrchidUse = OrchidUse + 1
		if player.playerWin == True:
			OrchidWin = OrchidWin + 1
	if player.playerEuls > 0:
		EulsUse = EulsUse + 1
		if player.playerWin == True:
			EulsWin = EulsWin + 1
	if player.playerRefresher > 0:
		RefresherUse = RefresherUse + 1
		if player.playerWin == True:
			RefresherWin = RefresherWin + 1
	if player.playerBloodstone > 0:
		BloodstoneUse = BloodstoneUse + 1
		if player.playerWin == True:
			BloodstoneWin = BloodstoneWin + 1
	if player.playerSoulboost > 0:
		SoulboostUse = SoulboostUse + 1
		if player.playerWin == True:
			SoulboostWin = SoulboostWin + 1
	if player.playerVeil > 0:
		VeilUse = VeilUse + 1
		if player.playerWin == True:
			VeilWin = VeilWin + 1
	if player.playerAtos > 0:
		AtosUse = AtosUse + 1
		if player.playerWin == True:
			AtosWin = AtosWin + 1
	if player.playerAghs > 0:
		AghsUse = AghsUse + 1
		if player.playerWin == True:
			AghsWin = AghsWin + 1
	if player.playerBKB > 0:
		BKBUse = BKBUse + 1
		if player.playerWin == True:
			BKBWin = BKBWin + 1
	if player.playerAssault > 0:
		AssaultUse = AssaultUse + 1
		if player.playerWin == True:
			AssaultWin = AssaultWin + 1
	if player.playerHeart > 0:
		HeartUse = HeartUse + 1
		if player.playerWin == True:
			HeartWin = HeartWin + 1
	if player.playerShiva > 0:
		ShivaUse = ShivaUse + 1
		if player.playerWin == True:
			ShivaWin = ShivaWin + 1
	if player.playerLinkens > 0:
		LinkensUse = LinkensUse + 1
		if player.playerWin == True:
			LinkensWin = LinkensWin + 1
	if player.playerBlademail > 0:
		BlademailUse = BlademailUse + 1
		if player.playerWin == True:
			BlademailWin = BlademailWin + 1
	if player.playerDivine > 0:
		DivineUse = DivineUse + 1
		if player.playerWin == True:
			DivineWin = DivineWin + 1
	if player.playerMKB > 0:
		MKBUse = MKBUse + 1
		if player.playerWin == True:
			MKBWin = MKBWin + 1
	if player.playerRadiance > 0:
		RadianceUse = RadianceUse + 1
		if player.playerWin == True:
			RadianceWin = RadianceWin + 1
	if player.playerButterfly > 0:
		ButterflyUse = ButterflyUse + 1
		if player.playerWin == True:
			ButterflyWin = ButterflyWin + 1
	if player.playerDaed > 0:
		DaedUse = DaedUse + 1
		if player.playerWin == True:
			DaedWin = DaedWin + 1
	if player.playerCryst > 0:
		CrystUse = CrystUse + 1
		if player.playerWin == True:
			CrystWin = CrystWin + 1
	if player.playerBasher > 0:
		BasherUse = BasherUse + 1
		if player.playerWin == True:
			BasherWin = BasherWin + 1
	if player.playerAbyssal > 0:
		AbyssalUse = AbyssalUse + 1
		if player.playerWin == True:
			AbyssalWin = AbyssalWin + 1
	if player.playerBattlefury > 0:
		BattlefuryUse = BattlefuryUse + 1
		if player.playerWin == True:
			BattlefuryWin = BattlefuryWin + 1
	if player.playerManta > 0:
		MantaUse = MantaUse + 1
		if player.playerWin == True:
			MantaWin = MantaWin + 1
	if player.playerYasha > 0:
		YashaUse = YashaUse + 1
		if player.playerWin == True:
			YashaWin = YashaWin + 1
	if player.playerDiffusal1 > 0:
		Diffusal1Use = Diffusal1Use + 1
		if player.playerWin == True:
			Diffusal1Win = Diffusal1Win + 1
	if player.playerDiffusal2 > 0:
		Diffusal2Use = Diffusal2Use + 1
		if player.playerWin == True:
			Diffusal2Win = Diffusal2Win + 1
	if player.playerArmlet > 0:
		ArmletUse = ArmletUse + 1
		if player.playerWin == True:
			ArmletWin = ArmletWin + 1
	if player.playerSnY > 0:
		SnYUse = SnYUse + 1
		if player.playerWin == True:
			SnYWin = SnYWin + 1
	if player.playerSange > 0:
		SangeUse = SangeUse + 1
		if player.playerWin == True:
			SangeWin = SangeWin + 1
	if player.playerHalberd > 0:
		HalberdUse = HalberdUse + 1
		if player.playerWin == True:
			HalberdWin = HalberdWin + 1
	if player.playerSatanic > 0:
		SatanicUse = SatanicUse + 1
		if player.playerWin == True:
			SatanicWin = SatanicWin + 1
	if player.playerHotD > 0:
		HotDUse = HotDUse + 1
		if player.playerWin == True:
			HotDWin = HotDWin + 1
	if player.playerMoM > 0:
		MoMUse = MoMUse + 1
		if player.playerWin == True:
			MoMWin = MoMWin + 1
	if player.playerMjollnir > 0:
		MjollnirUse = MjollnirUse + 1
		if player.playerWin == True:
			MjollnirWin = MjollnirWin + 1
	if player.playerMaelstrom > 0:
		MaelstromUse = MaelstromUse + 1
		if player.playerWin == True:
			MaelstromWin = MaelstromWin + 1
	if player.playerDesolator > 0:
		DesolatorUse = DesolatorUse + 1
		if player.playerWin == True:
			DesolatorWin = DesolatorWin + 1
	if player.playerEthereal > 0:
		EtherealUse = EtherealUse + 1
		if player.playerWin == True:
			EtherealWin = EtherealWin + 1
	if player.playerSkadi > 0:
		SkadiUse = SkadiUse + 1
		if player.playerWin == True:
			SkadiWin = SkadiWin + 1
	if player.playerShadowblade > 0:
		ShadowbladeUse = ShadowbladeUse + 1
		if player.playerWin == True:
			ShadowbladeWin = ShadowbladeWin + 1
			
a = open('[6.80][Phoenix]VeryHighItems.txt', "w")

spacer = ','

a.write('\n')
a.write('Boots' 		+ spacer + str(BootsWin)	+ spacer +str(BootsUse))
a.write('\nTreads' 		+ spacer + str(TreadsWin)	+ spacer +str(TreadsUse))
a.write('\nPhase' 		+ spacer + str(PhaseWin)	+ spacer +str(PhaseUse))
a.write('\nArcane' 		+ spacer + str(ArcaneWin)	+ spacer +str(ArcaneUse))
a.write('\nTranq' 		+ spacer + str(TranqWin)	+ spacer +str(TranqUse))
a.write('\nTravel' 		+ spacer + str(TravelWin)	+ spacer +str(TravelUse))

a.write('\nBlink' 		+ spacer + str(BlinkWin)  + spacer +str(BlinkUse))
a.write('\nForce' 		+ spacer + str(ForceWin)  + spacer +str(ForceUse))

a.write('\nWand' 		+ spacer + str(WandWin)   + spacer +str(WandUse))
a.write('\nGhost' 		+ spacer + str(GhostWin)  + spacer +str(GhostUse))
a.write('\nBottle' 		+ spacer + str(BottleWin) + spacer +str(BottleUse))
a.write('\nSoulring' 	+ spacer + str(SoulringWin)+ spacer+str(SoulringUse))
a.write('\nMidas' 		+ spacer + str(MidasWin)  + spacer +str(MidasUse))

a.write('\nPMS' 		+ spacer + str(PMSWin)    + spacer +str(PMSUse))
a.write('\nVanguard' 	+ spacer + str(VanguardWin)+ spacer+str(VanguardUse))

a.write('\nBracer' 		+ spacer + str(BracerWin) + spacer +str(BracerUse))
a.write('\nDrum' 		+ spacer + str(DrumWin)   + spacer +		str(DrumUse))
a.write('\nNull' 		+ spacer + str(NullWin)   + spacer +		str(NullUse))
a.write('\nDagon1' 		+ spacer + str(Dagon1Win) + spacer +		str(Dagon1Use))
a.write('\nDagon2' 		+ spacer + str(Dagon2Win) + spacer +		str(Dagon2Use))
a.write('\nDagon3' 		+ spacer + str(Dagon3Win) + spacer +		str(Dagon3Use))
a.write('\nDagon4' 		+ spacer + str(Dagon4Win) + spacer +		str(Dagon4Use))
a.write('\nDagon5' 		+ spacer + str(Dagon5Win) + spacer +		str(Dagon5Use))
a.write('\nWraith' 		+ spacer + str(WraithWin) + spacer +		str(WraithUse))
a.write('\nBasi' 		+ spacer + str(BasiWin)   + spacer +		str(BasiUse))
a.write('\nAquila' 		+ spacer + str(AquilaWin) + spacer +		str(AquilaUse))

a.write('\nNecro1' 		+ spacer + str(Necro1Win) + spacer +		str(Necro1Use))
a.write('\nNecro2' 		+ spacer + str(Necro2Win) + spacer +		str(Necro2Use))
a.write('\nNecro3' 		+ spacer + str(Necro3Win) + spacer +		str(Necro3Use))

a.write('\nUrn' 		+ spacer + str(UrnWin)    + spacer +		str(UrnUse))
a.write('\nMedallion' 	+ spacer + str(MedallionWin)+ spacer +		str(MedallionUse))
a.write('\nMek' 		+ spacer + str(MekWin)    + spacer +		str(MekUse))
a.write('\nPipe' 		+ spacer + str(PipeWin)   + spacer +		str(PipeUse))
a.write('\nHood' 		+ spacer + str(HoodWin)   + spacer +		str(HoodUse))
a.write('\nCloak' 		+ spacer + str(CloakWin)  + spacer +		str(CloakUse))

a.write('\nSheep' 		+ spacer + str(SheepWin)  + spacer +		str(SheepUse))
a.write('\nOrchid' 		+ spacer + str(OrchidWin) + spacer +		str(OrchidUse))
a.write('\nEuls' 		+ spacer + str(EulsWin)   + spacer +		str(EulsUse))
a.write('\nAtos' 		+ spacer + str(AtosWin)   + spacer +		str(AtosUse))

a.write('\nRefresher' 	+ spacer + str(RefresherWin)+ spacer +		str(RefresherUse))
a.write('\nBloodstone' 	+ spacer + str(BloodstoneWin)+ spacer +		str(BloodstoneUse))
a.write('\nSoulboost' 	+ spacer + str(SoulboostWin)+ spacer +		str(SoulboostUse))
a.write('\nVeil' 		+ spacer + str(VeilWin)   + spacer +		str(VeilUse))
a.write('\nAghs' 		+ spacer + str(AghsWin)   + spacer +		str(AghsUse))

a.write('\nBKB' 		+ spacer + str(BKBWin)    + spacer +		str(BKBUse))
a.write('\nAssault' 	+ spacer + str(AssaultWin)+ spacer +		str(AssaultUse))
a.write('\nHeart' 		+ spacer + str(HeartWin)  + spacer +		str(HeartUse))
a.write('\nShiva' 		+ spacer + str(ShivaWin)  + spacer +		str(ShivaUse))
a.write('\nLinkens' 	+ spacer + str(LinkensWin)+ spacer +		str(LinkensUse))
a.write('\nBlademail' 	+ spacer + str(BlademailWin)+ spacer +		str(BlademailUse))

a.write('\nArmlet' 		+ spacer + str(ArmletWin) + spacer +		str(ArmletUse))
a.write('\nMKB' 		+ spacer + str(MKBWin)    + spacer +		str(MKBUse))
a.write('\nRadiance' 	+ spacer + str(RadianceWin)+ spacer +		str(RadianceUse))
a.write('\nButterfly' 	+ spacer + str(ButterflyWin)+ spacer +		str(ButterflyUse))
a.write('\nDaed' 		+ spacer + str(DaedWin)   + spacer +		str(DaedUse))
a.write('\nCryst' 		+ spacer + str(CrystWin)  + spacer +		str(CrystUse))
a.write('\nBasher' 		+ spacer + str(BasherWin) + spacer +		str(BasherUse))
a.write('\nAbyssal' 	+ spacer + str(AbyssalWin)+ spacer +		str(AbyssalUse))
a.write('\nBattlefury' 	+ spacer + str(BattlefuryWin)+ spacer +		str(BattlefuryUse))

a.write('\nManta' 		+ spacer + str(MantaWin)  + spacer +		str(MantaUse))
a.write('\nYasha' 		+ spacer + str(YashaWin)  + spacer +		str(YashaUse))
a.write('\nSnY' 		+ spacer + str(SnYWin)    + spacer +		str(SnYUse))
a.write('\nSange' 		+ spacer + str(SangeWin)  + spacer +		str(SangeUse))
a.write('\nHalberd' 	+ spacer + str(HalberdWin)+ spacer +		str(HalberdUse))

a.write('\nSatanic' 	+ spacer + str(SatanicWin)+ spacer +		str(SatanicUse))
a.write('\nHotD' 		+ spacer + str(HotDWin)   + spacer +		str(HotDUse))
a.write('\nMoM' 		+ spacer + str(MoMWin)    + spacer +		str(MoMUse))
a.write('\nVlad' 		+ spacer + str(VladWin)   + spacer +		str(VladUse))

a.write('\nDiffusal1' 	+ spacer + str(Diffusal1Win)+ spacer +		str(Diffusal1Use))
a.write('\nDiffusal2' 	+ spacer + str(Diffusal2Win)+ spacer +		str(Diffusal2Use))
a.write('\nMjollnir' 	+ spacer + str(MjollnirWin)+ spacer +		str(MjollnirUse))
a.write('\nMaelstrom' 	+ spacer + str(MaelstromWin)+ spacer +		str(MaelstromUse))
a.write('\nDesolator' 	+ spacer + str(DesolatorWin)+ spacer +		str(DesolatorUse))
a.write('\nEthereal' 	+ spacer + str(EtherealWin)+ spacer +		str(EtherealUse))
a.write('\nSkadi' 		+ spacer + str(SkadiWin)  + spacer +		str(SkadiUse))
a.write('\nShadowblade' + spacer + str(ShadowbladeWin)+ spacer +		str(ShadowbladeUse))
a.write('\nDivine' 		+ spacer + str(DivineWin) + spacer +		str(DivineUse))