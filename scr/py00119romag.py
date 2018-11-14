from toee import *
from utilities import *
from py00439script_daemon import record_time_stamp, get_v, set_v, npc_set, npc_unset, npc_get, tsc, tpsts, within_rect_by_corners
from combat_standard_routines import *
from py00446earthcombat import switch_to_gatekeeper

def san_dialog( attachee, triggerer ):
	if (not attachee.has_met(triggerer)):
		record_time_stamp(501)
		if game.global_vars[454] & 2**8 != 0:
			triggerer.begin_dialog( attachee, 590 )
		elif (game.global_flags[91] == 1):
			triggerer.begin_dialog( attachee, 100 )
		else:
			triggerer.begin_dialog( attachee, 1 )
	else:
		triggerer.begin_dialog( attachee, 300 )
	return RUN_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_flags[372] == 1):
		attachee.object_flag_set(OF_OFF)
	else:
		if (attachee.leader_get() == OBJ_HANDLE_NULL and not game.combat_is_active()):
			game.global_vars[727] = 0
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_flags[104] = 1
	record_time_stamp(456)
	return RUN_DEFAULT


def san_enter_combat( attachee, triggerer ):
	game.global_flags[347] = 0
	return RUN_DEFAULT


def san_start_combat( attachee, triggerer ):
	if ( obj_percent_hp(attachee) < 50 and (not attachee.has_met(triggerer)) ):
		found_pc = OBJ_HANDLE_NULL
		for pc in game.party:
			if pc.type == obj_t_pc:
				found_pc = pc
				attachee.ai_shitlist_remove( pc )
		if found_pc != OBJ_HANDLE_NULL:
			record_time_stamp(501)
			found_pc.begin_dialog( attachee, 200 )
			return SKIP_DEFAULT
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[104] = 0
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (not game.combat_is_active()):
		for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
			if (not attachee.has_met(obj)):
				if (is_safe_to_talk(attachee,obj)):
					record_time_stamp(501)
					if (game.global_flags[91] == 1):
						obj.turn_towards(attachee)	## added by Livonya
						attachee.turn_towards(obj)	## added by Livonya
						obj.begin_dialog( attachee, 100 )
					elif ( (game.global_flags[107] == 1) or (game.global_flags[105] == 1) ):
						obj.turn_towards(attachee)	## added by Livonya
						attachee.turn_towards(obj)	## added by Livonya
						obj.begin_dialog( attachee, 590 )
					else:
						obj.turn_towards(attachee)	## added by Livonya
						attachee.turn_towards(obj)	## added by Livonya
						obj.begin_dialog(attachee,1)
						##game.new_sid = 0		## removed by Livonya
	if (game.global_vars[727] == 0 and attachee.leader_get() == OBJ_HANDLE_NULL and not game.combat_is_active()):
		attachee.cast_spell(spell_owls_wisdom, attachee)
		attachee.spells_pending_to_memorized()
	if (game.global_vars[727] == 4 and attachee.leader_get() == OBJ_HANDLE_NULL and not game.combat_is_active()):
		attachee.cast_spell(spell_shield_of_faith, attachee)
		attachee.spells_pending_to_memorized()
	game.global_vars[727] = game.global_vars[727] + 1
	return RUN_DEFAULT

def san_enter_combat( attachee, triggerer ):
	romag_call_help( attachee )
	game.global_flags[347] = 0
	return RUN_DEFAULT

def san_start_combat( attachee, triggerer ):
	romag_call_help( attachee )

	if ( obj_percent_hp(attachee) < 50 and (not attachee.has_met(triggerer)) ):
		found_pc = OBJ_HANDLE_NULL
		for pc in game.party[0].group_list():
			attachee.ai_shitlist_remove( pc )
			if pc.type == obj_t_pc:
				found_pc = pc
		if found_pc != OBJ_HANDLE_NULL:
			record_time_stamp(501)
			for pc in game.party[0].group_list():
				for npc in game.obj_list_vicinity( attachee.location, OLC_NPC):
					if npc.name in [14162, 14163, 14165, 14337, 14339, 14156] and npc.leader_get() == OBJ_HANDLE_NULL:
						npc.ai_shitlist_remove(pc)
			found_pc.begin_dialog( attachee, 200 )
			return SKIP_DEFAULT
	return RUN_DEFAULT

def talk_Hedrack( attachee, triggerer, line):
	npc = find_npc_near(attachee,8046)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc,line)
		npc.turn_towards(attachee)
		attachee.turn_towards(npc)
	else:
		triggerer.begin_dialog(attachee,580)
	return SKIP_DEFAULT


def escort_below( attachee, triggerer ):
	# game.global_flags[144] = 1
	game.global_vars[691] = 1
	attachee.standpoint_set( STANDPOINT_DAY, 267 )
	attachee.standpoint_set( STANDPOINT_NIGHT, 267 )
	game.fade_and_teleport(0,0,0,5080,478,451)
	return RUN_DEFAULT
	
def romag_call_help( attachee ):
	if attachee.map == 5066 and (get_f('j_earth_commander_troops_temple_1') == 0) and within_rect_by_corners(attachee, 440, 432, 440, 451) == 1: # temple level 1
		attachee.float_line(1000, attachee)
		set_f('j_earth_commander_troops_temple_1')
		yyp_max = 439
		party_in_troop_room = 0
		party_in_romag_room = 0
		party_outside_romag_room = 0
		for pc in game.party[0].group_list():
			xxp, yyp = location_to_axis( pc.location )
			if (xxp >= 440 and xxp <= 452 and yyp >= 439 and yyp <= 451):
				party_in_romag_room = 1
				if yyp > yyp_max:
					yyp_max = yyp
			if xxp >= 453 and yyp <= 451:
				party_outside_romag_room = 1
			if (yyp >= 455 and yyp <= 471 and xxp>= 439 and xxp <= 457) or ( (xxp - yyp) <=1 and yyp<= 471 and xxp >= 456 ):
				party_in_troop_room = 1
		y_troop = yyp_max + 18
		y_troop = min( 465, y_troop )
		y_troop_add = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3]
		x_troop_add = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5, -1, -2, -3]
		x_troop = 446
		troop_counter = 0
		
		if party_outside_romag_room == 1 and party_in_romag_room == 0:
			y_troop = 446
			x_troop = 445
			y_troop_add = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3,  0,  1,  2,  3,  0,  1]
			x_troop_add = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, -1, -1, -1, -1, -2, -2]
		
		if not party_in_troop_room:
			for npc in game.obj_list_vicinity(location_from_axis(453, 463), OLC_NPC):
				if npc.name in [14162, 14163, 14165, 14337, 14339, 14156] and npc.leader_get() == OBJ_HANDLE_NULL and npc.is_unconscious() == 0:
					xx, yy = location_to_axis( npc.location )
					if yy > y_troop:
						npc.move( location_from_axis( x_troop + x_troop_add[troop_counter] , y_troop + y_troop_add[troop_counter]), 0, 0)
						troop_counter += 1
						#npc.attack(game.leader)
		

		for npc in game.obj_list_vicinity( location_from_axis(453, 463), OLC_NPC):
			if npc.name in [14162, 14163, 14165, 14337, 14339, 14156] and npc.leader_get() == OBJ_HANDLE_NULL:
				npc.attack(game.leader)
