from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (game.leader.reputation_has(32) == 1 or game.leader.reputation_has(30) == 1 or game.leader.reputation_has(29) == 1):
		attachee.float_line(11004,triggerer)
	else:
		if (attachee.has_met(triggerer)):
			triggerer.begin_dialog( attachee, 30 )
		else:
			triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_flags[99] == 1):
		attachee.object_flag_unset(OF_OFF)
	if (game.global_vars[4] == 5):
		attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.global_vars[501] == 4 or game.global_vars[501] == 5 or game.global_vars[501] == 6 or game.global_vars[510] == 2):
		attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def run_off( attachee, triggerer ):
	game.global_vars[4] = 5
	game.global_flags[99] = 0
	loc = location_from_axis(545,456)
	attachee.runoff(loc)
	attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT
