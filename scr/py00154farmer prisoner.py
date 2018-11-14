from utilities import *
from combat_standard_routines import *
from toee import *


def san_dialog( attachee, triggerer ):
	if (attachee.map == 5001 and (game.leader.reputation_has(32) == 1 or game.leader.reputation_has(30) == 1 or game.leader.reputation_has(29) == 1)):
		attachee.float_line(11004,triggerer)
	else:
		if (not attachee.has_met(triggerer)):
			if (game.global_flags[169] == 0):
				triggerer.begin_dialog( attachee, 1 )
			else:
				triggerer.begin_dialog( attachee, 40 )
		elif (game.global_flags[169] == 1):
			triggerer.begin_dialog( attachee, 100 )
		elif (game.global_flags[170] == 1):
			triggerer.begin_dialog( attachee, 110 )
		else:
			triggerer.begin_dialog( attachee, 120 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def banter( attachee, triggerer, line):
	npc = find_npc_near(attachee,8037)
	if (npc != OBJ_HANDLE_NULL):
		triggerer.begin_dialog(npc,line)
		npc.turn_towards(attachee)
		attachee.turn_towards(npc)
	else:
		triggerer.begin_dialog(attachee,30)
	return SKIP_DEFAULT


def run_off( attachee, triggerer ):
	loc = location_from_axis(427,406)
	attachee.runoff(loc)
	return RUN_DEFAULT


def eat_in_three( attachee, triggerer ):
	game.timevent_add( mandy_eaten, ( attachee, ), 86400000 )
	game.timevent_add( whitman_eaten, ( attachee, ), 259200000 )
	return RUN_DEFAULT	


def mandy_eaten( attachee ):
	game.global_flags[170] = 1
	return RUN_DEFAULT


def whitman_eaten( attachee ):
	attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT