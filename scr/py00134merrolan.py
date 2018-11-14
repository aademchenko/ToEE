from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (game.global_flags[105] == 1):
		attachee.attack(triggerer)
	elif (find_npc_near(attachee,8028) == OBJ_HANDLE_NULL):
		triggerer.begin_dialog( attachee, 1 )
	elif (game.quests[46].state == qs_unknown):
		triggerer.begin_dialog( attachee, 20 )
	else:
		triggerer.begin_dialog( attachee, 40 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_flags[132] = 1
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[132] = 0
	return RUN_DEFAULT


def san_will_kos( attachee, triggerer ):
	if (game.global_flags[105] == 0):
		return SKIP_DEFAULT
	else:
		return RUN_DEFAULT

def switch_dialog( attachee, triggerer, line):
	npc = find_npc_near(attachee,8028)
	if (npc != OBJ_HANDLE_NULL):
		npc.critter_flag_unset(OCF_MUTE)
		triggerer.begin_dialog(npc,line)
		npc.turn_towards(attachee)
		attachee.turn_towards(npc)
	else:
		triggerer.begin_dialog(attachee,1)
	return SKIP_DEFAULT
