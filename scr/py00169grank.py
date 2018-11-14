from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	if ( attachee.has_met( triggerer ) ):
		triggerer.begin_dialog( attachee, 120 )
	else:
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT


def san_start_combat( attachee, triggerer ):
	if (game.global_vars[18] >= 7):
		triggerer.begin_dialog( attachee, 1 )
		game.global_vars[18] = 0
	return RUN_DEFAULT
