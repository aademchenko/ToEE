from toee import *
from utilities import *
from Co8 import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (attachee.leader_get() != OBJ_HANDLE_NULL):
		triggerer.begin_dialog( attachee, 1 )
	else:
		triggerer.begin_dialog( attachee, 10 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_vars[550] == 2):
		attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def san_start_combat( attachee, triggerer ):
	if (attachee.leader_get() != OBJ_HANDLE_NULL):
		return SKIP_DEFAULT
	else:
		StopCombat(attachee, 0)
		attachee.float_line(1000,triggerer)
		attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.quests[109].state == qs_mentioned or game.quests[109].state == qs_accepted):
		if (game.global_vars[536] == 4 or game.global_vars[536] == 5):
			if (attachee.name == 8819):
				if (game.global_vars[540] == 1):
					attachee.object_flag_unset(OF_OFF)
#					game.global_vars[540] = 5
					game.global_vars[536] = game.global_vars[536] + 1
			if (attachee.name == 8820):
				if (game.global_vars[540] == 2):
					attachee.object_flag_unset(OF_OFF)
#					game.global_vars[540] = 5
					game.global_vars[536] = game.global_vars[536] + 1
			if (attachee.name == 8821):
				if (game.global_vars[540] == 3):
					attachee.object_flag_unset(OF_OFF)
#					game.global_vars[540] = 5
					game.global_vars[536] = game.global_vars[536] + 1
			if (attachee.name == 8822):
				if (game.global_vars[540] == 4):
					attachee.object_flag_unset(OF_OFF)
#					game.global_vars[540] = 5
					game.global_vars[536] = game.global_vars[536] + 1
		elif (game.global_vars[536] == 6):
			if (game.global_vars[540] == 1 and attachee.name == 8819):
				if (not game.combat_is_active()):
					for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
						if (close_enough(attachee, obj)):
							if (obj.skill_level_get(attachee,skill_spot) >= 19):
								attachee.concealed_set(0)
			elif (game.global_vars[540] == 2 and attachee.name == 8820):
				if (not game.combat_is_active()):
					for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
						if (close_enough(attachee, obj)):
							if (obj.skill_level_get(attachee,skill_spot) >= 19):
								attachee.concealed_set(0)
			elif (game.global_vars[540] == 3 and attachee.name == 8821):
				if (not game.combat_is_active()):
					for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
						if (close_enough(attachee, obj)):
							if (obj.skill_level_get(attachee,skill_spot) >= 19):
								attachee.concealed_set(0)
			elif (game.global_vars[540] == 4 and attachee.name == 8822):
				if (not game.combat_is_active()):
					for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
						if (close_enough(attachee, obj)):
							if (obj.skill_level_get(attachee,skill_spot) >= 19):
								attachee.concealed_set(0)
	return RUN_DEFAULT


def san_join( attachee, triggerer ):
	if (not game.combat_is_active()):
		if (attachee.name == 8819):
			obj = find_npc_near( attachee, 8765)
			if (obj != OBJ_HANDLE_NULL):
				triggerer.follower_add(obj)
		elif (attachee.name == 8820):
			obj = find_npc_near( attachee, 8768)
			if (obj != OBJ_HANDLE_NULL):
				triggerer.follower_add(obj)
		elif (attachee.name == 8821):
			obj = find_npc_near( attachee, 8769)
			if (obj != OBJ_HANDLE_NULL):
				triggerer.follower_add(obj)
		elif (attachee.name == 8822):
			obj = find_npc_near( attachee, 8799)
			if (obj != OBJ_HANDLE_NULL):
				triggerer.follower_add(obj)
		game.global_vars[550] = 1
		return RUN_DEFAULT


def san_new_map( attachee, triggerer ):
	if (attachee.leader_get() != OBJ_HANDLE_NULL):
		if ( attachee.map != 5141 ):
			game.sound ( 4109, 1 )
			triggerer.follower_remove(attachee)
			attachee.runoff(attachee.location-3)
			if (attachee.name == 8819):
				becka = find_npc_near( attachee, 8765)
				triggerer.follower_remove(becka)
				becka.runoff(attachee.location-3)
				game.global_vars[550] = 2
			elif (attachee.name == 8820):
				becka = find_npc_near( attachee, 8768)
				triggerer.follower_remove(becka)
				becka.runoff(attachee.location-3)
				game.global_vars[550] = 2
			elif (attachee.name == 8821):
				becka = find_npc_near( attachee, 8769)
				triggerer.follower_remove(becka)
				becka.runoff(attachee.location-3)
				game.global_vars[550] = 2
			elif (attachee.name == 8822):
				becka = find_npc_near( attachee, 8799)
				triggerer.follower_remove(becka)
				becka.runoff(attachee.location-3)
				game.global_vars[550] = 2
	return SKIP_DEFAULT


def close_enough(speaker,listener):
	if (speaker.distance_to(listener) <= 10):
		return 1
	return 0