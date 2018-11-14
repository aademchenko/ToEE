from toee import *
from utilities import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.global_flags[991] == 0 ):
		attachee.object_flag_set(OF_OFF)
	if (game.global_flags[991] == 1 ):
		attachee.object_flag_unset(OF_OFF)
	return RUN_DEFAULT