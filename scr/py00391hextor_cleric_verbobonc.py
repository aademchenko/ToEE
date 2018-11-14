from toee import *
from utilities import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	attachee.turn_towards(triggerer)
	triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_vars[949] == 2 or game.party[0].reputation_has(47) == 1):
		attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


