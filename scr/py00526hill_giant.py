from toee import *
from combat_standard_routines import *


def san_dying(attachee, triggerer):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_vars[987] = game.global_vars[987] + 1
	if game.global_vars[987] == 2:
		game.global_flags[945] = 1
		game.global_vars[994] = 3
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.global_vars[954] == 1):
		attachee.object_flag_unset(OF_OFF)
	return RUN_DEFAULT