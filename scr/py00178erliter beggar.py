from toee import *
from py00439script_daemon import record_time_stamp, get_v, set_v, npc_set, npc_unset, npc_get, tsc, tpsts, within_rect_by_corners
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (game.leader.reputation_has(32) == 1 or game.leader.reputation_has(30) == 1 or game.leader.reputation_has(29) == 1):
		attachee.float_line(11004,triggerer)
	else:
		if (attachee.has_met(triggerer)):
			triggerer.begin_dialog( attachee, 60 )
		else:
			triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_flags[199] == 1):
		attachee.object_flag_unset(OF_OFF)
	if ( get_v(436) == 1 or get_v(436) == 2 or get_v(436) == 6 or get_v(436) == 7 ):
		attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.global_vars[501] == 4 or game.global_vars[501] == 5 or game.global_vars[501] == 6 or game.global_vars[510] == 2):
		attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def leave_for_city( attachee, triggerer ):
	loc = location_from_axis(625,420)
	attachee.runoff(loc)
	return RUN_DEFAULT
