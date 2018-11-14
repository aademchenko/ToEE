from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (game.global_flags[133] == 0):
		triggerer.begin_dialog( attachee, 1 )
	elif (not attachee.has_met(triggerer)):
		triggerer.begin_dialog( attachee, 90 )
	elif (game.global_flags[136] == 0):
		triggerer.begin_dialog( attachee, 70 )
	else:
		triggerer.begin_dialog( attachee, 120 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_flags[351] == 0):
		attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	attachee.float_line(12014,triggerer)
	game.global_flags[138] = 1
	if (attachee.leader_get() != OBJ_HANDLE_NULL):
		game.global_vars[29] = game.global_vars[29] + 1
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[138] = 0
	return RUN_DEFAULT