from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	if (attachee.has_met(triggerer)):
		triggerer.begin_dialog( attachee, 10 )
	else:
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT