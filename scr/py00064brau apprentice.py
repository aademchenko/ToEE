from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT

def san_first_heartbeat( attachee, triggerer ):
	if (game.global_vars[501] == 4 or game.global_vars[501] == 5 or game.global_vars[501] == 6 or game.global_vars[510] == 2):
		attachee.object_flag_set(OF_OFF)
	else:
		attachee.object_flag_unset(OF_OFF)
		if game.global_flags[205] == 1:
			attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


		
