from utilities import *
from combat_standard_routines import *
from toee import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	if (game.global_flags[140] == 1):
		if (game.global_vars[15] <= 4):
			triggerer.begin_dialog( attachee, 1 )
		else:
			triggerer.begin_dialog( attachee, 10 )
	elif (not attachee.has_met(triggerer)):
		triggerer.begin_dialog( attachee, 20 )
	elif (game.quests[52].state >= qs_accepted):
		triggerer.begin_dialog( attachee, 40 )
	else:
		triggerer.begin_dialog( attachee, 30 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_flags[310] == 1):
		attachee.object_flag_set(OF_OFF)
		game.global_flags[116] = 1
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_flags[116] = 1
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[116] = 0
	return RUN_DEFAULT


def kill_antonio( attachee ):
	game.timevent_add( antonio_dead, ( attachee, ), 86400000 )
	return RUN_DEFAULT


def antonio_dead( attachee ):
	game.global_flags[311] = 1
	return RUN_DEFAULT


def kill_alrrem( attachee ):
	game.timevent_add( alrrem_dead, ( attachee, ), 86400000 )
	return RUN_DEFAULT


def alrrem_dead( attachee ):
	game.global_flags[312] = 1
	return RUN_DEFAULT