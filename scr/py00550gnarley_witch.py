from toee import *
from utilities import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	if (attachee.has_met( triggerer )):
		if anyone( triggerer.group_list(), "has_item", 6655 ):
			triggerer.begin_dialog( attachee, 120 )
			return SKIP_DEFAULT
		else:
			triggerer.begin_dialog( attachee, 100 )
			return SKIP_DEFAULT
	else:
		triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	return RUN_DEFAULT

