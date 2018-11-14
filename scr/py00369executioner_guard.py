from toee import *
from combat_standard_routines import *


def san_first_heartbeat( attachee, triggerer ):
	if (attachee.map == 5121):
		if (game.global_flags[955] == 1):
			attachee.object_flag_unset(OF_OFF)
	return RUN_DEFAULT


def san_heartbeat( attachee, triggerer ):
	if (game.global_flags[955] == 1):
		if (not game.combat_is_active()):
			game.timevent_add( start_talking, ( attachee, triggerer ), 2000 )
			game.new_sid = 0
	return RUN_DEFAULT


def start_talking( attachee, triggerer ):
	attachee.turn_towards(game.party[0])
	game.party[0].begin_dialog( attachee, 50 )
	return RUN_DEFAULT