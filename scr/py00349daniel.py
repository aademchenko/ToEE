from toee import *
from utilities import *
from Co8 import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (game.global_vars[993] == 5):
		triggerer.begin_dialog( attachee, 20 )
	else:
		return RUN_DEFAULT
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_vars[993] == 2):
		attachee.object_flag_unset(OF_OFF)
	elif (game.global_vars[993] == 3 or game.global_flags[947] == 1):
		attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_vars[995] = game.global_vars[995] + 1
	return RUN_DEFAULT


def san_start_combat( attachee, triggerer ):
	if ( (game.global_flags[948] == 1) and (game.global_flags[949] == 1) and (game.global_flags[950] == 1) and (game.global_flags[951] == 1) and (game.global_flags[952] == 1) and (game.global_flags[953] == 1) and (game.global_flags[954] == 1) ):
		for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
			StopCombat(attachee, 0)
			obj.begin_dialog( attachee, 20 )
			return RUN_DEFAULT
	else:
		return SKIP_DEFAULT
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.global_vars[993] == 5):
		if (not game.combat_is_active()):
			for obj in game.obj_list_vicinity(attachee.location,OLC_PC):
				if (is_better_to_talk(attachee,obj)):
					attachee.turn_towards(obj)
					obj.begin_dialog( attachee, 20 )
					game.new_sid = 0
	return RUN_DEFAULT


def switch_to_tarah( attachee, triggerer, line):
	npc = find_npc_near(attachee,8805)
	daniel = find_npc_near(attachee,8720)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc, line)
		npc.turn_towards(daniel)
		daniel.turn_towards(npc)
	return SKIP_DEFAULT


def is_better_to_talk(speaker,listener):
	if (speaker.distance_to(listener) <= 40):
		return 1
	return 0