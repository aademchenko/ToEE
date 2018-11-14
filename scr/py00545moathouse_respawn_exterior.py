from utilities import *
from toee import *
from combat_standard_routines import *


def san_heartbeat( attachee, triggerer ):
	if (attachee.map == 5002):
		if (game.quests[95].state == qs_mentioned and game.global_vars[764] >= 8):
			attachee.object_flag_unset(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_vars[764] = game.global_vars[764] + 1
	if (game.global_vars[764] >=8):
		game.global_flags[977] = 1	#flag to say that bandits are gone from courtyard so ambush can fire
	return RUN_DEFAULT