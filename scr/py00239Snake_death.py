from toee import *
from combat_standard_routines import *


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	if (attachee.map == 5066):
		game.global_flags[117] = 1
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	if (attachee.map == 5066):
		game.global_flags[117] = 0
	return RUN_DEFAULT