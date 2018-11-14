from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_flags[351] == 1 or game.global_flags[353] == 1 or game.global_flags[354] == 1):
		attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.global_flags[355] == 1):
		game.new_sid = 0
		attachee.runoff(attachee.location-3)
	return RUN_DEFAULT


def run_off( attachee, triggerer ):
	game.global_flags[355] = 1
	attachee.runoff(attachee.location-3)
	return RUN_DEFAULT
	

