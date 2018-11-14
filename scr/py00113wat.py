from toee import *
from utilities import *
from scripts import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (not attachee.has_met( triggerer )):
		triggerer.begin_dialog( attachee, 1 )
	elif (find_npc_near(attachee, 14773) == OBJ_HANDLE_NULL):
		triggerer.begin_dialog( attachee, 270 )
	else:
		triggerer.begin_dialog( attachee, 70 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.quests[39].state = qs_botched
	return RUN_DEFAULT


def kill_dick( attachee ):
	game.timevent_add( kill_dick_callback, ( attachee, ), 14400000 ) # call kill_dick_callback in 4 hours
	return SKIP_DEFAULT


def kill_dick_callback( attachee ):
	npc = find_npc_near(attachee,8018)
	if (npc != OBJ_HANDLE_NULL):
		npc.object_flag_set(OF_OFF)
		game.global_flags[88] = 1
	return SKIP_DEFAULT
