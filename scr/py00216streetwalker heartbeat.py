from toee import *
from combat_standard_routines import *


def san_first_heartbeat( attachee, triggerer ):
	game.global_flags[322] = 1
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT