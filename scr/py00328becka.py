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
			if (attachee.name == 8765):
				if (game.global_vars[541] == 1):
					attachee.object_flag_unset(OF_OFF)
#					game.global_vars[541] = 5
					game.global_vars[536] = game.global_vars[536] + 1
			if (attachee.name == 8768):
				if (game.global_vars[541] == 2):
					attachee.object_flag_unset(OF_OFF)
#					game.global_vars[541] = 5
					game.global_vars[536] = game.global_vars[536] + 1
			if (attachee.name == 8769):
				if (game.global_vars[541] == 3):
					attachee.object_flag_unset(OF_OFF)
#					game.global_vars[541] = 5
					game.global_vars[536] = game.global_vars[536] + 1
			if (attachee.name == 8799):
				if (game.global_vars[541] == 4):
					attachee.object_flag_unset(OF_OFF)
#					game.global_vars[541] = 5
					game.global_vars[536] = game.global_vars[536] + 1
		elif (game.global_vars[536] == 6):
			if (game.global_vars[541] == 1 and attachee.name == 8765):
				if (not game.combat_is_active()):
					for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
						if (close_enough(attachee, obj)):
							if (obj.skill_level_get(attachee,skill_spot) >= 19):
								attachee.concealed_set(0)
			elif (game.global_vars[541] == 2 and attachee.name == 8768):
				if (not game.combat_is_active()):
					for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
						if (close_enough(attachee, obj)):
							if (obj.skill_level_get(attachee,skill_spot) >= 19):
								attachee.concealed_set(0)
			elif (game.global_vars[541] == 3 and attachee.name == 8769):
				if (not game.combat_is_active()):
					for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
						if (close_enough(attachee, obj)):
							if (obj.skill_level_get(attachee,skill_spot) >= 19):
								attachee.concealed_set(0)
			elif (game.global_vars[541] == 4 and attachee.name == 8799):
				if (not game.combat_is_active()):
					for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
						if (close_enough(attachee, obj)):
							if (obj.skill_level_get(attachee,skill_spot) >= 19):
								attachee.concealed_set(0)
	return RUN_DEFAULT


def san_join( attachee, triggerer ):
	if (not game.combat_is_active()):
		if (attachee.name == 8765):
			obj = find_npc_near( attachee, 8819)
			if (obj != OBJ_HANDLE_NULL):
				triggerer.follower_add(obj)
		elif (attachee.name == 8768):
			obj = find_npc_near( attachee, 8820)
			if (obj != OBJ_HANDLE_NULL):
				triggerer.follower_add(obj)
		elif (attachee.name == 8769):
			obj = find_npc_near( attachee, 8821)
			if (obj != OBJ_HANDLE_NULL):
				triggerer.follower_add(obj)
		elif (attachee.name == 8799):
			obj = find_npc_near( attachee, 8822)
			if (obj != OBJ_HANDLE_NULL):
				triggerer.follower_add(obj)
		game.global_vars[550] = 1
		return RUN_DEFAULT


def close_enough(speaker,listener):
	if (speaker.distance_to(listener) <= 10):
		return 1
	return 0