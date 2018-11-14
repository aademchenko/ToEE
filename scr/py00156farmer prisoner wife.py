from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (attachee.map == 5001 and (game.leader.reputation_has(32) == 1 or game.leader.reputation_has(30) == 1 or game.leader.reputation_has(29) == 1)):
		attachee.float_line(11004,triggerer)
	else:
		if (not attachee.has_met(triggerer)):
			if (game.global_flags[169] == 0):
				triggerer.begin_dialog( attachee, 1 )
			else:
				triggerer.begin_dialog( attachee, 40 )
		elif (game.global_flags[169] == 0):
			triggerer.begin_dialog( attachee, 90 )
		else:
			triggerer.begin_dialog( attachee, 100 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_flags[170] == 1):
		attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_flags[170] = 1
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[170] = 0
	return RUN_DEFAULT


def banter( attachee, triggerer, line):
	npc = find_npc_near(attachee,8038)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc,line)
		npc.turn_towards(attachee)
		attachee.turn_towards(npc)
	else:
		triggerer.begin_dialog(attachee,10)
	return SKIP_DEFAULT


def run_off( attachee, triggerer ):
	loc = location_from_axis(427,406)
	attachee.runoff(loc)
	return RUN_DEFAULT


def get_rep( attachee, triggerer ):
	if triggerer.reputation_has( 16 ) == 0:
		triggerer.reputation_add( 16 )
	game.global_vars[26] = game.global_vars[26] + 1
	if ( game.global_vars[26] >= 3 and triggerer.reputation_has( 17 ) == 0):
		triggerer.reputation_add( 17 )
	return RUN_DEFAULT