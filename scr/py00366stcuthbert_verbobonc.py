from toee import *
from combat_standard_routines import *


def san_first_heartbeat( attachee, triggerer ):
	if (game.global_vars[698] == 1):
		attachee.object_flag_unset(OF_OFF)
		game.sound( 4138, 1 )
	elif (game.global_vars[698] == 2):
		attachee.object_flag_set(OF_OFF)
	return RUN_DEFAULT


def san_dying( attachee, triggerer ):
	game.global_vars[695] = game.global_vars[695] + 1
	if (game.global_vars[695] == 4):
		game.quests[102].state = qs_completed
		game.party[0].reputation_add(59)
		random_fate()
	return RUN_DEFAULT


def san_exit_combat( attachee, triggerer ):
	if (attachee.map == 5121):
		attachee.object_flag_set(OF_OFF)
		game.global_vars[698] = 2
	return RUN_DEFAULT


def random_fate():
	pendulum = game.random_range(1,5)
	if (pendulum == 1 or pendulum == 2 or pendulum == 3):
		game.global_vars[508] = 1
	elif (pendulum == 4):
		game.global_vars[508] = 2
	elif (pendulum == 5):
		game.global_vars[508] = 3
	return RUN_DEFAULT