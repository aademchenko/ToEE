from toee import *
from utilities import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	return RUN_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_vars[993] == 2):
		attachee.object_flag_unset(OF_OFF)
	elif (game.global_vars[993] == 3):
		attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_flags[951] = 1
	if (game.global_flags[948] == 1 and game.global_flags[949] == 1 and game.global_flags[950] == 1 and game.global_flags[952] == 1 and game.global_flags[953] == 1 and game.global_flags[954] == 1):
		game.party[0].reputation_add(40)
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[951] = 0
	game.party[0].reputation_remove(40)
	return RUN_DEFAULT


def switch_to_tarah( attachee, triggerer, line):
	npc = find_npc_near(attachee,8805)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc, line)
	return SKIP_DEFAULT