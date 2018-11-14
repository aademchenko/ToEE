from toee import *
from council import *
from py00439script_daemon import record_time_stamp, get_v, set_v, npc_set, npc_unset, npc_get, tsc, tpsts, within_rect_by_corners
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	if (game.leader.reputation_has(32) == 1 or game.leader.reputation_has(30) == 1 or game.leader.reputation_has(29) == 1):
		attachee.float_line(11004,triggerer)
	elif (attachee.map == 5001) and (game.global_vars[4] <= 4):
		triggerer.begin_dialog( attachee, 110 )
	elif (attachee.map == 5001) and (game.global_vars[4] == 6):
		triggerer.begin_dialog( attachee, 200 )
	else:
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.map == 5031):
		if (game.quests[9].state == qs_accepted):
			if (is_daytime() == 0):
				attachee.object_flag_set(OF_OFF)
			else:
				attachee.object_flag_unset(OF_OFF)
		elif (game.global_vars[4] == 3):
			game.global_vars[4] = 4
			attachee.object_flag_set(OF_OFF)
			game.global_flags[99] = 1
			game.global_vars[24] = game.global_vars[24] + 1
			if (game.party[0].reputation_has( 5 ) == 0):
				game.party[0].reputation_add( 5 )
			if ((game.global_vars[24] >= 3) and (game.party[0].reputation_has( 6 ) == 0)):
				game.party[0].reputation_add( 6 )
		elif (game.global_vars[4] == 5):
			attachee.object_flag_unset(OF_OFF)
	elif (attachee.map == 5001):
		if (game.quests[9].state == qs_accepted):
			if (is_daytime() == 0):
				attachee.object_flag_unset(OF_OFF)
			else:
				attachee.object_flag_set(OF_OFF)
		else:
			attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	if (game.quests[9].state >= qs_accepted):
		game.global_vars[4] = 1
	if (game.party[0].reputation_has(9) == 0):
		game.party[0].reputation_add(9)
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.global_vars[501] == 4 or game.global_vars[501] == 5 or game.global_vars[501] == 6 or game.global_vars[510] == 2):
		attachee.object_flag_set(OF_OFF)
	else:
		attachee.object_flag_unset(OF_OFF)
	return RUN_DEFAULT


def run_off( attachee, triggerer ):
	attachee.runoff(attachee.location-3)
	return RUN_DEFAULT