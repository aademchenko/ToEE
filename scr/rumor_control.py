
# this function returns the message line (0, 10, 20, etc) of a
# rumor to be told to the PC in question, or -1 if no rumor is
# available

def find_rumor( pc, npc ):
	sk_mod = pc.skill_level_get(npc, skill_gather_information) + pc.stat_level_get(stat_level_bard)
	if (( game.story_state != game.global_vars[22] ) and ( game.story_state <= 6 )):
		game.global_vars[22] = game.story_state
		game.global_flags[211] = 0
		game.global_flags[212] = 0
		game.global_flags[213] = 0
		game.global_flags[214] = 0
		game.global_flags[215] = 0
		game.global_flags[216] = 0
		game.global_flags[217] = 0
		game.global_flags[218] = 0
		game.global_flags[219] = 0
		game.global_flags[220] = 0
		game.global_flags[221] = 0
		game.global_flags[222] = 0
		game.global_flags[223] = 0
		game.global_flags[224] = 0
		game.global_flags[225] = 0
		game.global_flags[226] = 0
		game.global_flags[209] = 0
		game.global_flags[210] = 0
	if game.story_state == 0:
		if sk_mod == 5:
			sk_mod = 4
		elif sk_mod >= 6:
			sk_mod = 5
	elif game.story_state == 1:
		if (sk_mod == 2):
			sk_mod = 1
		elif (sk_mod == 3) or (sk_mod == 4):
			sk_mod = 2
		elif (sk_mod == 5):
			sk_mod = 3
		elif (sk_mod == 6) or (sk_mod == 7):
			sk_mod = 4
		elif (sk_mod >= 8):
			sk_mod = 5
	elif game.story_state == 2:
		if (sk_mod == 2) or (sk_mod == 3):
			sk_mod = 1
		elif (sk_mod == 4) or (sk_mod == 5):
			sk_mod = 2
		elif (sk_mod == 6):
			sk_mod = 3
		elif (sk_mod == 7) or (sk_mod == 8):
			sk_mod = 4
		elif (sk_mod >= 9):
			sk_mod = 5	
	elif game.story_state == 3:
		if (sk_mod >= 1) and (sk_mod <= 4):
			sk_mod = 1
		elif (sk_mod == 5) or (sk_mod == 6):
			sk_mod = 2
		elif (sk_mod == 7):
			sk_mod = 3
		elif (sk_mod == 8) or (sk_mod == 9):
			sk_mod = 4
		elif (sk_mod >= 10):
			sk_mod = 5	
	elif game.story_state == 4:
		if (sk_mod >= 1) and (sk_mod <= 5):
			sk_mod = 1
		elif (sk_mod == 6):
			sk_mod = 2
		elif (sk_mod == 7):
			sk_mod = 3
		elif (sk_mod >= 8) and (sk_mod <= 10):
			sk_mod = 4
		elif (sk_mod >= 11):
			sk_mod = 5	
	elif game.story_state == 5:
		if (sk_mod >= 1) and (sk_mod <= 5):
			sk_mod = 1
		elif (sk_mod == 6) or (sk_mod == 7):
			sk_mod = 2
		elif (sk_mod == 8) or (sk_mod == 9):
			sk_mod = 3
		elif (sk_mod >= 10) and (sk_mod <= 12):
			sk_mod = 4
		elif (sk_mod >= 13):
			sk_mod = 5	
	elif game.story_state >= 6:
		if (sk_mod >= 1) and (sk_mod <= 5):
			sk_mod = 1
		elif (sk_mod >= 6) and (sk_mod <= 10):
			sk_mod = 2
		elif (sk_mod >= 11) and (sk_mod <= 14):
			sk_mod = 3
		elif (sk_mod >= 15) and (sk_mod <= 17):
			sk_mod = 4
		elif (sk_mod >= 18):
			sk_mod = 5		
	ss_num = (game.story_state) * 200
	sk_num = (sk_mod * 30) + 20
	while ( sk_num >= 0 ):
		rumor = ss_num + sk_num
		if rumor_valid( rumor, pc, npc ) == 1:
			return rumor
		else:
			sk_num = ( sk_num - 10 )
	return -1

def rumor_valid( rumor, pc, npc ):
	offset = (game.story_state) * 200
	sk_lookup = ( (rumor - offset)/10 )
	if game.global_flags[209+sk_lookup] == 1:
		return 0
	if (npc.map == 5007):
		if ((rumor == 120) or (rumor == 130) or (rumor == 520) or (rumor == 530)):
			return 0
	elif ((rumor == 150) or (rumor == 330) or (rumor == 510) or (rumor == 540) or (rumor == 560)):
		return 0
	if ((game.party_alignment == CHAOTIC_EVIL or game.party_alignment == NEUTRAL_EVIL) and (rumor == 550 or rumor == 630)):
		return 0
	if (game.quests[12].state == qs_completed and rumor == 40):
		return 0
	if ( pc.stat_level_get(stat_race) != race_human ) and (rumor == 800):
		return 0
	if ((rumor >= 590 and rumor <= 680) or (rumor >=800 and rumor <= 830) and (npc.area == 1)):
		return 1
	if ((rumor == 860 or rumor == 890 or rumor == 900 or rumor == 1030 or rumor == 1060 or rumor == 1090 or rumor == 1230 or rumor == 1260 or rumor == 1290) and (npc.area == 1 or npc.area == 3)):
		return 1
	if ( rumor >= 690 and npc.area == 1 ):
		return 0
	if (rumor >= 800 and npc.area == 3 ):
		return 0
	return 1

def rumor_given_out( rumor ):
	offset = (game.story_state) * 200
	sk_lookup = ( (rumor - offset)/10 )
	game.global_flags[209+sk_lookup] = 1
	return


	