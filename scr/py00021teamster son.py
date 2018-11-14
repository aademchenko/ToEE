from utilities import *
from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (attachee.map == 5001):
		triggerer.begin_dialog( attachee, 1 )	
	elif (game.global_flags[6] == 1):
		triggerer.begin_dialog( attachee, 80 )
	else:
		return RUN_DEFAULT
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.map == 5032):
		if (game.global_vars[501] == 4 or game.global_vars[501] == 5 or game.global_vars[501] == 6 or game.global_vars[510] == 2):
			attachee.object_flag_set(OF_OFF)
		else:
			attachee.object_flag_unset(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	if (attachee.map == 5001):
		game.global_flags[5] = 1
		create_item_in_inventory(12004,attachee)
		if (triggerer.reputation_has(9) == 0):
			trigger.reputation_add(9)
	else:
		game.global_flags[300] = 1
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_flags[5] = 0
	game.global_flags[300] = 0
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (attachee.map == 5001):
		if (game.global_vars[501] == 4 or game.global_vars[501] == 5 or game.global_vars[501] == 6 or game.global_vars[510] == 2):
			attachee.object_flag_set(OF_OFF)
		else:
			attachee.object_flag_unset(OF_OFF)
	return RUN_DEFAULT


def discovered_and_leaves_field( attachee, triggerer ):
#	attachee.standpoint_set( STANDPOINT_NIGHT, 164 )
	attachee.runoff(attachee.location-3)
	game.global_flags[230] = 1
#	game.timevent_add( turn_back_on, ( attachee, ), 43200000 )	
	return RUN_DEFAULT	


def turn_back_on( attachee ):
	attachee.object_flag_unset(OF_OFF)
#	game.timevent_add( assassinated, ( attachee, ), 86400000 )	
	return RUN_DEFAULT


def turn_back_on2( attachee ):
	game.timevent_add( assassinated, ( attachee, ), 86400000 )	
	return RUN_DEFAULT


def assassinated( attachee ):
	attachee.object_flag_set(OF_OFF)
	game.global_flags[7] = 1
	return RUN_DEFAULT