from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if (game.global_flags[55] == 1):
		triggerer.begin_dialog( attachee, 90 )
	elif (not attachee.has_met( triggerer )):
		triggerer.begin_dialog( attachee, 1 )
	else:
		triggerer.begin_dialog( attachee, 100 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_flags[55] == 1):
	## captives have been rescued from lubash
		attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def run_off( attachee, triggerer ):
	attachee.runoff(attachee.location-2)
	return RUN_DEFAULT
