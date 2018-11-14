from utilities import *
from toee import *
from combat_standard_routines import *


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.map == 5004):
		if (game.quests[95].state == qs_mentioned and game.global_vars[757] >= 9):
			attachee.object_flag_unset(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	if should_modify_CR( attachee ):
		modify_CR( attachee, get_av_level() )
	game.global_vars[757] = game.global_vars[757] + 1
	if attachee.name in [14070, 14074, 14069]:
		# Upper floor Brigands (Raul the Grim)
		if game.global_vars[407] == 0:
			game.global_vars[407] = game.time.time_game_in_seconds(game.time)
	return RUN_DEFAULT