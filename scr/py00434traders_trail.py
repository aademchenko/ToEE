from toee import *
from utilities import *
from council import *
from py00439script_daemon import record_time_stamp, get_v, set_v, npc_set, npc_unset, npc_get, tsc, within_rect_by_corners
from combat_standard_routines import *


# pad_i_3 bit flags:

def san_dialog( attachee, triggerer ):
	if (attachee.map == 5001):
		attachee.turn_towards(triggerer)
		a = trail_check()
		if (a == 1):
			triggerer.begin_dialog(attachee,1)
		elif (a == 2):
			triggerer.begin_dialog(attachee,100)
		elif (a == 3):
			triggerer.begin_dialog(attachee,200)
		elif (a == 50):
			triggerer.begin_dialog(attachee,500)
		elif (a == 60):
			triggerer.begin_dialog(attachee,600)
		elif (a == 65):
			triggerer.begin_dialog(attachee,650)
		else:
			triggerer.begin_dialog(attachee,700)
	if (attachee.map == 5051):
	#tracked them to Nulb
		triggerer.begin_dialog( attachee, 2000 )
	return SKIP_DEFAULT

def san_first_heartbeat(attachee, triggerer):
	if (attachee.map == 5049):
	#stonemason
		a = attachee.obj_get_int(obj_f_npc_pad_i_5)
		if (get_v(435) == 5 and get_v(436) != 5 and get_v(436) != 8):
			for npc in game.obj_list_vicinity(attachee.location, OLC_NPC):
				if ( (npc.name == 14801 or npc.name == 14039) and npc.leader_get() == OBJ_HANDLE_NULL):
					npc.destroy()
		elif (get_v(435) == 4 and a == 0):
			attachee.obj_set_int( obj_f_npc_pad_i_5, 1 )
			for npc in game.obj_list_vicinity(attachee.location, OLC_NPC):
				if npc.name == 14039:
					gister = npc
			bad1 = game.obj_create(14801,location_from_axis(471,485))
			bad1.move(location_from_axis(471,485),0.0,0.0)
			bad1.rotation = 4
			bad2 = game.obj_create(14801,location_from_axis(474,481))
			bad2.move(location_from_axis(474,481),0.0,0.0)
			bad2.rotation = 3.5
			bad3 = game.obj_create(14801,location_from_axis(473,483))
			bad3.move(location_from_axis(473,483),7.0,0.0)
			bad3.rotation = 3.9
			heavily_damage(gister)
			game.timevent_add(proactivity, (bad3, 400), 200)

	elif attachee.map == 5009:
	#traders' barn
		ggv435 = get_v(435)
		game.particles('sp-Bless Water', attachee)
		council_heartbeat()
		a = attachee.obj_get_int(obj_f_npc_pad_i_3)
		if (ggv435 >= 3 or (ggv435 == 2 and council_time() == 3)) and a & 1 == 0:
			a = a | 1
			npc_set(attachee, 1)
			courier = find_npc_near(attachee, 14063)
			courier.destroy()
			if game.quests[17].state == qs_mentioned or game.quests[17].state == qs_accepted:
				game.quests[17].state = qs_botched
		if a & 2 == 0 and (game.global_flags[438] == 1) and not (game.global_flags[814] == 1 and game.global_flags[815] == 1):
			a = a | 2
			npc_set(attachee,2)
			badger = game.obj_create( 14371 , location_from_axis(493, 487))
			for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
				if (obj.distance_to(badger) <= 25 and critter_is_unconscious(obj) != 1):
					pc = obj
			pc.begin_dialog( badger, 5000 )	
	elif attachee.map == 5051 and get_v(437) == 100:
	#Nulb exterior
		game.particles('sp-Bless Water', attachee)
		for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
			if (obj.distance_to(attachee) <= 25 and critter_is_unconscious(obj) != 1):
				game.new_sid = 0
				obj.begin_dialog( attachee, 2000 )
	elif attachee.map == 5007:
	#Inn, first floor
		ggv435 = get_v(435)
		c = attachee.obj_get_int(obj_f_npc_pad_i_3)
		#c & 1 - spawned mickey
		#c & 2 - Glora, the new innkeeper
		#c & 4 - switched gundigoot off
		#c & 8 - destroyed gundigoot
		#c & 16 - switched Turuko off (since you killed him)
		#c & 32 - switched Kobort off (since you killed him)
		game.particles('sp-Bless Water', attachee)
		c_time = council_time()
		council_heartbeat()
		if game.global_flags[45] == 1 and c & 16 == 0:
			c = c | 16
			npc_set(attachee,5)
			turuko = find_npc_near(attachee, 8004)
			if turuko != OBJ_HANDLE_NULL:
				turuko.destroy()
		if game.global_flags[44] == 1 and c & 32 == 0:
			c = c | 32
			npc_set(attachee,6)
			kobort = find_npc_near(attachee, 8005)
			if kobort != OBJ_HANDLE_NULL:
				kobort.destroy()
				game.particles('orb-summon-water-elemental', game.party[1])
		if c & 1 == 0:
			c = c | 1
			npc_set(attachee,1)
			mecr = game.obj_create( 14637, location_from_axis (475L, 475L) )
			mecr.rotation = 2.5
			mecr.object_flag_set(OF_OFF)
		if c & 2 == 0 and (game.global_vars[436] == 6 or game.global_vars[436] == 7):
			c = c | 2
			npc_set(attachee,2)
			glora = find_npc_near(attachee, 14100)
			if glora != OBJ_HANDLE_NULL:
				glora.standpoint_set( STANDPOINT_DAY, 340 )
				glora.standpoint_set( STANDPOINT_NIGHT, 340 )
				glora.rotation = 5.0
		if (c_time == 1 or c_time == 2 or c_time == 5) and (c & 4 == 0 or find_npc_near(attachee, 8008) != OBJ_HANDLE_NULL) and c & 8 == 0:
			c = c | 4
			npc_set(attachee,3)
			gundi = find_npc_near(attachee, 8008)
			if game.global_vars[436] == 6 or game.global_vars[436] == 7:
				gundi.destroy()
				c = c | 8
				npc_set(attachee,4)
			else:
				#gundi.move(location_from_axis(476,445),0.0,0.0)
				gundi.scripts[10] = 73
				gundi.scripts[19] = 73
				gundi.object_flag_set( OF_OFF )
		elif c & 4 == 4 and c & 8 == 0 and c_time != 1 and c_time != 2 and c_time != 5:
			gundi = find_npc_near(attachee, 8008)
			if (game.global_vars[436] == 6 or game.global_vars[436] == 7) and gundi != OBJ_HANDLE_NULL:
				gundi.destroy()
				c = c | 8
				c = c - 4
				attachee.obj_set_int( obj_f_npc_pad_i_3, c )
			elif gundi != OBJ_HANDLE_NULL:
				gundi.scripts[10] = 0
				gundi.scripts[19] = 0
	elif attachee.map == 5063:
	#The Renton Residence (village militia captain)
		game.particles('orb-summon-water-elemental',attachee)
		c_time = council_time()
		council_heartbeat()
		if (c_time == 1 or c_time == 2 or c_time == 5) and find_npc_near(attachee, 20007) != OBJ_HANDLE_NULL:
			renton = find_npc_near(attachee, 20007)
			renton.scripts[10] = 6
			renton.scripts[19] = 6
			renton.object_flag_set( OF_OFF )
	return SKIP_DEFAULT


def san_heartbeat(attachee, triggerer):
	c = attachee.obj_get_int(obj_f_npc_pad_i_3)
	if attachee.map == 5001:
	#Hommlet exterior
		game.particles('sp-Bless Water', attachee)
		if c & 1 == 0 and game.global_vars[435] == 4:
			for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
				if (obj.distance_to(attachee) <= 25 and critter_is_unconscious(obj) != 1):
					c = c | 1
					attachee.obj_set_int(obj_f_npc_pad_i_3, c)
					a = trail_check()
					game.global_vars[437] = a
					if (a == 1):
						obj.begin_dialog(attachee,1)
					elif (a == 2):
						obj.begin_dialog(attachee,100)
					elif (a == 3):
						obj.begin_dialog(attachee,200)
					elif (a == 50):
						obj.begin_dialog(attachee,500)
					elif (a == 60):
						obj.begin_dialog(attachee,600)
					elif (a == 65):
						obj.begin_dialog(attachee,650)
					else:
						obj.begin_dialog(attachee,700)
		elif c & 2 == 2:
			c = c - 2
			attachee.obj_set_int(obj_f_npc_pad_i_3, c)
			for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
				if (obj.distance_to(attachee) <= 25 and critter_is_unconscious(obj) != 1):
					obj.begin_dialog(attachee,710)
		elif c & 4 == 4:
			c = c - 4
			attachee.obj_set_int(obj_f_npc_pad_i_3, c)
			for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
				if (obj.distance_to(attachee) <= 25 and critter_is_unconscious(obj) != 1):
					obj.begin_dialog(attachee,620)
	elif attachee.map == 5007:
	#Inn, first floor
		#c & 1 - spawned mickey
		#c & 2 - Glora, the new innkeeper
		#c & 4 - switched gundigoot off
		game.particles('sp-Bless Water', attachee)
		c_time = council_time()
		council_heartbeat()
		if c & 2 == 0 and (game.global_vars[436] == 6 or game.global_vars[436] == 7):
			c = c | 2
			attachee.obj_set_int( obj_f_npc_pad_i_3, c )
			glora = find_npc_near(attachee, 14100)
			if glora != OBJ_HANDLE_NULL:
				glora.standpoint_set( STANDPOINT_DAY, 340 )
				glora.standpoint_set( STANDPOINT_NIGHT, 340 )
				glora.rotation = 5.0
		elif (c_time == 1 or c_time == 2 or c_time == 5) and (c & 4 == 0 or find_npc_near(attachee, 8008) != OBJ_HANDLE_NULL) and c & 8 == 0:
			c = c | 4
			attachee.obj_set_int( obj_f_npc_pad_i_3, c )
			gundi = find_npc_near(attachee, 8008)
			if game.global_vars[436] == 6 or game.global_vars[436] == 7:
				gundi.destroy()
				c = c | 8
				attachee.obj_set_int( obj_f_npc_pad_i_3, c )
			else:
				#gundi.move(location_from_axis(476,445),0.0,0.0)
				gundi.scripts[10] = 73
				gundi.scripts[19] = 73
				gundi.object_flag_set( OF_OFF )
		elif c & 4 == 4 and c & 8 == 0 and c_time != 1 and c_time != 2 and c_time != 5:
			gundi = find_npc_near(attachee, 8008)
			if (game.global_vars[436] == 6 or game.global_vars[436] == 7) and gundi != OBJ_HANDLE_NULL:
				gundi.destroy()
				c = c | 8
				c = c - 4
				attachee.obj_set_int( obj_f_npc_pad_i_3, c )
			elif gundi != OBJ_HANDLE_NULL:
				gundi.scripts[10] = 0
				gundi.scripts[19] = 0
	elif attachee.map == 5051 and game.global_vars[437] == 100:
	#Nulb exterior
		game.particles('sp-Bless Water', attachee)
		for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
			if (obj.distance_to(attachee) <= 25 and critter_is_unconscious(obj) != 1):
				game.new_sid = 0
				obj.begin_dialog( attachee, 2000 )
	elif attachee.map == 5009:
	#traders' barn
		game.particles('sp-Bless Water', attachee)
		council_heartbeat()
		a = attachee.obj_get_int(obj_f_npc_pad_i_3)
		if (game.global_vars[435] >= 3 or (game.global_vars[435] == 2 and council_time() == 3)) and a & 1 == 0:
			a = a | 1
			npc_set(attachee,1)
			courier = find_npc_near(attachee, 14063)
			courier.destroy()
			if game.quests[17].state == qs_mentioned or game.quests[17].state == qs_accepted:
				game.quests[17].state = qs_botched
		if a & 2 == 0 and (game.global_flags[438] == 1) and not (game.global_flags[814] == 1 and game.global_flags[815] == 1):
			a = a | 2
			npc_set(attachee,2)
			badger = game.obj_create( 14371 , location_from_axis(493, 487))
			for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
				if (obj.distance_to(badger) <= 25 and critter_is_unconscious(obj) != 1):
					pc = obj
			pc.begin_dialog( badger, 5000 )	
	elif attachee.map == 5063:
	#The Renton Residence (village militia captain)
		game.particles('orb-summon-water-elemental',attachee)
		c_time = council_time()
		council_heartbeat()
		if (c_time == 1 or c_time == 2 or c_time == 5) and find_npc_near(attachee, 20007) != OBJ_HANDLE_NULL:
			renton = find_npc_near(attachee, 20007)
			renton.scripts[10] = 6
			renton.scripts[19] = 6
			renton.object_flag_set( OF_OFF )
	return RUN_DEFAULT

def trail_check():
	#returned number, meaning
	#1 - has attack dog companion
	#2 - has wolf companion
	#3 - has jackal companion
	#50 - made successful listen check
	#60 - spotted tracks, but no tracking feat
	#65 - spotted tracks, got tracking feat

	#look for canine animal companions
	for pc in game.party:
		if ( pc.has_feat(feat_animal_companion) ):
			for npc in game.obj_list_vicinity(game.leader.location, OLC_NPC):
				if (is_canine_companion(npc) > 0 and npc.leader_get() != OBJ_HANDLE_NULL):
					abcd = is_canine_companion(npc)
					return abcd

	#failing that, make listen check
	listen_chk = game.random_range(1,20)
	highest_listen_modifier = 0
	for obj in pc.group_list():
		if (obj.skill_level_get(skill_listen) > highest_listen_modifier):
			listen_chk = game.random_range(1,20)
			if (listen_chk + obj.skill_level_get(skill_listen) >= 20):
				return 50

	#failing that, the traders got away while you were searching (and looking away); but after a while you find their tracks
	#if you have the tracking feat, you can follow the tracks; otherwise it's all over in Hommlet
	spot_highest = 0
	for obj in pc.group_list():
		spot_chk = game.random_range(1,20)
		if (spot_chk + obj.skill_level_get(skill_spot) >= spot_highest):
			spot_highest = spot_chk + obj.skill_level_get(skill_spot)
	if (spot_highest >= 20):
		for pc in game.party:
			if (pc.has_feat(feat_track) ):
				return 65
		return 60
	return 0

def is_canine_companion(testee):
	#14049 - attack dog
	#14050 - wolf
	#14051 - jackal
	if (testee.name == 14049):
		return 1
	if (testee.name == 14050):
		return 2
	if (testee.name == 14051):
		return 3
	return 0

def traders_reveal(triggerer, rev_id):
	for obj in game.obj_list_vicinity(triggerer.location,OLC_NPC):
		if (obj.name == 8049):
			gremag = obj
		elif (obj.name == 8048):
			rannos = obj
	if (rev_id == 1 or rev_id == 2 or rev_id == 3):
		gremag.condition_add_with_args("prone", 0, 0)
	else:
		gremag.turn_towards(triggerer)
	gremag.object_flag_unset(OF_DONTDRAW)
	gremag.object_flag_unset(OF_CLICK_THROUGH)
	rannos.object_flag_unset(OF_DONTDRAW)
	rannos.object_flag_unset(OF_CLICK_THROUGH)
	rannos.turn_towards(triggerer)
	if (rev_id == 1 or rev_id == 2 or rev_id == 3 or rev_id == 4):
		game.timevent_add(traders_reveal_pt2,(triggerer,rev_id,gremag,rannos,800),700)
	return

def traders_reveal_pt2(triggerer,rev_id,gremag,rannos,line):
	triggerer.begin_dialog(rannos,line)
	return

def traders_runoff(attachee):
	game.particles('orb-summon-fire-elemental', game.party[0])
	gremag = find_npc_near(attachee, 8049)
	rannos = find_npc_near(attachee, 8048)
	if gremag != OBJ_HANDLE_NULL:
		gremag.runoff(gremag.location-3)
	if rannos != OBJ_HANDLE_NULL:
		rannos.runoff(gremag.location-3)
	if game.party[0].reputation_has(23) == 0:
		game.party[0].reputation_add(23)
	if game.leader.map == 5051:
		qq = 0
		enc_size = len(game.encounter_queue)
		while qq < enc_size:
			if game.encounter_queue[qq] == 3159:
				del game.encounter_queue[qq]
				qq = 1000
			qq = qq + 1
	attachee.destroy()
	return


def proactivity(npc,line_no):
	for pc in game.party:
		 if (critter_is_unconscious(pc) != 1 and pc.type == obj_t_pc):
			pc.begin_dialog(npc,line_no)
	return

def heavily_damage(npc):
	#note: this script kills an NPC
	#since the san_dying is triggered, it makes the game think you killed him
	#so to avoid problems, reduce global_vars[23] (which counts the # of Hommeletans killed) beforehand
	if (game.global_vars[23] == 0):
		flag = 0
	else:
		flag = 1
		game.global_vars[23] = game.global_vars[23] - 1
	npc.damage(OBJ_HANDLE_NULL,D20DT_POISON,dice_new("30d1"))
	npc.damage(OBJ_HANDLE_NULL,D20DT_SUBDUAL,dice_new("15d1"))
	if (flag == 0 and game.global_vars[23] > 0):
		game.global_vars[23] = game.global_vars[23] - 1
	if (game.global_vars[23] < 2 and game.party[0].reputation_has(92) == 1):
		for pc in game.party:
			pc.reputation_remove( 92 )
	return

