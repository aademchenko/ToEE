from toee import *
from combat_standard_routines import *


def san_dialog( attachee, triggerer ):
	triggerer.begin_dialog( attachee, 1 )
	return SKIP_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	if (game.party[0].reputation_has(9) == 0):
		game.party[0].reputation_add(9)
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.global_vars[501] == 4 or game.global_vars[501] == 5 or game.global_vars[501] == 6 or game.global_vars[510] == 2):
		attachee.object_flag_set(OF_OFF)
	else:
		if (game.global_flags[528] == 0):
			if (attachee.name == 8073):
				if (is_daytime() != 1):
					attachee.object_flag_set(OF_OFF)
				elif (is_daytime() == 1):
					attachee.object_flag_unset(OF_OFF)
			elif (attachee.name == 8074):
				if (is_daytime() != 1):
					attachee.object_flag_unset(OF_OFF)
				elif (is_daytime() == 1):
					attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def run_off( attachee, triggerer ):
	# loc = location_from_axis(427,406)
	# attachee.runoff(loc)
	attachee.runoff(attachee.location-3)
	return RUN_DEFAULT