from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (not attachee.has_met(triggerer)):
		if ( game.global_flags[177] == 1 ):
			triggerer.begin_dialog( attachee, 20 )
		elif ( triggerer.stat_level_get(stat_race) == race_halforc ):
			triggerer.begin_dialog( attachee, 10 )
		else:
			triggerer.begin_dialog( attachee, 1 )
	elif ( game.global_flags[178] == 0 ):
		triggerer.begin_dialog( attachee, 40 )
	elif ( game.global_flags[177] == 1 ):
		triggerer.begin_dialog( attachee, 50 )
	else:
		triggerer.begin_dialog( attachee, 30 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_flags[174] = 1
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[174] = 0
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.global_flags[174] == 1):
		attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT
