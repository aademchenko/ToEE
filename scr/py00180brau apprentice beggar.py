from utilities import *
from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (game.leader.reputation_has(32) == 1 or game.leader.reputation_has(30) == 1 or game.leader.reputation_has(29) == 1):
		attachee.float_line(11004,triggerer)
	else:
		if (attachee.leader_get() != OBJ_HANDLE_NULL):
			if (game.global_flags[207] == 1):
				triggerer.begin_dialog( attachee, 80 )
			else:
				triggerer.begin_dialog( attachee, 100 )
		elif (game.global_flags[207] == 1):
			triggerer.begin_dialog( attachee, 50 )
		elif (attachee.has_met(triggerer)):
			triggerer.begin_dialog( attachee, 30 )
		else:
			triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_flags[205] == 1):
		attachee.object_flag_unset(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	if (game.global_flags[240] == 0):
		game.global_vars[23] = game.global_vars[23] + 1
		if game.global_vars[23] >= 2:
			game.party[0].reputation_add( 92 )
	else:
		game.global_vars[29] = game.global_vars[29] + 1
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (attachee.leader_get() == OBJ_HANDLE_NULL):
		if (game.global_vars[501] == 4 or game.global_vars[501] == 5 or game.global_vars[501] == 6 or game.global_vars[510] == 2):
			attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def san_join( attachee, triggerer ):
	game.global_flags[240] = 1
	return RUN_DEFAULT


def san_disband( attachee, triggerer ):
	game.global_flags[240] = 0
	for pc in game.party:
		attachee.ai_shitlist_remove( pc )
		attachee.reaction_set( pc, 50 )
	return RUN_DEFAULT


def get_drunk( attachee, triggerer ):
	attachee.object_flag_set(OF_OFF)
	game.timevent_add( comeback_drunk, ( attachee ),3600000 )
	return RUN_DEFAULT


def comeback_drunk( attachee ):
	attachee.object_flag_unset(OF_OFF)
	game.global_flags[207] = 1
	time = ( 3600000 * game.global_vars[21] )  
	game.timevent_add( get_sober, ( attachee ), time )
	return RUN_DEFAULT


def get_sober( attachee ):
	game.global_flags[207] = 0
	return RUN_DEFAULT


def run_off( attachee, triggerer ):
	loc = location_from_axis(427,406)
	attachee.runoff(loc)
	return RUN_DEFAULT