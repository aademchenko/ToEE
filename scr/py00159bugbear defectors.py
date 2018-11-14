from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_vars[11] = game.global_vars[11] + 1
	return RUN_DEFAULT


def san_resurrect( attachee, triggerer ):
	game.global_vars[11] = game.global_vars[11] - 1
	return RUN_DEFAULT

